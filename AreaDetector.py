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

if file_path is not None:
    # cv2用にアップロード画像のパスを変換
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_path.read())
        img_for_detection = cv2.imread(temp_file.name)
    h, w, _ = img_for_detection.shape
    # スケールバー入力
    with st.sidebar.expander("スケールバーのサイズ", expanded=True):
        left_scale_column, right_scale_column = st.columns(2)
        scale_unit = left_scale_column.selectbox("単位", ["μm", "nm", "mm"])
        scale_value = right_scale_column.text_input("数値", None)  # サイズ
    with st.sidebar.expander("スケールバーの読み込み", expanded=True):
        scalebary_columns = st.columns(2)
        with scalebary_columns[0]:
            triming_scalebar_min_y_slider = st.slider("上端", 0, h)
            triming_scalebar_min_y = st.number_input("", value=triming_scalebar_min_y_slider)
        with scalebary_columns[1]:
            triming_scalebar_max_y_slider = st.slider("下端", 0, -1 * h)
            triming_scalebar_max_y = st.number_input(" ", value=triming_scalebar_max_y_slider)
        scalebarx_columns = st.columns(2)
        with scalebarx_columns[0]:
            triming_scalebar_min_x_slider = st.slider("左端", 0, w)
            triming_scalebar_min_x = st.number_input("   ", value=triming_scalebar_min_x_slider)
        with scalebarx_columns[1]:
            triming_scalebar_max_x_slider = st.slider("右端", 0, -1 * w)
            triming_scalebar_max_x = st.number_input("    ", value=triming_scalebar_max_x_slider)
    # 画像入力
    with st.sidebar.expander("分析範囲", expanded=True):
        detectareay_columns = st.columns(2)
        with detectareay_columns[0]:
            triming_detect_area_min_y_slider = st.slider("上端 ", 0, h)
            triming_detect_area_min_y = st.number_input("     ", value=triming_detect_area_min_y_slider)
        with detectareay_columns[1]:
            triming_detect_area_max_y_slider = st.slider("下端 ", 0, -1 * h)
            triming_detect_area_max_y = st.number_input("      ", value=triming_detect_area_max_y_slider)
        detectareax_columns = st.columns(2)
        with detectareax_columns[0]:
            triming_detect_area_min_x_slider = st.slider("左端 ", 0, w)
            triming_detect_area_min_x = st.number_input("       ", value=triming_detect_area_min_x_slider)
        with detectareax_columns[1]:
            triming_detect_area_max_x_slider = st.slider("右端 ", 0, -1 * w)
            triming_detect_area_max_x = st.number_input("        ", value=triming_detect_area_max_x_slider)
    # 元画像の白黒反転
    # 閾値の数（=検出領域の分類数）
    with st.sidebar.expander("検出パラメーター", expanded=True):
        left_bwinv_column, right_thresh_column = st.columns(2)
        bwinv = left_bwinv_column.selectbox("検出領域の色", ["白", "黒"])  # 0:反転しない　1:反転する
        thresh_n = right_thresh_column.number_input("検出領域の数", 0, max_value=5)
        # 各閾値の値
        if thresh_n == 1:
            thresh = [0] * (thresh_n + 1)
            thresh0 = st.slider("閾値", 0, 255)
            thresh[0] = st.number_input("         ", value=thresh0)
            thresh[1] = 255
        elif thresh_n == 2:
            thresh = [0] * (thresh_n + 1)
            thresh_columns = st.columns(thresh_n)
            with thresh_columns[0]:
                thresh0 = st.slider("閾値", 0, 255)
                thresh[0] = st.number_input("         ", value=thresh0)
            with thresh_columns[1]:
                thresh1 = st.slider("", 0, 255)
                thresh[1] = st.number_input("          ", value=thresh1)
            thresh[2] = 255
        elif thresh_n == 3:
            thresh = [0] * (thresh_n + 1)
            thresh_columns = st.columns(thresh_n)
            with thresh_columns[0]:
                with thresh_columns[0]:
                    thresh0 = st.slider("閾値", 0, 255)
                    thresh[0] = st.number_input("         ", value=thresh0)
                with thresh_columns[1]:
                    thresh1 = st.slider("", 0, 255)
                    thresh[1] = st.number_input("          ", value=thresh1)
                with thresh_columns[2]:
                    thresh2 = st.slider(" ", 0, 255)
                    thresh[2] = st.number_input("           ", value=thresh2)
                thresh[3] = 255
        elif thresh_n == 4:
            thresh = [0] * (thresh_n + 1)
            thresh_columns = st.columns(thresh_n)
            with thresh_columns[0]:
                with thresh_columns[0]:
                    thresh0 = st.slider("閾値", 0, 255)
                    thresh[0] = st.number_input("         ", value=thresh0)
                with thresh_columns[1]:
                    thresh1 = st.slider("", 0, 255)
                    thresh[1] = st.number_input("          ", value=thresh1)
                with thresh_columns[2]:
                    thresh2 = st.slider(" ", 0, 255)
                    thresh[2] = st.number_input("           ", value=thresh2)
                with thresh_columns[3]:
                    thresh3 = st.slider("  ", 0, 255)
                    thresh[3] = st.number_input("            ", value=thresh3)
            thresh[4] = 255
        elif thresh_n == 5:
            thresh = [0] * (thresh_n + 1)
            thresh_columns = st.columns(thresh_n)
            with thresh_columns[0]:
                with thresh_columns[0]:
                    thresh0 = st.slider("閾値", 0, 255)
                    thresh[0] = st.number_input("         ", value=thresh0)
                with thresh_columns[1]:
                    thresh1 = st.slider("", 0, 255)
                    thresh[1] = st.number_input("          ", value=thresh1)
                with thresh_columns[2]:
                    thresh2 = st.slider(" ", 0, 255)
                    thresh[2] = st.number_input("           ", value=thresh2)
                with thresh_columns[3]:
                    thresh3 = st.slider("  ", 0, 255)
                    thresh[3] = st.number_input("            ", value=thresh3)
                with thresh_columns[4]:
                    thresh4 = st.slider("   ", 0, 255)
                    thresh[4] = st.number_input("             ", value=thresh4)
            thresh[5] = 255
        # メジアンフィルタのカーネルサイズ（奇数）
        if thresh_n == 1:
            ksize = [0] * thresh_n
            ksize[0] = st.number_input("フィルター", 1, step=2)
        elif thresh_n == 2:
            ksize = [0] * thresh_n
            zero_column, first_column = st.columns(thresh_n)
            ksize[0] = zero_column.number_input("フィルター", 1, step=2)
            ksize[1] = first_column.number_input("         ", 1, step=2)
        elif thresh_n == 3:
            ksize = [0] * thresh_n
            zero_column, first_column, second_column = st.columns(thresh_n)
            ksize[0] = zero_column.number_input("フィルター", 1, step=2)
            ksize[1] = first_column.number_input("         ", 1, step=2)
            ksize[2] = second_column.number_input("          ", 1, step=2)
        elif thresh_n == 4:
            ksize = [0] * thresh_n
            zero_column, first_column, second_column, third_column = st.columns(thresh_n)
            ksize[0] = zero_column.number_input("フィルター", 1, step=2)
            ksize[1] = first_column.number_input("         ", 1, step=2)
            ksize[2] = second_column.number_input("          ", 1, step=2)
            ksize[3] = third_column.number_input("           ", 1, step=2)
        elif thresh_n == 5:
            ksize = [0] * thresh_n
            zero_column, first_column, second_column, third_column, fourth_column = \
                st.columns(thresh_n)
            ksize[0] = zero_column.number_input("フィルター", 1, step=2)
            ksize[1] = first_column.number_input("         ", 1, step=2)
            ksize[2] = second_column.number_input("          ", 1, step=2)
            ksize[3] = third_column.number_input("           ", 1, step=2)
            ksize[4] = fourth_column.number_input("            ", 1, step=2)
    # 輪郭の色
    # 輪郭の太さ
    with st.sidebar.expander("描画パラメーター", expanded=True):
        if thresh_n == 0:
            st.write("")
        elif thresh_n == 1:
            cont_colorRGB = [0] * thresh_n
            cont_color = st.color_picker("領域色", "#ff0000")
            cont_colorRGB[0] = ImageColor.getcolor(cont_color, "RGB")
            cont_thick = st.number_input("領域輪郭の太さ", 2)
        elif thresh_n == 2:
            cont_colorRGB = [0] * thresh_n
            zero_column, first_column = st.columns(thresh_n)
            cont_color0 = zero_column.color_picker("領域色", "#ff0000")
            cont_color1 = first_column.color_picker("", "#0000ff")
            cont_colorRGB[0] = ImageColor.getcolor(cont_color0, "RGB")
            cont_colorRGB[1] = ImageColor.getcolor(cont_color1, "RGB")
            cont_thick = st.number_input("領域輪郭の太さ", 2)
        elif thresh_n == 3:
            cont_colorRGB = [0] * thresh_n
            zero_column, first_column, second_column = st.columns(thresh_n)
            cont_color0 = zero_column.color_picker("領域色", "#ff0000")
            cont_color1 = first_column.color_picker("", "#0000ff")
            cont_color2 = second_column.color_picker(" ", "#00ff00")
            cont_colorRGB[0] = ImageColor.getcolor(cont_color0, "RGB")
            cont_colorRGB[1] = ImageColor.getcolor(cont_color1, "RGB")
            cont_colorRGB[2] = ImageColor.getcolor(cont_color2, "RGB")
            cont_thick = st.number_input("領域輪郭の太さ", 2)
        elif thresh_n == 4:
            cont_colorRGB = [0] * thresh_n
            zero_column, first_column, second_column, third_column = st.columns(thresh_n)
            cont_color0 = zero_column.color_picker("領域色", "#ff0000")
            cont_color1 = first_column.color_picker("", "#0000ff")
            cont_color2 = second_column.color_picker(" ", "##00ff00")
            cont_color3 = third_column.color_picker("  ", "#ffd700")
            cont_colorRGB[0] = ImageColor.getcolor(cont_color0, "RGB")
            cont_colorRGB[1] = ImageColor.getcolor(cont_color1, "RGB")
            cont_colorRGB[2] = ImageColor.getcolor(cont_color2, "RGB")
            cont_colorRGB[3] = ImageColor.getcolor(cont_color3, "RGB")
            cont_thick = st.number_input("領域輪郭の太さ", 2)
        elif thresh_n == 5:
            cont_colorRGB = [0] * thresh_n
            zero_column, first_column, second_column, third_column, fourth_column = \
                st.columns(thresh_n)
            cont_color0 = zero_column.color_picker("領域色", "#ff0000")
            cont_color1 = first_column.color_picker("", "#0000ff")
            cont_color2 = second_column.color_picker(" ", "##00ff00")
            cont_color3 = third_column.color_picker("  ", "#ffd700")
            cont_color4 = fourth_column.color_picker("   ", "#ff00ff")
            cont_colorRGB[0] = ImageColor.getcolor(cont_color0, "RGB")
            cont_colorRGB[1] = ImageColor.getcolor(cont_color1, "RGB")
            cont_colorRGB[2] = ImageColor.getcolor(cont_color2, "RGB")
            cont_colorRGB[3] = ImageColor.getcolor(cont_color3, "RGB")
            cont_colorRGB[4] = ImageColor.getcolor(cont_color4, "RGB")
            cont_thick = st.number_input("領域輪郭の太さ", 2)

    # 閾値以上の値の変換値（閾値以下は0）
    thresh_val = [255, 255, 255, 255, 255]
