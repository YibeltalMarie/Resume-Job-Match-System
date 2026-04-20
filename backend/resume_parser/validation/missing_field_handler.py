"""
Missing field handler - adds default values for missing fields.
"""

from typing import Dict


class MissingFieldHandler:
    """
    Handles missing fields by adding default values.
    """
    
    DEFAULTS = {
        "candidate_id": None,  # Will be generated
        "name": "Unknown",
        "email": None,
        "skills": [],
        "education": [],
        "experience": [],
        "total_experience_years": 0,
    }
    
    def handle(self, data: Dict) -> Dict:
        """
        Add default values for missing fields.
        
        Args:
            data: Dictionary with extracted fields
            
        Returns:
            Dictionary with all fields populated
        """
        result = data.copy()
        
        for field, default_value in self.DEFAULTS.items():
            if field not in result or result[field] is None:
                result[field] = default_value
        
        # Generate candidate_id if missing
        if not result.get("candidate_id"):
            import hashlib
            name = result.get("name", "unknown")
            email = result.get("email", "unknown")
            unique_string = f"{name}{email}"
            result["candidate_id"] = hashlib.md5(unique_string.encode()).hexdigest()[:8]
        
        return result