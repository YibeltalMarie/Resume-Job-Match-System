"""
Degree normalizer - standardizes degree names.
"""

import re
from typing import List, Dict


class DegreeNormalizer:
    """
    Normalizes degree names to standard format.
    
    Examples:
        "BSc" -> "Bachelor of Science"
        "MSc" -> "Master of Science"
        "PhD" -> "Doctor of Philosophy"
    """
    
    DEGREE_MAPPING = {
        # Bachelor's degrees
        "bsc": "Bachelor of Science",
        "b.s.": "Bachelor of Science",
        "bs": "Bachelor of Science",
        "b.a.": "Bachelor of Arts",
        "ba": "Bachelor of Arts",
        "beng": "Bachelor of Engineering",
        "b.e.": "Bachelor of Engineering",
        "btech": "Bachelor of Technology",
        "b.tech": "Bachelor of Technology",
        "bba": "Bachelor of Business Administration",
        "b.b.a.": "Bachelor of Business Administration",
        
        # Master's degrees
        "msc": "Master of Science",
        "m.s.": "Master of Science",
        "ms": "Master of Science",
        "m.a.": "Master of Arts",
        "ma": "Master of Arts",
        "meng": "Master of Engineering",
        "m.e.": "Master of Engineering",
        "mtech": "Master of Technology",
        "m.tech": "Master of Technology",
        "mba": "Master of Business Administration",
        "m.b.a.": "Master of Business Administration",
        
        # Doctoral degrees
        "phd": "Doctor of Philosophy",
        "ph.d.": "Doctor of Philosophy",
        "dphil": "Doctor of Philosophy",
        "edd": "Doctor of Education",
        "dba": "Doctor of Business Administration",
        
        # Professional degrees
        "jd": "Juris Doctor",
        "j.d.": "Juris Doctor",
        "md": "Doctor of Medicine",
        "m.d.": "Doctor of Medicine",
    }
    
    def normalize(self, degree: str) -> str:
        """
        Normalize a single degree name.
        """
        if not degree:
            return degree
        
        degree_lower = degree.lower().strip()
        
        # Remove field in parentheses
        degree_lower = re.sub(r'\s*\([^)]+\)', '', degree_lower)
        
        # Check mapping
        if degree_lower in self.DEGREE_MAPPING:
            return self.DEGREE_MAPPING[degree_lower]
        
        # Fix: Use proper title case (not .title() which capitalizes every word)
        # "Master of Science" not "Master Of Science"
        words = degree.split()
        if len(words) >= 3 and words[1].lower() == 'of':
            # Keep 'of' lowercase
            words[1] = 'of'
            return ' '.join(words)
        
        return degree
    
    def normalize_education(self, education: List[Dict]) -> List[Dict]:
        """
        Normalize degree names in education entries.
        
        Args:
            education: List of education dictionaries
            
        Returns:
            Same list with normalized degree names
        """
        for edu in education:
            if "degree" in edu:
                edu["degree"] = self.normalize(edu["degree"])
        return education