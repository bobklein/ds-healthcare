#!/usr/bin/env python3
"""
DS Healthcare Site - Nav & Footer Updater
==========================================
Updates all HTML files in the ds-healthcare repo with new nav and footer.

Usage:
    1. Place this script in your ds-healthcare folder
    2. Place ds-nav-final.html and ds-footer-final.html in the same folder
    3. Run: python3 update-nav-footer.py
    4. Review changes, then: git add . && git commit -m "Update nav and footer" && git push
"""

import os
import re
import glob
from datetime import datetime

# Configuration
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
NAV_FILE = os.path.join(REPO_DIR, 'ds-nav-final.html')
FOOTER_FILE = os.path.join(REPO_DIR, 'ds-footer-final.html')
BACKUP_DIR = os.path.join(REPO_DIR, 'backups', datetime.now().strftime('%Y%m%d_%H%M%S'))

# Files to skip
SKIP_FILES = [
    'ds-nav-final.html',
    'ds-footer-final.html',
    'ds-nav-v2.html',
    'ds-footer-v2.html',
    'ds-footer-v3.html',
    'healthcare-hub-preview.html',
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


def find_nav_boundaries(content):
    """
    Find the start and end of the navigation section.
    Returns (start_index, end_index) or (None, None) if not found.
    """
    # Pattern 1: DS-NAV markers (preferred)
    start_match = re.search(r'<!-- START DS-NAV -->', content)
    end_match = re.search(r'<!-- END DS-NAV -->', content)
    if start_match and end_match:
        return start_match.start(), end_match.end()
    
    # Pattern 2: Look for nav style block and mobile nav end
    style_match = re.search(r'<style>\s*/\*\s*(?:Utility Bar|Mega|Nav)', content)
    if style_match:
        # Find end of mobile nav div
        end_patterns = [
            r'<!-- END NAVIGATION -->',
            r'</div>\s*<!-- Mobile Navigation end -->',
            r'</div>\s*(?=\s*<!--\s*Hero)',
            r'</div>\s*(?=\s*<(?:header|main|section)\s)',
        ]
        for pattern in end_patterns:
            end_match = re.search(pattern, content[style_match.start():])
            if end_match:
                return style_match.start(), style_match.start() + end_match.end()
    
    # Pattern 3: Look for utility bar or main nav
    patterns = [
        (r'<div class="ds-utility-bar">', r'</div>\s*</div>\s*(?=<(?:header|main|section))'),
        (r'<!-- DS Healthcare Mega Menu Navigation -->', r'</div>\s*(?=\s*<!--\s*Hero)'),
        (r'<nav class="[^"]*main-nav[^"]*">', r'</nav>\s*(?:<div[^>]*mobile-nav)?.*?</div>\s*(?=<(?:header|main|section))'),
    ]
    
    for start_pattern, end_pattern in patterns:
        start_match = re.search(start_pattern, content, re.IGNORECASE | re.DOTALL)
        if start_match:
            end_match = re.search(end_pattern, content[start_match.start():], re.IGNORECASE | re.DOTALL)
            if end_match:
                return start_match.start(), start_match.start() + end_match.end()
    
    return None, None


def find_footer_boundaries(content):
    """
    Find the start and end of the footer section.
    Returns (start_index, end_index) or (None, None) if not found.
    """
    # Pattern 1: DS-FOOTER markers (preferred)
    start_match = re.search(r'<!-- START DS-FOOTER -->', content)
    end_match = re.search(r'<!-- END DS-FOOTER -->', content)
    if start_match and end_match:
        return start_match.start(), end_match.end()
    
    # Pattern 2: Find footer tag
    footer_match = re.search(r'<footer[^>]*>', content, re.IGNORECASE)
    if footer_match:
        # Find the closing </footer> tag
        close_match = re.search(r'</footer>', content[footer_match.start():], re.IGNORECASE)
        if close_match:
            return footer_match.start(), footer_match.start() + close_match.end()
    
    return None, None


def update_html_file(filepath, nav_content, footer_content):
    """
    Update a single HTML file with new nav and footer.
    Returns (success, message).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # Update navigation
        nav_start, nav_end = find_nav_boundaries(content)
        if nav_start is not None and nav_end is not None:
            content = content[:nav_start] + nav_content + content[nav_end:]
            changes.append('nav')
        else:
            # Try to insert after <body> tag
            body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
            if body_match:
                insert_pos = body_match.end()
                content = content[:insert_pos] + '\n' + nav_content + '\n' + content[insert_pos:]
                changes.append('nav (inserted)')
        
        # Update footer
        footer_start, footer_end = find_footer_boundaries(content)
        if footer_start is not None and footer_end is not None:
            content = content[:footer_start] + footer_content + content[footer_end:]
            changes.append('footer')
        else:
            # Try to insert before </body> tag
            body_end_match = re.search(r'</body>', content, re.IGNORECASE)
            if body_end_match:
                insert_pos = body_end_match.start()
                content = content[:insert_pos] + '\n' + footer_content + '\n' + content[insert_pos:]
                changes.append('footer (inserted)')
        
        if content != original_content:
            # Backup original
            backup_file(filepath)
            
            # Write updated content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, f"Updated: {', '.join(changes)}"
        else:
            return False, "No changes needed"
            
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    print("=" * 60)
    print("DS Healthcare - Nav & Footer Updater")
    print("=" * 60)
    print(f"\nRepository: {REPO_DIR}")
    print(f"Backups: {BACKUP_DIR}")
    print()
    
    # Check for required files
    if not os.path.exists(NAV_FILE):
        print(f"ERROR: Nav file not found: {NAV_FILE}")
        print("Please ensure ds-nav-final.html is in the same folder as this script.")
        return
    
    if not os.path.exists(FOOTER_FILE):
        print(f"ERROR: Footer file not found: {FOOTER_FILE}")
        print("Please ensure ds-footer-final.html is in the same folder as this script.")
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
    
    # Process each file
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for filepath in sorted(html_files):
        filename = os.path.basename(filepath)
        success, message = update_html_file(filepath, nav_content, footer_content)
        
        if success:
            print(f"✓ {filename}: {message}")
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
    print("Next steps:")
    print("  1. Review the changes in your editor or browser")
    print("  2. Test locally: open index.html in your browser")
    print("  3. Deploy: git add . && git commit -m 'Update nav and footer' && git push")


if __name__ == '__main__':
    main()
