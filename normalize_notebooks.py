#!/usr/bin/env python3
"""
Normalize Jupyter notebooks by adding missing cell IDs.
This fixes the MissingIDFieldWarning from nbformat.
"""
import nbformat
import sys
import os
from pathlib import Path

def normalize_notebook(filepath):
    """Normalize a notebook by adding missing cell IDs."""
    try:
        # Read the notebook
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Normalize (adds missing IDs automatically)
        nb = nbformat.v4.upgrade(nb)
        nbformat.validate(nb)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        return True
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python normalize_notebooks.py <file1.ipynb> [file2.ipynb ...]")
        print("   Or: python normalize_notebooks.py <directory>")
        sys.exit(1)
    
    paths = sys.argv[1:]
    files_to_process = []
    
    # Collect all notebook files
    for path in paths:
        p = Path(path)
        if p.is_file() and p.suffix == '.ipynb':
            files_to_process.append(p)
        elif p.is_dir():
            # Recursively find all .ipynb files
            files_to_process.extend(p.rglob('*.ipynb'))
    
    if not files_to_process:
        print("❌ No notebook files found")
        sys.exit(1)
    
    print(f"Found {len(files_to_process)} notebook(s) to process\n")
    
    success_count = 0
    fail_count = 0
    
    for filepath in files_to_process:
        print(f"Processing: {filepath}")
        if normalize_notebook(filepath):
            print(f"  ✅ Normalized successfully")
            success_count += 1
        else:
            fail_count += 1
        print()
    
    print(f"\n{'='*50}")
    print(f"✅ Successfully normalized: {success_count}")
    if fail_count > 0:
        print(f"❌ Failed: {fail_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
