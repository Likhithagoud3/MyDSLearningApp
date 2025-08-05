import streamlit as st

# Set the title and subheader
st.title("📊 Learn Data Science App")
st.subheader("Welcome! Learn Data Science topics easily. 😊")

# Dropdown menu
topic = st.selectbox("Choose Topic:", ["Python Basics", "EDA", "Data Visualization", "Machine Learning"])

# Show content based on selected topic
if topic == "Python Basics":
    st.markdown("""
### Python Basics 🐍
This section will cover:
- Variables
- Data Types
- Loops
- Functions
""")

elif topic == "EDA":
    st.markdown("""
### Exploratory Data Analysis (EDA) 🔍
This section includes:
- Descriptive Statistics
- Data Cleaning
- Outlier Detection
""")

elif topic == "Data Visualization":
    st.markdown("""
### Data Visualization 📈
This section includes:
- Matplotlib
- Seaborn
- Plotly
""")

elif topic == "Machine Learning":
    st.markdown("""
### Machine Learning 🤖
This section includes:
- Supervised Learning
- Unsupervised Learning
- Model Evaluation
""")

# Footer
st.write("Designed by Likhitha ✨")
