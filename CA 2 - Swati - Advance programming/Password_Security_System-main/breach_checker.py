import hashlib
import requests

# Check if password is present in known breaches
def check_password_breach(password):

    # Convert password to SHA-1 hash (required by API)
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    # Split hash into prefix and suffix (k-anonymity)
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    # Query API with prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    # Process returned hashes
    hashes = (line.split(":") for line in response.text.splitlines())

    for h, count in hashes:
        if h == suffix:
            return True, count

    return False, 0