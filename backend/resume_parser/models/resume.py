"""
Resume data model.
Represents the complete parsed resume with all fields.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from .education import Education
from .experience import Experience


@dataclass
class Resume:
    """
    Complete parsed resume.
    
    Attributes:
        candidate_id: Unique identifier (auto-generated)
        name: Candidate's full name
        email: Candidate's email address
        skills: List of technical/professional skills
        education: List of Education objects
        experience: List of Experience objects
        total_experience_years: Sum of all experience years
    """
    candidate_id: str
    name: str
    email: Optional[str]
    skills: List[str] = field(default_factory=list)
    education: List[Education] = field(default_factory=list)
    experience: List[Experience] = field(default_factory=list)
    total_experience_years: float = 0.0
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "candidate_id": self.candidate_id,
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "education": [edu.to_dict() for edu in self.education],
            "experience": [exp.to_dict() for exp in self.experience],
            "total_experience_years": self.total_experience_years
        }
    
    def __str__(self) -> str:
        return f"Resume(id={self.candidate_id}, name={self.name}, skills={len(self.skills)}, experience={self.total_experience_years}yrs)"