"""
Base class for all text extractors.
Defines the interface that PDF, DOCX, and TXT extractors must implement.
"""

from abc import ABC, abstractmethod


class TextExtractor(ABC):
    """
    Abstract base class for text extraction from different file formats.
    
    All extractors (PDF, DOCX, TXT) must inherit from this class
    and implement the extract() method.
    """
    
    @abstractmethod
    def extract(self, file_bytes: bytes) -> str:
        """
        Extract text from file bytes.
        
        Args:
            file_bytes: Raw bytes content of the file
            
        Returns:
            Extracted text as a string
            
        Raises:
            Exception: If extraction fails (corrupted file, wrong format, etc.)
        """
        pass
    
    def _handle_error(self, error: Exception, file_type: str) -> str:
        """
        Helper method for consistent error handling.
        Returns empty string on error (graceful degradation).
        """
        print(f"Warning: Failed to extract text from {file_type} file: {error}")
        return ""