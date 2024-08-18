import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import numpy as np

######## Fill constants here ########
cmPerPixel = 5.9/1104.0
checkWidth = 30
removeLastElements = 3
removeFirstElements = 2
threadEnd = 50
#####################################


GPIO.setmode(GPIO.BCM)
 
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24
laser_pin = 3
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(laser_pin, GPIO.OUT)

camera = picamera.PiCamera()
time.sleep(1)

GPIO.output(enable_pin, 1)


class Image:
    processed_image_index = 0

    def __init__(self):
        self.image = np.array([])
        self.is_pic_taken = True
        self.is_pic_processed = False

    def take_image(self, camera, rawCapture):
        camera.capture(rawCapture, format='bgr')
        self.image = rawCapture.array
        self.is_pic_taken = True
        self.processed_image_index+=1

    def process_image(self):
       if self.is_pic_taken:
           print("Hello")
           if not self.is_pic_processed:
                '''if not process(self.image):
                    print("Error in measuring bolt dimensions")
                else:
                    print("hello")
                    self.is_pic_processed = True'''
                try:
                    process(self.image)
                except:
                    try:
                        process(self.image)
                    except:
                        print("Error in image")
                    



def find_peak(th_row, th_col):
    start=time.time()
    rows = th_row.shape[0]
    check_width = 30
    p_row = np.array([], np.int16)
    p_column = np.array([], np.int16)
    i = check_width
    end_flag = False
    first_time = True
    
    while i < rows - check_width:
        
        if th_row[i] <= th_row[i-1] and th_row[i] <= th_row[i+1]:
            peak_flag = True
            
            for p in range(1, check_width):
                if th_row[i] > th_row[i-p] or th_row[i] > th_row[i+p]:
                    peak_flag = False
                    break

            if peak_flag:
                if first_time:
                    first_time = False
                elif p_row[-1] - th_row[i] > threadEnd:
                    print("thread length is " + str(th_col[i] - th_col[0]))
                    end_flag = True
                    break
                p_row = np.append(p_row, th_row[i])
                p_column = np.append(p_column, th_col[i])
                i += check_width - 5
        
        if end_flag:
            break
        i += 1
    stop=time.time()-start
    print(stop)
    print("sizep"+str(p_row.size))
    return p_row, p_column


def find_valley(th_row, th_col):
    start=time.time()
    rows = th_row.shape[0]
    check_width = 30
    v_row = np.array([], np.int16)
    v_column = np.array([], np.int16)
    i = check_width
    end_flag = False
    first_time = True

    while i < rows - check_width:
        
        if th_row[i] >= th_row[i-1] and th_row[i] >= th_row[i+1]:
            valley_flag = True
            
            for p in range(1, check_width):
                if th_row[i] < th_row[i-p] or th_row[i] < th_row[i+p]:
                    valley_flag = False
                    break

            if valley_flag:
                if first_time:
                    first_time = False
                elif (v_row[-1] - th_row[i]) > threadEnd:
                        end_flag = True
                        break
                v_row = np.append(v_row, th_row[i])
                v_column = np.append(v_column, th_col[i])
                i += check_width - 5
        
        if end_flag:
            break
        i += 1
    stop=time.time()-start
    print(stop)
    return v_row, v_column



def process(bolt_image):
    print("hello")
    retval, binaryImage = cv2.threshold(bolt_image[:,:,2], 80, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thread_row = np.array([])
    thread_col = np.array([])

    nonz_r, nonz_c = binaryImage.nonzero()
    last_col = max(nonz_c)
    first_col = min(nonz_c)
    if(first_col < 0):
        first_col = 0

    for column in range(first_col, last_col):
        col_array = binaryImage[:, column]
        white = np.where(col_array != 0)[0]
        if white.size != 0:
            thread_row = np.append(thread_row, int(white[0]))
            thread_col = np.append(thread_col, column)

    valley_row, valley_col = find_valley(thread_row, thread_col)
    peak_row, peak_col = find_peak(thread_row, thread_col)

    if valley_row.size > peak_row.size:
        arr_length = peak_row.size
    else:
        arr_length = valley_row.size

    valley_row = valley_row[removeFirstElements : arr_length - removeLastElements]
    valley_col = valley_col[removeFirstElements : arr_length - removeLastElements]
    peak_row = peak_row[removeFirstElements : arr_length - removeLastElements]
    peak_col = peak_col[removeFirstElements : arr_length - removeLastElements]

    length_of_bolt = np.abs(thread_col[0] - thread_col[-1])

    thread_pitch = np.mean(np.diff(peak_col, 1))
    thread_height = np.mean(peak_row - valley_row)
    show_peak_valley(bolt_image, valley_row, valley_col, peak_row, peak_col)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



  
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def rotate(i):
    delay_rotate = 5/1000.0
    fourStepForward(delay_rotate)
    print(i)
    setStep(0, 0, 0, 0)
    time.sleep(0.2)
    #GPIO.output(laser_pin, True)
    #time.sleep(0.2)
    #camera.capture('znap' + str(i) + '.jpg')
    #GPIO.output(laser_pin, False)
    #time.sleep(1)
    #time.sleep(0.2)

def fourStepForward(delay):
    for i in range(0, 40):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)




img=Image()
for i in range(0,25):
    GPIO.output(laser_pin,True)
    time.sleep(0.1)
    img.take_image()
    GPIO.output(laser_pin,False)
    rotate(i)
    img.process_image()

print("Finished Inspection of Bolt")
#image_obj.image = cv2.imread('/home/theabysswalker/Documents/Dimensional-Accuracy-Assertion/znap5.jpg')
#cv2.imshow("asd",image_obj.image)
#image_obj.process_image()