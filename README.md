# DEFECT DETECTION USING MACHINE VISION

This is our senior year engineering project done in Raspberry PI + a Camera module, line-laser and a  motor.

The project can calculate the dimensions of nut and bolt.
It uses laser triangulation technique for measurement of dimensions.

	> For bolt, it can calculate thread pitch, thread height, length and major diameter.
	> For nut, it can calculate thread pitch and diameter.

### Introduction

Quality checking is an integral step in the production of any product. This involves maintaining a desired level of quality in a service or product by paying attention to every stage of the process of delivery or production. In manufacturing, quality control ensures that customers receive products free from defects that meet their needs and demands. Improper quality control can put consumers at risk; for example, the recent defect found in Takata airbags resulted in the biggest automotive recall in history. Quality plays a vital role in a company’s reputation, especially with the growth of social media. Positive reviews can reinforce marketing efforts, but quality problems can damage a company's reputation.

Quality control helps reduce production and product support costs by lowering levels of waste and rework, improving productivity, and increasing production efficiency. Delivering quality products can also reduce the number of returns and the cost of repairing or servicing products in the field. However, implementing these techniques using existing technology can be obstructive, ineffective, and expensive.

Thus, our aim is to create a low-cost and efficient prototype system that can detect defects in an object using image processing techniques and estimate the size of such defects.

### Motivation

In most manufacturing industries, it is common to obtain a few defective products among the perfect ones. On a large scale, it is quite complex to accurately detect a defective product.

Defects in manufacturing occur when a product is improperly manufactured and departs from its intended design. One of the common defects in a product is dimensional inaccuracy. Conventionally, there are two ways to detect these inaccuracies, but the methods employed are usually expensive, slow, or both.

Hence, there is a need for detecting these defects cost-effectively and efficiently in the early stages of manufacturing.

### Problem Statement

An automated system is to be assembled which can detect and label the dimensional defects of a given object. Such a system must perform with a high degree of accuracy and be cost-effective. The designed system must also be easy to operate so that it is deployable in a production line with relative ease.

### Objective

This work presents a new, real-time, highly automated tool for defect detection based on Image Processing. The specific goals of this investigation are to develop an efficient and non-intrusive dimensional defect detection system. These goals are achieved by creating a machine-vision system capable of performing real-time acquisition, image processing, and classification. The automatic inspection system will allow the detection and classification of the most frequently occurring dimensional defects in manufactured products while storing and displaying possible solutions to the user.

### Block Diagram

