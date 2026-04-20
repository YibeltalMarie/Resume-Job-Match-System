"""
Regex-based field extraction strategy - Clean and strict version.
"""

import re
from typing import List, Dict, Optional
from ..base import FieldExtractionStrategy
from ...utils.constants import COMMON_SKILLS


class RegexStrategy(FieldExtractionStrategy):
    
    def get_strategy_name(self) -> str:
        return "RegexStrategy"
    
    def extract_fields(self, text: str) -> Dict:
        # Reconstruct text by joining words
        reconstructed = ' '.join(text.split())
        
        return {
            "name": self._extract_name(reconstructed),
            "email": self._extract_email(reconstructed),
            "skills": self._extract_skills(reconstructed),
            "experience": self._extract_experience(reconstructed),
            "education": self._extract_education(reconstructed),
        }
    
    def _extract_email(self, text: str) -> Optional[str]:
        pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        match = re.search(pattern, text.lower())
        return match.group(0) if match else None
    
    def _extract_name(self, text: str) -> str:
        first_part = text[:200]
        pattern = r'\b([A-Z][a-z]+)\s+([A-Z][a-z]+)\b'
        match = re.search(pattern, first_part)
        if match:
            return f"{match.group(1)} {match.group(2)}"
        return "Unknown"
    
    def _extract_skills(self, text: str) -> List[str]:
        text_lower = text.lower()
        found_skills = []
        
        for skill in COMMON_SKILLS:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.append(skill.title())
        
        seen = set()
        unique_skills = []
        for skill in found_skills:
            if skill.lower() not in seen:
                seen.add(skill.lower())
                unique_skills.append(skill)
        
        return unique_skills[:10]
    
    def _extract_experience(self, text: str) -> List[Dict]:
        """Extract experience - strict pipe pattern matching."""
        experience_entries = []
        
        # Strict pattern: Role | Company | Year-Year or Year-Present
        pattern = r'([A-Za-z\s]+?)\s*\|\s*([A-Za-z\s]+?)\s*\|\s*(\d{4}\s*[-–—]\s*(?:Present|\d{4}))'
        matches = re.findall(pattern, text)
        
        for match in matches:
            role = match[0].strip()
            company = match[1].strip()
            years_str = match[2].strip()
            years = self._parse_years(years_str)
            
            # Clean role - keep only meaningful job titles
            role = self._clean_job_title(role)
            company = self._clean_company(company)
            
            if role and company and len(role) < 50:
                experience_entries.append({
                    "role": role,
                    "company": company,
                    "years": years
                })
        
        return experience_entries
    
    def _extract_education(self, text: str) -> List[Dict]:
        """Extract education - strict pipe pattern matching."""
        education_entries = []
        
        # First, find the EDUCATION section in the text
        edu_section_match = re.search(r'EDUCATION\s+(.*?)(?=\s*(?:SKILLS|EXPERIENCE|$))', text, re.IGNORECASE | re.DOTALL)
        
        if edu_section_match:
            edu_text = edu_section_match.group(1)
            
            # Find pipe patterns within the EDUCATION section only
            pattern = r'([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d{4})'
            matches = re.findall(pattern, edu_text)
            
            for match in matches:
                degree = match[0].strip()
                institution = match[1].strip()
                year = match[2].strip()
                
                # Clean up degree and institution
                degree = self._clean_degree(degree)
                institution = self._clean_institution(institution)
                
                # Only add if it looks like a real degree
                if self._is_real_degree(degree) and institution:
                    education_entries.append({
                        "degree": degree,
                        "institution": institution,
                        "year": year
                    })
        
        return education_entries
    
    def _clean_job_title(self, title: str) -> str:
        """Extract clean job title."""
        # Look for common job title patterns
        patterns = [
            r'(Senior|Junior|Lead|Principal)?\s*(Software|Data|System|Frontend|Backend|Full[-\s]Stack)?\s*(Engineer|Developer|Analyst|Scientist|Manager)',
            r'(Data|Business|Financial)?\s*(Analyst|Scientist)',
            r'(Product|Project|Program)?\s*Manager',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, title, re.IGNORECASE)
            if match:
                return match.group(0).strip().title()
        
        # Fallback: take last 2-3 words
        words = title.split()
        if len(words) >= 2:
            return ' '.join(words[-2:]).title()
        return title.title()
    
    def _clean_company(self, company: str) -> str:
        """Extract clean company name."""
        known_companies = ['Google', 'Amazon', 'Microsoft', 'Meta', 'Apple', 'Netflix', 'Spotify', 'Uber', 'Airbnb']
        
        for known in known_companies:
            if known.lower() in company.lower():
                return known
        
        # Fallback: take first word that starts with capital letter
        words = company.split()
        for word in words:
            if word and word[0].isupper() and len(word) > 2:
                return word
        
        return company.title()
    
    def _clean_degree(self, degree: str) -> str:
        """Extract clean degree name."""
        # Look for degree patterns
        patterns = [
            r'(Bachelor|Master)[\s]+of[\s]+(Science|Arts|Engineering|Business Administration)',
            r'(BSc|MSc|PhD|MBA|B\.?A\.?|M\.?A\.?)',
            r'(Bachelor|Master)[\s]+(?:of[\s]+)?(?:Science|Arts|Engineering)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, degree, re.IGNORECASE)
            if match:
                return match.group(0).strip()
        
        return degree
    
    def _clean_institution(self, institution: str) -> str:
        """Extract clean institution name."""
        known_unis = ['Stanford', 'Harvard', 'MIT', 'UC Berkeley', 'Oxford', 'Cambridge', 'Columbia', 'Yale', 'Princeton', 'University']
        
        for known in known_unis:
            if known.lower() in institution.lower():
                return known
        
        # Fallback: take first 2 words that start with capitals
        words = institution.split()
        capital_words = [w for w in words if w and w[0].isupper()]
        if capital_words:
            return ' '.join(capital_words[:2])
        
        return institution
    
    def _is_real_degree(self, degree: str) -> bool:
        """Check if text is a real degree."""
        degree_lower = degree.lower()
        valid_keywords = ['bachelor', 'master', 'bsc', 'msc', 'phd', 'mba', 'doctor']
        return any(kw in degree_lower for kw in valid_keywords)
    
    def _parse_years(self, date_string: str) -> float:
        """Parse date string and calculate number of years."""
        from datetime import datetime
        
        match = re.search(r'(\d{4})\s*[-–—]\s*(\d{4})', date_string)
        if match:
            start = int(match.group(1))
            end = int(match.group(2))
            return max(0, end - start)
        
        match = re.search(r'(\d{4})\s*[-–—]\s*Present', date_string, re.IGNORECASE)
        if match:
            start = int(match.group(1))
            current_year = datetime.now().year
            return max(0, current_year - start)
        
        return 1.0