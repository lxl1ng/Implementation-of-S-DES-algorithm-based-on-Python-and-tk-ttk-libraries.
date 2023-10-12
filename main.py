import tkinter as tk
from tkinter.messagebox import showerror
import numpy as np
from PIL.ImageTk import PhotoImage
from key import *


# 生成十位随机密钥
def romdom_key():
    while len(e0.get()) > 0:
        e0.delete(0)
    i = 0
    # 生成10位数组
    key = np.random.randint(0, 2, size=10)
    key_show = ''.join(str(i) for i in key)
    for char in key_show:
        # 获取每个字符并插入密钥框
        char = key_show[i]
        print(i, char)
        e0.insert(i, char)
        i += 1
    print(key_show)


# 加密按钮函数
def bind_encrypt():
    e2.delete(0, tk.END)
    key = e0.get()
    if len(key) < 10:
        result = showerror('错误', '密钥应是10位！')
        print(f'错误: {result}')
    else:
        text = e1.get()
        ciphertext = sdes_process_data('encrypt', text, key)
        e2.insert(0, ciphertext)
        print(ciphertext)


# 解密按钮函数
def bind_decrypt():
    e4.delete(0, tk.END)
    key = e0.get()
    if len(key) < 10:
        result = showerror('错误', '密钥应是10位！')
        print(f'错误: {result}')
    else:
        text = e3.get()
        print(key, text)
        plaintext = sdes_process_data('decrypt', text, key)
        e4.insert(0, plaintext)
        print(plaintext)


# 控制密钥输入只能为0、1，并且是十位
def validate_binary_input(char, input_value):
    return char in '01' and len(input_value) <= 10


# 基于tk生成的GUI界面
root = tk.Tk()
root.title('S-DES')
root.geometry('600x400+600+300')

# 加载背景图片
bg_image = PhotoImage(file="bg.jpg")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 密钥部分
key_validator = root.register(validate_binary_input)
tk.Label(root, text="密钥：", bg="white", fg='#7f7f7f').place(x=180, y=40)
e0 = tk.Entry(root, validate="key", validatecommand=(key_validator, "%S", "%P"), foreground='#000000')
e0.place(x=227, y=40)
tk.Button(root, text='随机生成!', command=romdom_key).place(x=260, y=70)


# 加密部分
tk.Label(root, text="明文：", bg="white", fg='#7f7f7f').place(x=30, y=140)
e1 = tk.Entry(root)
e1.place(x=77, y=140)
tk.Label(root, text="----------------------->", bg="black", fg='#7f7f7f').place(x=230, y=140)
tk.Label(root, text="密文：", bg="white", fg='#7f7f7f').place(x=370, y=140)
e2 = tk.Entry(root)
e2.place(x=417, y=140)
tk.Button(root, text='加密!', command=bind_encrypt).place(x=277, y=170)
tk.Label(root, text="密文：", bg="white", fg='#7f7f7f').place(x=30, y=240)

# 解密部分
e3 = tk.Entry(root)
e3.place(x=77, y=240)
tk.Label(root, text="----------------------->", bg="black", fg='#7f7f7f').place(x=230, y=240)
tk.Label(root, text="明文：", bg="white", fg='#7f7f7f').place(x=370, y=240)
e4 = tk.Entry(root)
e4.place(x=417, y=240)
tk.Button(root, text='解密!', command=bind_decrypt).place(x=277, y=270)


# 保持窗口存在
root.mainloop()
