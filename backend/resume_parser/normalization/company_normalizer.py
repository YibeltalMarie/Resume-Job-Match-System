"""
Company normalizer - standardizes company names.
"""

import re
from typing import List, Dict


class CompanyNormalizer:
    """
    Normalizes company names to standard format.
    
    Examples:
        "Google Inc" -> "Google"
        "Amazon.com" -> "Amazon"
        "MSFT" -> "Microsoft"
    """
    
    COMPANY_MAPPING = {
        # Tech giants
        "google": "Google",
        "google inc": "Google",
        "alphabet": "Google",
        "amazon": "Amazon",
        "amazon.com": "Amazon",
        "microsoft": "Microsoft",
        "msft": "Microsoft",
        "meta": "Meta",
        "facebook": "Meta",
        "apple": "Apple",
        "netflix": "Netflix",
        "spotify": "Spotify",
        
        # Social/Communication
        "twitter": "Twitter",
        "linkedin": "LinkedIn",
        "snapchat": "Snapchat",
        "tiktok": "TikTok",
        "reddit": "Reddit",
        
        # Cloud/DevOps
        "aws": "AWS",
        "amazon web services": "AWS",
        "azure": "Azure",
        "microsoft azure": "Azure",
        "gcp": "GCP",
        "google cloud": "GCP",
        "digitalocean": "DigitalOcean",
        "heroku": "Heroku",
        
        # Consulting/Agencies
        "accenture": "Accenture",
        "deloitte": "Deloitte",
        "pwc": "PwC",
        "ey": "EY",
        "kpmg": "KPMG",
        "mckinsey": "McKinsey",
        "bain": "Bain",
        "bcg": "BCG",
        
        # Finance
        "goldman sachs": "Goldman Sachs",
        "jpmorgan": "JPMorgan",
        "jpmc": "JPMorgan",
        "morgan stanley": "Morgan Stanley",
        "citibank": "Citi",
        "bank of america": "Bank of America",
        "wells fargo": "Wells Fargo",
        
        # Other common
        "uber": "Uber",
        "lyft": "Lyft",
        "airbnb": "Airbnb",
        "stripe": "Stripe",
        "square": "Square",
        "paypal": "PayPal",
        "salesforce": "Salesforce",
        "oracle": "Oracle",
        "ibm": "IBM",
        "hp": "HP",
        "dell": "Dell",
        "intel": "Intel",
        "nvidia": "NVIDIA",
        "amd": "AMD",
        "qualcomm": "Qualcomm",
    }
    
    def normalize(self, company: str) -> str:
        """
        Normalize a single company name.
        
        Args:
            company: Raw company string
            
        Returns:
            Normalized company name
        """
        if not company:
            return company
        
        company_lower = company.lower().strip()
        
        # Remove common suffixes
        company_lower = re.sub(r'\s+(inc|llc|ltd|corp|corporation|co)\.?$', '', company_lower)
        company_lower = re.sub(r'\.com$', '', company_lower)
        
        # Check mapping
        if company_lower in self.COMPANY_MAPPING:
            return self.COMPANY_MAPPING[company_lower]
        
        # Capitalize properly
        return company.title()
    
    def normalize_experience(self, experience: List[Dict]) -> List[Dict]:
        """
        Normalize company names in experience entries.
        
        Args:
            experience: List of experience dictionaries
            
        Returns:
            Same list with normalized company names
        """
        for exp in experience:
            if "company" in exp:
                exp["company"] = self.normalize(exp["company"])
        return experience