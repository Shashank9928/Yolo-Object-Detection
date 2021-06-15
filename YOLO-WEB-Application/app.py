from numpy.lib.type_check import imag
import streamlit as st
from Resources.CreateDataName import cfdn
from Resources.CtreateTrainTest import ctnttf
from Resources.Prepration import run_command,run_make_cpu,run_make_gpu,begain_trainig,detect_image
import subprocess
import os
from zipfile import ZipFile
from PIL import Image
import numpy as np
import cv2 as cv
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent
st.title('YOLO-Custom-Object-Detection')
def save_uploadedfile(uploadedfile):
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
         ZipFile(f"tempDir/{uploadedfile.name}").extractall("Upload_Data")
     return ("Upload_Data/"+uploadedfile.name.split('.')[0])

def file_selector(folder_path=BASE_DIR.joinpath("Upload_Data"),uni=""):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames,key=uni)
    return os.path.join(folder_path, selected_filename)

st.write("""
    # Data upload formet:-
        1) Data must be in zip formet.
        2) contains the images and their lablles data as same name as image.
        3) in Data "classes.txt" and "classes.names" file shoud contain having names of all classes to classify. 
""")



st.info("Upload and prepare Data")
with st.beta_expander('Upload and prepare for training', expanded=True):
    # pro_unit = st.selectbox(
    # 'How would you like to be contacted?',
    # ("Hardware",'CPU', 'GPU')
    # )
    # st.info(pro_unit)

    # if("CPU"):
    #     subprocess.run("Resources/makefile_cpu.sh",shell=True)
    # elif("GPU"):
    #     subprocess.run("Resources/makefile_gpu.sh",shell=True)
    # else:
    #     subprocess.run("Resources/makefile_cpu.sh",shell=True)

    try:
        u_data = st.file_uploader(label='DATA')
        data_path = save_uploadedfile(u_data)
        st.write(BASE_DIR.joinpath("Upload_Data"))
    except:
        st.info("UPLOAD ZIP")

    try:
        cfdn(df_path=data_path)
        ctnttf(df_path=data_path)
        st.success("Data Prepared")
    except:
        st.write("Data Prepraring")

st.info("Select Data to start training")
with st.beta_expander('Training-Model', expanded=False):        
    fname = file_selector(uni="train")
    st.write('You selected `%s`' % fname)

    no_of_classes = st.number_input("Enter the no of classe: ",min_value=1,max_value=50)

    if(st.button("Start Training")):
        begain_trainig(b_dir=BASE_DIR,data_path=fname,classes=no_of_classes)
        st.success("TRAINING IS COMPLETED")



st.info("Test your Traied model")
with st.beta_expander('Testing-Model', expanded=False):  
    st.info("Select your data:-")
    
    f_name = file_selector(uni="test")

    img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    try:
        image = image = Image.open(img_file_buffer)
        open_cv_image = np.array(image) 
        st.write(type(open_cv_image))
        wth_pth = BASE_DIR.joinpath("backup/yolov3_custom_last.weights")
        cfg_pth = BASE_DIR.joinpath("darknet/cfg/yolov3_custom_test.cfg")
        image = detect_image(image=open_cv_image,classes_loc=f_name,weights_pth=wth_pth,cfg_path=cfg_pth)
        st.image(image=image,caption="Predicted")
    except:
        st.text("Upload image to test")
