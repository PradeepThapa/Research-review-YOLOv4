# -*- coding: utf-8 -*-
"""YOLOv4_Tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12QusaaRj_lUwCGDvQNfICpa7kA7_a2dE
"""

# clone darknet repo
!git clone https://github.com/AlexeyAB/darknet

# Commented out IPython magic to ensure Python compatibility.
# change makefile to have GPU and OPENCV enabled
# %cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

# verify CUDA
!/usr/local/cuda/bin/nvcc --version

# make darknet (builds darknet so that you can then use the darknet executable file to run or train object detectors)
!make

"""Download pre-trained YOLOv4 weights"""

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

"""Define Helper Functions"""

# Commented out IPython magic to ensure Python compatibility.
# define helper functions
def imShow(path):
  import cv2
  import matplotlib.pyplot as plt
#   %matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.show()

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/00000b4dcff7f799.jpg

# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/00001a21632de752.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/0001c8fbfb30d3a6.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/0001dd930912683d.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/000313fed9979d24.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/0003d1c3be9ed3d6.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/0007e8279612ac07.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/000912f449df9180.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/000f579533500448.jpg
# show image using our helper function
imShow('predictions.jpg')

# run darknet detection on test images
!./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights /content/002060b1d41fa170.jpg
# show image using our helper function
imShow('predictions.jpg')