import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Title
st.title("🌤 Weather Prediction using Decision Tree (Percentage Data)")

# Load dataset
df = pd.read_csv("weather_percentage.csv")

# Features and target
X = df.drop(columns=['play'])
y = df['play']

# Train model
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# Sidebar Inputs
st.sidebar.header("Enter Today's Weather (in %)")
outlook = st.sidebar.slider("Outlook (Sunny=30, Overcast=60, Rain=90)", 0, 100, 30)
temperature = st.sidebar.slider("Temperature (Cool=40, Mild=60, Hot=80)", 0, 100, 60)
humidity = st.sidebar.slider("Humidity (Normal=50, High=90)", 0, 100, 70)
windy = st.sidebar.slider("Windy (False=20, True=80)", 0, 100, 20)

# Prepare input data
input_data = pd.DataFrame({
    'outlook': [outlook],
    'temperature': [temperature],
    'humidity': [humidity],
    'windy': [windy]
})

# Make prediction
prediction = model.predict(input_data)[0]
result = "✅ Yes, Play!" if prediction == 100 else "❌ No, Don’t Play."

# Display results
st.subheader("Prediction Result:")
st.success(result)

# Show decision tree rules
st.subheader("🧩 Decision Tree Rules:")
rules = export_text(model, feature_names=list(X.columns))
st.text(rules)

# Optional: show dataset
with st.expander("📄 View Training Dataset"):
    st.dataframe(df)
