import streamlit as st
st.title("\U0001F522 Basic Calculator")

num1=st.number_input("Enter a first number",value=0.0)
num2=st.number_input("Enter a second number",value=0.0)

operations=st.selectbox("Choose your operation",["Addition","Subtraction","Multiplication","Division"])

if st.button("start caculate"):
    if operations=="Addition":
     result=num1+num2
     st.success(f"your answer:{result}")
    elif operations=="Subtraction":
      result=num1-num2
      st.success(f"your answer:{result}")
    elif operations=="Multiplication":
      result=num1*num2
      st.success(f"your answer:{result}")
    elif operations=="Division":
     if num2!=0:
      result=num1/num2
      st.success(f"your answer:{result}")
     else:
        st.error("Dision by zero is not allowed")