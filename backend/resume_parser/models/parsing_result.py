"""
Parsing result data model.
Wraps a Resume object with metadata about extraction quality.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from .resume import Resume


@dataclass
class ParsingResult:
    """
    Result of parsing a resume, including metadata.
    
    Attributes:
        resume: The parsed Resume object
        confidence: Overall confidence score (0-1)
        warnings: List of warning messages
        processing_time_ms: Time taken to parse in milliseconds
        raw_text: Original extracted text (for debugging)
    """
    resume: Resume
    confidence: float
    warnings: List[str] = field(default_factory=list)
    processing_time_ms: float = 0.0
    raw_text: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "resume": self.resume.to_dict(),
            "_metadata": {
                "confidence": self.confidence,
                "warnings": self.warnings,
                "processing_time_ms": self.processing_time_ms
            }
        }
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def is_valid(self) -> bool:
        """Check if parsing was successful enough."""
        # Consider valid if confidence > 0.5 or we have at least name+email
        if self.confidence > 0.5:
            return True
        if self.resume.name != "Unknown" and self.resume.email:
            return True
        return False
    
    def __str__(self) -> str:
        return f"ParsingResult(confidence={self.confidence}, valid={self.is_valid()}, warnings={len(self.warnings)})"