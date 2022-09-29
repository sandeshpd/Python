# function to check if there is an intersection between two lines is added
# the function uses line intersection formula to find intersection

import cv2 as cv
import os
import numpy as np

os.system('cls')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def pointOfIntersetion(self, p):
        print(f"({p.x}, {p.y})")

# following is the funtion to check the intersection of lines
def LineIntersect(start_1, end_1, start_2, end_2):
    a1 = (end_1.y) - (start_1.y)
    b1 = (start_1.x) - (end_1.x)
    c1 = a1 * (start_1.x) + b1 * (start_1.y)

    a2 = (end_2.y) - (start_2.y)
    b2 = (start_2.x) - (end_2.x)
    c2 = a2 * (start_2.x) + b2 * (start_2.y)

    determinant = a1*b2 - a2*b1

    # if the lines are parallel
    if(determinant == 0):
        return Point(10**9, 10**9)
    else:
        x = (b2*c1 - b1*c2) / determinant
        y = (a1*c2 - a2*c1) / determinant
        return Point(x, y)


# window dimensions are hard-coded
image_height = 700
image_width = 900
number_of_colors = 3
image_background_color = (36,143,36)
Image_Window_display = np.full((image_height, image_width, number_of_colors), image_background_color, dtype=np.uint8)

# cv.imshow('The Window', Image_Window_display)
# cv.waitKey()

# draw the first line
Start_x1 = int(input('Enter X co-ordinate to start line 1: '))
Start_y1 = int(input('Enter Y co-ordinate to start line 1: '))

End_x1 = int(input('Enter X co-ordinate to end line 1 :'))
End_y1 = int(input('Enter Y co-ordinate to end line 1: '))

startPoint_1 = (Start_x1, Start_y1) # A
endPoint_1 = (End_x1, End_y1)       # B

noCVLineStart_1 = Point(Start_x1, Start_y1)
noCVLineEnd_1 = Point(End_x1, End_y1)

FirstLineDrawInWindow = cv.line(Image_Window_display, startPoint_1, endPoint_1, color=(64,64,64), thickness = 2)

# draw the second line
Start_x2 = int(input('Enter X co-ordinate to start line 2: '))
Start_y2 = int(input('Enter Y co-ordinate to start line 2: '))

End_x2 = int(input('Enter X co-ordinate to end line 2 :'))
End_y2 = int(input('Enter Y co-ordinate to end line 2: '))

startPoint_2 = (Start_x2, Start_y2) # C
endPoint_2 = (End_x2, End_y2)       # D

noCVLineStart_2 = Point(Start_x2, Start_y2)
noCVLineEnd_2 = Point(End_x2, End_y2)

cv.line(Image_Window_display, startPoint_2, endPoint_2, color=(64,64,64), thickness = 2)

cv.imshow('The line on image ', Image_Window_display)
cv.waitKey(0)

intersection = LineIntersect(noCVLineStart_1, noCVLineEnd_1, noCVLineStart_2, noCVLineEnd_2)

if(intersection.x <= 0.0 or intersection.y <= 0.0):
    print()
    print('NO intersection is happening.')
else:
    print()
    print('Yes! There is intersection. Intersecting Point is ')
    intersection.pointOfIntersetion(intersection)