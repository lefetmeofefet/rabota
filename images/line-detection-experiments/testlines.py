import cv2 as cv
import numpy as np
import math
from PIL import Image, ImageFilter

#
# image = Image.open("test.png")
#
# # for _ in range(10):
# #     image = image.filter(ImageFilter.BLUR)
#
# image.save('blurred.png')
#
# src_img = cv.imread('blurred.png')
#
# lower_threshold = 50
# higher_threshold = 200
# aperture_size = 3
# # src_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
#
# dst_img = cv.Canny(src_img, lower_threshold, higher_threshold, apertureSize=aperture_size)
#
# # cv.imshow("Image with lines", src_img)
# # cv.waitKey(0)
#
# threshold = 50
# min_line_length = 100
# max_line_gap = 50
# linesP = cv.HoughLinesP(
#     dst_img,
#     1,
#     np.pi / 180,
#     threshold,
#     min_line_length,
#     max_line_gap
# )
#
# lines_list = []
# for points in linesP:
#     # Extracted points nested in the list
#     x1, y1, x2, y2 = points[0]
#     # Draw the lines joing the points
#     # On the original image
#     cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#     # Maintain a simples lookup list for points
#     lines_list.append([(x1, y1), (x2, y2)])
#
# cv.imshow("Image with lines", src_img)
# cv.waitKey(0)


import cv2
import numpy as np

# Read image
image = Image.open("../shlombif/test.png")

for _ in range(3):
# for _ in range(15):
    image = image.filter(ImageFilter.BLUR)

thresh = 0
fn = lambda x : 255 if x > thresh else 0
image = image.convert('L').point(fn, mode='1')

image.save('blurred.png')





# Do the gap filling
# image = image.filter(ImageFilter.RankFilter(3, 3))
# # image = image.rankfilter(3, 3)

# exit()

# class FillFilter(ImageFilter.Filter):
#     """
#     Create a rank filter.  The rank filter sorts all pixels in
#     a window of the given size, and returns the ``rank``'th value.
#
#     :param size: The kernel size, in pixels.
#     :param rank: What pixel value to pick.  Use 0 for a min filter,
#                  ``size * size / 2`` for a median filter, ``size * size - 1``
#                  for a max filter, etc.
#     """
#
#     name = "Rank"
#
#     def __init__(self):
#         self.size = 3
#         self.rank = 3
#
#     def filter(self, image):
#         if image.mode == "P":
#             raise ValueError("cannot filter palette images")
#         image = image.expand(self.size // 2, self.size // 2)
#         return image.rankfilter(self.size, self.rank)
# def blur(image):
#     new_image = image.copy()
#     for x in range(1, image.width - 1):
#         for y in range(1, image.height - 1):
#
#             neighbors = 0
#             for window_x in range(-1, 2):
#                 for window_y in range(-1, 2):
#                     pix = image.getpixel((x + window_x, y + window_y))
#                     if pix > 0:
#                         neighbors += 1
#
#             if neighbors >= 4:
#                 new_image.putpixel((x, y), 255)
#     return new_image
#
#
# for _ in range(1):
#     image = blur(image)
# image.save('filled.png')

# asdd
image = cv.imread('blurred.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def fillfilter(image):
    # fill shit
    pix_inner = 0.1
    pix_outer = 0.001
    kernel = np.array([
      [pix_outer, pix_outer, pix_outer, pix_outer, pix_outer],
      [pix_outer, pix_inner, pix_inner, pix_inner, pix_outer],
      [pix_outer, pix_inner, 1,         pix_inner, pix_outer],
      [pix_outer, pix_inner, pix_inner, pix_inner, pix_outer],
      [pix_outer, pix_outer, pix_outer, pix_outer, pix_outer],
    ])
    image = cv2.filter2D(image, -1, kernel, )
    thresh = 255 * (4 * pix_inner + 7 * pix_outer)
    image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
    return image

nonzeros = np.count_nonzero(image)
for count in range(100):
    image = fillfilter(image)
    new_nonzeros = np.count_nonzero(image)
    if nonzeros == new_nonzeros:
        break
    nonzeros = new_nonzeros
print("Iterations: " + str(count))
cv.imwrite('fuck.png', image)
# exit()
height = image.shape[0]
width = image.shape[1]
skel = np.zeros([height, width, 1], dtype=np.uint8)  # [height,width,3]
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
temp_nonzero = np.count_nonzero(image)
while (np.count_nonzero(image) != 0):
    eroded = cv2.erode(image, kernel)
    # cv2.imshow("eroded", eroded)
    temp = cv2.dilate(eroded, kernel)
    # cv2.imshow("dilate", temp)
    temp = cv2.subtract(image, temp)
    skel = cv2.bitwise_or(skel, temp)
    image = eroded.copy()

# cv2.imshow("skel", skel)
# cv2.imshow("img", image)
cv.waitKey(0)

image = skel
cv2.imwrite('skeleton.png', image)


# Convert image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(image, 0, 20, apertureSize=3)
cv2.imwrite('canny.png', edges)

# Apply HoughLinesP method to
# to directly obtain line end points
lines_list = []
lines = cv2.HoughLinesP(
    edges,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 180,  # Angle resolution in radians
    threshold=10,  # The minimum number of intersections to detect a line
    minLineLength=100,  # The minimum number of points that can form a line. Lines with less than this number of points are disregarded
    maxLineGap=15  # The maximum gap between two points to be considered in the same line
)

# Iterate over points
for points in lines:
    # Extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    # Draw the lines joing the points
    # On the original image
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1, y1), (x2, y2)])

# Save the result image
print(len(lines))
cv2.imwrite('detectedLines.png', image)