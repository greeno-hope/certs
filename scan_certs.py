import cert_utils as cu
import math
import os

def gcd_pem_moduli(file1, file2):

    cert1 = cu.read_cert_file(file1)
    cert2 = cu.read_cert_file(file2)

    mod1 = cu.get_modulus_from_cert(cert1)
    mod2 = cu.get_modulus_from_cert(cert2)

    gcd = math.gcd(mod1, mod2);
    if gcd == mod1:
        return 0
    else:
        return gcd


def do_scan_all():
    count = 0
    files = os.listdir('./RSA')
    file_count = len(files)
    comparisons = int(0.5 * file_count * file_count);
    matches = 0
    for i in range(0, len(files)-1):
        for j in range(i+1, len(files)):
            print( str(count) + ' of ' + str(comparisons) + ' certificates scanned : ' + str(matches) + ' matches found' )
            gcd = gcd_pem_moduli('./RSA/' + files[i], './RSA/' + files[j])
            count = count + 1
            if gcd > 1:
                with open('./matches.txt', 'a') as f:
                    matches = matches + 1
                    f.write('Match!\n')
                    f.write( files[i] + ' and ' + files[j] + 'gcd= ' + str(gcd) )
                    f.close()


if __name__ == '__main__':
    do_scan_all()
    print('Done!')


