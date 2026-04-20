"""
Test normalization on extracted data.
"""
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.resume_parser.text_extraction.extractor_factory import ExtractorFactory
from backend.resume_parser.field_extraction.strategies.regex_strategy import RegexStrategy
from backend.resume_parser.normalization.normalizer_pipeline import NormalizerPipeline

# Extract text
factory = ExtractorFactory()
file_path = Path("data/test_resumes/pdf/sample_pdf.pdf")

with open(file_path, 'rb') as f:
    file_bytes = f.read()

extractor = factory.get_extractor(str(file_path))
raw_text = extractor.extract(file_bytes)

# Extract fields
strategy = RegexStrategy()
extracted = strategy.extract_fields(raw_text)

print("=== BEFORE NORMALIZATION ===\n")
print(f"Skills: {extracted['skills']}")
print(f"Experience: {extracted['experience']}")
print(f"Education: {extracted['education']}")

# Normalize
pipeline = NormalizerPipeline()
normalized = pipeline.normalize(extracted)

print("\n=== AFTER NORMALIZATION ===\n")
print(f"Skills: {normalized['skills']}")
print(f"Experience: {normalized['experience']}")
print(f"Education: {normalized['education']}")
print(f"Total Experience Years: {normalized.get('total_experience_years', 0)}")