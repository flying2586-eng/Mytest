import cv2
import numpy as np

def find_circles(image, dp=1.7, minDist=100, param1=50, param2=50, minRadius=0, maxRadius=0):
    """ find the center of circular objects in image using hough circle transform

    Keyword arguments:
    image -- uint8: numpy ndarray of a single channel image (grayscale)
    dp -- float: inverse ratio of the accumulator resolution to the image resolution (default 1.7)
    minDist -- float: minimum distance between the centers of the detected circles (default 100)
    param1 -- float: first method-specific parameter (default 50)
    param2 -- float: second method-specific parameter (default 50)
    minRadius -- float: minimum circle radius (default 0)
    maxRadius -- float: maximum circle radius (default 0)

    Return:
    center -- tuple: (x, y)
    radius -- int : radius of the circle
    ERROR if circle is not detected, return (-1) in this case
    """

    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles = circles.reshape(circles.shape[1], circles.shape[2])
        circles = np.squeeze(circles)
        return(circles)
    else:
        raise Exception('Circle not detected')
    
def find_od(iamge_path: str, is_show: bool = True):
    image_origin = cv2.imread(iamge_path, cv2.IMREAD_GRAYSCALE)
    image = image_origin[1500:2500, 2000:3500]
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    thresh_img = cv2.bilateralFilter(thresh, 9, 75, 75)
    edges = cv2.Canny(thresh_img, 50, 150)
    circles = find_circles(edges, dp=1.15, minDist=100, param1=100, param2=33, minRadius=300, maxRadius=400)
    # array([628.475, 458.275, 323.805], dtype=float32)
    if is_show:
        image_copy = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles:
                cv2.circle(image_copy, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(image_copy, (i[0], i[1]), 2, (0, 0, 255), 3)
        else:
            raise Exception('Circle not detected')

        cv2.imshow('image', image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return circles

def create_output_json(image_path:str):
    circle_result = find_od(image_path, is_show=False)
    json_data = {
        "identify_state": 200,
        "image_path": [image_path],
        "HolesNum": 1,
        "recognition_result":[
            {
                "diameter": circle_result[2],
                "center_x": circle_result[0],
                "center_y": circle_result[1]
            }
        ]
    }
    return json_data

if __name__ == '__main__':
    find_od("D:\BaiduNetdiskDownload\Image_20241104141307516.bmp")