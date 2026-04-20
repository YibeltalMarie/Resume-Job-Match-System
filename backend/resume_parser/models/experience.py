"""
Experience data model.
Represents a single work experience entry (role, company, years).
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Experience:
    """
    Work experience entry from a resume.
    
    Attributes:
        role: Job title (e.g., "Data Scientist", "Software Engineer")
        company: Employer name (e.g., "Google", "Amazon")
        years: Number of years in this role (calculated from dates)
    """
    role: str
    company: str
    years: float
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "role": self.role,
            "company": self.company,
            "years": self.years
        }
    
    def __str__(self) -> str:
        return f"{self.role} at {self.company} ({self.years} years)"