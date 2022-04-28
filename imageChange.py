

# 图片二值化
from PIL import Image
import cv2
 
img = cv2.imread("test.jpg")#这里是原始图片！！！
print(img.shape)
cropped = img[0:200, 0:200] # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite('testx.jpg', cropped)
img = Image.open('testx.jpg')#这个是裁剪完的原始图片，还没做其他处理
 
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
Img = img.convert('L')
Img.save("test1.jpg")#这个是灰度处理完的图像
 
# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 127
 
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
 
# 图片二值化
photo = Img.point(table, '1')
photo.save("test2.jpg")#这个是二值化之后的图像

#二值图片转为数组
bdata_list = list(photo.getdata())
#print(bdata_list)

#8位一组
ob_list=[]
s=""
for i in range(1,len(bdata_list)+1):
    s+=str(bdata_list[i-1])
    if i%8==0:
        ob_list.append(s)
        s=""
#print(ob_list)

#二进制string转换为16进制数组
tempdata=[]#这个是字符串的16进制数组
lastdata=[]#这里是数字数组，每个元素值都在0-255之间
num=0
for i in range(1,len(ob_list)+1):
    a=hex(int(ob_list[i-1],2))
    tempdata.append(a)
for i in range(1,len(tempdata)+1):
    lastdata.append(int(tempdata[i-1],16))
    num=num+1
print(num)
#print(lastdata)
file=open('imgdata.txt','w') 
file.write(str(lastdata)) 
file.close() 