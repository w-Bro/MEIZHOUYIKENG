'''
Created on 2018年8月26日

@author: 沈淋泽
'''
from PIL import Image
import numpy as np

info = "I am new to python."   #要写入的信息
img = np.array(Image.open('watermarking_1.jpg'))#把图像作为数字矩阵打开
     
num = []
for ch in info:
    for index in range(8):
        num.append((ord(ch)>>(7-index))&1)  #把字符转换成二进制，并把二进制拆成8位单独保存进list
 
rows,cols,dims = img.shape
for i in range(rows):
    for j in range(cols):
        for k in range(3):
            img[i,j][k] = img[i,j][k]//2*2
            if (i * rows + j)*3 + k < len(num): #全部信息写入完成就不用写了
                img[i,j][k] = img[i,j][k] | num[(i * rows + j)*3 + k]
                #(i * rows + j)*3 + k为每个像素点对应在num中的位置
                 
im = Image.fromarray(img)
im.save('watermarking_2.bmp')
print('saved successfully')

num = []
info = []
exit_flag = False
img_info = np.array(Image.open('watermarking_2.bmp'))

rows,cols,dims = img_info.shape
for i in range(rows):
    for j in range(cols):
        for k in range(3):
            num.append(str((img_info[i,j][k]>>0)&1))
            if len(num) == 8:
                s = ''.join(num)    #将数字拼接成8位的二进制字符串
                if s == "00000000": #全为0说明不是我们写入的信息，此时退出循环，不必再继续遍历
                    exit_flag = True
                    break
                else:
                    info.append(chr(int(s,2)))#把二进制转换成字符
                num = []
        if exit_flag:
            break
    if exit_flag:
        break

print('the info hided in image is:',''.join(info))
            