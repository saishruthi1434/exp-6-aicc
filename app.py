import streamlit as st
import joblib
model = joblib.load("iris_model.pkl")
st.title("Iris Flower Prediction")
sl = st.number_input("Sepal Length")
sw = st.number_input("Sepal Width")
pl = st.number_input("Petal Length")
pw = st.number_input("Petal Width")
flowers = ["Setosa", "Versicolor", "Virginica"]
if st.button("Predict"):
	pred = model.predict([[sl, sw, pl, pw]])
	st.success(flowers[pred[0]])