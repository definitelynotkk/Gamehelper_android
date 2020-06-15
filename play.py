import os
import cv2
import numpy as np
import time

def get_screenshot(id):
    os.system('adb shell screencap -p /sdcard/%s.png' % str(id))
    os.system('adb pull /sdcard/%s.png .' % str(id))
    
def build(distance):
    press_time = int(distance * 0.75)
    cmd = ('adb shell input swipe 500 1500 500 1500 ' + str(press_time)) 
    os.system(cmd)
    print('distance:' + str(distance) + 'press time:' + str(press_time))

temp1 = cv2.imread('template.png', 0)


for i in range(10000):
    get_screenshot(0)
    img_rgb = cv2.imread('%s.png' % 0, 0)

    res2 = cv2.matchTemplate(img_rgb, temp1, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res2 >= 0.8)
    target_x = 0
    for pt in zip(*loc[::-1]):
        if pt[0] > 300:
            print('target found!')
            target_x = pt[0]
            target_y = pt[1]
            print(target_x, target_y)
            break
            



    #img_rgb = cv2.circle(img_rgb, (target_x, 2030), 10, 255, -1)

    #cv2.imwrite('last.png', img_rgb)
    print(target_x)

    distance = target_x - 235
    #distance = distance ** 1.5
    build(distance)
    time.sleep(3)
