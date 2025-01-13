import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Agriplex Farms grows and supplies potatoes to local and international markets.\n"
        f"* The farm faces yield losses and financial risks due to potato diseases caused by bacteria "
        f"and phytophthora.\n"
        f"* Current manual disease detection is slow, error-prone, and lacks scalability.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset of potato leaf images are the 3 most important categories out of a dataset containing 3076 images in 7 categories. It contains 1117 images labeled as healthy, Bacterial or Phytopthora.\n"
        f"* Augmentation techniques (e.g., flipping, rotation, brightness adjustments) are applied to enhance the dataset’s variability and improve model robustness.\n\n"
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/fancypigeon5/potato-leaf-diseases/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"Healthy, Bacterial or Phytopthora infected leaves visually.\n"
        f"* 2 - The client is interested in telling whether a given plant is healthy, infected by bacteria or infected by Pytopthora."
    )
