import zlib
import base64

def decompress_zlib_data(encoded_data: str) -> str:
    """
    Decompresses zlib compressed data that has been Base64 encoded.
    
    Parameters:
    - encoded_data (str): Base64 encoded, zlib-compressed data
    
    Returns:
    - str: Decompressed data as a UTF-8 string
    """
    try:
        # Step 1: Base64 decoding
        compressed_data = base64.urlsafe_b64decode(encoded_data + "==")
        print(compressed_data)
        
        # Step 2: zlib decompression
        decompressed_data = zlib.decompress(compressed_data).decode("utf-8")
        
        return decompressed_data
    except Exception as e:
        return f"Error during decompression: {e}"

# Example usage with the encoded session data
encoded_session_data = ""
print(decompress_zlib_data(encoded_session_data))