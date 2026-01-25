#!/usr/bin/env python3
"""
DS Healthcare - Clean Nav & Footer Replacement
===============================================
Removes ALL old navigation and footer content, then inserts new versions.

Usage:
    python3 clean-nav-footer.py
"""

import os
import re
import glob
from datetime import datetime

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
NAV_FILE = os.path.join(REPO_DIR, 'ds-nav-final.html')
FOOTER_FILE = os.path.join(REPO_DIR, 'ds-footer-final.html')
BACKUP_DIR = os.path.join(REPO_DIR, 'backups_clean', datetime.now().strftime('%Y%m%d_%H%M%S'))

SKIP_FILES = [
    'ds-nav-final.html',
    'ds-footer-final.html', 
    'ds-nav-v2.html',
    'ds-footer-v2.html',
    'ds-footer-v3.html',
    'healthcare-hub-preview.html',
    'update-nav-footer.py',
    'update-nav-footer-fix.py',
    'clean-nav-footer.py',
]


def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def backup_file(filepath):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    filename = os.path.basename(filepath)
    backup_path = os.path.join(BACKUP_DIR, filename)
    content = load_file(filepath)
    save_file(backup_path, content)


def find_content_start(content):
    """Find where the actual page content starts (after all nav stuff)."""
    # Look for common content markers
    patterns = [
        r'<!-- Hero Section -->',
        r'<!-- Hero -->',
        r'<header class="relative pt-',
        r'<header class="pt-',
        r'<!-- Main Content -->',
        r'<main',
        r'<!-- Page Content -->',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.start()
    
    return None


def find_footer_start(content):
    """Find where the footer section starts."""
    # Look for footer markers - find the FIRST one
    patterns = [
        r'\n<!-- Footer -->',
        r'\n<footer class=',
        r'\n<!-- DS 2\.0 Footer',
        r'\n<!-- START DS-FOOTER -->',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.start()
    
    return None


def update_html_file(filepath, nav_content, footer_content):
    """Clean and update a single HTML file."""
    try:
        content = load_file(filepath)
        
        # Find the <body> tag
        body_match = re.search(r'<body[^>]*>', content)
        if not body_match:
            return False, "No <body> tag found"
        
        body_end = body_match.end()
        
        # Find where content starts
        content_start = find_content_start(content)
        if not content_start:
            return False, "Could not find content start"
        
        # Find where footer starts
        footer_start = find_footer_start(content)
        if not footer_start:
            return False, "Could not find footer"
        
        # Find </body> tag
        body_close_match = re.search(r'</body>', content, re.IGNORECASE)
        if not body_close_match:
            return False, "No </body> tag found"
        
        # Build the new file:
        # 1. Everything up to and including <body>
        # 2. New nav
        # 3. Content (from content_start to footer_start)
        # 4. New footer
        # 5. </body></html>
        
        new_content = (
            content[:body_end] +
            '\n' + nav_content + '\n\n' +
            content[content_start:footer_start].strip() +
            '\n\n' + footer_content + '\n\n' +
            content[body_close_match.start():]
        )
        
        # Backup and save
        backup_file(filepath)
        save_file(filepath, new_content)
        
        return True, "Updated"
        
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    print("=" * 60)
    print("DS Healthcare - Clean Nav & Footer Replacement")
    print("=" * 60)
    
    if not os.path.exists(NAV_FILE):
        print(f"ERROR: {NAV_FILE} not found")
        return
    
    if not os.path.exists(FOOTER_FILE):
        print(f"ERROR: {FOOTER_FILE} not found")
        return
    
    nav_content = load_file(NAV_FILE)
    footer_content = load_file(FOOTER_FILE)
    
    print(f"Nav: {len(nav_content)} chars")
    print(f"Footer: {len(footer_content)} chars")
    print()
    
    html_files = glob.glob(os.path.join(REPO_DIR, '*.html'))
    html_files = [f for f in html_files if os.path.basename(f) not in SKIP_FILES]
    
    print(f"Processing {len(html_files)} files...")
    print("-" * 60)
    
    success = 0
    errors = 0
    
    for filepath in sorted(html_files):
        filename = os.path.basename(filepath)
        ok, msg = update_html_file(filepath, nav_content, footer_content)
        
        if ok:
            print(f"✓ {filename}")
            success += 1
        else:
            print(f"✗ {filename}: {msg}")
            errors += 1
    
    print("-" * 60)
    print(f"Done: {success} updated, {errors} errors")
    print(f"Backups: {BACKUP_DIR}")
    print()
    print("Next: In GitHub Desktop, commit and push")


if __name__ == '__main__':
    main()
