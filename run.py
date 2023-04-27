import streamlit as st
import streamlit.components.v1 as components
import os


files = [file for file in os.listdir("templates/css/") if file.endswith('.css')]
files2 = [file for file in os.listdir("templates/js/") if file.endswith('.js')]      

source_code = ''
HtmlFile = open("templates/index.html", 'r', encoding="utf-8")
for fl in files:
    with open("templates/css/"+fl) as f:
        source_code = source_code + f'<style>{f.read()}</style>'
        
for fl in files2:
    with open("templates/js/"+fl) as f:
        source_code = source_code + f'<script>{f.read()}</script>'
        
source_code = source_code + HtmlFile.read() 
# print(source_code)
# components.html(source_code)
components.html(source_code,height=1080, width=1920, scrolling=True)
