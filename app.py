import streamlit as st
import src.prediction as predict
st.title("Insurance Prediction🏁")
st.write("This is a simple insurance prediction app built with Streamlit. It allows users to input their information and get a prediction on whether they are likely to have an insurance claim or not.")
Age=st.number_input("enter ur age:")
Annual_Income_LPA=st.number_input("enter ur annual income (LPA):")
Policy_Term_Years=st.number_input("enter policy term (years):")
Sum_Assured_Lakhs=st.number_input("enter sum assured (lakhs):")
if st.button("Predict"):
    # 1. Initialize the class
    predictor = predict.insurance_prediction()
    
    # 2. Pass the variables collected from the sliders/inputs
    result = predictor.predict(Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs)
    
    st.success(f"The predicted insurance value is: {result}")