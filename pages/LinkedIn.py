import streamlit as st
import pandas as pd

st.title("📊 LinkedIn Data Explorer")

# Function to handle file upload and display sheets
def handle_file_upload(label):
    uploaded_file = st.file_uploader(f"Upload {label} file:", type=["xls", "xlsx"], key=label)
    if uploaded_file is not None:
        try:
            # Determine file extension and appropriate engine
            if uploaded_file.name.endswith('.xls'):
                engine = 'xlrd'
            else:
                engine = 'openpyxl'

            # Load available sheet names
            xls = pd.ExcelFile(uploaded_file, engine=engine)
            sheet_names = xls.sheet_names

            # User selects a sheet
            selected_sheet = st.selectbox(f"Select a sheet from {label} file:", sheet_names, key=f"{label}_sheet")

            # Load the selected sheet into a DataFrame
            df = pd.read_excel(uploaded_file, sheet_name=selected_sheet, engine=engine)

            # Display the dataframe
            st.write(f"### Data from `{selected_sheet}` in `{label}` file")
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error reading file: {e}")

# Define labels for each file you want the user to upload
file_labels = ["Content Data", "Followers Data", "Visitors Data", "Competitor Data"]

# Loop over each file type and apply the upload handler
for label in file_labels:
    st.header(f"📁 {label}")
    handle_file_upload(label)
