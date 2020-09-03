import math 
from PIL import Image, ImageDraw, ImageColor, ImagePath

import random
 
    
def draw_a_shape(number):
    
    img = Image.new("RGB", (128,128), "white")  
    
    image = ImageDraw.Draw(img)

    a = random.randint(0,129)

    #The center is at (64,64)

    side = 3
    
    angle = ((2*math.pi)/side)

    length = abs(64-a)

    if a > 64:
    
        point_1 = (a,64)
    
    else:
        
        point_1 = (64+length, 64)
    
    xy = [point_1]

    for i in range (side-1):
    
        x_coor = (length*math.cos((i+1)*angle)) +64
    
        y_coor = (length*math.sin((i+1)*angle)) +64
        
        x_coor = round(x_coor,5)
        
        y_coor = round(y_coor,5)
        
        point_2 = (x_coor, y_coor)
        
        xy.append(point_2)
    
        e = 64 - length

        f = 64 + length

    if a > 64:
   
        distance_x = abs(a-e)
    
        distance_y = abs(e-f)
    
    else:
    
        distance_x = abs(a-f)
    
        distance_y = abs(e-f)
       
    image.polygon(xy, fill =None, outline ="black")  
 
    img.save("a.png")

    imm = Image.open("a.png")

    if a > 64:
    
        im_1 = imm.crop((e,e,a,f)) 

    else:
        
        im_1 = imm.crop((a,e,f,f))

    im_1.save("a.png")

    imgg = Image.open("a.png")
    
    angle = random.randint(0,361)
    
    out = im_1.rotate(angle, fillcolor = "white")

    out.save("a.png")

    img_2 = Image.new("RGB", (128,128), "white")  

    image_2 = ImageDraw.Draw(img_2)

    coo = random.randint(0,128-distance_x)

    doo = random.randint(0,128-distance_y)

    back_im = img_2.copy()

    back_im.paste(out, (coo,doo))


    back_im.save("3_sides_"+str(number)+".png")

#     pix_val = list(back_im.getdata())

#     print(pix_val)

def main():
    for i in range(10000):
        draw_a_shape(i+4543)
        
main()
