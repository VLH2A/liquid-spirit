"""Wine & Spirits Menu Analyzer — Streamlit entry point (placeholder)."""

import streamlit as st

st.set_page_config(page_title="Wine & Spirits Menu Analyzer", page_icon="🥃")

st.title("🥃 Wine & Spirits Menu Analyzer")
st.caption("Demo — photograph a drinks menu and get sales intelligence.")

st.file_uploader(
    "Upload a menu photo",
    type=["png", "jpg", "jpeg"],
    help="Placeholder — no processing yet.",
)
