import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body

app = MultiPage("Potato Leaf Disease Detection")

app.add_page("Quick Project Summary", page_summary_body)

app.run()
