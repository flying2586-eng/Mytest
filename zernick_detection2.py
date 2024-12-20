import time

import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np



g_N = 7

M00 = np.array([0, 0.0287, 0.0686, 0.0807, 0.0686, 0.0287, 0,
                0.0287, 0.0815, 0.0816, 0.0816, 0.0816, 0.0815, 0.0287,
                0.0686, 0.0816, 0.0816, 0.0816, 0.0816, 0.0816, 0.0686,
                0.0807, 0.0816, 0.0816, 0.0816, 0.0816, 0.0816, 0.0807,
                0.0686, 0.0816, 0.0816, 0.0816, 0.0816, 0.0816, 0.0686,
                0.0287, 0.0815, 0.0816, 0.0816, 0.0816, 0.0815, 0.0287,
                0, 0.0287, 0.0686, 0.0807, 0.0686, 0.0287, 0]).reshape((7, 7))

M11R = np.array([0, -0.015, -0.019, 0, 0.019, 0.015, 0,
                 -0.0224, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0224,
                 -0.0573, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0573,
                 -0.069, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.069,
                 -0.0573, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0573,
                 -0.0224, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0224,
                 0, -0.015, -0.019, 0, 0.019, 0.015, 0]).reshape((7, 7))

M11I = np.array([0, -0.0224, -0.0573, -0.069, -0.0573, -0.0224, 0,
                 -0.015, -0.0466, -0.0466, -0.0466, -0.0466, -0.0466, -0.015,
                 -0.019, -0.0233, -0.0233, -0.0233, -0.0233, -0.0233, -0.019,
                 0, 0, 0, 0, 0, 0, 0,
                 0.019, 0.0233, 0.0233, 0.0233, 0.0233, 0.0233, 0.019,
                 0.015, 0.0466, 0.0466, 0.0466, 0.0466, 0.0466, 0.015,
                 0, 0.0224, 0.0573, 0.069, 0.0573, 0.0224, 0]).reshape((7, 7))

M20 = np.array([0, 0.0225, 0.0394, 0.0396, 0.0394, 0.0225, 0,
                0.0225, 0.0271, -0.0128, -0.0261, -0.0128, 0.0271, 0.0225,
                0.0394, -0.0128, -0.0528, -0.0661, -0.0528, -0.0128, 0.0394,
                0.0396, -0.0261, -0.0661, -0.0794, -0.0661, -0.0261, 0.0396,
                0.0394, -0.0128, -0.0528, -0.0661, -0.0528, -0.0128, 0.0394,
                0.0225, 0.0271, -0.0128, -0.0261, -0.0128, 0.0271, 0.0225,
                0, 0.0225, 0.0394, 0.0396, 0.0394, 0.0225, 0]).reshape((7, 7))

M31R = np.array([0, -0.0103, -0.0073, 0, 0.0073, 0.0103, 0,
                 -0.0153, -0.0018, 0.0162, 0, -0.0162, 0.0018, 0.0153,
                 -0.0223, 0.0324, 0.0333, 0, -0.0333, -0.0324, 0.0223,
                 -0.0190, 0.0438, 0.0390, 0, -0.0390, -0.0438, 0.0190,
                 -0.0223, 0.0324, 0.0333, 0, -0.0333, -0.0324, 0.0223,
                 -0.0153, -0.0018, 0.0162, 0, -0.0162, 0.0018, 0.0153,
                 0, -0.0103, -0.0073, 0, 0.0073, 0.0103, 0]).reshape(7, 7)

M31I = np.array([0, -0.0153, -0.0223, -0.019, -0.0223, -0.0153, 0,
                 -0.0103, -0.0018, 0.0324, 0.0438, 0.0324, -0.0018, -0.0103,
                 -0.0073, 0.0162, 0.0333, 0.039, 0.0333, 0.0162, -0.0073,
                 0, 0, 0, 0, 0, 0, 0,
                 0.0073, -0.0162, -0.0333, -0.039, -0.0333, -0.0162, 0.0073,
                 0.0103, 0.0018, -0.0324, -0.0438, -0.0324, 0.0018, 0.0103,
                 0, 0.0153, 0.0223, 0.0190, 0.0223, 0.0153, 0]).reshape(7, 7)

M40 = np.array([0, 0.013, 0.0056, -0.0018, 0.0056, 0.013, 0,
                0.0130, -0.0186, -0.0323, -0.0239, -0.0323, -0.0186, 0.0130,
                0.0056, -0.0323, 0.0125, 0.0406, 0.0125, -0.0323, 0.0056,
                -0.0018, -0.0239, 0.0406, 0.0751, 0.0406, -0.0239, -0.0018,
                0.0056, -0.0323, 0.0125, 0.0406, 0.0125, -0.0323, 0.0056,
                0.0130, -0.0186, -0.0323, -0.0239, -0.0323, -0.0186, 0.0130,
                0, 0.013, 0.0056, -0.0018, 0.0056, 0.013, 0]).reshape(7, 7)