![Basic Block Diagram](https://github.com/rahulmranga/Dimensional-Accuracy-Assertion/blob/master/reports/bd.JPG)

A basic block diagram of the proposed project is given above.

The first step is to acquire the image of the object. The image is captured using a camera with the help of a line LASER (3-D triangulation). Since the object can have defects along any axis, multiple images of the object will be taken from different angles. Some images are also taken from the top view.

The set of images thus obtained undergoes pre-processing, in which the background, noise, and other unnecessary parameters are removed from the images.

The pre-processed images undergo image processing using spatial or transform filters. In this stage, the images are compared with another set of images containing the required result. The difference is detected as a defect. Depending on the type of defect, the object is classified as pass/rework/fail. The size of the defect is also estimated from the given set of images.

Finally, the detected defects are marked on the images, showing where they are present for further processing.

### Project Outcome

The designed automated system will be able to take pictures of the object in all three dimensions using cameras and process the images using image processing techniques. The system will compare the processed image with an initially stored reference image and detect abnormalities or flaws, if any. Finally, it will display the area or part where the defect is present and suggest an alternative method for resolving the flaw or problem.

### Applications

- The proposed system can be used to check defects in manufacturing industries, playing a vital role in the quality control of the goods manufactured.
- If such a system is employed in the early stages of production, it can be used to detect faulty goods beforehand and rectify errors, thus reducing wastage.
- It can be used in 3D printing and CNC machining to check for defects in printed materials.
- It can be used to check the dimensions of an unknown object.

## Literature Survey

Machine vision (MV) is the technology and methods used to provide imaging-based automatic inspection and analysis for such applications as automatic inspection, process control, and robot guidance, usually in industry. The main task of machine vision systems is providing computer-understandable descriptions of objects from either a single image or a whole array of images. One such area of application is in automated visual product inspection. An automated visual inspection system must discover and classify possible defects from product images and should be fairly quick and robust. Such an automated system can be assembled with digital image processing at its core to detect defects in large-scale manufacturing industries.

Machine vision systems usually find applications in the PCB manufacturing industry since PCBs can be approximated as a 2-D plane. Thus, only one image is sufficient to describe a PCB. A study by Suhasini A., Sonal D. Kalro, Prathiksha B. G., Meghashree B. S., and Phaneendra H. D.[^2], utilized a non-contact reference-based image processing approach for defect detection and classification and simple image processing algorithm (concerned with arithmetic and logical operation between images where pixel by pixel transformation was applied) for locating the defects on PCB boards. A template of defected test PCB images involved many stages, including grayscale image conversion, thresholding, and segmentation based on different intensities, and was compared with defect-free PCB images using image subtraction and other procedures. Discrepancies between the images were considered defects and classified based on similarities and area of occurrence.

Heriansyah[^3] proposed a better technique using a referential pixel-based approach where the PCB could be formed into three groups: the defects on the foreground, on the background, and on both. The LVQ neural network had been selected to classify the defects. The designed patterns were trained and tested using the neural network. For the neural network implementation, 2 groups of defects were used for training (i.e., foreground and background). For performance comparison, a pixel-based approach was developed to classify seven defects (short, missing hole, pinhole, open, nosebite, spur, and etching problem). The stages involved were segmentation, windowing (reference image and detected defects), defects detection, pattern assignment, normalization, and classification. All these processes were offline and hence did not affect the overall processing time.

Lins and Givigi[^4] developed a system based on machine vision concepts with the goal of automating the crack measurement process. In their method, they used only a single camera for the processing of the sequence of the images for the crack dimension estimation. The crack model algorithm HSB and RSV were used, by which the sequences of the images were subjected to crack detection algorithms in order to detect the crack. The proposed algorithm receives images and outputs a new image with red particles along the detected crack. The pixel positions of the particles were stored in a vector and passed along to the crack measurement algorithm. With the pixel positions, the algorithm estimates the number of pixels in a cross-section and outputs the crack dimension. Li et al.[^5] incorporated a new approach for detecting cracks in defects with dark color and low contrast using fast discrete curvelet waveform and texture analysis. They initially decomposed and reconstructed the original image using the FDCT algorithm. Then, the thresholds of the decomposition coefficients were calculated by the texture feature measurements, from which the surface textures in the images were eliminated. Finally, by extracting the contours from the reconstructed images, the expected image without texture but with crack defect contours was obtained.

But these systems work well for a 2-D view since we are taking an image or a set of images. These methods fail to work for 3-D objects. M Jonathan Wu et al.[^6] designed a 3-D sensing system applying artificial intelligence methodology for quantity assurance in automatic manufacturing processes. Using a single 2-D CCD camera, laser-structured light, and fuzzy techniques for rule-based decision-making, it was possible to successfully interpret a 3-D view. The surface environment information was converted into the orientation, curvature, and depth of the shape to incorporate into symbolic 3-D object-oriented information base and reasoning algorithm.

## Mathematical Analysis

In order for an object to be scanned so that defects can be detected, a simple 3-D triangulation setup is created using a line LASER and a camera.

![A simple triangulation setup consisting of a Line LASER diode projecting a line on the 3D object](https://github.com/rahulmranga/Dimensional-Accuracy-Assertion/blob/master/reports/lasercamera.JPG)

The image above shows a very simple triangulation setup using a camera and a line LASER. The LASER diode is positioned such that it creates a triangle with the view direction of the camera. As you can see from the image, the LASER line projects on the object and intersects the view direction of the camera exactly at the axis of rotation of the object. The angle at the intersection of the LASER line and the view direction (THETA) provides us with the first tool for extracting depth-related information from the image captured by the camera.

The length of X and Y can be obtained from the image itself.
$$X=N_v * X_s$$
$$Y=Scanline * Y_s$$
where,

- \(N_v\) is the number of pixels from the view direction
- \(X_s\) is the X scaling factor
- \(Y_s\) is the Y scaling factor

![Top view of the triangulation setup](https://github.com/rahulmranga/Dimensional-Accuracy-Assertion/blob/master/reports/triangle.JPG)
![View from the camera](https://github.com/rahulmranga/Dimensional-Accuracy-Assertion/blob/master/reports/yline.JPG)

Since we know the angle (THETA), we can calculate the depth of the image or the Z component as,
$$Z=\frac{X}{\tan(\text{THETA})}$$
$$D=\frac{X}{\sin(\text{THETA})}$$

Let the set of images of the object on which the LASER is incident be defined as,
$$f_i(x,y),{\quad}0{\leq}i<N{\quad}(N \text{ is the number of images taken})$$

Let the set of images of the object which does not have the LASER incident on it be defined as,
$$g_i(x,y),{\quad}0{\leq}i<N$$

Initially, the backgrounds of all the images are removed by subtracting the background image from the set of images present. If \(b(x,y)\) is an image only containing the background, then,
$$f'_i(x,y)=f_i(x,y)-b(x,y),{\quad}\forall i\in[0,N)$$
The images now contain only the object devoid of the background. After removing the background, it checks for any defects by comparing \(f'\_i(x,y)\) with respect to a previously stored image of a perfectly fine, LASER incident object. The comparison is done using subtraction or bit-wise XOR operation,
$$f_i"(x,y)=f'_i(x,y)-p_i(x,y),{\quad}\forall i\in[0,N)$$
or,
$$f_i"(x,y)=f'_i(x,y){\wedge}p_i(x,y),{\quad}\forall i\in[0,N)$$
where, \(p_i(x,y)\) is a set of images of an object without any defects, stored within the processor.

The resultant image \(f"\_i(x,y)\) contains a contour that represents the deviation from the required value. This represents the defect present in the object. The size of the defect is later estimated by comparing all such images which do not match with \(p_i(x,y)\). If \(f"\_i(x,y)\) does not have any contours, then it can be classified as an object with no defects.

Finally, the contour is superimposed on the corresponding \(g_i(x,y)\) to mark where the defect is present. Hence the set of output images is,
$$h_i(x,y)=f_i"(x,y)\vert g_i(x,y)$$

## Software Requirements

### OpenCV

OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. It was originally developed by Intel and is released under a BSD license. Hence, it is free for both academic and commercial purposes. It has C++, C, Python, and Java interfaces and supports Windows, Linux, macOS, iOS, and Android. OpenCV was designed for computational efficiency and with a strong focus on real-time applications. Written in optimized C/C++, the library can take advantage of multi-core processing. Enabled with OpenCL, it can take advantage of the hardware acceleration of the underlying heterogeneous compute platform.

### Arduino IDE

The Arduino project provides the Arduino integrated development environment (IDE), which is a cross-platform application written in the programming language Java. It originated from the IDE for the languages Processing and Wiring. It includes a code editor with features such as text cutting and pasting, searching and replacing text, automatic indenting, brace matching, and syntax highlighting, and provides simple one-click mechanisms to compile and upload programs to an Arduino board. It also contains a message area, a text console, a toolbar with buttons for common functions, and a hierarchy of operation menus.

The Arduino IDE supports the languages C and C++ using special rules of code structuring. The Arduino IDE supplies a software library from the Wiring project, which provides many common input and output procedures. User-written code only requires two basic functions: one for starting the sketch and the main program loop. These are compiled and linked with a program stub main() into an executable cyclic executive program with the GNU tool-chain, also included with the IDE distribution. The Arduino IDE employs the program avrdude to convert the executable code into a text file in hexadecimal encoding that is loaded into the Arduino board by a loader program in the board's firmware.

### Python

Python is a widely used high-level programming language for general-purpose programming. Python has a design philosophy that emphasizes code readability and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale. Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. Python can be run on a variety of OSes like Windows, macOS, Linux, and even Raspbian.

## Hardware Requirements

### Arduino Uno

The Arduino Uno is a micro-controller board based on the ATmega328 (datasheet). It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, a 16 MHz crystal oscillator, a USB connection, a power jack, an ICSP header, and a reset button. It contains everything needed to support the micro-controller; simply connect it to a computer with a USB cable or power it with an AC-to-DC adapter or battery to get started. The Uno differs from all preceding boards in that it does not use the FTDI USB-to-serial driver chip. Instead, it features the Atmega16U2 (Atmega8U2 up to version R2) programmed as a USB-to-serial converter.

### Raspberry Pi

Raspberry Pi is an ARM-based credit card-sized SBC (Single Board Computer) created by the Raspberry Pi Foundation. Raspberry Pi runs a Debian-based GNU/Linux operating system Raspbian, and ports of many other OSes exist for this SBC. The Raspberry Pi 3 Model B is the third generation Raspberry Pi. This powerful credit-card-sized single board computer can be used for many applications and supersedes the original Raspberry Pi Model B+ and Raspberry Pi 2 Model B. Additionally, it adds wireless LAN and Bluetooth connectivity, making it the ideal solution for powerful connected designs.

### Camera Module

The Raspberry Pi camera module can be used to take high-definition video, as well as still photographs. The camera consists of a small (25mm by 20mm by 9mm) circuit board, which connects to the Raspberry Pi's Camera Serial Interface (CSI) bus connector via a flexible ribbon cable. The camera's image sensor has a native resolution of five megapixels and has a fixed-focus lens. The software for the camera supports full-resolution still images up to 2592x1944 and video resolutions of 1080p30, 720p60, and 640x480p60/90.

## References

[^1]: Consumer Reports. (July 14, 2017). _Takata Airbag Recall - Everything You Need to Know_, retrieved on September 20, 2017. [URL](https://www.consumerreports.org/cro/news/2016/05/everything-you-need-to-know-about-the-takata-air-bag-recall/index.htm)
[^2]: Suhasini A., Sonal D. Kalro, Prathiksha B. G., Meghashree B. S., Phaneendra H. D., _PCB Defect Detection Using Image Subtraction Algorithm_, International Journal of Computer Science Trends and Technology (IJCST) – Volume 3 Issue 3, May-June 2015.
[^3]: R. Heriansyah and S. A. R. Abu-Bakar(2004), _Defects classification on bare PCB using multiple learning vector quantization neural network paradigm_, International Conference on Computer Graphics, Imaging, and Visualization 2004 (CGIV 2004), pp.50-53.
[^4]: Romulo Gonçalves Lins, Sidney N. Givigi, _Automatic crack detection and measurement based on image analysis_, IEEE Trans. Instrum. Meas., 65 (3) (2016), pp. 583-590.
[^5]: Xueqin Li, Honghai Jiang, Guofu Yin, _Detection of surface crack defects on ferrite magnetic tile_, NDT E Int., 62 (2014), pp. 6-13.
[^6]: Q.M. Jonathan Wu, M.F. Ricky Lee, Clarence W. de Silva, _Intelligent 3-D Sensing in Automated Manufacturing Processes_, IEEE, pp. 334-339, 2001.
[^7]: Makerzone. (July 12, 2016). _Raspberry Pi + MATLAB based 3D Scanner_, retrieved on September 15, 2017. [URL](https://makerzone.mathworks.com/resources/raspberry-pi-matlab-based-3d-scanner/)
