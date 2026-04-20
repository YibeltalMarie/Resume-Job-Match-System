from pathlib import Path
from backend.resume_parser.text_extraction.extractor_factory import ExtractorFactory

# Extract text
factory = ExtractorFactory()
file_path = Path("data/test_resumes/pdf/sample_pdf.pdf")

with open(file_path, 'rb') as f:
    file_bytes = f.read()

extractor = factory.get_extractor(str(file_path))
raw_text = extractor.extract(file_bytes)

print("=== RAW TEXT (showing where pipes are) ===\n")
print(repr(raw_text))
print("\n=== LINES ===\n")
for i, line in enumerate(raw_text.split('\n')):
    if '|' in line:
        print(f"Line {i}: {repr(line)}")