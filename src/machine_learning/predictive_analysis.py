import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0, 0],
        index={'Bacteria': 0, 'Healthy': 1, 'Phytopthora': 2}.keys(),
        columns=['Probability']
    )
    for i, key in enumerate(prob_per_class.index):
        prob_per_class.loc[key] = pred_proba[i]
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version, model):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(
        f"outputs/{version}/model_{model}/disease_identification_model.keras")

    pred_proba = model.predict(my_image)[0]

    target_map = {v: k for k, v in {'Bacteria': 0,
                                    'Healthy': 1, 'Phytopthora': 2}.items()}
    pred_class_index = np.argmax(pred_proba)
    pred_class = target_map[pred_class_index]

    if pred_class == 'Healthy':
        st.write(
            f"The predictive analysis indicates the sample cell is "
            f"**Healthy**")
    else:
        st.write(
            f"The predictive analysis indicates the sample cell is "
            f"Infected with **{pred_class.lower()}**")

    return pred_proba, pred_class
