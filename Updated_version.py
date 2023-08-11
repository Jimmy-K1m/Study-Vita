import numpy as np
import cv2
import math

lower_watermelon = np.array([0, 0, 100]) 
upper_watermelon = np.array([50, 50, 255])  

lower_orange = np.array([0, 100, 150])
upper_orange = np.array([50, 150, 255])

lower_kiwi = np.array([0, 100, 0])
upper_kiwi = np.array([70, 180, 140])

def get_average_pixel(imag):

    print(imag.shape)
    total_b, total_g, total_r = 0, 0, 0
    count = 0

    for i in range(320):
        for j in range(240):
            b,g,r = imag[j][i]
           
            if(b!=0 and g!=0 and r!= 0):
                total_b += b
                total_g += g
                total_r += r
                count += 1

    average_b = total_b / count
    average_g = total_g / count
    average_r = total_r / count

    print("count: ", count)

    return average_b, average_g, average_r


def calculation_of_distance(total_average, index): 
    if index == 0 :
        squared_kiwi = math.pow((total_average[0]-44),2) + math.pow((total_average[1]-99),2) + math.pow((total_average[2]-106),2)
        distance_from_object = math.sqrt(squared_kiwi)

    elif index == 1:
        squred_watermelon =  math.pow((total_average[0]-18),2) + math.pow((total_average[1]-6),2) + math.pow((total_average[2]-194),2)
        distance_from_object = math.sqrt(squred_watermelon)

    elif index == 2:
        squared_orange =  math.pow((total_average[0]),2) + math.pow((total_average[1]-107),2) + math.pow((total_average[2]-254),2)
        distance_from_object= math.sqrt(squared_orange)

    return distance_from_object



def main():
    img_path = "C:/Users/orange.jpg" 
    image = cv2.imread(img_path)
    image = cv2.resize(image,(320,240))
   
    mask_watermelon = cv2.inRange(image, lower_watermelon, upper_watermelon)
    mask_orange = cv2.inRange(image, lower_orange, upper_orange)
    mask_kiwi = cv2.inRange(image, lower_kiwi, upper_kiwi)


    watermelon_only = cv2.bitwise_and(image, image, mask=mask_watermelon)  
    orange_only = cv2.bitwise_and(image, image, mask=mask_orange)
    kiwi_only = cv2.bitwise_and(image, image, mask=mask_kiwi)

    semi_combined = cv2.bitwise_or(watermelon_only,orange_only)
    combined = cv2.bitwise_or(semi_combined, kiwi_only)

    average_b, average_g, average_r = get_average_pixel(combined)
    average = average_b, average_g, average_r

    print(average)

    item = [calculation_of_distance(average,0),calculation_of_distance(average,1),calculation_of_distance(average,2)]
    index = item.index(min(item))

    if min(item) > 30 : 
        print("Wrong item is placed")


    if index == 0 :
        print("Kiwi juice is detected!\n" ,item[0])
    elif index == 1 :
        print("Watermelon juice is detected!\n",item[1])
    elif index == 2 :
        print("Orange juice is detected!\n",item[2])
    

    cv2.imshow("Original", image)
    cv2.imshow("Filtered", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
