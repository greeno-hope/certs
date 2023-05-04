'''

openssl s_client -showcerts -connect www.example.com:443 < /dev/null | openssl x509 -outform PEM > certfile.pem

'''

import math
#import nmap
import ssl

import cert_utils as cu

def get_server_cert(ip, port):
    cert_pem = None;
    try:
        conn = ssl.create_connection((ip, port), timeout=0.5)
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        sock = context.wrap_socket(conn, server_hostname=ip)
        cert_der = sock.getpeercert(True)
        cert_pem = ssl.DER_cert_to_PEM_cert(cert_der)
    except:
        pass
    return cert_pem


def write_pem_file(ip, cert):
    with open ('./XRSA/' + ip + '.pem', "w") as out:
        out.writelines(cert)
        out.close()

if __name__ == '__main__':

    count = 0
    print('Starting')

# This is dumb but let's see

    '''
    This code checks all IP addresses in the range 104.82.112.0 to 104.82.187.255
    '''
    for a in range(212, 213):
        for b in range(58, 59):
            for c in range(235, 236):
                for d in range(0, 256):
                    ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
                    print('Trying ' + ip)
                    cert = get_server_cert(ip, 443)
                    if cert is not None:
                        modulus = cu.get_modulus_from_pem(cert)
                        if modulus is not None:
                            count += 1
                            print(count)
                            print(ip + ':' + str(modulus))
                            write_pem_file(ip, cert)

    print('Done fetching ' + str(count) + ' pem files')

'''
here's the code the only thing i have changed is the ip address ranges so far i 
tried to connect to british servers as i was having connection issues
the ip address range i tried to connect to is 103.170.155.0 to 103.170.155.255
i'm not 100% sure if i did it right though.
'''