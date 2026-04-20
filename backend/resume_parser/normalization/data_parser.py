"""
Date parser - extracts years from various date formats.
"""

import re
from datetime import datetime
from typing import Optional, Tuple


class DateParser:
    """
    Parses dates from various formats and calculates experience years.
    
    Examples:
        "2020-2023" -> 3 years
        "2020-Present" -> years since 2020
        "Jan 2020 - Dec 2023" -> 3 years
    """
    
    def parse_year(self, date_string: str) -> Optional[int]:
        """
        Extract a single year from a date string.
        
        Args:
            date_string: String containing a date
            
        Returns:
            Year as integer, or None if not found
        """
        if not date_string:
            return None
        
        # Look for 4-digit year
        match = re.search(r'(19|20)\d{2}', date_string)
        if match:
            return int(match.group(0))
        
        return None
    
    def calculate_years(self, date_string: str) -> float:
        """
        Calculate number of years from a date range.
        
        Args:
            date_string: String like "2020-2023" or "2020-Present"
            
        Returns:
            Number of years as float
        """
        if not date_string:
            return 0.0
        
        date_string = date_string.strip()
        
        # Pattern: YYYY-YYYY
        match = re.search(r'(\d{4})\s*[-–—]\s*(\d{4})', date_string)
        if match:
            start = int(match.group(1))
            end = int(match.group(2))
            return max(0.0, float(end - start))
        
        # Pattern: YYYY-Present
        match = re.search(r'(\d{4})\s*[-–—]\s*Present', date_string, re.IGNORECASE)
        if match:
            start = int(match.group(1))
            current_year = datetime.now().year
            return max(0.0, float(current_year - start))
        
        # Pattern: Month YYYY - Month YYYY
        match = re.search(r'(\d{4})\s*[-–—]\s*(\d{4})', date_string)
        if match:
            start = int(match.group(1))
            end = int(match.group(2))
            return max(0.0, float(end - start))
        
        # Single year (assume 1 year)
        match = re.search(r'(19|20)\d{2}', date_string)
        if match:
            return 1.0
        
        return 0.0
    
    def parse_experience_years(self, experience: list) -> float:
        """
        Calculate total experience years from a list of experience entries.
        
        Args:
            experience: List of experience dictionaries with 'years' field
            
        Returns:
            Total years as float
        """
        if not experience:
            return 0.0
        
        total = 0.0
        for exp in experience:
            if "years" in exp:
                total += float(exp.get("years", 0))
        
        return total