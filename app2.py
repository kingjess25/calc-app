import streamlit as st
from PIL import Image
st.title("Calculator App")

def add(a,b):
    c= a+b
    return c

def sub(x,y):
    z= x-y
    return z   
    

def mul(e,f):
    g= e*f
    return g
col1,col2=st.columns(2)

with col1:
    x = st.number_input("input your first number")
    y= st.number_input("input your next number")

with col2:   

    if st.button("Add"):
        st.write(add(x,y))
        

    if st.button("multiplication") :
        st.write(mul(x,y)) 

    
    if st.button("subraction"):
       st.write(sub(x,y))         
      









