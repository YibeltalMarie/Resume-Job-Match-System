"""
Education data model.
Represents a single education entry (degree, institution, year).
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Education:
    """
    Education entry from a resume.
    
    Attributes:
        degree: Degree name (e.g., "Bachelor of Science in Computer Science")
        institution: School/University name (e.g., "Stanford University")
        year: Graduation year (e.g., "2020")
    """
    degree: str
    institution: str
    year: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "degree": self.degree,
            "institution": self.institution,
        }
        if self.year:
            result["year"] = self.year
        return result
    
    def __str__(self) -> str:
        return f"{self.degree} from {self.institution} ({self.year or 'year unknown'})"