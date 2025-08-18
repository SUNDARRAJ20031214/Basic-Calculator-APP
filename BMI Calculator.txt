import streamlit as st

st.title("🧮 BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (cm):", min_value=10.0, step=0.5)

if st.button("Calculate BMI"):
    if height > 0:
        # Convert height cm → meters
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.success(f"✅ Your BMI is: {bmi:.2f}")

        # BMI Categories
        if bmi < 18.5:
            st.warning("⚠️ Underweight")
        elif 18.5 <= bmi < 25:
            st.info("✅ Normal weight")
        elif 25 <= bmi < 30:
            st.warning("⚠️ Overweight")
        else:
            st.error("🚨 Obese")
    else:
        st.error("Height must be greater than 0")
