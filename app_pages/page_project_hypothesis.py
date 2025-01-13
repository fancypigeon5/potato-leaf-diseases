import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"**We suspect healthy plants are distinguishable from infected plants.**\n\n"
        f"* Image Montages show that healthy plants have a consistent appearance: \n"
        f"  - Bright green color without brown spots \n"
        f"  - Large open leaves \n\n"
        f"* Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."
    )

    st.success(
        f"**We suspect bacteria infected plants have deviations in appearance and are therefore distinguishable from other plants.** \n\n"
        f"* Image Montages show that bacteria infected plants have certain deviations: \n"
        f"  - A more pale and yellowish green color \n"
        f"  - Smaller curled up leaves \n\n"
        f"* Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."
    )

    st.success(
        f"**We suspect phytopthora infected plants have deviations in appearance and are therefore distinguishable from other plants.** \n\n"
        f"* Image Montages show that phytopthora infected plants have certain deviations: \n"
        f"  - A darker green color \n"
        f"  - Deformed leaves with brouwn patches/spots on them \n\n"
        f"* Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."
    )

    st.success(
        f"**We suspect that a NN will be able to learn the differences between when a plant is Healthy, infected by bacteria or infected by phytopthora.** \n\n"
        f"* The NN was able to learn the differences between the classes with an accuracy of 92% on the test set."
    )
