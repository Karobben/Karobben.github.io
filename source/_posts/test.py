import cv2
import numpy as np
import scrcpy


client = scrcpy.Client('192.168.1.71:5555')
client.start(threaded=True)

Ratio = 3
#start to cast to screen
img = cv2.resize(client.last_frame, (int(client.resolution[0]/Ratio),  int(client.resolution[1]/Ratio)), interpolation = cv2.INTER_AREA)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
click_area_old = grey[279:280,:]


kernel = np.ones((10,10),np.float32)/100


while(True):
    img = cv2.resize(client.last_frame, (int(client.resolution[0]/Ratio),  int(client.resolution[1]/Ratio)), interpolation = cv2.INTER_AREA)
    grey = img[:,:,2]
    click_area = grey[279:280,:]
    if np.sum(click_area - click_area_old) != 0:
        click_diff = click_area - click_area_old
        click_area_old = click_area
        #click_diff[click_diff!=0] == 255
        click_diff = cv2.filter2D(click_diff,-1,kernel)
        click_diff = cv2.filter2D(click_diff,-1,kernel)
        click_diff = cv2.filter2D(click_diff,-1,kernel)
        click_diff = cv2.filter2D(click_diff,-1,kernel)
        click_diff = cv2.filter2D(click_diff,-1,kernel)
        click_diff = cv2.filter2D(click_diff,-1,kernel)
        MAX = click_diff.max()
        if MAX <200:
            for i in np.where(click_diff[0]==MAX)[0]:
                X = int(i * Ratio)
                print("click", X, Y, MAX)
                Y = int(279 * Ratio)
                client.control.touch(X, Y, scrcpy.ACTION_DOWN)
                client.control.touch(X, Y, scrcpy.ACTION_UP)

    # get the click area 
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()



img = cv2.resize(client.last_frame, (int(client.resolution[0]/Ratio),  int(client.resolution[1]/Ratio)), interpolation = cv2.INTER_AREA)
old_gray = img[:,:,2].copy()
while(True):
    img = cv2.resize(client.last_frame, (int(client.resolution[0]/Ratio),  int(client.resolution[1]/Ratio)), interpolation = cv2.INTER_AREA)
    gray = img[:,:,2].copy()
    diff = old_gray - gray
    old_gray = gray.copy()
    print(np.sum(diff))
    cv2.imshow('image',diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()








# store the background 
BK = img
BK = cv2.cvtColor(BK, cv2.COLOR_BGR2GRAY)
# Gaussian smooth
kernel = np.ones((10,10),np.float32)/100
BK = cv2.filter2D(BK,-1,kernel)


# detect the change
while(True):
    with mss() as sct :
        img = np.array(sct.grab(cords)) #sct.grab(cords/monitor)
    output = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.filter2D(img,-1,kernel)
    img = img - BK
    #img = cv2.filter2D(img,-1,kernel)
    img[img<=10] = 255
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()










while(True):
    with mss() as sct :
        img = np.array(sct.grab(cords)) #sct.grab(cords/monitor)
    output = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.filter2D(img,-1,kernel)
    img = img - BK
    #img = cv2.filter2D(img,-1,kernel)
    img[img<=5] = 255
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 4, 100)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    # show the output image
    cv2.imshow("output", output)
    #cv2.imshow("output2", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()

gray = img
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 10, 100)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	cv2.imshow("output", output)
	cv2.waitKey(0)

