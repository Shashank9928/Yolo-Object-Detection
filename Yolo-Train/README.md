
# Training the YOLO(version-3) for custom Data:- 

	
> ## Data-Preparation:
> - Needed to label the images of different objects which you are going to train.
> - Here ['Narendra Modi', 'Barack Obama', 'Shahrukh khan', 'Cristiano Ronaldo'] Are those are we are going to Detect using Yolo.
> - Use https://tzutalin.github.io/labelImg/ this software for labelling the data.
> - Set configuration to Yolo and mark box on the image using this software.


> ## Requirments for custom training:
> - Clone the official darknet repository. `!git clone https://github.com/AlexeyAB/darknet`.
> #### Download pre-trained YOLOv3 weights
> - YOLOv3 has been trained already on the coco dataset which has 80 classes that it can predict. We will grab these pre-trained weights so that we can run YOLOv3 on these pre-trained classes and get detections.


> ## Custom Configuration of darknet:
> #### 1. Config  File:-
> - Copy over the yolov3.cfg to edit **"darknet/cfg/yolov3.cfg"** make copy as **"yolov3_custom.cfg"**.
> - Open  **"yolov3_custom.cfg"** comment testing and swwitch to training.
>
>    > - [ 6] batch=64
>     > - [ 7] subdivisions=16
>    > - [ 20] max_batches = 8000 ( max_batches => no of classes x 2000 => 4*2000 =8000 )
>    > - [610 ] classes=4 **{No of classes you are detectiing in this case it is 4}**
>     > - [603 ] filters=27 { **filter=> (classes+5)x3** = (4+5)*3 =>27  }
>    > - [696] classes=4 
>     > - [689] filters=27
>    > - [783] classes=4 
>    > - [776] filters=27 