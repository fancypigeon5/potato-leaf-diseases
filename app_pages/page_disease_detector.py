import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def page_disease_detector_body():
    st.info(
        f"* The client is interested in telling whether a given plant is "
        f"healthy, infected by bacteria or infected by Pytopthora. ")

    st.write(
        f"* You can download images for live prediction. "
        f"You can download the images from [here](https://www.kaggle.com/datasets/warcoder/potato-leaf-disease-dataset/data)."
        f"Make sure to download from the Healthy, Bacteria and Phytopthora folders.")

    st.write("---")

    images_buffer = st.file_uploader('Upload plant image. You may select more than one.',
                                     type='jpg', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Plant image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v2'
            model = 'V4'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version, model=model)
            plot_predictions_probabilities(pred_proba, pred_class)

            new_row = pd.DataFrame(
                {"Name": [image.name], 'Result': [pred_class]})
            df_report = pd.concat([df_report, new_row], ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
