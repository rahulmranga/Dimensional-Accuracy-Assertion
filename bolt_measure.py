import cv2
import numpy as np


def find_peak(pos):
    rows = pos.shape[0]
    print(rows)
    check_width = 20
    p_row = np.array([], np.int16)
    p_column = np.array([], np.int16)
    i = check_width
    while i < rows - check_width:
        if pos[i] <= pos[i-1] and pos[i] <= pos[i+1]:
            peak_flag = True
            for p in range(1, check_width):
                if pos[i] > pos[i-p] or pos[i] > pos[i+p]:
                    peak_flag = False
                    break

            if peak_flag:
                p_row = np.append(p_row, pos[i])
                p_column = np.append(p_column, i+50)
                i += check_width - 5
        i += 1
    print(p_row.shape)
    return p_row, p_column


def find_valley(pos):
    rows = pos.shape[0]
    print(rows)
    check_width = 20
    v_row = np.array([], np.int16)
    v_column = np.array([], np.int16)
    i = check_width
    while i < rows - check_width:
        if pos[i] >= pos[i-1] and pos[i] >= pos[i+1]:
            valley_flag = True
            for p in range(1, check_width):
                if pos[i] < pos[i-p] or pos[i] < pos[i+p]:
                    valley_flag = False
                    break

            if valley_flag:
                v_row = np.append(v_row, pos[i])
                v_column = np.append(v_column, i+50)
                i += check_width - 5
        i += 1
    print(v_row.shape)
    return v_row, v_column


def show_peak_valley(img, v_row, v_column, p_row, p_column):
    #cv2.circle(img, (250, 250), 50, (100, 50, 200), -1)
    for i in range(v_row.shape[0]):
        cv2.circle(img, (v_column[i], int(v_row[i])), 1, (0, 255, 0), -1)

    for i in range(p_row.shape[0]):
        cv2.circle(img, (p_column[i], int(p_row[i])), 1, (255, 0, 0), -1)

    cv2.imshow("valleysssss", img)



img = cv2.imread('/home/theabysswalker/Documents/python_files/znap24.jpg')

img = img[400:600, 500:1700]

redChannel = img[:, :, 2]

#redChannel = cv2.bilateralFilter(redChannel, 10, 100, 100)

retval,binaryImage = cv2.threshold(redChannel, 80, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
kernel = np.array([[0,0,1],[0,1,1],[1,1,1]],np.uint8)
kernel = np.ones((15, 15), np.uint8)
binaryImage2 = cv2.morphologyEx(binaryImage, cv2.MORPH_CLOSE, kernel)
'''

thread_row = np.array([])

top=0
bottom=0
#print(binaryImage.shape[0])
#print(binaryImage.shape[1])

for column in range(1, binaryImage.shape[1]):
    top_flag = False
    for row in range(1, binaryImage.shape[0]):
        if binaryImage[row, column] != 0:
            top = column
            break

    if top != 0:
        break

for column in range(binaryImage.shape[1] - 1, top, -1):
    
    for row in range(1, binaryImage.shape[0]):
        if binaryImage[row, column] != 0:
            bottom = column;
            break

    if bottom != 0:
        break
print(top)
print(bottom)
'''
for column in range(top, bottom):

    for row in range(binaryImage.shape[0]):
        if binaryImage[row, column] != 0:
            thread_row = np.append(thread_row, row)
            break

valley_row, valley_column = find_valley(thread_row)

peak_row, peak_column = find_peak(thread_row)

print("Peaks:")
print(peak_row)
print("their pos:")
print(peak_column)

print("Valleys")
print(valley_row)
print("their pos:")
print(valley_column)

show_peak_valley(img, valley_row, valley_column, peak_row, peak_column)

#cv2.imshow('org', redChannel)
cv2.imshow('otsu', binaryImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
