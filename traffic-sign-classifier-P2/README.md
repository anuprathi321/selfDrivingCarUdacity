#**Traffic Sign Recognition** 

Overview
---
Detecting correct traffic sign is one of the key aspect of self driving car. In this project I have build traffic sign classifier using convolutional neural networks to train, validate and test German traffic signs. Nvidia GTX1080 card is used to train, validate and test data.

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./signs.png "Signs"
[image2]: ./original_dataset.png "Dataset distribution "
[image3]: ./augmented_dataset.png "Augumented dataset distribution"
[image4]: ./images_from_web.png "Images from web"

Dataset Summary  and Exploration
---
[German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) is used in this project. Below is summary of dataset:
* The size of training set is 34799
* The size of the validation set is 4410
* The size of test set is 12630
* The shape of a traffic sign image is (32, 32, 3)
* The number of unique classes/labels in the data set is 43

Visualization of dataset
---
Dataset distribution for 43 images is ![alt text][image2]. 

Design  Test model architechture
---
Dataset was augumented to make equal distribution for training examples. Affine transformations: rotation, translation and Shear translation is preformed on original dataset to generate more images. Augumented dataset contains 3000 images per label. 
![alt text][image3]

Preprocessing steps included data augumentation, converting augumented data to gray scale and then normalizing data. 
Summary of dataset after pre-processing:
* The size of training set is 94201
* The shape of a traffic sign image is (32, 32, 1)

Architechture:

---
| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x1 RGB image   							| 
| Convolution 5x5     	| 1x1 stride, Valid padding, outputs 28x28x16 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x16 				|
| Convolution 5x5	    | 1x1 stride, Valid padding, outputs 10x10x32     									|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x32 				|
| Fully connected		| input: 800, output: 120        									|
| RELU					|												|
| Dropout       |    keep_prob:0.7                  |                
| Fully connected		| input: 120, output: 120        									|
| RELU					|												|
| Dropout       |  keep_prob: 0.7                     |                
| Fully connected		| input: 120, output: 43  									|
| L2 regularization |          |
| Softmax				|         									|

Training model
---
Input for training is normalized gray scale images. Adam optimizer is used to reduce loss, batch size for training is set to 256, Epochs for training is 100, learning rate is set to 0.0005.
 
Iterative approach
---
I used LeNet as base model and build final solution on top of it iteratively. With Vanila LeNet model validation accuracy was around 92%. Converting images from RGB to gray scale improved validation accuracy which tells color is not important factor in recognizing signs. Model was made wider and deeper by increasing features in fully connected layer and adding one more fully connected layer. With this approach validation accuracy increased till 60 Epochs and reached 94 but it started decreasing later, clearly model was overfit. To avoid overfitting L2 regularization and dropout was introduced. I choosed to use dropout on fully connected layers with keep probability 0.7 and L2 regularization on all the weights and biases of convolutional layers and fully connected layers. 

Below are accuracy for final model:
Training set accuracy: 1.0
Validation set accuracy: 97.00
Test set accuracy: 94.76
 
###Test a Model on New Images

Here are 9 German traffic signs that I found on the web. All the 9 images are cropped to 32x32, converted to gray scale and then normalized before testing, below is gray scale output of signs from web:

![alt text][image4]

When tested I found accuracy of 77% for 9 images. 2 images were wrongly classified. Below are results for each image:

---
| Description         		|     Actual value	        					|  Predicted value |
|:---------------------:|:-----------------------------:|:----------------:|
| Roundabout mandatory  | 40   							                  | 40            |
| Speed limit (20km/h)  | 0   						                   	| 1             |
| General caution       | 18   						                  	| 18            |
| Keep right Actual     | 38   							                  | 38 |
| Speed limit (60km/h)  | 3   							                   | 1 |
| Stop Actual         		| 14   					                  		| 14 |
| Go straight or right Actual value | 36   							   | 36    |
| No entry Actual      	| 17   						                  	| 17 |
| Yield Actual        		| 13   					                  		| 13 |


As seen from above results both the spped limit signs were wrongly classified. Reason I guess is speed limit sign images from web are not correctly cropped and include background information as well.

Below is top 5 softmax probabilities for each image: <br/>
[[  9.997e-01   3.197e-04   6.043e-06   1.195e-14   5.023e-18]<br/>
 [  5.517e-01   4.478e-01   5.385e-04   1.133e-10   2.224e-11]<br/>
 [  1.000e+00   5.767e-23   6.866e-30   5.923e-30   3.020e-30]<br/>
 [  1.000e+00   0.000e+00   0.000e+00   0.000e+00   0.000e+00]<br/>
 [  9.997e-01   3.226e-04   8.868e-07   3.522e-09   2.317e-09]<br/>
 [  1.000e+00   6.141e-06   9.875e-07   6.918e-07   3.828e-07]<br/>
 [  1.000e+00   3.424e-21   1.009e-21   2.917e-22   8.215e-26]<br/>
 [  1.000e+00   7.392e-30   1.128e-30   4.141e-33   7.132e-34]<br/>
 [  1.000e+00   0.000e+00   0.000e+00   0.000e+00   0.000e+00]]<br/>

Labels corresponding to top 5 softmax probabilities:<br/>
[[40 16  7 30 28]<br/>
 [ 1  0 28 32 38]<br/>
 [18 26 37  0 27]<br/>
 [38  0  1  2  3]<br/>
 [ 1 18 34 38  0]<br/>
 [14 33 25  4 39]<br/>
 [36 35 26 22 15]<br/>
 [17 26 32  0  8]<br/>
 [13  0  1  2  3]]<br/>
 

