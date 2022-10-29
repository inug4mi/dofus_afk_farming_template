import pyautogui as pg
import time

imageOffset = 25

def checkImage():
  try:
    pos = pg.locateOnScreen("./image1.jpg", confidence=0.8)
    pg.moveTo(pos[0]+imageOffset,pos[1]+imageOffset)
    pg.click()
    time.sleep(1)
  except:
    print("image loaded but couldn't find it in Dofus")

checkImage()
