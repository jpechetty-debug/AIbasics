import re
import frontmatter

def parse_quiz_content(content):
    """Robustly parse questions, options, feedback, and metadata from markdown content."""
    questions = []
    
    # 1. Try to parse from frontmatter first (more robust)
    try:
        post = frontmatter.loads(content)
        if 'quiz' in post.metadata:
            return post.metadata['quiz']
    except Exception:
        pass

    # 2. Fallback to regex parsing if not in frontmatter
    # Remove frontmatter if present for regex parsing
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    
    # Use ### Question N or **Q N: as question markers
    question_blocks = re.split(r'### Question \s*\d+|\*\*Q\d+:', content)[1:]
    
    for i, block in enumerate(question_blocks, start=1):
        # Extract question text
        q_text_match = re.search(r'\*\*(.+?)\*\*', block)
        if q_text_match:
            q_text = q_text_match.group(1).strip()
        else:
            lines = [l.strip() for l in block.split('\n') if l.strip()]
            q_text = lines[0] if lines else f"Question {i}"
        
        # Extract options
        options = []
        option_matches = re.findall(r'^\s*([A-E])\)\s*(.+?)(?=\n\s*[A-E]\)|$|(?:\n\s*\*\*))', block, re.MULTILINE | re.DOTALL)
        for opt_letter, opt_text in option_matches:
            options.append({
                'letter': opt_letter.strip(),
                'text': opt_text.strip().replace('\n', ' ').strip().replace('**', '')
            })
        
        # Extract correct answer
        correct_match = re.search(r'\*\*Correct Answer(?:s?):\*\*\s*([A-E, \s]+)', block, re.IGNORECASE)
        if not correct_match:
            correct_match = re.search(r'Correct Answer:\s*([A-E, \s]+)', block, re.IGNORECASE)
        
        if not correct_match: continue
        correct = [c.strip() for c in correct_match.group(1).split(',')]
        
        # Extract feedback
        feedback_match = re.search(r'\*\*Feedback:\*\*\s*\n(.*?)(?=\n\s*---|\n\s*\*\*Why|$)', block, re.DOTALL)
        if not feedback_match:
            feedback_match = re.search(r'Feedback:\s*\n(.*?)(?=\n\s*---|\n\s*\*\*Why|$)', block, re.DOTALL)
        
        feedback = feedback_match.group(1).strip() if feedback_match else ""
        
        # Extract "Why this matters"
        why_match = re.search(r'\*\*Why this matters.*?\*\*\s*:?\s*(.*?)(?=\n\s*---|$)', block, re.DOTALL | re.IGNORECASE)
        why_matters = why_match.group(1).strip() if why_match else ""
        
        q_type = 'multiple' if len(correct) > 1 else 'single'
        
        questions.append({
            'number': i,
            'text': q_text,
            'options': options,
            'correct': correct,
            'type': q_type,
            'feedback': feedback,
            'why_matters': why_matters
        })
        
    return questions
