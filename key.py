import re


# 生成密钥函数
def creat_key(key):
    def P_10(arr):
        arr = [arr[2], arr[4], arr[1], arr[6], arr[3], arr[9], arr[0], arr[8], arr[7], arr[5]]
        return arr

    def P_8(arr):
        arr = [arr[5], arr[2], arr[6], arr[3], arr[7], arr[4], arr[9], arr[8]]
        return arr

    def left_shitf1(arr):
        arr = [arr[1], arr[2], arr[3], arr[4], arr[0]]
        return arr

    def left_shitf2(arr):
        arr = [arr[1], arr[2], arr[3], arr[4], arr[0]]
        return arr

    def slicing(arr):
        arr_l = arr[:5]
        arr_r = arr[5:]
        return arr_l, arr_r

    def compose(arr_l, arr_r):
        arr = arr_l + arr_r
        return arr

    arr = P_10(key)
    arr_l, arr_r = slicing(arr)
    arr_l = left_shitf1(arr_l)
    arr_r = left_shitf1(arr_r)
    arr = compose(arr_l, arr_r)
    key1 = P_8(arr)
    arr_l = left_shitf2(arr_l)
    arr_r = left_shitf2(arr_r)
    arr = compose(arr_l, arr_r)
    key2 = P_8(arr)
    # print(key1, key2)
    return key1, key2


# 初始置换函数
def initial_permutation(input_data):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    return [input_data[i - 1] for i in ip]


# 逆初始置换函数
def inverse_initial_permutation(input_data):
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    return [input_data[i - 1] for i in ip_inv]


# 轮函数
def round_function(input_data, subkey):
    ep_box = [4, 1, 2, 3, 2, 3, 4, 1]
    sbox1 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
    sbox2 = [[0, 1, 2, 3], [2, 3, 1, 0], [3, 0, 1, 2], [2, 1, 0, 3]]
    spbox = [2, 4, 3, 1]
    # EP-BOX扩展
    expanded_data = [input_data[i - 1] for i in ep_box]
    # 异或运算（加轮密钥）
    xor_result = [expanded_data[i] ^ subkey[i] for i in range(8)]
    # S-Box替换
    sbox1_row = xor_result[:4]
    sbox2_row = xor_result[4:]
    sbox1_output = sbox1[sbox1_row[0] * 2 + sbox1_row[3]][sbox1_row[1] * 2 + sbox1_row[2]]
    sbox2_output = sbox2[sbox2_row[0] * 2 + sbox2_row[3]][sbox2_row[1] * 2 + sbox2_row[2]]

    p4_output = [sbox1_output // 2, sbox1_output % 2, sbox2_output // 2, sbox2_output % 2]

    # SP-BOX置换
    final_output = [p4_output[i - 1] for i in spbox]
    return final_output


# S-DES 加密函数
def sdes_encrypt(plaintext, key):
    subkey1, subkey2 = creat_key(key)
    plaintext = initial_permutation(plaintext)
    # 第一轮
    round1_output = round_function(plaintext[4:], subkey1)
    new_right = [plaintext[i] ^ round1_output[i] for i in range(4)]
    new_left = plaintext[4:]
    # 第二轮
    round2_output = round_function(new_right, subkey2)
    final_left = [new_left[i] ^ round2_output[i] for i in range(4)]
    final_right = new_right

    # 组合并反置换
    ciphertext = final_left + final_right
    ciphertext = inverse_initial_permutation(ciphertext)
    return ciphertext


# S-DES 解密函数
def sdes_decrypt(ciphertext, key):
    subkey1, subkey2 = creat_key(key)
    ciphertext = initial_permutation(ciphertext)
    # 第一轮
    round1_output = round_function(ciphertext[4:], subkey2)
    new_right = [ciphertext[i] ^ round1_output[i] for i in range(4)]
    new_left = ciphertext[4:]
    # 第二轮
    round2_output = round_function(new_right, subkey1)
    final_left = [new_left[i] ^ round2_output[i] for i in range(4)]
    final_right = new_right

    # 组合并反置换
    plaintext = final_left + final_right
    plaintext = inverse_initial_permutation(plaintext)
    return plaintext


# 主函数 根据操作选择执行加密或解密
def sdes_process_data(operation, text, key):
    # 判断是否为8位2进制数
    determine = bool(re.match(r'^[01]+$', text)) and len(text) % 8 == 0
    if determine:
        text_num = int(len(text) / 8)
        binary_text = [int(bit) for bit in text]
    # 将不是的转换为2进制字符串
    else:
        text_num = len(text)
        binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_key = [int(bit) for bit in key]
    result = ''
    # 加解密
    if operation == 'encrypt':
        for i in range(text_num):
            t = [int(binary_text[j + i * 8]) for j in range(8)]
            result += ''.join(map(str, sdes_encrypt(t, binary_key)))
    else:
        for i in range(text_num):
            t = [int(binary_text[j + i * 8]) for j in range(8)]
            result += ''.join(map(str, sdes_decrypt(t, binary_key)))
    # 输出结果
    if determine:
        return result
    else:
        # 将二进制字符串分组，每组8位
        binary_chunks = [result[i:i + 8] for i in range(0, len(result), 8)]

        # 将每组转换为ASCII码
        ascii_characters = [chr(int(chunk, 2)) for chunk in binary_chunks]

        # 将结果连接成一个字符串
        result = ''.join(ascii_characters)
        return result
