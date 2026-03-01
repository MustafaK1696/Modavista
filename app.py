import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="MODAVISTA", layout="wide")

BASE = Path(__file__).parent

JS_FILE = BASE / "index-BF5fFsDi.js"
CSS_FILE = BASE / "index-UyH8M1lL.css"

missing = [p.name for p in (JS_FILE, CSS_FILE) if not p.exists()]
if missing:
    st.error("Eksik dosyalar: " + ", ".join(missing))
    st.write("Bu klasörde görünen dosyalar:")
    for p in sorted(BASE.iterdir()):
        st.write("-", p.name)
    st.stop()

js = JS_FILE.read_text(encoding="utf-8", errors="ignore")
css = CSS_FILE.read_text(encoding="utf-8", errors="ignore")

# React/Vite build'in çalışması için root div yeterli.
# JS'i root'tan sonra koyuyoruz ki mount edebilsin.
html = f"""
<div id="root"></div>
<style>{css}</style>
<script>{js}</script>
"""

components.html(html, height=1000, scrolling=True)
