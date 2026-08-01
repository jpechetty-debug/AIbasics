/**
 * QuizHandler - Centralized logic for interactive quizzes
 */
class QuizHandler {
    constructor(config) {
        this.quizId = config.quizId;
        this.questions = config.questions;
        this.submitUrl = config.submitUrl;
        this.csrfToken = config.csrfToken;
        this.isAssessment = config.isAssessment || false;

        this.form = document.getElementById(config.formId || 'quiz-form');
        this.submitBtn = document.getElementById(config.submitBtnId || 'submit-btn');
        this.resultsModal = document.getElementById('results-modal');

        this.init();
    }

    init() {
        if (!this.form) return;

        // Handle option selection styling
        this.form.querySelectorAll('.quiz-option input').forEach(input => {
            input.addEventListener('change', (e) => this.handleOptionChange(e.target));
        });

        // Handle form submission
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.submit();
        });
    }

    handleOptionChange(input) {
        const parent = input.closest('.question-block');
        const options = parent.querySelectorAll('.quiz-option');

        if (input.type === 'radio') {
            options.forEach(opt => opt.classList.remove('selected'));
        }

        if (input.checked) {
            input.closest('.quiz-option').classList.add('selected');
        } else {
            input.closest('.quiz-option').classList.remove('selected');
        }
    }

    collectAnswers() {
        const answers = {};
        this.questions.forEach(q => {
            const inputs = this.form.querySelectorAll(`input[name="q${q.number}"]:checked`);
            if (q.type === 'multiple') {
                answers[q.number] = Array.from(inputs).map(i => i.value);
            } else {
                answers[q.number] = inputs.length > 0 ? inputs[0].value : '';
            }
        });
        return answers;
    }

    async submit() {
        const answers = this.collectAnswers();

        // Basic validation: ensure at least one answer if it's an assessment
        if (this.isAssessment && Object.values(answers).every(a => !a || a.length === 0)) {
            alert('Please answer at least one question.');
            return;
        }

        this.setLoading(true);

        try {
            const response = await fetch(this.submitUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.csrfToken
                },
                body: JSON.stringify({
                    answers: answers,
                    questions: this.questions
                })
            });

            const data = await response.json();

            if (data.success) {
                this.showFeedback(data.results);
                if (this.isAssessment) {
                    this.showResultsModal(data);
                } else {
                    this.showDailyQuizSummary(data);
                }
            } else {
                alert('There was an error submitting your quiz. Please try again.');
            }
        } catch (error) {
            console.error('Quiz Submission Error:', error);
            alert('Network error. Please check your connection.');
        } finally {
            this.setLoading(false);
        }
    }

    setLoading(isLoading) {
        if (!this.submitBtn) return;

        this.submitBtn.disabled = isLoading;
        if (isLoading) {
            this.submitBtn.dataset.originalText = this.submitBtn.innerHTML;
            this.submitBtn.innerHTML = `
                <svg class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Processing...
            `;
        } else {
            this.submitBtn.innerHTML = this.submitBtn.dataset.originalText || 'Submit';
        }
    }

    showFeedback(results) {
        results.forEach(result => {
            const block = this.form.querySelector(`.question-block[data-question="${result.number}"]`);
            if (!block) return;

            const feedbackEl = block.querySelector('.feedback');
            const options = block.querySelectorAll('.quiz-option');
            const questionData = this.questions.find(q => q.number === result.number);

            options.forEach(opt => {
                const input = opt.querySelector('input');
                const letter = input.value;

                // Reset styles
                opt.classList.remove('correct', 'incorrect');
                input.disabled = true;

                if (result.correct_answer.includes(letter)) {
                    opt.classList.add('correct');
                } else if (result.user_answer.includes(letter)) {
                    opt.classList.add('incorrect');
                }
            });

            if (feedbackEl) {
                feedbackEl.classList.remove('hidden');

                const formatFeedback = (text) => {
                    if (!text) return '';
                    // Convert newlines to <br> for basic formatting
                    // and handle the markdown-style bullets if present
                    return text.split('\n').map(line => line.trim()).filter(l => l).join('<br>');
                };

                let feedbackHtml = `
                    <div class="flex items-start gap-3">
                        <span class="text-xl">${result.correct ? '✅' : '❌'}</span>
                        <div class="flex-1">
                            <p class="font-bold ${result.correct ? 'text-green-800' : 'text-red-800'}">
                                ${result.correct ? 'Correct!' : 'Incorrect.'}
                            </p>
                            ${questionData && questionData.feedback ? `<div class="mt-1 text-slate-700 leading-relaxed">${formatFeedback(questionData.feedback)}</div>` : ''}
                            ${!result.correct ? `<p class="mt-2 text-sm font-medium">Correct answer: ${result.correct_answer.join(', ')}</p>` : ''}
                        </div>
                    </div>
                `;

                if (questionData && questionData.why_matters) {
                    feedbackHtml += `
                        <div class="mt-3 pt-3 border-t border-slate-200">
                            <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Why this matters</p>
                            <p class="text-sm text-slate-600 italic leading-relaxed">${formatFeedback(questionData.why_matters)}</p>
                        </div>
                    `;
                }

                feedbackEl.innerHTML = feedbackHtml;
                feedbackEl.className = `feedback mt-4 ml-12 p-4 rounded-xl border-l-4 ${result.correct ? 'bg-green-50 border-green-500 text-green-800' : 'bg-red-50 border-red-500 text-red-800'
                    }`;
            }
        });

        // Hide submit button after completion for daily quizzes
        if (!this.isAssessment) {
            this.submitBtn.classList.add('hidden');
        }
    }

    showResultsModal(data) {
        if (!this.resultsModal) return;

        const icon = document.getElementById('result-icon');
        const title = document.getElementById('result-title');
        const score = document.getElementById('result-score');
        const message = document.getElementById('result-message');

        if (data.passed) {
            icon.className = 'w-20 h-20 mx-auto mb-6 rounded-full flex items-center justify-center bg-green-100';
            icon.innerHTML = `<svg class="w-10 h-10 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>`;
            title.textContent = 'Congratulations!';
            title.className = 'text-2xl font-bold mb-2 text-green-600';
            message.textContent = 'You passed the Week ' + (this.questions.length > 5 ? 'Assessment' : 'Quiz') + '. Great job!';
        } else {
            icon.className = 'w-20 h-20 mx-auto mb-6 rounded-full flex items-center justify-center bg-red-100';
            icon.innerHTML = `<svg class="w-10 h-10 text-red-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path>
            </svg>`;
            title.textContent = 'Keep Practicing!';
            title.className = 'text-2xl font-bold mb-2 text-red-600';
            message.textContent = 'You need 70% to pass. Review the material and try again.';
        }

        score.textContent = `${data.score}/${data.total} (${data.percentage}%)`;
        score.className = `text-4xl font-bold mb-4 ${data.passed ? 'text-green-600' : 'text-red-600'}`;

        this.resultsModal.classList.remove('hidden');
    }

    showDailyQuizSummary(data) {
        // For daily quizzes, we might just show a success message or mark the lesson as complete visually
        const summaryMsg = document.createElement('div');
        summaryMsg.className = `mt-8 p-6 rounded-2xl border-2 text-center animate-bounce-in ${data.passed ? 'bg-green-50 border-green-200 text-green-800' : 'bg-blue-50 border-blue-200 text-blue-800'
            }`;

        summaryMsg.innerHTML = `
            <h3 class="text-xl font-bold mb-2">${data.passed ? 'Section Mastered!' : 'Knowledge Check Complete!'}</h3>
            <p class="text-lg">You scored ${data.percentage}% (${data.score}/${data.total})</p>
            ${data.passed ? '<p class="mt-2 text-sm">Lesson progress updated ✅</p>' : ''}
            <button onclick="location.reload()" class="mt-4 text-sm font-semibold underline">Reset Quiz</button>
        `;

        this.form.appendChild(summaryMsg);

        // Update "Mark as Complete" button if it exists
        const markCompleteBtn = document.getElementById('mark-complete-btn');
        if (markCompleteBtn && data.passed) {
            markCompleteBtn.innerHTML = '✓ Completed';
            markCompleteBtn.disabled = true;
            markCompleteBtn.classList.add('bg-green-600');
        }
    }
}
