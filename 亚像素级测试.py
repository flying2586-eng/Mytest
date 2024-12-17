import cv2
import numpy as np
import mahotas

def zernike_moments(image, radius):
    # Compute Zernike moments for the given radius
    zernike = mahotas.features.zernike_moments(image, radius)
    return zernike

def subpixel_edge_detection(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a Gaussian blur to the image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges using Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    
    return image, contours

def main():
    # Load the image
    image = cv2.imread('contour_image.jpg')
    
    # Detect edges and contours
    result_image, contours = subpixel_edge_detection(image)
    
    # Compute Zernike moments for each contour
    for contour in contours:
        # Create a mask for the contour
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, 255, -1)
        
        # Compute the radius for Zernike moments (e.g., half of the bounding box width)
        x, y, w, h = cv2.boundingRect(contour)
        radius = w // 2
        
        # Compute Zernike moments
        zernike = zernike_moments(mask, radius)
        
        # Print the Zernike moments
        print(f'Zernike moments for contour: {zernike}')
    
    # Display the result image with contours
    cv2.imshow('Contours', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
