import cv2 as cv
import numpy as np

main_image=cv.imread(r'C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/Task 2/CVTask.png')
ha_img=cv.imread(r'C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/Task 2/Ha.jpg')
haha_img=cv.imread(r'C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/Task 2/HaHa.jpg')
lamo_img=cv.imread(r'C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/Task 2/LAMO.jpg')
xd_img=cv.imread(r'C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/Task 2/XD.jpg')
black=np.zeros((512,512,3),np.uint8)
point_main=[]
point_ha=[]
point_haha=[]
point_lamo=[]
point_xd=[]


def click_mouse_event_1(event,x,y,flags,params):
    img=params[0]
    pointlist=params[1]
    name=params[2]
    if len(pointlist)%4!=0 or len(pointlist)==0:
        if event==cv.EVENT_LBUTTONDOWN:
            pointlist.append([x,y])
            img=cv.circle(img,(x,y),3,(0,0,255),-1)
            print(pointlist)
            cv.imshow(name,img)

def click_mouse_event(event,x,y,flags,params):
    if len(point_main)%16!=0 or len(point_main)==0:
        if event==cv.EVENT_LBUTTONDOWN:
              point_main.append([x,y])
              clc=cv.circle(main_image,(x,y),3,(255,0,0),-1)
              print(point_main)
              cv.imshow("main",clc)  
                  
        
ha,main,haha,lamo,xd="ha","main","haha","lamo","xd"

while len(point_ha)!=4:
    cv.imshow("ha",ha_img)
    cv.setMouseCallback("ha",click_mouse_event_1,[ha_img,point_ha,ha])
    cv.waitKey(0)
while len(point_haha)!=4:  
    cv.imshow("haha",haha_img)
    cv.setMouseCallback("haha",click_mouse_event_1,[haha_img,point_haha,haha])  
    cv.waitKey(0)
while len(point_lamo)!=4:
    cv.imshow("lamo",lamo_img)
    cv.setMouseCallback("lamo",click_mouse_event_1,[lamo_img,point_lamo,lamo])
    cv.waitKey(0)
while len(point_xd)!=4:
    cv.imshow("xd",xd_img)
    cv.setMouseCallback("xd",click_mouse_event_1,[xd_img,point_xd,xd])
    cv.waitKey(0)

while len(point_main)!=16:
    cv.imshow("main",main_image)
    cv.setMouseCallback("main",click_mouse_event)
    cv.waitKey(0)    

points_backgroundha=np.array([[point_main[0][0],point_main[0][1]],[point_main[1][0],point_main[1][1]],[point_main[2][0],point_main[2][1]],[point_main[3][0],point_main[3][1]]],dtype=np.float32)
points_backgroundhaha=np.array([[point_main[4][0],point_main[4][1]],[point_main[5][0],point_main[5][1]],[point_main[6][0],point_main[6][1]],[point_main[7][0],point_main[7][1]]],dtype=np.float32)
points_backgroundlamo=np.array([[point_main[8][0],point_main[8][1]],[point_main[9][0],point_main[9][1]],[point_main[10][0],point_main[10][1]],[point_main[11][0],point_main[11][1]]],dtype=np.float32)
points_backgroundxd=np.array([[point_main[12][0],point_main[12][1]],[point_main[13][0],point_main[13][1]],[point_main[14][0],point_main[14][1]],[point_main[15][0],point_main[15][1]]],dtype=np.float32)

pointblack=np.array([[0,0],[510,310],[126,345],[231,432]],dtype=np.float32)

points_overlayha=np.array([[point_ha[0][0],point_ha[0][1]],[point_ha[1][0],point_ha[1][1]],[point_ha[2][0],point_ha[2][1]],[point_ha[3][0],point_ha[3][1]]],dtype=np.float32)
points_overlayhaha=np.array([[point_haha[0][0],point_haha[0][1]],[point_haha[1][0],point_haha[1][1]],[point_haha[2][0],point_haha[2][1]],[point_haha[3][0],point_haha[3][1]]],dtype=np.float32)
points_overlaylamo=np.array([[point_lamo[0][0],point_lamo[0][1]],[point_lamo[1][0],point_lamo[1][1]],[point_lamo[2][0],point_lamo[2][1]],[point_lamo[3][0],point_lamo[3][1]]],dtype=np.float32)
points_overlayxd=np.array([[point_xd[0][0],point_xd[0][1]],[point_xd[1][0],point_xd[1][1]],[point_xd[2][0],point_xd[2][1]],[point_xd[3][0],point_xd[3][1]]],dtype=np.float32)

transformation_matrixha = cv.getPerspectiveTransform(points_overlayha, points_backgroundha)
transformation_matrixhaha = cv.getPerspectiveTransform(points_overlayhaha, points_backgroundhaha)
transformation_matrixlamo = cv.getPerspectiveTransform(points_overlaylamo, points_backgroundlamo)
transformation_matrixxd = cv.getPerspectiveTransform(points_overlayxd, points_backgroundxd)

warped_overlayha = cv.warpPerspective(ha_img, transformation_matrixha, (main_image.shape[1], main_image.shape[0]))
warped_overlayhaha = cv.warpPerspective(haha_img, transformation_matrixhaha, (main_image.shape[1], main_image.shape[0]))
warped_overlaylamo = cv.warpPerspective(lamo_img, transformation_matrixlamo, (main_image.shape[1], main_image.shape[0]))
warped_overlayxd = cv.warpPerspective(xd_img, transformation_matrixxd, (main_image.shape[1], main_image.shape[0]))

result_imageh = cv.addWeighted(main_image, 1, warped_overlayha, 1, 0)
result_imageha = cv.addWeighted(result_imageh, 1, warped_overlayhaha, 1, 0)
result_imagel = cv.addWeighted(result_imageha, 1, warped_overlaylamo, 1, 0)
result_imagex = cv.addWeighted(result_imagel, 1, warped_overlayxd, 1, 0)

cv.imshow("main",result_imagex)

cv.imwrite(r"C:/Users/Atul Kumar/Documents/roboism/after end sem/final task/Task 2/output task 22.png",result_imagex)

cv.waitKey(0)
cv.destroyAllWindows()