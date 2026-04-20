"""
DOCX text extractor using python-docx library.
Handles Microsoft Word .docx files.
"""

import io
from docx import Document
from .base import TextExtractor


class DOCXExtractor(TextExtractor):
    """
    Extracts text from DOCX files.
    
    How it works:
    1. Converts bytes to a file-like object using BytesIO
    2. Opens the document
    3. Loops through all paragraphs
    4. Extracts text from each paragraph
    5. Joins with newlines
    """
    
    def extract(self, file_bytes: bytes) -> str:
        """
        Extract all text from a DOCX file.
        
        Args:
            file_bytes: Raw DOCX file bytes
            
        Returns:
            Combined text from all paragraphs, or empty string on error
        """
        try:
            # Convert bytes to file-like object
            file_like = io.BytesIO(file_bytes)
            
            # Open the document from file-like object
            doc = Document(file_like)
            
            # Extract text from all paragraphs
            all_text = []
            for paragraph in doc.paragraphs:
                text = paragraph.text.strip()
                if text:  # Only add non-empty paragraphs
                    all_text.append(text)
            
            # Join with newlines
            return "\n".join(all_text)
            
        except Exception as e:
            return self._handle_error(e, "DOCX")