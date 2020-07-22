import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(img_name):
    image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("faild to read the image")
        exit
    return image


def draw_images(images, circles):
    plt.subplot(122), plt.imshow(images[0], cmap='gray'), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(121), plt.imshow(circles[0], cmap='gray'), plt.title('Circles Image')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    images = []
    images.append(read_image('q2_images/00401.png'))

    img = cv2.medianBlur(images[0], 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 20,
                               param1=50, param2=80, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        # cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    # circles = [cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20) for image in images]
    draw_images(images, [cimg])


