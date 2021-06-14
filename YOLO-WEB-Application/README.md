
# YOLO WEB APP
>#### Introduction:-
> It is a basic application, in which you can just drop your data and using some automated, tasks it will train the model on the provided data.

> #### Specifications:-
> * Uses streamlit framework to deliver the frontend.
> * Based on darknet YOLO(V3).
> * Uses the concept of transfer learning technique to work efficiently.

## Enviroment needed to work:

> ### Needs on oprating system:-
> > - [ ] Darknet:-
> > `sudo apt install darknet`
>
> > - [ ] Graphics and Cuda enviroment:-
> > - `sudo add-apt-repository ppa:graphics-drivers/ppa`
> > 
> > For GeForce 10, 20 and RTX series GPUs use nvidia-430
> > For GeForce 8 and 9 series GPUs use nvidia-340
> > For GeForce 6 and 7 series GPUs use nvidia-304
>  > - `sudo apt install nvidia-340`
>  > ##### Cuda-toolkit:-
>  > - `sudo apt install nvidia-cuda-toolkit`
>  > - `sudo apt-get install cuda`
>  > ##### Supporting libraries for OpenCv (c ++)
>  > - `sudo apt install libopencv-dev`
> ### Deployment:-
> > **1. Clone the repositery.**
> > **2. Initiate an empty folder **"Custom_weights"** .**
> > > `mkdir Custom_weights`
> > > `cd Custom_weights`
> > > `wget https://pjreddie.com/media/files/darknet53.conv.74`
> >
> > **3. Now initiate another Empty folder  **"backup"** in order to store trained weights.**
> > >`cd ..`
> > > `mkdir backup`
> >
> > **4. Configure the yolo according to system:-**
> > 
> > > **For GPU:-**
> > > `cd darknet`
> > > `sed -i 's/OPENCV=0/OPENCV=1/' Makefile`
> > > `sed -i 's/GPU=0/GPU=1/' Makefile`
> > >  `sed -i 's/CUDNN=0/CUDNN=1/' Makefile`
> > > `make`
> > >
> > > **For CPU:-**
> > > `cd darknet`
> > > `sed -i 's/OPENCV=0/OPENCV=1/' Makefile`
> > > `sed -i 's/GPU=1/GPU=0/' Makefile`
> > >  `sed -i 's/CUDNN=1/CUDNN=0/' Makefile`
> > > `make`
> >
> > **4. Python packeges:-**
> > 
> > > `pip -m install requirments.txt`
> >
> > **5. Run application:-**
> > >`streamlit run app.py`
> >
> >