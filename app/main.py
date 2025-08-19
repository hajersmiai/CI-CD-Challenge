import os
import streamlit as st
from app import app as app_component


def get_env_config(env: str):
    env = (env or "dev").lower()
    if env in {"dev", "development"}:
        return ("Dev Environment","#e6ffed")  # greenish
    if env in {"qa", "test", "staging"}:
        return ("QA Environment", "#fff8db")  # yellowish
    return ("Production Environment", "#ffe6e6")  # red-ish


def page():
    app_env = os.getenv("APP_ENV", "dev")
    title, bg = get_env_config(app_env)
    st.set_page_config(page_title=title, layout="wide")
    st.markdown(
        f"""
        <style>
            .stApp {{ background-color: {bg}; }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title(title)
    st.write(f"Running with APP_ENV = `{app_env}`")

    # Monte la sous‑application et lui transmet l'environnement
    app_component(app_env)


if __name__ == "__main__":
    page()