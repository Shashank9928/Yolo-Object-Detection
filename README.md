
## Yolo-Object-Detection

> Yolo-model-making:-

- contains the model making procedure along with pre-trained weights.

  

> Object-Detection-Yolo-Trained-Model:-

- Loaded the model produced by the Yolo-model-making.

- Contains the functionality that predicts the object detection and gives output.

  

> obj-detection-opencv:-

- Yolo using pre-trained weights with open-cv.

- Not much very reliable.

  

  

## :warning: Dependencies:

* Download and paste these two folders in the Yolo-Object-Detection repo to execute any files.

[Model and weight yolo](https://drive.google.com/drive/folders/1twsK4s3DfXzD0O1n1UwrnUvHuzpy9Rce?usp=sharing)

  
  

## Project Working Structure:-

* **images:**  Folder contains the 50 different images containing the different objects.

* **Object-Detection-Yolo-Trained-Model:**
	*  containd the code to load model.
	*  Also the function **(detect_objects)** that takes the **image path** as input and return an dictionery conatining the **key=>** as object name and **value** as  count of that object.
![detect function](https://github.com/Shashank9928/Yolo-Object-Detection/blob/master/readme-resources/detect_func.png)

* **Working on multiple images:-** 
	*  Loaded all the images from the image folder and passes in the detect_objects function then store each image information in the objects-data folder
		* objects-data: contains the text files having the information of every object in a particular image.
	```python

	import os
	
	for i in os.listdir("images"):
		# print(os.path.splitext(i)[0])
		f = open("objects-data/"+os.path.splitext(i)[0]+".txt", "a")
		f.write(str(detect_objects("images/"+i)))
		f.close()

```