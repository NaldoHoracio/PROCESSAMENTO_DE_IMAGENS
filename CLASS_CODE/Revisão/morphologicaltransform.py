from dip import *

img = cv.imread('img/j.png', cv.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(img, kernel, iterations = 1)
dilation = cv.dilate(img, kernel, iterations = 1)
plt.subplot('131')
plt.imshow(img, 'gray')
plt.title('Original')
plt.subplot('132')
plt.imshow(erosion, 'gray')
plt.title('Erosion')
plt.subplot('133')
plt.imshow(dilation, 'gray')
plt.title('Dilation')
plt.show()
