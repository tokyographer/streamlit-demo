import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Simple Data Explorer Demo App")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(data.head())

        st.write("Summary Statistics:")
        st.write(data.describe())

        st.write("Data Visualization:")
        column = st.selectbox("Select a column to visualize", data.columns)
        
        plt.figure(figsize=(10, 4))
        plt.hist(data[column], bins=20, alpha=0.7)
        st.pyplot(plt)

if __name__ == "__main__":
    main()