else:
    st.write("ファイルをアップロードして下さい")


def multithreshold(detect_img, img_raw, threshold_num,
                   threshold, maxval, lineHEX, line_thickness,
                   ex_value, k
                   ):
    total_detect_area = []
    for i in range(threshold_num):
        # 多値化
        thresh_img = np.empty_like(detect_img)
        for n in range(detect_img.shape[0]):
            for m in range(detect_img.shape[1]):
                if threshold[i] < detect_img[n, m] <= threshold[i + 1]:
                    thresh_img[n, m] = maxval[i]
                else:
                    thresh_img[n, m] = 0

        # ノイズ除去（メジアンフィルタ）
        detect_img_mod = cv2.medianBlur(thresh_img, k[i])  # ksizeは奇数
        st.header(f"領域{i}用ノイズ処理")
        st.image(detect_img_mod)
        # 輪郭の識別
        detect_conts, _ = cv2.findContours(detect_img_mod,
                                           mode=cv2.RETR_EXTERNAL,  # 輪郭の取り方
                                           method=cv2.CHAIN_APPROX_NONE)  # 輪郭座標の取り方
        # 輪郭の描画
        areadraw_img = cv2.drawContours(img_raw, detect_conts, -1,
                                        color=lineHEX[i],  # 輪郭の色
                                        thickness=line_thickness)  # 輪郭線の太さ
        st.header(f"領域{i}")
        st.image(areadraw_img)
        # 検出領域の面積計算（実スケール）
        detect_area = []
        for m in detect_conts:
            detect_area.append(cv2.contourArea(m) * ex_value ** 2)
        st.write(f"閾値：{str(threshold[i])}")
        # st.write("検出面積(" + scale_unit + "): " + str(detect_area))
        st.write(f"検出総面積({scale_unit}^2):{str(sum(detect_area))}")


