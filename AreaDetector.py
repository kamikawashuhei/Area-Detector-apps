import streamlit as st
import streamlit_nested_layout as stnl
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageColor
import tempfile

# 図のフォント指定
plt.rc('font', family='Meiryo')

# 画像アプロード
file_path = st.file_uploader("", type=['png', 'jpeg', 'jpg'])

