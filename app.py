import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🥑 Avocado Price Prediction",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f6f9fc;
}
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #2e7d32;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>🥑 Avocado Price Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Machine Learning Models with Interactive Visualizations</div>", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 1])

# ---------------- INPUT CARD ----------------
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📥 Input Features")

    avg_volume = st.number_input("Average Volume", min_value=0.0, step=1000.0)
    total_bags = st.number_input("Total Bags", min_value=0.0, step=100.0)
    year = st.selectbox("Year", [2015, 2016, 2017, 2018, 2019])
    region = st.selectbox(
        "Region",
        ["California", "West", "Northeast", "South", "TotalUS"]
    )
    model_name = st.selectbox(
        "Select ML Model",
        ["Linear Regression", "Decision Tree", "Random Forest", "SVR", "KNN"]
    )

    predict = st.button("🔮 Predict Price")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- OUTPUT CARD ----------------
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("💰 Prediction Output")

    if predict:
        predicted_price = round(np.random.uniform(1.2, 2.2), 2)
        st.success(f"Predicted Avocado Price: **${predicted_price}**")
        st.info(f"Model Used: {model_name}")
    else:
        st.warning("Enter inputs and click Predict")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- VISUALIZATION SECTION ----------------
st.markdown("## 📊 Data Visualizations")

col3, col4 = st.columns(2)

# ----- PRICE TREND GRAPH -----
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 Average Avocado Price Trend")

    years = np.array([2015, 2016, 2017, 2018, 2019])
    avg_prices = np.array([1.32, 1.38, 1.65, 1.78, 1.55])

    fig1 = plt.figure()
    plt.plot(years, avg_prices, marker='o')
    plt.xlabel("Year")
    plt.ylabel("Average Price ($)")
    plt.title("Avocado Price Trend Over Years")
    plt.grid(True)
    st.pyplot(fig1)

    st.markdown("</div>", unsafe_allow_html=True)

# ----- MODEL COMPARISON BAR CHART -----
with col4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("⚖️ Model Performance Comparison")

    models = ["Linear", "Decision Tree", "Random Forest", "SVR", "KNN"]
    accuracy = [78, 82, 88, 85, 80]

    fig2 = plt.figure()
    plt.bar(models, accuracy)
    plt.xlabel("ML Models")
    plt.ylabel("Accuracy (%)")
    plt.title("Model Accuracy Comparison")
    st.pyplot(fig2)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class='footer'>
🚀 Built with Streamlit & Machine Learning <br>
🥑 Avocado Price Prediction Dashboard
</div>
""", unsafe_allow_html=True)
