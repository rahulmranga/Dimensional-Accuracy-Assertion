import cv2

import numpy as np

def find_peak(th_row, th_col):
    cdef int rows = th_row.shape[0]
    cdef int check_width = 30
    p_row = np.array([], np.int16)
    p_column = np.array([], np.int16)
    i = check_width
    end_flag = False
    first_time = True

    while i < rows - check_width:
        
        if th_row[i] <= th_row[i-1] and th_row[i] <= th_row[i+1]:
            peak_flag = True
            for p from 1<=p <check_width by 1:
                if th_row[i] > th_row[i-p] or th_row[i] > th_row[i+p]:
                    peak_flag = False
                    break

            if peak_flag:
                if first_time:
                    first_time = False
                elif p_row[-1] - th_row[i] > 50:
                    end_flag = True
                    break
                p_row = np.append(p_row, th_row[i])
                p_column = np.append(p_column, th_col[i])
                i += check_width - 5
        
        if end_flag:
            break
        i += 1
    return p_row, p_column


def find_valley(th_row, th_col):
    cdef int rows = th_row.shape[0]
    cdef int check_width = 30
    v_row = np.array([], np.int16)
    v_column = np.array([], np.int16)
    i = check_width
    end_flag = False
    first_time = True

    while i < rows - check_width:
        
        if th_row[i] >= th_row[i-1] and th_row[i] >= th_row[i+1]:
            valley_flag = True
            for v from 1 <=v <check_width by 1:
                if th_row[i] < th_row[i-v] or th_row[i] < th_row[i+v]:
                    valley_flag = False
                    break

            if valley_flag:
                if first_time:
                    first_time = False
                elif (v_row[-1] - th_row[i]) > 50:
                        end_flag = True
                        break
                v_row = np.append(v_row, th_row[i])
                v_column = np.append(v_column, th_col[i])
                i += check_width - 5
        
        if end_flag:
            break
        i += 1
    return v_row, v_column


def image_read(img):



    image = cv2.imread(img)

    redChannel = image[:, :, 2]

    retval,binaryImg = cv2.threshold(redChannel, 80, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return redChannel,binaryImg

def thread_row_column(binaryImg):
    

    rownonzero_pos,colnonzero_pos=binaryImg.nonzero()
    cdef int width = max(colnonzero_pos)
    cdef int height = max(rownonzero_pos)
    

    thread_row = np.array([])
    thread_col = np.array([])
    
    cdef int mini_col=min(colnonzero_pos)-50
    cdef int mini_row=min(rownonzero_pos)-50
    print("min "+str(mini_col) + " " +str(mini_row))
    print("min "+str(width) + " " +str(height))

    if(mini_row<0):mini_row=0
    if(mini_col<0):mini_col=0
    
    for column from mini_col <= column < width:
        c = binaryImg[:,column]
        
        white = np.where(c!=0)[0]
        if (white.size != 0):
            thread_row = np.append(thread_row, int(white[0]))
            thread_col = np.append(thread_col, column)

    return thread_row,thread_col

def find_peak_valley(thread_row,thread_col,img,binaryImage):
    valley_row, valley_column = find_valley(thread_row, thread_col)

    peak_row, peak_column = find_peak(thread_row, thread_col)

    top = thread_col[0]
    bottom = thread_col[-1]

    print("No of pixels from top to bottom is {}".format((bottom - top)*5.9/1104))

    print("Peaks:")
    print(peak_row)
    print("their pos:")
    print(peak_column)
    print("peak diff")
    print(np.diff(peak_column, 1))

    print("Valleys")
    print(valley_row)
    print("their pos:")
    print(valley_column)
    print("valley diff")
    print(np.diff(valley_column,1)*5.9/1104)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


cdef shobha(img):
    image,binary_image=image_read(img)
    thread_rows,thread_columns=thread_row_column(binary_image)
    find_peak_valley(thread_rows,thread_columns,image,binary_image)


shobha('znap24.jpg')
