import ldap3
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

# LDAP Configuration
ldap_server = 'ldap://your_ldap_server'
ldap_user = 'your_ldap_user'
ldap_password = 'your_ldap_password'
ldap_search_base = 'ou=people,dc=example,dc=com'

# Path for storing the previous fingerprint
fingerprint_file_path = 'previous_fingerprint.txt'

def get_ldap_ssl_fingerprint():
    with ldap3.Connection(ldap_server, user=ldap_user, password=ldap_password, auto_bind=True, receive_timeout=10) as conn:
        conn.start_tls()
        cert_data = conn.server_info.cert.bytes
        cert = x509.load_der_x509_certificate(cert_data, default_backend())
        fingerprint = cert.fingerprint(hashes.SHA256()).hex()
        return fingerprint

def main():
    current_fingerprint = get_ldap_ssl_fingerprint()

    if os.path.exists(fingerprint_file_path):
        with open(fingerprint_file_path, 'r') as file:
            previous_fingerprint = file.read().strip()
    else:
        previous_fingerprint = None

    if current_fingerprint != previous_fingerprint:
        # Print change information (you can customize this part)
        print(f'SSL certificate change detected!\nPrevious Fingerprint: {previous_fingerprint}\nCurrent Fingerprint: {current_fingerprint}')

        # Update the stored fingerprint
        with open(fingerprint_file_path, 'w') as file:
            file.write(current_fingerprint)

if __name__ == "__main__":
    main()

