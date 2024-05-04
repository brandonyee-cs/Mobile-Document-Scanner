# Mobile-Document-Scanner
Built By Brandon Yee

This is a mobile document scanner application created using OpenCV and Python. The entire process is broken down into three fundamental steps.
This project references Pyimagesearch's ["How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes"](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/) tutorial.

# Steps Involved

- Edge Detection: The initial step involves applying edge detection techniques to the input image. This helps identify the boundaries of the document within the image.
- Contour Detection: Following edge detection, the program finds contours within the processed image. Contours represent the document's outline. Here, a heuristic is applied assuming the largest contour with four corners corresponds to the document.
- Perspective Transform & Thresholding: Finally, a perspective transform is applied using the four corners of the document's contour. This rectifies the image, producing a top-down, "bird's eye view" of the document. Lastly, thresholding is employed to achieve a clear, black-and-white scanned document effect.

# Implementation Details

- The code utilizes OpenCV and libraries like NumPy for numerical processing and argparse for handling command-line arguments.
- The four_point_transform function is used for perspective transformation.

# Key Points

- This approach offers a basic yet effective method for document scanning using computer vision techniques.
- The project leverages OpenCV's functionalities for image processing and contour detection.
