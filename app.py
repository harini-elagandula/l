import streamlit as st
import sys
import os

# Connect backend
sys.path.append(os.path.abspath("../backend"))

from main import run_agents

st.title("💰 Multi-AI Finance Assistant")

st.write("Enter your financial details below:")

budget = st.number_input("Monthly Budget", min_value=0)
shopping = st.number_input("Shopping खर्च", min_value=0)
food = st.number_input("Food खर्च", min_value=0)
electronics = st.number_input("Electronics खर्च", min_value=0)

if st.button("Analyze"):

    user_input = f"""
    My monthly budget is {budget}.
    I spent {shopping} on shopping, {food} on food,
    and {electronics} on electronics.
    """

    result = run_agents(user_input)

    st.subheader("📊 AI Analysis")
    st.write(result)