def zernike_detection(image):
    #
     # @func zernike_detection
     # @desc 根据得到的二维实心圆图像，计算Zernike模板优化后的轮廓坐标
     # @param {}  image:Mat 二维实心圆图像
     # @return {} points:List 优化后的轮廓坐标
    #
    # image = cv2.Canny(image, 0, 255)
    # cv2.imshow('image', image)
    blur_img = cv2.medianBlur(image, 3)
    # image = cv2.adaptiveThreshold(blur_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 4)
    ret, image = cv2.threshold(blur_img, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('image', image)
    ZerImgM00 = cv2.filter2D(image, cv2.CV_64F, M00)
    ZerImgM11R = cv2.filter2D(image, cv2.CV_64F, M11R)
    ZerImgM11I = cv2.filter2D(image, cv2.CV_64F, M11I)
    ZerImgM20 = cv2.filter2D(image, cv2.CV_64F, M20)
    ZerImgM31R = cv2.filter2D(image, cv2.CV_64F, M31R)
    ZerImgM31I = cv2.filter2D(image, cv2.CV_64F, M31I)
    ZerImgM40 = cv2.filter2D(image, cv2.CV_64F, M40)

    point_temporary_x = []
    point_temporary_y = []
    scatter_arr = cv2.findNonZero(ZerImgM00).reshape(-1, 2)
    # 将scatter_arr中的点在image中用红色标出
    # image_clone = image.copy()
    # image_clone = cv2.cvtColor(image_clone, cv2.COLOR_GRAY2BGR)
    # for point in scatter_arr:
    #     image_clone[point[1], point[0]] = (0, 0, 255)
    # cv2.imshow('image_clone', image_clone)
    # print(scatter_arr)
    for idx in scatter_arr:
        j, i = idx
        theta_temporary = np.arctan2(ZerImgM31I[i][j], ZerImgM31R[i][j])    
        # print('x: ', ZerImgM31R[i][j], 'y: ', ZerImgM31I[i][j], 'theta: ', theta_temporary)
        rotated_z11 = np.sin(theta_temporary) * ZerImgM11I[i][j] + np.cos(theta_temporary) * ZerImgM11R[i][j]
        rotated_z31 = np.sin(theta_temporary) * ZerImgM31I[i][j] + np.cos(theta_temporary) * ZerImgM31R[i][j]
        l_method1 = np.sqrt((5 * ZerImgM40[i][j] + 3 * ZerImgM20[i][j]) / (8 * ZerImgM20[i][j]))    #l_method1 = sqrt((5 * M40 + 3 * M20) / (8 * M20)) 代表的是Zernike矩的归一化矩
        l_method2 = np.sqrt((5 * rotated_z31 + rotated_z11) / (6 * rotated_z11))   #l_method2 = sqrt((5 * rotated_z31 + rotated_z11) / (6 * rotated_z11)) 代表的是Zernike矩的归一化矩
        l = (l_method1 + l_method2) / 2
        k = 3 * rotated_z11 / (2 * (1 - l_method2 ** 2) ** 1.5)

        k_value = 200
        l_value = 2 ** 0.5 / g_N / 2

        absl = np.abs(l_method2 - l_method1)    #abs()函数返回数字的绝对值
        if k >= k_value and absl <= l_value:
            y = i + g_N * l * np.sin(theta_temporary) / 2
            x = j + g_N * l * np.cos(theta_temporary) / 2
            point_temporary_x.append(x)
            point_temporary_y.append(y)
        else:
            continue
    
    return point_temporary_x, point_temporary_y, image


if __name__ == '__main__':
    # 在560*560的图像中，创造一个实心圆，半径为100，中心在(280, 280)

    # 生成一个560*560的图像
    # img_circle = np.zeros((560, 560), dtype=np.uint8)

    # 生成一个实心圆
    # cv2.circle(img_circle, (280, 280), 100, 255, -1)
    
    # 生成一个圆环 
    # cv2.circle(img_circle, (280, 280), 100, 255, 1)

    # print(img_circle.shape)

    img_circle = cv2.imread('img_circle.png', cv2.IMREAD_GRAYSCALE)
    point_temporary_x, point_temporary_y, image = zernike_detection(img_circle)
    # plt.rcParams['figure.dpi'] = 72
    plt.imshow(image, cmap='gray')
    point = np.array([point_temporary_x, point_temporary_y])
    plt.scatter(point[0, :], point[1, :], s = 1, marker="*")
    plt.show()
