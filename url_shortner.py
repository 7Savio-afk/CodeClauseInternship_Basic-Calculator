import string
import random

# Base62 characters
BASE62 = string.ascii_letters + string.digits

# In-memory storage for URL mappings
url_mapping = {}
id_mapping = {}

# Function to encode a number into Base62
def encode_base62(num):
    if num == 0:
        return BASE62[0]
    base62 = []
    while num:
        num, rem = divmod(num, 62)
        base62.append(BASE62[rem])
    return ''.join(reversed(base62))

# Function to decode a Base62 string back to number (not needed unless reverse lookup is required)
def decode_base62(s):
    num = 0
    for char in s:
        num = num * 62 + BASE62.index(char)
    return num

# Function to generate a unique ID
def generate_unique_id():
    return random.randint(100000, 99999999)

# Main function to shorten a URL
def shorten_url(long_url, base_url="http://short.url/"):
    if long_url in url_mapping:
        return base_url + url_mapping[long_url]
    
    unique_id = generate_unique_id()
    short_code = encode_base62(unique_id)
    
    # Save mappings
    url_mapping[long_url] = short_code
    id_mapping[short_code] = long_url
    
    return base_url + short_code

# Function to expand a short URL back to the original
def expand_url(short_url, base_url="http://short.url/"):
    short_code = short_url.replace(base_url, "")
    return id_mapping.get(short_code, "URL not found")

# Example usage
if __name__ == "__main__":
    long_url_input = input("Enter the long URL: ").strip()
    short_url = shorten_url(long_url_input)
    print("Shortend URL:",short_url)

    # Optional: test expanding 
    print("Expand back:",expand_url(short_url))