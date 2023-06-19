import math
import cv2
import numpy as np
import HandTracking as htm
import autopy
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import pyautogui
import time
import web
import concurrent.futures



##########################
wCam, hCam = 640, 480
frameR = 120 # Frame Reduction
smoothening = 7
volflag=False
brflag=False
scroll=False
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
vol=0
minVol= volRange[0]
maxVol = volRange[1]

GetBright = sbc.get_brightness(display=0)[0]
print(GetBright)
w=web.web()



cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


detector = htm.HandDetector(maxHands=2)
wScr, hScr = autopy.screen.size()

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        hands,img=executor.submit(detector.findHands,img).result()
    # hands, img = detector.findHands(img)

    if hands:
        # Hand 1

        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
    
    # lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers and thumb
        if len(lmList1) != 0:
            x1, y1 = lmList1[8][0:2]
            x2, y2 = lmList1[12][0:2]
            x4, y4 = lmList1[4][0:2]
            vx, vy = (x1+x4)//2, (y1+y4)//2
            mx, my=(x1+x2)//2,(y1+y2)//2

        

        # 3. Check which fingers are up
        with concurrent.futures.ThreadPoolExecutor() as executor:
            fingers=executor.submit(detector.fingersUp,hand1).result()

        # fingers = detector.fingersUp(hand1)


        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                  (255, 0, 255), 2)
        if handType1=="Left":
            if fingers[1]==1 and fingers[2:5]==[0,0,0] and fingers[0]==0:
                volflag= True
                brflag=False
            elif fingers[1:3]==[1,1] and fingers[3:5]==[0,0] and fingers[0]==0:
                volflag=False
                brflag=True
            elif fingers[0:3]==[1,1,1] and fingers[3:5]==[0,0]:
                volflag=False
                brflag=False
                timestamp = time.strftime('%Y%m%d%H%M%S')
                ss=pyautogui.screenshot()
                ss.save(r"C:\Users\muhaa\Pictures\MouseScreenshots\Ss"+timestamp+".png")
            elif fingers[1:5]==[1,1,1,1] and fingers[0]==0:
                # web.web.uwl()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(w.uwl).result()
            elif fingers[0:5]==[1,1,1,1,1]:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(w.email).result()
                # web.web.email()
            elif fingers[0:2]==[0,0] and fingers[2:5]==[1,1,1]:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(w.guiweb).result()

            elif fingers[0:5]==[0,0,0,0,0]:
                volflag=False
                brflag=False
            

            print ("volflag=",volflag)
            print ("brflag=",brflag)

        if handType1 == "Right":

            if brflag == True:
                if fingers[0] == 1 and fingers[1] == 1 and fingers[2:4]==[0,0]:
                    cv2.line(img, (x1,y1), (x4,y4), (255,0,255), 3 )

                    cv2.circle(img, (vx,vy), 15, (255,0,255), cv2.FILLED )
                    brlength= math.hypot(x1-x4, y1-y4)
                    brightness = np.interp(brlength, [0, 100], [0, 100])
                    if fingers[4]==1:
                        sbc.set_brightness(brightness)

            if volflag==True:

                if fingers[0] == 1 and fingers[1] == 1 and fingers[2:4]==[0,0]:
                    cv2.line(img, (x1,y1), (x4,y4), (255,0,255), 3 )

                    cv2.circle(img, (vx,vy), 15, (255,0,255), cv2.FILLED )

                    vollength= math.hypot(x1-x4, y1-y4)

                # volume control

                    vol = np.interp(vollength, [0, 100], [minVol, maxVol])

                    if fingers[4]==1:
                        volume.SetMasterVolumeLevel(vol, None)



        # 4. Only Index Finger : Moving Mode
            if fingers[1:3] == [1,1] and fingers[3:5] == [0,0] and fingers[0]==0:
            # 5. Convert Coordinates
                x3 = np.interp(mx, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(my, (frameR, hCam - frameR), (0,hScr))

              # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

    #         # 7. Move Mouse
                length, lineInfo, img = detector.findDistance((x1,y1), (x2,y2), img)
                scroll=False
                if length < 30:
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        executor.submit(autopy.mouse.move,wScr - clocX, clocY).result()
                    # autopy.mouse.move(wScr - clocX, clocY)

                plocX, plocY = clocX, clocY

    #      Clicking Mode
            if fingers[0:2] == [0,0] and fingers[2] == 1 and fingers[3:5]==[0,0]:
                autopy.mouse.click()

            # 9. Find distance between fingers
                length, lineInfo, img = detector.findDistance((x1,y1), (x2,y2), img)
                # print(length)
            # 10. Click mouse if distance short
                # if length < 40:
                #     cv2.circle(img, (lineInfo[4], lineInfo[5]),
                #         15, (0, 255, 0), cv2.FILLED)



            if fingers[1]==1 and fingers[2:5] == [0,0,0] and fingers[0]==0:
                autopy.mouse.click(autopy.mouse.Button.RIGHT)

            if fingers[0]==0 and fingers[1:4]==[1,1,1] and fingers[4]==0:
                pyautogui.mouseDown(button='left')

            if fingers[0:2]==[0,0] and fingers[2:5]==[1,1,1]:
                w = web.web()
            if fingers[0:4]==[0,0,0,0] and fingers[4]==1:
                scroll=True
            if scroll:
                if lmList1[20][1]> lmList1[17][1]:
                    pyautogui.scroll(-120)
                elif lmList1[20][1]< lmList1[17][1]:
                    pyautogui.scroll(120)







    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # 12. Display
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)



