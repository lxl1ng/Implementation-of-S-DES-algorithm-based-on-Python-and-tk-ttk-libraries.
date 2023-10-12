import time

# 暴力破解
from key import sdes_process_data

# 1111100000  or 1011100000
plaintext1 = '11111011'
ciphertext1 = '11111001'
plaintext2 = '01100100'
ciphertext2 = '10000111'
plaintext3 = '10101010'
ciphertext3 = '00011011'
plaintext4 = '11001011'
ciphertext4 = '01110010'
i = 0
while i <= 1023:
    binary = bin(i)[2:]
    key = str.zfill(binary, 10)
    i += 1
    p_ciphertext1 = sdes_process_data('encrypt', plaintext1, key)
    p_ciphertext2 = sdes_process_data('encrypt', plaintext2, key)
    p_ciphertext3 = sdes_process_data('encrypt', plaintext3, key)
    p_ciphertext4 = sdes_process_data('encrypt', plaintext4, key)
    if p_ciphertext1 == ciphertext1 and p_ciphertext2 == ciphertext2 and p_ciphertext3 == ciphertext3 \
            and p_ciphertext4 == ciphertext4:
        print(i + 1)
        print(key)
        print(p_ciphertext1, ciphertext1)
        print(p_ciphertext2, ciphertext2)
        print(p_ciphertext3, ciphertext3)
        print(p_ciphertext4, ciphertext4)
