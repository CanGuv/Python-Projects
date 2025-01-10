# Check My Password

This Python script, checkmypass.py, helps users verify if their passwords have been compromised in a data breach by interacting with the Have I Been Pwned (HIBP) API. It securely checks the password without revealing it in full by using hashing and k-anonymity.

## How it works
1. **Password Hashing**: The script hashes the password using the SHA-1 algorithm, generating a unique fixed-length string.
2. **K-Anonymity Search**:
   - The first 5 characters of the hashed password are sent to the HIBP API.
   - The API returns a list of all hashes that match this prefix.
3. **Checking Against Breaches**:
   - The script compares the remainder of the hash with the API response to determine if the password has been breached.
   - If found, it provides the count of occurrences in breaches.
4. **Feedback**:
   - If the password is safe, it notifies the user.
   - Otherwise, it warns the user and recommends changing the password.
5. Make sure `requests` library is installed:
   ```bash
   pip install requests
   ```


## Getting Started
1. Clone Repository
   ```bash
   git clone https://github.com/CanGuv/Python-Projects.git
   cd Passwordchecker
   ```
2. For the Python script:
   - Modify the file as needed.
   - Run it using:
     ```bash
     python checkmypass.py
     ```
