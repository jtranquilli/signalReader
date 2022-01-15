import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
        
    if results.multi_hand_landmarks:
    
        for handLms in results.multi_hand_landmarks:
            
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #height width and channels of image
                
                #print(id,cx,cy) to get id then x and y pixels
                thumbTip = handLms.landmark[mpHands.HandLandmark.THUMB_TIP].y * h * (-1) + 700
                
                indexTip = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y * h * (-1) + 700
                
                midFingerTip = handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y * h * (-1) + 700
                
                ringFingerTip = handLms.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y * h * (-1) + 700
                
                print(handLms.landmark[mpHands.HandLandmark.THUMB_TIP].y * h * (-1) + 700)
                 
            
            
            if (thumbTip > indexTip and thumbTip < midFingerTip):
                 cv2.putText(img, str("Undefined"),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)
            
            if (thumbTip > indexTip and thumbTip < midFingerTip):
                 cv2.putText(img, str("Undefined"),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)
            
            if (int(thumbTip - indexTip) in range(-90,120)):
                 cv2.putText(img, str("Undefined"),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)     
                 
            else:
                if (thumbTip > indexTip and thumbTip > ringFingerTip and thumbTip > midFingerTip):
                    cv2.putText(img, str("Thumbs up"),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)
                if (thumbTip < indexTip and thumbTip < midFingerTip):
                    cv2.putText(img, str("Thumbs down"),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)
                
        
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            #simply remove the last parameter to stop illustrating lines
            
    cv2.imshow("Image", img)
    
    cv2.waitKey(1)
