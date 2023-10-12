import time
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
plaintext5 = '10101111'
ciphertext5 = '01001011'


# 暴力破解
def for_power():
    time_start = time.time()  # 开始计时
    i = 0
    while i <= 1023:
        binary = bin(i)[2:]
        key = str.zfill(binary, 10)
        i += 1
        p_ciphertext1 = sdes_process_data('encrypt', plaintext1, key)
        p_ciphertext2 = sdes_process_data('encrypt', plaintext2, key)
        p_ciphertext3 = sdes_process_data('encrypt', plaintext3, key)
        p_ciphertext4 = sdes_process_data('encrypt', plaintext4, key)
        p_ciphertext5 = sdes_process_data('encrypt', plaintext5, key)
        if p_ciphertext1 == ciphertext1 and p_ciphertext2 == ciphertext2 and p_ciphertext3 == ciphertext3 \
                and p_ciphertext4 == ciphertext4 and p_ciphertext5 == ciphertext5:
            print('密钥编号：', i + 1)
            print('密钥：', key)

    time_end = time.time()  # 结束计时
    time_c = time_end - time_start  # 运行所花时间
    print('time cost', time_c, 's')


def close_test():
    time_start = time.time()  # 开始计时
    i = 0
    while i <= 1023:
        binary = bin(i)[2:]
        key = str.zfill(binary, 10)
        i += 1
        p_ciphertext1 = sdes_process_data('encrypt', plaintext2, key)
        if p_ciphertext1 == ciphertext2:
            print('密钥编号：', i + 1)
            print('密钥：', key)

    time_end = time.time()  # 结束计时
    time_c = time_end - time_start  # 运行所花时间
    print('time cost', time_c, 's')


# 暴力破解
for_power()
# 封闭测试
# close_test()
