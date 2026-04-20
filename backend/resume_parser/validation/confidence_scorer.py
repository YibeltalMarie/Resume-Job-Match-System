"""
Confidence scorer - assigns confidence scores to extracted fields.
"""

from typing import Dict


class ConfidenceScorer:
    """
    Calculates confidence scores for extracted fields.
    
    Score range: 0.0 to 1.0
    """
    
    def calculate(self, extracted_data: Dict) -> float:
        """
        Calculate overall confidence score.
        
        Args:
            extracted_data: Dictionary with extracted fields
            
        Returns:
            Confidence score between 0 and 1
        """
        scores = []
        
        # Name confidence
        if extracted_data.get("name") and extracted_data["name"] != "Unknown":
            scores.append(1.0)
        else:
            scores.append(0.0)
        
        # Email confidence
        if extracted_data.get("email"):
            scores.append(1.0)
        else:
            scores.append(0.0)
        
        # Skills confidence
        skills_count = len(extracted_data.get("skills", []))
        if skills_count >= 5:
            scores.append(1.0)
        elif skills_count >= 3:
            scores.append(0.7)
        elif skills_count >= 1:
            scores.append(0.4)
        else:
            scores.append(0.0)
        
        # Experience confidence
        exp_count = len(extracted_data.get("experience", []))
        if exp_count >= 2:
            scores.append(1.0)
        elif exp_count >= 1:
            scores.append(0.6)
        else:
            scores.append(0.0)
        
        # Education confidence
        edu_count = len(extracted_data.get("education", []))
        if edu_count >= 2:
            scores.append(1.0)
        elif edu_count >= 1:
            scores.append(0.6)
        else:
            scores.append(0.0)
        
        # Calculate average
        if scores:
            return sum(scores) / len(scores)
        return 0.0