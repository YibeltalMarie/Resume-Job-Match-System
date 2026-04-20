"""
Schema validator - ensures output matches required format.
"""

from typing import Dict, List, Tuple


class SchemaValidator:
    """
    Validates that parsed resume matches the required schema.
    """
    
    # Required fields and their expected types
    REQUIRED_FIELDS = {
        "candidate_id": str,
        "name": str,
        "email": (str, type(None)),  # Can be None
        "skills": list,
        "education": list,
        "experience": list,
        "total_experience_years": (int, float),
    }
    
    def validate(self, data: Dict) -> Tuple[bool, List[str]]:
        """
        Validate data against schema.
        
        Args:
            data: Dictionary to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check all required fields exist
        for field, expected_type in self.REQUIRED_FIELDS.items():
            if field not in data:
                errors.append(f"Missing required field: {field}")
            else:
                # Check type
                actual_type = type(data[field])
                if isinstance(expected_type, tuple):
                    if not isinstance(data[field], expected_type):
                        errors.append(f"Field '{field}' has wrong type. Expected {expected_type}, got {actual_type}")
                else:
                    if not isinstance(data[field], expected_type):
                        errors.append(f"Field '{field}' has wrong type. Expected {expected_type}, got {actual_type}")
        
        # Validate education entries
        if "education" in data and data["education"]:
            for i, edu in enumerate(data["education"]):
                if "degree" not in edu:
                    errors.append(f"Education[{i}] missing 'degree'")
                if "institution" not in edu:
                    errors.append(f"Education[{i}] missing 'institution'")
        
        # Validate experience entries
        if "experience" in data and data["experience"]:
            for i, exp in enumerate(data["experience"]):
                if "role" not in exp:
                    errors.append(f"Experience[{i}] missing 'role'")
                if "company" not in exp:
                    errors.append(f"Experience[{i}] missing 'company'")
                if "years" not in exp:
                    errors.append(f"Experience[{i}] missing 'years'")
        
        return len(errors) == 0, errors