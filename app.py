#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     app.py
   @Author:        Luyao.zhang
   @Date:          2023/5/15
   @Description:
-------------------------------------------------
"""
from pathlib import Path
from PIL import Image
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# setting page layout
st.set_page_config(
    page_title="基于YOLOV8的蚕茧检测系统",
    page_icon=r"C:\Users\w1309\Downloads\OIP-C.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
    # 颜色
    )

# main page heading
st.title("基于YOLOV8的蚕茧检测系统")
# 放入一个logo 居中

st.sidebar.image(r"https://www.fynu.edu.cn/images/logo.png", width=300)
# sidebar
st.sidebar.header("模型设置")

# model options
task_type = st.sidebar.selectbox(
    "选择目标检测方式",
    ["Detection"]
)

model_type = None
if task_type == "Detection":
    model_type = st.sidebar.selectbox(
        "选择模型",
        config.DETECTION_MODEL_LIST
    )
else:
    st.error("Currently only 'Detection' function is implemented")

confidence = float(st.sidebar.slider(
    "设置执行度区间", 0, 100, 50)) / 100

model_path = r"best.pt"
# if model_type:
#     model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
# else:
#     st.error("Please Select Model in Sidebar")

# load pretrained DL model
model = load_model(model_path)

# try:
#     model = load_model(model_path)
# except Exception as e:
#     st.error(f"Unable to load model. Please check the specified path: {model_path}")

# image/video options
st.sidebar.header("图像/视频配置")
source_selectbox = st.sidebar.selectbox(
    "上传数据",
    config.SOURCES_LIST
)
# st.set_page_config{}
source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(confidence, model)
else:
    st.error("Currently only 'Image' and 'Video' source are implemented")
# 写入版权信息
st.sidebar.write("© 2023 FYN University. All Rights Reserved.")