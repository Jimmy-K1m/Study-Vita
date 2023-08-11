import numpy as np
import cv2
import math

def main():
    img_path = "C:\\Users\\watermelon.jpg"
    image = cv2.imread(img_path)
    image = cv2.resize(image,(320,240))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,mask = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)

    red = cv2.bitwise_and(image,image,mask=mask)

    ret,dst1 = cv2.threshold(image,100, 255, cv2.THRESH_TOZERO)


    cv2.imshow("Original", image)
    cv2.imshow("Converted",mask)
    cv2.imshow("DST1", dst1)
    cv2.imshow("red",red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

