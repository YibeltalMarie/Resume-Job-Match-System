"""
Field mapper - converts extracted fields to the standard output schema.
"""

from typing import Dict, List, Optional


class FieldMapper:
    """
    Maps extracted fields to the required output format.
    Ensures field names match the competition schema.
    """
    
    def map_to_schema(self, extracted: Dict) -> Dict:
        """
        Convert extracted fields to standard schema.
        
        Args:
            extracted: Raw extracted fields from strategy
            
        Returns:
            Mapped fields ready for normalization
        """
        return {
            "name": self._map_name(extracted.get("name")),
            "email": self._map_email(extracted.get("email")),
            "skills": self._map_skills(extracted.get("skills", [])),
            "experience": self._map_experience(extracted.get("experience", [])),
            "education": self._map_education(extracted.get("education", [])),
        }
    
    def _map_name(self, name: Optional[str]) -> str:
        """Ensure name is a string."""
        if name and isinstance(name, str) and name.strip():
            return name.strip()
        return "Unknown"
    
    def _map_email(self, email: Optional[str]) -> Optional[str]:
        """Ensure email is valid format."""
        if email and isinstance(email, str) and '@' in email:
            return email.strip().lower()
        return None
    
    def _map_skills(self, skills: List) -> List[str]:
        """Ensure skills is a list of strings."""
        if not skills:
            return []
        return [str(skill).strip() for skill in skills if skill]
    
    def _map_experience(self, experience: List) -> List[Dict]:
        """Ensure each experience entry has required fields."""
        mapped = []
        for exp in experience:
            if isinstance(exp, dict):
                mapped.append({
                    "role": exp.get("role", "Unknown"),
                    "company": exp.get("company", "Unknown"),
                    "years": float(exp.get("years", 0))
                })
        return mapped
    
    def _map_education(self, education: List) -> List[Dict]:
        """Ensure each education entry has required fields."""
        mapped = []
        for edu in education:
            if isinstance(edu, dict):
                mapped.append({
                    "degree": edu.get("degree", "Unknown"),
                    "institution": edu.get("institution", "Unknown"),
                    "year": edu.get("year")
                })
        return mapped