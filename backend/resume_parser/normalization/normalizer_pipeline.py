"""
Normalizer pipeline - runs all normalizers in sequence.
"""

from typing import Dict, List
from .skill_normalizer import SkillNormalizer
from .company_normalizer import CompanyNormalizer
from .degree_normalizer import DegreeNormalizer
from .data_parser import DateParser


class NormalizerPipeline:
    """
    Runs all normalizers on extracted data.
    
    Order:
    1. Skills normalization
    2. Company normalization
    3. Degree normalization
    4. Date/year calculation
    """
    
    def __init__(self):
        self.skill_normalizer = SkillNormalizer()
        self.company_normalizer = CompanyNormalizer()
        self.degree_normalizer = DegreeNormalizer()
        self.date_parser = DateParser()
    
    def normalize(self, extracted_data: Dict) -> Dict:
        """
        Normalize all fields in extracted data.
        
        Args:
            extracted_data: Dictionary with extracted fields
            
        Returns:
            Normalized dictionary
        """
        result = extracted_data.copy()
        
        # Normalize skills
        if "skills" in result and result["skills"]:
            result["skills"] = self.skill_normalizer.normalize_list(result["skills"])
        
        # Normalize experience (company names)
        if "experience" in result and result["experience"]:
            result["experience"] = self.company_normalizer.normalize_experience(result["experience"])
        
        # Normalize education (degree names)
        if "education" in result and result["education"]:
            result["education"] = self.degree_normalizer.normalize_education(result["education"])
        
        # Calculate total experience years
        if "experience" in result:
            total_years = self.date_parser.parse_experience_years(result["experience"])
            result["total_experience_years"] = total_years
        
        return result