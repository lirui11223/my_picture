import easygui
import random
from PIL import Image,ImageFilter,ImageDraw,ImageFont

def welcome():
        easygui.msgbox('欢迎使用my_picture', 'my_picture', '进入程序')
def filter(path):
    img = Image.open(path)
    m = ['进行模糊效果', '进行轮廓效果', '进行细节效果', '边缘加强效果', '让边缘部分更加明显', '进行浮雕效果','进行边界效果', '进行平滑效果', '让图片更平滑', '进行锐化效果']
    use = easygui.choicebox('请选择要对图片的编辑选择','my_picture',m)
    while True:
        if use == '进行模糊效果':
            b = img.filter(ImageFilter.BLUR)
        elif use == '进行轮廓效果':
            b = img.filter(ImageFilter.CONTOUR)
        elif use == '进行细节效果':
            b = img.filter(ImageFilter.DETAIL)
        elif use == '边缘加强效果':
            b = img.filter(ImageFilter.EDGE_ENHANCE)
        elif use == '让边缘部分更加明显':
            b = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif use == '进行浮雕效果':
            b = img.filter(ImageFilter.EMBOSS)
        elif use == '进行边界效果':
            b = img.filter(ImageFilter.FIND_EDGES)
        elif use == '进行平滑效果':
            b = img.filter(ImageFilter.SMOOTH)
        elif use == '让图片更平滑':
            b = img.filter(ImageFilter.SMOOTH_MORE)
        elif use == '进行锐化效果':
            b = img.filter(ImageFilter.SHARPEN)
        elif use == None:
            c = easygui.msgbox('是否退出此功能？', 'my_picture', '是')
            if use != None:
                img.show()
                break
def keep(path):
    img = Image.open(path)
    color_choice = easygui.choicebox('请选择要保留的通道','my_picture',['保留红色通道','保留绿色通道','保留蓝色通道'])
    if color_choice == '保留红色通道':
        color = 'r'
    elif color_choice == '保留绿色通道':
        color = 'g'
    elif color_choice == '保留蓝色通道':
        color = 'b'
    w = img.width
    h = img.height
    for x in range(w):
        for y in range(h):
            l = img.getpixel((x, y))
            r = l[0]
            g = l[1]
            b = l[2]
            if color == 'r':
                img.putpixel((x, y), (r, 0, 0))
            elif color == 'g':
                img.putpixel((x, y), (0, g, 0))
            elif color == 'b':
                img.putpixel((x, y), (0, 0, b))
    img.show()