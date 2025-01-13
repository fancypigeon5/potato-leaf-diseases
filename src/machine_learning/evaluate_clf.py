import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version, model):
    return load_pkl_file(f'outputs/{version}/model_{model}/evaluation.pkl')
