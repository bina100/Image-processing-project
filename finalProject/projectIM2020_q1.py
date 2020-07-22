import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(img_name):
    image = cv2.imread(img_name, cv2.COLOR_BGR2GRAY)
    if image is None:
        print("faild to read the image")
        exit
    return image


def corner_identify(img):
    img_cpy = img.copy()
    gray = cv2.cvtColor(img_cpy, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 4, 3, 0.04)
    dst = cv2.dilate(dst, None)
    img_cpy[dst > 0.01 * dst.max()] = [255, 0, 0]
    return img_cpy


def draw_images(src, corners, just_sole):
    plt.subplot(133), plt.imshow(src, cmap='gray'), plt.title('Rect Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(corners, cmap='gray'), plt.title('Harris corner')
    plt.xticks([]), plt.yticks([])
    plt.subplot(131), plt.imshow(just_sole, cmap='gray'), plt.title('Just sole')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img1 = read_image('q1_images/2.JPG')
    img2 = read_image('q1_images/3.JPG')
    img3 = read_image('q1_images/25.JPG')
    ####################### A #########################
    img1_corners = corner_identify(img1)
    img2_corners = corner_identify(img2)
    img3_corners = corner_identify(img3)

    ####################### B #########################
    filter_x = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    filter_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    img1_for_sole = np.int32(img1)
    img2_for_sole = np.int32(img2)
    img3_for_sole = np.int32(img3)

    draw_images(img1, img1_corners, img1_for_sole)
    draw_images(img2, img2_corners, img2_for_sole)
    draw_images(img3, img3_corners, img3_for_sole)

