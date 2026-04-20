"""
Base class for field extraction strategies.
Defines the interface that all strategies (Regex, spaCy, Transformer) must implement.
"""

from abc import ABC, abstractmethod
from typing import Dict


class FieldExtractionStrategy(ABC):
    """
    Abstract base class for field extraction strategies.
    
    All extraction strategies (RegexStrategy, SpacyStrategy, TransformerStrategy)
    must inherit from this class and implement the extract_fields() method.
    
    This enables the fallback chain pattern:
    Try Strategy 3 → if fails → Strategy 2 → if fails → Strategy 1
    """
    
    @abstractmethod
    def extract_fields(self, text: str) -> Dict:
        """
        Extract resume fields from raw text.
        
        Args:
            text: Raw text extracted from resume file
            
        Returns:
            Dictionary containing extracted fields with keys:
            - name: str
            - email: str or None
            - skills: List[str]
            - experience: List[Dict] with keys: role, company, years
            - education: List[Dict] with keys: degree, institution, year
        """
        pass
    
    def get_strategy_name(self) -> str:
        """
        Return the name of this strategy (for logging/debugging).
        Override in child classes.
        """
        return self.__class__.__name__