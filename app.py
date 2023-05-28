import streamlit as st
import pickle
import numpy as np
import pandas as pd

a1 = ["Female", "Male"]
a2 = ["No", "Yes"]
a3 = ["0", "1", "2", "3+"]
a4 = ["Graduate", "No Graduate"]
a5 = ["No", "Yes"]
a6 = ["Rural", "Semiurban", "Urban"]

model = pickle.load(open("rf.pkl", "rb"))

st.title("Loan Approval Prediction")
gender = st.selectbox("Gender", a1)
married = st.selectbox("Married", a2)
dependents = st.selectbox("Dependents", a3)
education = st.selectbox("Education", a4)
self_employed = st.selectbox("Self Employed", a5)
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Co-Applicant Income")
loan_amount = st.number_input("Loan Amount")
loan_amount_term = st.number_input("Loan Amount Term")
credit_history = st.number_input("Credit History")
property_area = st.selectbox("Property Area", a6)

if st.button("Predict"):
    gender = a1.index(gender)
    married = a2.index(married)
    dependents = a3.index(dependents)
    education = a4.index(education)
    self_employed = a5.index(self_employed)
    property_area = a6.index(property_area)
    test = np.array([[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]])
    res = model.predict(test)
    print(res)
    st.success("Loan status: " + str(res[0]))
