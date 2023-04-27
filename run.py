import streamlit as st
import streamlit.components.v1 as components


# st.header("index html import")

HtmlFile = open("templates/index.html", 'r', encoding="utf-8")
source_code = HtmlFile.read() 
# print(source_code)
#components.html(source_code)
components.html(source_code,height=2500, width=2000, scrolling=False)
