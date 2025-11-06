#!/usr/bin/env python3
"""
Batch translation script for Angular documentation files.
This script reads Japanese markdown files and creates English translations.
"""

import os
import glob

# Base directory
BASE_DIR = r"C:\Users\Admin\coding\movie\angular\document"

# Standard section heading translations
TRANSLATIONS = {
    "概要": "Overview",
    "学習目標": "Learning Objectives",
    "技術ポイント": "Technical Points",
    "📺 画面表示用コード(動画用)": "📺 On-Screen Code (for video)",
    "📺 画面表示用コード(動画用)": "📺 On-Screen Code (for video)",
    "💻 詳細実装例(学習用)": "💻 Detailed Implementation Example (for learning)",
    "💻 詳細実装例(学習用)": "💻 Detailed Implementation Example (for learning)",
    "ベストプラクティス": "Best Practices",
    "注意点": "Considerations",
    "関連技術": "Related Technologies",
}

def get_files_to_translate(start, end):
    """Get list of files to translate in range"""
    files = []
    for i in range(start, end + 1):
        pattern = os.path.join(BASE_DIR, f"{i}_*.md")
        matches = glob.glob(pattern)
        if matches:
            # Exclude already translated files
            matches = [m for m in matches if not m.endswith('-en.md')]
            if matches:
                files.append(matches[0])
    return files

def main():
    # Get files from 441 to 500
    files = get_files_to_translate(441, 500)
    print(f"Found {len(files)} files to translate")
    for f in files:
        print(f"  - {os.path.basename(f)}")

if __name__ == "__main__":
    main()
