import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Uygulama", layout="wide")

BASE = Path(__file__).parent
html_path = BASE / "index.html"

# index.html içeriğini aynen göm
html = html_path.read_text(encoding="utf-8")

# Not: index.html içinde referans verilen js/css dosyaları aynı klasörde olmalı:
# index-BF5fFsDi.js
# index-UyH8M1lL.css

components.html(html, height=900, scrolling=True)
