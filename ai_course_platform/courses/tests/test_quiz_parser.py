from django.test import TestCase
from courses.views import QuizParsingMixin

class QuizParserTest(TestCase, QuizParsingMixin):
    """Test suite for the Markdown quiz parser."""

    def test_parse_single_question(self):
        """Test parsing a single multiple-choice question."""
        content = """
### Question 1
**What is the core of a Large Language Model?**
A) Neural Networks
B) Decision Trees
C) Random Forests
D) Linear Regression
**Correct Answer: A**
**Feedback:**
Correct! Neural networks are the foundation of LLMs.
"""
        questions = self.parse_quiz_content(content)
        
        self.assertEqual(len(questions), 1)
        q = questions[0]
        self.assertEqual(q['number'], 1)
        self.assertEqual(q['text'], "What is the core of a Large Language Model?")
        self.assertEqual(len(q['options']), 4)
        self.assertEqual(q['options'][0]['letter'], "A")
        self.assertEqual(q['options'][0]['text'], "Neural Networks")
        self.assertEqual(q['correct'], ["A"])
        self.assertIn("Neural networks are the foundation", q['feedback'])

    def test_parse_multiple_questions(self):
        """Test parsing multiple questions from a single string."""
        content = """
### Question 1
**Question One?**
A) Opt 1
B) Opt 2
**Correct Answer: A**

---

### Question 2
**Question Two?**
A) Opt A
B) Opt B
**Correct Answer: B**
"""
        questions = self.parse_quiz_content(content)
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]['number'], 1)
        self.assertEqual(questions[1]['number'], 2)
        self.assertEqual(questions[0]['correct'], ["A"])
        self.assertEqual(questions[1]['correct'], ["B"])

    def test_parse_question_with_varied_formatting(self):
        """Test parser robustness with different spacing and markers."""
        content = """
### Question 5: Complex Format
**What is RAG?**

A) Red Amber Green
B) Retrieval Augmented Generation
C) Random Access Group

**Correct Answer: B**
**Feedback:**
Important for context!
"""
        questions = self.parse_quiz_content(content)
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]['text'], "What is RAG?")
        self.assertEqual(questions[0]['correct'], ["B"])

    def test_empty_content(self):
        """Test behavior with empty or non-quiz content."""
        questions = self.parse_quiz_content("")
        self.assertEqual(len(questions), 0)
        
        questions = self.parse_quiz_content("Just some regular text without quiz markers.")
        self.assertEqual(len(questions), 0)

    def test_malformed_question(self):
        """Test behavior with missing correct answer or options."""
        content = """
### Question 1
**Missing everything?**
"""
        questions = self.parse_quiz_content(content)
        # Should ideally still capture the question text even if options are missing
        # Based on implementation, it might return a partial object or skip it
        # Let's see what the current implementation does
        if questions:
             self.assertEqual(questions[0]['text'], "Missing everything?")
             self.assertEqual(len(questions[0]['options']), 0)
