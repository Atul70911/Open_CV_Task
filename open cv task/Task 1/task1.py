import cv2 as cv
import numpy as np

def rectangle(img,a,b):#used for the big rectangle
    img = cv.rectangle(img,(a,a), (b,b), (0,255,0), 5)
    return img

def horizontal_lines(img,a,b):#used for the horizantal grid lines
    for i in range(1,5,1):
        y = int(i * (b / 5))
        img = cv.line(img, (a,y), (b,y), (0, 255, 0), 5)
    return img    

def vertical_lines(img,a,b):#used for the vertical grid lines
    y = int(2* (b / 5))
    img = cv.line(img, (y,a), (y,b), (0, 255, 0), 5)

    y = int(3* (b / 5))
    img = cv.line(img, (y,a), (y,b), (0, 255, 0), 5)
    
    y = int(1* (b / 5))
    x=int(2*(b/5))
    img = cv.line(img, (y,x), (y,b), (0, 255, 0), 5)
    
    y = int(4* (b / 5))
    x=int(2*(b/5))
    img = cv.line(img, (y,x), (y,b), (0, 255, 0), 5)

    y = int(1* (b / 5))
    x=int(2*(b/5))
    f=int(1*(b/5))
    img = cv.line(img, (y,f), (y,x), (0, 0, 255), 5,lineType=cv.LINE_AA)
    y = int(4* (b / 5))
    x=int(2*(b/5))
    f=int(1*(b/5))
    img = cv.line(img, (y,f), (y,x), (0, 0, 255), 5,lineType=cv.LINE_AA)
    return img

def dotted_line(img, a, b,c,d, diff):#used to generate teh dotted lines
    if a == c:  # Vertical line
        y_start = min(b, d)
        y_end = max(b, d)
        for y in range(y_start, y_end, diff * 4):
            img=cv.line(img, (a, y), (a, y + diff), (0, 0, 255), 5)
    elif b == d:  # Horizontal line
        x_start = min(a, c)
        x_end = max(a, c)
        for x in range(x_start, x_end, diff * 2):
            img=cv.line(img, (x, b), (x + diff, d), (0, 0, 255), 5)
            

    return img

task_img=cv.imread('Task.png')
#######Customisation to make the image image size multiple of 10##############
a=10
b=task_img.shape[0]-13
###########Customisation Ends##############################

########Calling other function###########
task_img =rectangle(task_img,a,b)
task_img =horizontal_lines(task_img,a,b)   
task_img=vertical_lines(task_img,a,b)
################Done Calling#######################

#####Calling dotted line fuction for placing dotted line a different places#############
a,b,c,d,diff=162,10,320,10,10
task_img=dotted_line(task_img,a,b,c,d,diff)#line 1
a,b,c,d,diff=162,160,320,160,10
task_img=dotted_line(task_img,a,b,c,d,diff)#line 2
a,b,c,d,diff=162,480,320,480,10
task_img=dotted_line(task_img,a,b,c,d,diff)#line 3
a,b,c,d,diff=162,640,320,640,10
task_img=dotted_line(task_img,a,b,c,d,diff)#line 4
a,b,c,d,diff=640,10,640,160,6
task_img=dotted_line(task_img,a,b,c,d,diff)#line 5
a,b,c,d,diff=162,10,162,160,6
task_img=dotted_line(task_img,a,b,c,d,diff)#line 6
#############Dotted Function Ends ####################
cv.imshow("task",task_img)
#####saving the image as output_task1.png###############
cv.imwrite(r"C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/output_task1.png",task_img)
###Done##########
cv.waitKey(0)
cv.destroyAllWindows
###########End Of Code##################