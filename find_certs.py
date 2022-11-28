'''

openssl s_client -showcerts -connect www.example.com:443 < /dev/null | openssl x509 -outform PEM > certfile.pem

'''




import math
#import nmap
import ssl

import cert_utils as cu

def get_server_cert(hostname, port):
    cert_pem = None;
    conn = ssl.create_connection((ip, port))
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    try:
        sock = context.wrap_socket(conn, server_hostname=hostname)
        cert_der = sock.getpeercert(True)
        cert_pem = ssl.DER_cert_to_PEM_cert(cert_der)
    except:
        pass
    return cert_pem


def write_pem_file(ip, cert):
    with open ('./RSA/' + ip + '.pem', "w") as out:
        out.writelines(cert)
        out.close()

if __name__ == '__main__':

    count = 0
    print('Starting')

    # This is dumb but lets see
    for a in range(146,147):
        for b in range(75,76):
            for c in range(72,255):
                for d in range(1, 255):
                    ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
                    cert = get_server_cert(ip, 443)
                    if cert != None:
                        count = count + 1
                        print(count)
                        print(ip + ':' + str(cu.get_modulus_from_pem(cert)))
                        write_pem_file(ip, cert)

    print('Done fetching ' + str(count) + ' pem files')



