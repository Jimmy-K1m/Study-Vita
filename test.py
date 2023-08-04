
import numpy as np
import cv2

red_color = (0, 0, 255)

def calculate_neighborhood_average(image, center_x, center_y):
    # Differences with other neighbor pixels
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

    total_b, total_g, total_r = 0, 0, 0
    count = 0

    for i in range(9):
        x = center_x + dx[i]
        y = center_y + dy[i]

        if 0 <= x < len(image[0]) and 0 <= y < len(image):
            b, g, r = image[y][x]
            total_b += b
            total_g += g
            total_r += r
            count += 1

    average_b = total_b / count
    average_g = total_g / count
    average_r = total_r / count

    return average_b, average_g, average_r



def main():
    img_path = "C:\\Users\\orange.jpg"
    image = cv2.imread(img_path)
    image = cv2.resize(image,(320,240))

    height, width, _ = image.shape
    print(image.shape)
    center_x = width // 2
    center_y = height // 2

    print(center_y, center_x)

    b_half, g_half, r_half = image[center_y, center_x]
    b_three_fifth, g_three_fifth, r_three_fifth = image[(width // 2), (3 * height // 5)]
    b_two_third, g_two_third, r_two_third = image[(width // 2), (2 * height // 3)]

    cv2.imshow("image", image)

    pinned_image = image.copy()
    cv2.line(pinned_image, ((width // 2), (height // 2)), ((width // 2), (height // 2)), red_color, 5)
    cv2.line(pinned_image, ((width // 2), (3 * height // 5)), ((width // 2), (3 * height // 5)), red_color, 5)
    cv2.line(pinned_image, ((width // 2), (2 * height // 3)), ((width // 2), (2 * height // 3)), red_color, 5)

    print("color from center: ", b_half, g_half, r_half)
    print("color from 2/5 point", b_three_fifth, g_three_fifth, r_three_fifth)
    print("color from 1/3 point", b_two_third, g_two_third, r_two_third)

    # Calculation average 
    average_b_center, average_g_center, average_r_center = calculate_neighborhood_average(image, center_x, center_y)
    average_b_three_fifth, average_g_three_fifth, average_r_three_fifth = calculate_neighborhood_average(image, width // 2, 3 * height // 5)
    average_b_two_third, average_g_two_third, average_r_two_third = calculate_neighborhood_average(image, width // 2, 2 * height // 3)

    print("Average B,G,R from center pixel:", average_b_center,average_g_center,average_r_center)

    print("Average B,G,R from 2/5 point:", average_b_three_fifth,average_g_three_fifth,average_r_three_fifth)

    print("Average B,G,R from 1/3 point:", average_b_two_third, average_g_two_third, average_r_two_third)

    total_average_b = (average_b_center+ average_b_three_fifth + average_b_two_third) / 3
    total_average_g = (average_g_center+ average_g_three_fifth + average_g_two_third) / 3
    total_average_r = (average_r_center+ average_r_three_fifth + average_r_two_third) / 3

    print("Total Average:", total_average_b, total_average_g, total_average_r)

    # Algorithm for classification with 3 dimension distances between two points(3차원 공간 상 가장 적은 거리를 가진 클래스를 선택하는 알고리즘) 
    # kiwi bgr(44,99,106) watermelon bgr(18,6,194) orange bgr(0,107,254)




    
    cv2.imshow("pin", pinned_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
