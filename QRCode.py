'''
Created on 2018年10月22日

@author: 沈淋泽
'''
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# version: 一个整数，范围为1到40，表示二维码的大小（最小值是1，是个12×12的矩阵），如果想让程序自动生成，将值设置为 None 并使用 fit=True 参数即可。
# error_correction: 二维码的纠错范围，可以选择4个常量： 
# ERROR_CORRECT_L 7%以下的错误会被纠正 
# ERROR_CORRECT_M (default) 15%以下的错误会被纠正 
# ERROR_CORRECT_Q 25 %以下的错误会被纠正 
# ERROR_CORRECT_H. 30%以下的错误会被纠正
# boxsize: 每个点（方块）中的像素个数
# border: 二维码距图像外围边框距离，默认为4，而且相关规定最小为4

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

#生成并显示二维码
def makeQrCode(text, savePathAndName):
    qr.add_data(text)
    img = qr.make_image()
    # 图片数据保存至本地文件
    img.save(savePathAndName)
    # 显示二维码图片
    img.show()
    
#解码二维码
def decodeQrcode(pathAndName):
    res = decode(Image.open(pathAndName))
    return str(res[0].data, encoding='utf-8')
    
if __name__ == '__main__':
    print('生成中...')
    makeQrCode('hello world', './qrcode.png')
    print('生成完成！')
    print('正在解码...')
    text = decodeQrcode('./qrcode.png')
    print('二维码信息为：', text)
    print('解码完成！')