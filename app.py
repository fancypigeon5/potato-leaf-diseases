import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_disease_detector import page_disease_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body

app = MultiPage("Potato Leaf Disease Detection")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaves Visualizer", page_leaves_visualizer_body)
app.add_page("Disease Detector", page_disease_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)

app.run()
