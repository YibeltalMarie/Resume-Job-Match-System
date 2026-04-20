"""
Test script for Phase 1 text extraction.
Works with your current folder structure.
"""
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.resume_parser.text_extraction.extractor_factory import ExtractorFactory

def test_extraction(file_path: Path):
    """Test extraction on a single file."""
    factory = ExtractorFactory()
    
    print(f"\n{'='*60}")
    print(f"Testing: {file_path.name}")
    print(f"Type: {file_path.suffix}")
    print(f"Size: {file_path.stat().st_size} bytes")
    print(f"{'='*60}")
    
    try:
        # Read file as bytes
        with open(file_path, 'rb') as f:
            file_bytes = f.read()
        
        # Get the correct extractor
        extractor = factory.get_extractor(str(file_path))
        
        # Extract text
        text = extractor.extract(file_bytes)
        
        if text:
            print(f"✅ Extraction successful!")
            print(f"   Characters extracted: {len(text)}")
            print(f"\n--- First 500 characters ---")
            print(text[:500])
            
            if len(text) < 100:
                print(f"\n⚠️ Warning: Very little text extracted. File may be image-based PDF.")
        else:
            print(f"⚠️ Extraction returned empty string")
        
    except ValueError as e:
        print(f"❌ Unsupported file type: {e}")
    except Exception as e:
        print(f"❌ Failed: {e}")
        import traceback
        traceback.print_exc()

# ============================================
# Scan your actual folder structure
# ============================================

test_base = Path("data/test_resumes")

# Look for files in pdf/ and txt/ folders
test_files = []

# Check pdf folder
pdf_folder = test_base / "pdf"
if pdf_folder.exists():
    for f in pdf_folder.glob("*.pdf"):
        test_files.append(f)

# Check txt folder
txt_folder = test_base / "txt"
if txt_folder.exists():
    for f in txt_folder.glob("*.txt"):
        test_files.append(f)
    
# Also check docx files
for f in txt_folder.glob("*.docx"):
    test_files.append(f)

if test_files:
    print(f"\n📄 Found {len(test_files)} test file(s)")
    for file_path in test_files:
        test_extraction(file_path)
else:
    print("\n❌ No test files found in:")
    print(f"   - {test_base}/pdf/")
    print(f"   - {test_base}/txt/")
    print(f"\nBut I see you have files! Let me check directly...")
    
    # Direct check
    print(f"\nDirect inspection:")
    print(f"PDF folder exists: {pdf_folder.exists()}")
    if pdf_folder.exists():
        print(f"PDF files: {list(pdf_folder.glob('*'))}")
    print(f"TXT folder exists: {txt_folder.exists()}")
    if txt_folder.exists():
        print(f"TXT/DOCX files: {list(txt_folder.glob('*'))}")