if file_path is not None:
    # 検出領域描画用の画像作成
    img_raw = img_for_detection
    img_for_scale = img_for_detection.copy()

    # 白黒反転(検出したい領域が白色の場合に必要)
    if bwinv == "黒":
        img_for_detection = cv2.bitwise_not(img_for_detection)

    # 画像のグレイ化
    gray_img_for_detection = cv2.cvtColor(img_for_detection, cv2.COLOR_BGR2GRAY)
    gray_img_for_scale = cv2.cvtColor(img_for_scale, cv2.COLOR_BGR2GRAY)

    # 画像の抽出
    h, w = gray_img_for_detection.shape

    # 画像端部の座標 (左上座標と右下座標)
    min_x, min_y, max_x, max_y = 0, 0, w, h

    # スケールバーの切り取り
    scale_bar_img = gray_img_for_scale[min_y + triming_scalebar_min_y: max_y + triming_scalebar_max_y,
                    min_x + triming_scalebar_min_x: max_x + triming_scalebar_max_x]
    st.header("スケールバー")
    st.image(scale_bar_img)

    # 検出領域用画像の切り取り（下部の照射電圧などの情報カット）
    detect_img = gray_img_for_detection[min_y + triming_detect_area_min_y: max_y + triming_detect_area_max_y,
                 min_x + triming_detect_area_min_x: max_x + triming_detect_area_max_x]
    st.header("分析範囲")
    st.image(detect_img)
    if scale_value is not None:
        # スケールバーの長さ計算(ピクセル)
        scale_cont, _ = cv2.findContours(scale_bar_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        # 右端：scale_cont[0][1][0][0]、左端：scale_cont[0][2][0][0]
        bar_len_px = scale_cont[0][2][0][0] - scale_cont[0][1][0][0]
        # 1ピクセルのサイズをスケールの単位に換算
        px_to_real = int(scale_value) / bar_len_px  # scale_valueはstrなのでintに変換

        # 複数閾値による輪郭分類
        multithreshold(detect_img, img_raw, threshold_num=thresh_n, threshold=thresh, maxval=thresh_val,
                       lineHEX=cont_colorRGB,
                       line_thickness=cont_thick, ex_value=px_to_real, k=ksize)