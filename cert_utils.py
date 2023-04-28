from OpenSSL.crypto import load_certificate
from OpenSSL.crypto import FILETYPE_PEM
from OpenSSL.crypto import dump_certificate

def get_modulus_from_pem_file(certfile):
    # Takes a cert file (xxx.pem) and returns the modulus
    with open(certfile, 'rb') as fp:
        cert = load_certificate(FILETYPE_PEM, fp.read())
    modn = cert.get_pubkey().to_cryptography_key().public_numbers().n
    return modn

def get_modulus_from_pem(cert_pem):
    # takes a cert file in a buffer (contents of xxx.pem) and returns a modulus
    cert = load_certificate(FILETYPE_PEM, cert_pem)
    modn = cert.get_pubkey().to_cryptography_key().public_numbers().n
    return modn

def get_modulus_from_cert(cert):
    # Returns a modulus from a OpenSSL.crypto.X509 object
    modn = cert.get_pubkey().to_cryptography_key().public_numbers().n
    return modn

def read_cert_file(file):
    with open(file, 'rb') as fp:
        cert = load_certificate(FILETYPE_PEM, fp.read())
    return cert
