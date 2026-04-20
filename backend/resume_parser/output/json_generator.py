"""
JSON generator - creates final JSON output matching competition schema.
"""

import json
from typing import Dict, Optional
from datetime import datetime


class JSONGenerator:
    """
    Generates JSON output in the required competition format.
    """
    
    def generate(self, resume_data: Dict, confidence: float, warnings: list, processing_time_ms: float) -> str:
        """
        Generate JSON string matching required schema.
        
        Args:
            resume_data: Normalized resume data
            confidence: Confidence score (0-1)
            warnings: List of warning messages
            processing_time_ms: Processing time in milliseconds
            
        Returns:
            JSON string
        """
        # Build output structure
        output = {
            "candidate_id": resume_data.get("candidate_id"),
            "name": resume_data.get("name"),
            "email": resume_data.get("email"),
            "skills": resume_data.get("skills", []),
            "education": resume_data.get("education", []),
            "experience": resume_data.get("experience", []),
            "total_experience_years": resume_data.get("total_experience_years", 0),
            "_metadata": {
                "confidence": round(confidence, 3),
                "warnings": warnings,
                "processing_time_ms": round(processing_time_ms, 2),
                "parser_version": "phase1_regex",
                "timestamp": datetime.now().isoformat()
            }
        }
        
        # Convert to JSON with proper formatting
        return json.dumps(output, indent=2, ensure_ascii=False)