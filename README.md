## Yolo-Object-Detection
    > yolo-model-making:-
        - contains the model making procedure along with pre trained weights.

    > Object-Detection-Yolo-Trained-Model:-
        - Loaded the model produced by the Yolo-model-making.
        - Containd the functionallity that predicts the object detection and gives output.

    > obj-detection-opencv:-
        - Yolo using pre trained weights with open-cv.
        - Not much very reliable.

    

## :warning: Dependencies:
    * Download and paste these two folders in Yolo-Object-Detection repo in order to execute any files.
        [Model and weight yolo](https://drive.google.com/drive/folders/1twsK4s3DfXzD0O1n1UwrnUvHuzpy9Rce?usp=sharing)


### Project Working Structure:-
    *  **images**


### To make files containg the data of every image:-


```python
import os
for i in os.listdir("images"):
#     print(os.path.splitext(i)[0])
    f = open("objects-data/"+os.path.splitext(i)[0]+".txt", "a")
    f.write(str(detect_objects("images/"+i)))
    f.close()
```