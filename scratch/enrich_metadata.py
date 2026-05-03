import os
import re
import frontmatter
from pathlib import Path

CURRICULUM_DIR = Path(r'd:\LMS\Ai-basicscourse\curriculum')

def extract_title(content):
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def extract_duration(content):
    match = re.search(r'\*\*Duration:\*\*\s*(.+)', content)
    if not match:
        match = re.search(r'Duration:\s*(.+)', content)
    if match:
        return match.group(1).strip()
    return "30-60 min"

def process_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if it already has frontmatter
    if content.startswith('---'):
        print(f"  Skipping {file_path.name} (already has frontmatter)")
        return

    title = extract_title(content)
    duration = extract_duration(content)
    
    # Determine difficulty based on week
    week_match = re.search(r'week(\d+)', str(file_path.parent))
    week_num = int(week_match.group(1)) if week_match else 1
    
    if week_num <= 2:
        difficulty = "Beginner"
    elif week_num <= 5:
        difficulty = "Intermediate"
    else:
        difficulty = "Advanced"

    # Tags based on content
    tags = []
    if 'prompt' in content.lower(): tags.append('prompting')
    if 'python' in content.lower(): tags.append('python')
    if 'rag' in content.lower(): tags.append('rag')
    if 'agent' in content.lower(): tags.append('agents')
    if 'automation' in content.lower(): tags.append('automation')
    if 'assessment' in file_path.name.lower(): tags.append('assessment')

    post = frontmatter.Post(content, 
                            title=title or file_path.stem,
                            duration=duration,
                            difficulty=difficulty,
                            week=week_num,
                            tags=tags)
    
    with open(file_path, 'wb') as f:
        frontmatter.dump(post, f)

def main():
    for week_dir in sorted(CURRICULUM_DIR.glob('week*')):
        if week_dir.is_dir():
            for md_file in week_dir.glob('*.md'):
                process_file(md_file)

if __name__ == "__main__":
    main()
