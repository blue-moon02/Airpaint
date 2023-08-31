import HandTrackingModule as htm
import cv2

capture = cv2.VideoCapture(0)
detector = htm.handDetector(detectionConfidence=0.85)

draw_list = [] #The list of the coordinates of points that we want to draw upon

while True:
    _,image = capture.read()
    image = cv2.flip(image, 1)

    img = detector.findHands(image)
    userHands = detector.findPosition(image)    #userHands = [[id, x, y], [id, x, y]]
                                                #userHands = [[0, 100, 20], [1, 90,10]...
    
    for i in draw_list:
        cv2.circle(image, i, 10, 0, -1)

    if len(userHands) != 0:

        drawX = userHands[8][1]     # X-coordinate of the TIP OF MY INDEX FINGER     
        drawY = userHands[8][2]     # Y-coordinate of the TIP OF MY INDEX FINGER
                                    # (drawX, drawY)

        # The case where I want to draw

        if userHands[8][2] < userHands[6][2] and userHands[12][2] > userHands[10][2]:
            # Condtion to draw

            draw_list.append((drawX, drawY))

        # The case when I want to erase

        if userHands[8][2] < userHands[6][2] and userHands[12][2] < userHands[10][2]:
            # Condtion to erase
            
            for (x,y) in draw_list:
                if (x < drawX + 20 and x > drawX - 20) and (y < drawY + 20 and y > drawY - 20):
                    draw_list.remove((x,y))

    cv2.imshow("Drawing Board", image)
    cv2.waitKey(1)