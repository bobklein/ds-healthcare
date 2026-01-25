#!/usr/bin/env python3
"""
DS Healthcare Site - Nav & Footer Updater (FIXED)
==================================================
Properly removes old nav/footer before inserting new ones.

Usage:
    1. Place this script in your ds-healthcare folder
    2. Place ds-nav-final.html and ds-footer-final.html in the same folder
    3. Run: python3 update-nav-footer-fix.py
"""

import os
import re
import glob
from datetime import datetime

# Configuration
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
NAV_FILE = os.path.join(REPO_DIR, 'ds-nav-final.html')
FOOTER_FILE = os.path.join(REPO_DIR, 'ds-footer-final.html')
BACKUP_DIR = os.path.join(REPO_DIR, 'backups_fix', datetime.now().strftime('%Y%m%d_%H%M%S'))

# Files to skip
SKIP_FILES = [
    'ds-nav-final.html',
    'ds-footer-final.html',
    'ds-nav-v2.html',
    'ds-footer-v2.html',
    'ds-footer-v3.html',
    'healthcare-hub-preview.html',
    'update-nav-footer.py',
    'update-nav-footer-fix.py',
]


def load_component(filepath):
    """Load nav or footer component from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def backup_file(filepath):
    """Create backup of original file."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    filename = os.path.basename(filepath)
    backup_path = os.path.join(BACKUP_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return backup_path


def remove_all_navs(content):
    """Remove ALL navigation elements from the content."""
    
    # Pattern 1: Remove DS-NAV marked sections (may be multiple)
    content = re.sub(
        r'<!-- START DS-NAV -->.*?<!-- END DS-NAV -->\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Remove old style nav with mega-menu-container styles
    content = re.sub(
        r'<!-- DS Healthcare Mega Menu Navigation -->\s*<style>.*?</style>\s*.*?</nav>\s*<!-- Mobile Navigation -->.*?</div>\s*(?=\s*<!--\s*Hero|\s*<header|\s*<main|\s*<section)',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 3: Remove any standalone nav style blocks
    content = re.sub(
        r'<style>\s*\.mega-menu-container\s*\{.*?</style>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 4: Remove utility bar + main nav + mobile nav pattern
    content = re.sub(
        r'<div class="ds-utility-bar">.*?</div>\s*</div>\s*<!-- Mobile Navigation -->\s*<div id="ds-mobile-nav".*?</div>\s*(?=\s*<!--|\s*<header|\s*<main|\s*<section)',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 5: Remove any nav with sticky positioning
    content = re.sub(
        r'<!-- Utility Bar -->\s*<div class="ds-utility-bar">.*?<!-- END DS-NAV -->\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content


def remove_all_footers(content):
    """Remove ALL footer elements from the content."""
    
    # Pattern 1: Remove DS-FOOTER marked sections
    content = re.sub(
        r'<!-- START DS-FOOTER -->.*?<!-- END DS-FOOTER -->\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Remove any footer tag with dark background
    content = re.sub(
        r'<footer class="[^"]*bg-\[#2d2d2d\][^"]*".*?</footer>\s*(?:<!-- Pipedrive[^>]*-->\s*)?(?:<script[^>]*pipedrive[^>]*></script>\s*)?',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 3: Remove old footer with bg-dsBlack
    content = re.sub(
        r'<footer class="[^"]*bg-dsBlack[^"]*".*?</footer>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 4: Remove any remaining footer tags
    content = re.sub(
        r'<!-- Footer -->\s*<footer[^>]*>.*?</footer>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content


def update_html_file(filepath, nav_content, footer_content):
    """Update a single HTML file with new nav and footer."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Step 1: Remove ALL existing navs
        content = remove_all_navs(content)
        
        # Step 2: Remove ALL existing footers
        content = remove_all_footers(content)
        
        # Step 3: Clean up any leftover Pipedrive scripts
        content = re.sub(
            r'<script src="https://webforms\.pipedrive\.com/f/loader"></script>\s*',
            '',
            content
        )
        
        # Step 4: Insert new nav after <body>
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + nav_content + '\n' + content[insert_pos:]
        
        # Step 5: Insert new footer before </body>
        body_end_match = re.search(r'</body>', content, re.IGNORECASE)
        if body_end_match:
            insert_pos = body_end_match.start()
            content = content[:insert_pos] + '\n' + footer_content + '\n' + content[insert_pos:]
        
        # Step 6: Clean up excessive whitespace
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        if content != original_content:
            backup_file(filepath)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Updated"
        else:
            return False, "No changes needed"
            
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    print("=" * 60)
    print("DS Healthcare - Nav & Footer Updater (FIX)")
    print("=" * 60)
    print(f"\nRepository: {REPO_DIR}")
    print(f"Backups: {BACKUP_DIR}")
    print()
    
    # Check for required files
    if not os.path.exists(NAV_FILE):
        print(f"ERROR: Nav file not found: {NAV_FILE}")
        return
    
    if not os.path.exists(FOOTER_FILE):
        print(f"ERROR: Footer file not found: {FOOTER_FILE}")
        return
    
    # Load components
    nav_content = load_component(NAV_FILE)
    footer_content = load_component(FOOTER_FILE)
    
    print(f"Loaded nav component: {len(nav_content)} chars")
    print(f"Loaded footer component: {len(footer_content)} chars")
    print()
    
    # Find all HTML files
    html_files = glob.glob(os.path.join(REPO_DIR, '*.html'))
    html_files = [f for f in html_files if os.path.basename(f) not in SKIP_FILES]
    
    print(f"Found {len(html_files)} HTML files to process")
    print("-" * 60)
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for filepath in sorted(html_files):
        filename = os.path.basename(filepath)
        success, message = update_html_file(filepath, nav_content, footer_content)
        
        if success:
            print(f"✓ {filename}")
            success_count += 1
        elif "No changes" in message:
            print(f"- {filename}: {message}")
            skip_count += 1
        else:
            print(f"✗ {filename}: {message}")
            error_count += 1
    
    print("-" * 60)
    print(f"\nSummary:")
    print(f"  Updated: {success_count}")
    print(f"  Skipped: {skip_count}")
    print(f"  Errors:  {error_count}")
    print(f"\nBackups saved to: {BACKUP_DIR}")
    print()
    print("Next steps in GitHub Desktop:")
    print("  1. You'll see the changed files")
    print("  2. Type 'Fix nav and footer' in Summary")
    print("  3. Click 'Commit to main'")
    print("  4. Click 'Push origin'")


if __name__ == '__main__':
    main()
