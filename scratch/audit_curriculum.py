import os
import frontmatter
from pathlib import Path
import json

CURRICULUM_DIR = Path(r'd:\LMS\Ai-basicscourse\curriculum')
STRUCTURE_FILE = CURRICULUM_DIR / 'structure.json'

def audit_curriculum():
    print(f"--- Curriculum Audit: {CURRICULUM_DIR} ---")
    
    # 1. Check structure.json
    if not STRUCTURE_FILE.exists():
        print("[ERROR] structure.json is missing!")
    else:
        print("[OK] structure.json found.")
        try:
            with open(STRUCTURE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"[OK] structure.json is valid JSON. Course: {data.get('course_title')}")
        except Exception as e:
            print(f"[ERROR] structure.json is invalid: {e}")

    # 2. Check lessons
    required_fields = ['title', 'difficulty', 'duration', 'week']
    missing_metadata = []
    total_lessons = 0
    
    for week_dir in sorted(CURRICULUM_DIR.glob('week*')):
        if week_dir.is_dir():
            for md_file in week_dir.glob('*.md'):
                total_lessons += 1
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                    
                    missing = [field for field in required_fields if field not in post]
                    if missing:
                        missing_metadata.append(f"{md_file.relative_to(CURRICULUM_DIR)}: missing {missing}")
                except Exception as e:
                    missing_metadata.append(f"{md_file.relative_to(CURRICULUM_DIR)}: Error reading file ({e})")

    if not missing_metadata:
        print(f"[OK] All {total_lessons} lessons have required metadata.")
    else:
        print(f"[WARNING] {len(missing_metadata)} lessons have issues:")
        for issue in missing_metadata:
            print(f"  - {issue}")

    print("--- Audit Complete ---")

if __name__ == "__main__":
    audit_curriculum()
