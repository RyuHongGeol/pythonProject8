import cv2 as cv
import numpy as np
import pyautogui
import time
from pynput.keyboard import Key, Controller

kbControl = Controller()

cv.namedWindow("result");
cv.moveWindow("result", 0, 500);

img_piece = cv.imread('dino.png', cv.IMREAD_COLOR)
img_catcus = cv.imread('Catcus.png', cv.IMREAD_COLOR)
img_minicatcus = cv.imread('Catcus2.png', cv.IMREAD_COLOR)

h,w = img_piece.shape[:2]
catcus_h, catcust_w = img_catcus.shape[:2]
minicatcus_h, minicatcust_w = img_minicatcus.shape[:2]

while 1:
    pic = pyautogui.screenshot(region=(0 ,0, 700, 500))
    img_frame = np.array(pic)
    img_frame = cv.cvtColor(img_frame, cv.COLOR_RGB2BGR)
    meth = 'cv.TM_CCOEFF'
    method = eval(meth)

    res = cv.matchTemplate(img_piece, img_frame, method)
    res2 = cv.matchTemplate(img_catcus, img_frame, method)
    res3 = cv.matchTemplate(img_minicatcus, img_frame, method)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    catcus_min_val, catcus_max_val, catcus_min_loc, catcus_max_loc = cv.minMaxLoc(res2)
    minicatcus_min_val, minicatcus_max_val, minicatcus_min_loc, minicatcus_max_loc = cv.minMaxLoc(res3)


    top_left = max_loc
    catcus_top_left = catcus_max_loc
    minicatcus_top_left = minicatcus_max_loc



    bottom_right = (top_left[0] + w, top_left[1] + h)
    catcus_bottom_right = (catcus_top_left[0] + catcust_w, catcus_top_left[1] + catcus_h)
    minicatcus_bottom_right = (minicatcus_top_left[0] + minicatcust_w, minicatcus_top_left[1] + minicatcus_h)


    cv.rectangle(img_frame, top_left, bottom_right, (0, 255, 0),2)
    print("dino:",max_val, top_left)

    cv.rectangle(img_frame, catcus_top_left, catcus_bottom_right, (0, 255, 0),2)
    print("Catcus:",catcus_min_val, catcus_top_left)

    cv.rectangle(img_frame, minicatcus_top_left, minicatcus_bottom_right, (0, 255, 0), 2)
    print("MiniCatcus:", minicatcus_min_val, minicatcus_top_left)


    cv.imshow('result', img_frame)
    # cv.imshow('result', img_frame)
    jumpValue =  catcus_top_left[1] - top_left[1]
    jumpValue2 = minicatcus_top_left[1] - top_left[1]

    print("log", jumpValue, jumpValue2)
    # if(jumpValue < 0 or jumpValue2 < 0):
    #     jumpValue = 100
    #     jumpValue2 = 100

    if(jumpValue < 20 or jumpValue2 < 20 ):
        kbControl.press(Key.space)
        print("jump",jumpValue,jumpValue2)
        time.sleep(1)

    key = cv.waitKey(1)
    if key==27:
        break