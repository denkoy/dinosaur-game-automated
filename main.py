# This is a sample Python script.
from PIL import ImageGrab
import time
import pyautogui
dinosaur_lower=(130,700)
dinosaur_high=(130,580)
treshold=100

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

#time.sleep(2)

def obstacle(photo):
    for y in range(photo.height):
        for x in range(photo.width):
            if photo.getpixel((x,y))<treshold:
                return True
    return False

def jump(sleep):
    pyautogui.keyDown('space')
    time.sleep(sleep)
    pyautogui.keyUp('space')




time.sleep(2)
sleep=.1
counter=0
photo1=ImageGrab.grab([870,415,900,430])
photo1_gray=photo1.convert('L')
while(True):
    photo = ImageGrab.grab([300,560,400,670])
    gray_image=photo.convert('L')
    if counter==10:
        counter-=10
        sleep+=.05
    if obstacle(gray_image):
        jump(sleep)
        counter+=1
    if obstacle(photo1_gray):
        break
    photo1=ImageGrab.grab([870,415,900,430])
    photo1_gray=photo1.convert('L')
