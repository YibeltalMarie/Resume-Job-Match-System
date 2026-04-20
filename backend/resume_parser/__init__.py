"""
Main ResumeParser orchestrator - ties all modules together.
"""

import time
from typing import Dict, Optional
from pathlib import Path

from .text_extraction.extractor_factory import ExtractorFactory
from .field_extraction.strategies.regex_strategy import RegexStrategy
from .field_extraction.field_mapper import FieldMapper
from .normalization.normalizer_pipeline import NormalizerPipeline
from .validation.schema_validator import SchemaValidator
from .validation.confidence_scorer import ConfidenceScorer
from .validation.missing_field_handler import MissingFieldHandler
from .output.json_generator import JSONGenerator


class ResumeParser:
    """
    Main orchestrator for resume parsing.
    
    Usage:
        parser = ResumeParser()
        result = parser.parse(file_bytes, "resume.pdf")
        print(result)
    """
    
    def __init__(self):
        self.extractor_factory = ExtractorFactory()
        self.extraction_strategy = RegexStrategy()
        self.field_mapper = FieldMapper()
        self.normalizer = NormalizerPipeline()
        self.validator = SchemaValidator()
        self.confidence_scorer = ConfidenceScorer()
        self.missing_handler = MissingFieldHandler()
        self.json_generator = JSONGenerator()
    
    def parse(self, file_bytes: bytes, filename: str) -> str:
        """
        Parse a resume file and return JSON output.
        
        Args:
            file_bytes: Raw file bytes
            filename: Original filename (to determine format)
            
        Returns:
            JSON string matching competition schema
        """
        start_time = time.time()
        warnings = []
        
        # Step 1: Extract raw text
        try:
            extractor = self.extractor_factory.get_extractor(filename)
            raw_text = extractor.extract(file_bytes)
        except Exception as e:
            warnings.append(f"Text extraction failed: {str(e)}")
            raw_text = ""
        
        # Step 2: Extract fields using regex
        try:
            extracted = self.extraction_strategy.extract_fields(raw_text)
        except Exception as e:
            warnings.append(f"Field extraction failed: {str(e)}")
            extracted = {}
        
        # Step 3: Map to schema
        mapped = self.field_mapper.map_to_schema(extracted)
        
        # Step 4: Normalize
        normalized = self.normalizer.normalize(mapped)
        
        # Step 5: Handle missing fields
        complete = self.missing_handler.handle(normalized)
        
        # Step 6: Calculate confidence
        confidence = self.confidence_scorer.calculate(complete)
        
        # Step 7: Validate schema
        is_valid, errors = self.validator.validate(complete)
        if not is_valid:
            warnings.extend(errors)
        
        # Step 8: Generate JSON
        processing_time_ms = (time.time() - start_time) * 1000
        json_output = self.json_generator.generate(
            resume_data=complete,
            confidence=confidence,
            warnings=warnings,
            processing_time_ms=processing_time_ms
        )
        
        return json_output