import numpy as np
import cv2
import keyboard
import mss

template_list = []
'''for i in range(10):
    template_list.append(str(i))'''
template_list.extend(str(i) for i in range(10))
template_list.extend(['bird1', 'bird2', 'cactus1', 'cactus2', 'return'])
template = []
template_hight = []
template_width = []
res = []
threshold = 0.90
loc = []

window = {"top": 320, "left": 160, "width": 800-160, "height": 480-320}
mss = mss.mss()


for i, template_name in enumerate(template_list):
    template.insert(i, cv2.imread('images/%s.png' % template_name, 0))
    template_hight.insert(i, template[i].shape[0])
    template_width.insert(i, template[i].shape[1])

while True:
    test_img = np.array(mss.grab(window))
    test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2BGR)
    gray_test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2GRAY)

    for i, template_name in enumerate(template_list):
        res.insert(i, cv2.matchTemplate(gray_test_img, template[i], cv2.TM_CCOEFF_NORMED))
        loc.insert(i, np.where(res[i] >= threshold))


        for pt in zip(*loc[i][::-1]):
            cv2.rectangle(test_img, pt, (pt[0] + template_width[i], pt[1] + template_hight[i]), (0, 0, 255), 2)

            if pt[0] < 155 :
                keyboard.press('space')
                #keyboard.release('space')

    if loc[14]:
        empty_check = np.array(loc[14])
        if empty_check.size != 0:
            keyboard.press('space')
            keyboard.release('space')

    cv2.imshow('window', test_img)
    cv2.waitKey(1)