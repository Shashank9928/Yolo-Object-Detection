import streamlit as st
import subprocess
import cv2 as cv
import numpy as np



def run_make_cpu():
    """Run command, transfer stdout/stderr back into Streamlit and manage error"""
    st.info("Running Getting the yolo ready ")
    result = subprocess.run('../../Resources/makefile_cpu.sh', capture_output=True, text=True,shell=True)
    try:
        result.check_returncode()
        # st.info(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(result.stderr)
        raise e

def run_make_gpu():
    """Run command, transfer stdout/stderr back into Streamlit and manage error"""
    st.info("Running Getting the yolo ready ")
    result = subprocess.run('../../Resources/makefile_gpu.sh', capture_output=True, text=True,shell=True)
    try:
        result.check_returncode()
        # st.info(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(result.stderr)
        raise e

def run_command(cmd):
    """Run command, transfer stdout/stderr back into Streamlit and manage error"""
    # st.info("Running Getting the yolo ready ")
    result = subprocess.run(cmd, capture_output=True, text=True,shell=True)
    try:
        result.check_returncode()
        st.info(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(result.stderr)
        raise e

def begain_trainig(b_dir,data_path="Data",classes=1):
    max_batches = (classes*2000)
    filters = ((classes+5)*3)
    # st.warning(b_dir)
    # run_command("ls")
    # try:
    # run_command("ls")
    subprocess.run(f"cp {b_dir}/darknet/cfg/yolov3_training.cfg {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)
    
    subprocess.run(f"sed -i '20s/max_batches=500200/max_batches = {max_batches}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)

    subprocess.run(f"sed -i '603s/filters=255/filters = {filters}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)
    subprocess.run(f"sed -i '610s/classes=80/classes = {classes}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)

    subprocess.run(f"sed -i '689s/filters=255/filters = {filters}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)
    subprocess.run(f"sed -i '696s/classes=80/classes = {classes}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)

    subprocess.run(f"sed -i '776s/filters=255/filters = {filters}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)
    subprocess.run(f"sed -i '783s/classes=80/classes = {classes}/' {b_dir}/darknet/cfg/yolov3_custom_train.cfg",shell=True)
    st.info("TRAINING UNDER PROCESS MAY TAKE TIME")

    run_command(cmd=f"{b_dir}/darknet/darknet detector train {data_path}/labelled_data.data {b_dir}/darknet/cfg/yolov3_custom_train.cfg {b_dir}/Custom_weights/darknet53.conv.74 -dont_show")




def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h,classes):

    label = str(classes[class_id])
    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
    color = COLORS[class_id]

    cv.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv.putText(img, label, (x-10,y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def detect_image(image,classes_loc="",weights_pth="",cfg_path=""):

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    classes = (classes_loc + "/classes.txt")


    st.warning(classes)
    st.warning(weights_pth)
    st.warning(cfg_path)
    
    
    with open(classes, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
    # run_command(cmd="ls")
    net = cv.dnn.readNet(str(weights_pth), str(cfg_path))
    blob = cv.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4
    present_classes = []

    for out in outs:
    #     print(out)
        for detection in out:
    #         print(detection)
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                print(center_x,center_y)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])


    indices = cv.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        present_classes.append(classes[class_ids[i]])
        draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h),classes=classes)
        return (image)
        # cv.imwrite("object-detection.jpg", image)
        # cv.destroyAllWindows()