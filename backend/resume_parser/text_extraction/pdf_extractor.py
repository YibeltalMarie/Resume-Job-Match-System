"""
PDF text extractor using PyPDF2 library.
Handles standard PDF files and gracefully handles errors.
"""

import io
from PyPDF2 import PdfReader
from .base import TextExtractor


class PDFExtractor(TextExtractor):
    """
    Extracts text from PDF files.
    
    How it works:
    1. Converts bytes to a file-like object using BytesIO
    2. Reads the PDF file
    3. Loops through each page
    4. Extracts text from each page
    5. Joins all pages with newlines
    """
    
    def extract(self, file_bytes: bytes) -> str:
        """
        Extract all text from a PDF file.
        
        Args:
            file_bytes: Raw PDF file bytes
            
        Returns:
            Combined text from all pages, or empty string on error
        """
        try:
            # Convert bytes to file-like object (what PyPDF2 expects)
            file_like = io.BytesIO(file_bytes)
            
            # Create PDF reader from file-like object
            reader = PdfReader(file_like)
            
            # Extract text from each page
            all_text = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text.append(text)
            
            # Join all pages with newlines
            return "\n".join(all_text)
            
        except Exception as e:
            # Return empty string on error (graceful degradation)
            return self._handle_error(e, "PDF")