"""
Factory pattern for selecting the correct text extractor.
Given a filename, returns the appropriate extractor instance.
"""

from pathlib import Path
from .pdf_extractor import PDFExtractor
from .docx_extractor import DOCXExtractor
from .txt_extractor import TXTExtractor


class ExtractorFactory:
    """
    Factory class that returns the correct extractor for a file.
    
    Usage:
        factory = ExtractorFactory()
        extractor = factory.get_extractor("resume.pdf")
        text = extractor.extract(file_bytes)
    """
    
    # Map file extensions to extractor classes
    _EXTRACTORS = {
        '.pdf': PDFExtractor,
        '.docx': DOCXExtractor,
        '.txt': TXTExtractor,
    }
    
    def get_extractor(self, filename: str):
        """
        Get the appropriate extractor for a file.
        
        Args:
            filename: Name of the file (e.g., "resume.pdf")
            
        Returns:
            Instance of the correct extractor class
            
        Raises:
            ValueError: If file extension is not supported
        """
        # Get file extension (e.g., ".pdf")
        extension = Path(filename).suffix.lower()
        
        # Check if extension is supported
        if extension not in self._EXTRACTORS:
            supported = ", ".join(self._EXTRACTORS.keys())
            raise ValueError(
                f"Unsupported file type: {extension}. "
                f"Supported types: {supported}"
            )
        
        # Return an instance of the correct extractor
        extractor_class = self._EXTRACTORS[extension]
        return extractor_class()
    
    def get_supported_extensions(self) -> list:
        """Return list of supported file extensions."""
        return list(self._EXTRACTORS.keys())