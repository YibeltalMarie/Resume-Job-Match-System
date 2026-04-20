"""
TXT text extractor for plain text files.
Handles different text encodings (UTF-8, Latin-1, etc.).
"""

from .base import TextExtractor


class TXTExtractor(TextExtractor):
    """
    Extracts text from plain TXT files.
    
    How it works:
    1. Tries UTF-8 decoding first (most common)
    2. Falls back to Latin-1 if UTF-8 fails
    3. Returns decoded string
    """
    
    def extract(self, file_bytes: bytes) -> str:
        """
        Extract text from a TXT file.
        
        Args:
            file_bytes: Raw TXT file bytes
            
        Returns:
            Decoded text string, or empty string on error
        """
        try:
            # Try UTF-8 first (most common)
            return file_bytes.decode('utf-8')
        except UnicodeDecodeError:
            try:
                # Fallback to Latin-1 (handles almost everything)
                return file_bytes.decode('latin-1')
            except Exception as e:
                return self._handle_error(e, "TXT")
        except Exception as e:
            return self._handle_error(e, "TXT")