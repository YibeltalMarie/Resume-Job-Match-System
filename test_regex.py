"""
Test regex field extraction on a resume file.
"""

from pathlib import Path
from backend.resume_parser.text_extraction.extractor_factory import ExtractorFactory
from backend.resume_parser.field_extraction.strategies.regex_strategy import RegexStrategy
from backend.resume_parser.field_extraction.field_mapper import FieldMapper

def test_regex_extraction(file_path: Path):
    """Test regex extraction on a file."""
    
    # Step 1: Extract text
    factory = ExtractorFactory()
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    
    extractor = factory.get_extractor(str(file_path))
    raw_text = extractor.extract(file_bytes)
    
    print(f"\n{'='*60}")
    print(f"Testing: {file_path.name}")
    print(f"Text length: {len(raw_text)} characters")
    print(f"{'='*60}")
    
    # Step 2: Extract fields using regex
    strategy = RegexStrategy()
    extracted = strategy.extract_fields(raw_text)
    
    # Step 3: Map to schema
    mapper = FieldMapper()
    mapped = mapper.map_to_schema(extracted)
    
    # Step 4: Display results
    print("\n📌 EXTRACTED FIELDS:")
    print(f"   Name: {mapped['name']}")
    print(f"   Email: {mapped['email']}")
    print(f"   Skills: {', '.join(mapped['skills']) if mapped['skills'] else 'None'}")
    
    print(f"\n💼 Experience ({len(mapped['experience'])} entries):")
    for exp in mapped['experience']:
        print(f"   - {exp['role']} at {exp['company']} ({exp['years']} years)")
    
    print(f"\n🎓 Education ({len(mapped['education'])} entries):")
    for edu in mapped['education']:
        year_str = f", {edu['year']}" if edu['year'] else ""
        print(f"   - {edu['degree']} from {edu['institution']}{year_str}")
    
    return mapped

# Test on your resume
test_file = Path("data/test_resumes/txt/sample_pdf.pdf")

if not test_file.exists():
    # Try PDF folder
    test_file = Path("data/test_resumes/pdf/sample_pdf.pdf")

if test_file.exists():
    result = test_regex_extraction(test_file)
    
    print(f"\n{'='*60}")
    print("✅ Regex extraction complete!")
else:
    print(f"❌ No test file found at: {test_file}")
    print("Please ensure you have a resume file in data/test_resumes/txt/ or data/test_resumes/pdf/")