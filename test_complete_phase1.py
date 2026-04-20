"""
Complete Phase 1 test - end to end.
"""

from pathlib import Path
from backend.resume_parser import ResumeParser

# Initialize parser
parser = ResumeParser()

# Test file
file_path = Path("data/test_resumes/pdf/sample_pdf.pdf")

if file_path.exists():
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    
    # Parse
    result = parser.parse(file_bytes, file_path.name)
    
    # Print result
    print("\n" + "="*60)
    print("PHASE 1 COMPLETE - FINAL OUTPUT")
    print("="*60 + "\n")
    print(result)
    
    # Save to file
    output_path = Path("data/exports/parsed_resume.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result)
    print(f"\n✅ Output saved to: {output_path}")
else:
    print(f"File not found: {file_path}")