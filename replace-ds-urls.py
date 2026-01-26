#!/usr/bin/env python3
"""
DS Healthcare Image URL Replacement Script
Replaces external digitalscientists.com image URLs with local paths
"""

import os
import re
import sys
from pathlib import Path

def get_local_images(images_dir):
    """Get set of available local image filenames"""
    images = set()
    if os.path.exists(images_dir):
        for f in os.listdir(images_dir):
            images.add(f.lower())  # lowercase for matching
            images.add(f)  # original case
    return images

def extract_filename_from_url(url):
    """Extract filename from DS.com URL"""
    # Pattern: https://digitalscientists.com/wp-content/uploads/YYYY/MM/filename.ext
    match = re.search(r'/([^/]+\.(png|jpg|jpeg|svg|gif|webp))(?:\?.*)?$', url, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def replace_ds_urls(html_content, local_images, filename):
    """Replace DS.com URLs with local paths"""
    changes = []
    
    # Pattern to match DS.com image URLs
    pattern = r'(src|href)=["\']?(https://digitalscientists\.com/wp-content/uploads/[^"\'>\s]+)["\']?'
    
    def replace_match(match):
        attr = match.group(1)
        url = match.group(2)
        extracted_filename = extract_filename_from_url(url)
        
        if extracted_filename:
            # Check if we have this file locally (case-insensitive)
            local_match = None
            for local_file in local_images:
                if local_file.lower() == extracted_filename.lower():
                    local_match = local_file
                    break
            
            if local_match:
                new_ref = f'{attr}="images/{local_match}"'
                changes.append(f"  {extracted_filename}: {url[:50]}... → images/{local_match}")
                return new_ref
            else:
                changes.append(f"  [MISSING] {extracted_filename}: {url[:60]}...")
        
        return match.group(0)  # Return unchanged if no local file
    
    new_content = re.sub(pattern, replace_match, html_content)
    
    return new_content, changes

def process_html_files(repo_dir, dry_run=True):
    """Process all HTML files in the repo"""
    images_dir = os.path.join(repo_dir, 'images')
    local_images = get_local_images(images_dir)
    
    print(f"Found {len(local_images)} local images")
    print(f"Mode: {'DRY RUN (no changes)' if dry_run else 'LIVE (making changes)'}")
    print("=" * 60)
    
    total_changes = 0
    missing_images = set()
    
    for html_file in Path(repo_dir).glob('*.html'):
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if file has DS.com URLs
        if 'digitalscientists.com/wp-content/uploads' not in content:
            continue
        
        new_content, changes = replace_ds_urls(content, local_images, html_file.name)
        
        if changes:
            print(f"\n📄 {html_file.name}")
            for change in changes:
                if '[MISSING]' in change:
                    # Extract filename from missing message
                    match = re.search(r'\[MISSING\] ([^:]+):', change)
                    if match:
                        missing_images.add(match.group(1))
                print(change)
                total_changes += 1
            
            if not dry_run and new_content != content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ✓ File updated")
    
    print("\n" + "=" * 60)
    print(f"Total replacements: {total_changes}")
    
    if missing_images:
        print(f"\n⚠️  Missing images ({len(missing_images)}):")
        for img in sorted(missing_images):
            print(f"  - {img}")
    
    if dry_run:
        print("\n👆 This was a DRY RUN. To apply changes, run:")
        print(f"   python3 {sys.argv[0]} --apply")

if __name__ == '__main__':
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check for --apply flag
    dry_run = '--apply' not in sys.argv
    
    process_html_files(repo_dir, dry_run=dry_run)
