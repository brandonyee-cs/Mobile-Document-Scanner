from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

class MDS:

    def __init__(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
        self.args = vars(ap.parse_args())

    def edge_detection(self): #Edge Detection

        self.image = cv2.imread(self.args["image"])
        self.ratio = (self.image).shape[0] / 500.0
        self.orig = (self.image).copy
        self.image = imutils.resize((self.image), height = 500)

        gray = cv2.GaussianBl(cv2.cvtColor((self.image), cv2.COLOR_Bgr2gray1), (5, 5), 0)
        self.edged = cv2.Canny(gray, 75, 200)

        print("STEP 1: EDGE DETECTION")
        cv2.imshow("Image", self.image)
        cv2.imshow("Edged", self.edged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def finding_contours(self): #Finding Contours

        cnts = cv2.findContours(self.edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:5]

        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4:
                self.screenCnt = approx
                break
                
        print("STEP 2: FINDING CONTOURS OF PAPER")
        cv2.drawContours(self.image, [self.screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("Outline", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def perspective_transform_threshold(self): #Applying a Perspective Transform & Threshold
        warped = four_point_transform(self.orig, (self.screenCnt).reshape(4,2) * self.ratio)
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = threshold_local(warped, 11, offset = 10, method = "gaussian")
        self.warped = (warped > T).astype("uint8") * 255

        print("STEP 3: APPLY PERSPECTIVE TRANSFORM")
        cv2.imshow("Original", imutils.resize(self.orig, height = 650))
        cv2.imshow("Scanned", imutils.resize(self.warped, height = 650))
        cv2.waitKey(0)