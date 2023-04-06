# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset into a DataFrame
bank_df = pd.read_csv("https://www.fdic.gov/bank/individual/failed/banklist.csv", encoding = "latin-1")

# Remove white space from column headers
bank_df.columns = bank_df.columns.str.strip()

# Define the layout of the Streamlit app
st.set_page_config(page_title='Failed Banks Dashboard', page_icon=':moneybag:', layout='wide')

# Create a sidebar for selecting the analysis to perform
analysis_type = st.sidebar.selectbox('Select Analysis', ['State Counts', 'Bank Counts', 'Year Counts', 'Acquiring Institution Counts', 'Highest Failed Banks by State'])

# Perform the selected analysis and display the results
if analysis_type == 'State Counts':
    # Count number of failed banks in each state
    state_counts = bank_df['State'].value_counts()
    st.write('## Number of Failed Banks in Each State')
    # Create bar chart of failed banks by state
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(state_counts.index, state_counts)
    ax.set_xticklabels(state_counts.index, rotation=90)
    ax.set_xlabel('State')
    ax.set_ylabel('Number of Failed Banks')
    plt.title('Number of Failed Banks in Each State')
    st.pyplot(fig)
    st.markdown("""
    **Number of Failed Banks in Each State:** This visualization shows the number of failed banks in each state. From the plot, it is evident that **the state of Georgia has the highest number of failed banks,** *followed by Florida and Illinois.* This plot helps to identify the states that have experienced the most bank failures.
                """)

elif analysis_type == 'Bank Counts':
    # Count the number of times each bank failed
    bank_counts = bank_df['Bank Name'].value_counts()
    st.write('## Number of Failed Banks by Bank Name')
    # st.bar_chart(bank_counts[:20])
    # Create bar chart of top 20 failed banks
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(bank_counts[:20].index, bank_counts[:20])
    ax.set_xticklabels(bank_counts[:20].index, rotation=90)
    ax.set_xlabel('Bank Name')
    ax.set_ylabel('Number of Failures')
    plt.title('Number of Failed Banks by Bank Name')
    st.pyplot(fig)
    st.markdown("""
    **Number of Failed Banks by Bank Name:** This visualization shows the number of times each bank failed. It is evident that **four banks have had the highest number of failures, each failing three times. These banks are First National Bank, Horizon Bank, Premier Bank, The First State Bank**. This plot helps to identify the banks that have had the most failures.
    """)

elif analysis_type == 'Year Counts':
    # Convert "Closing Date" column to datetime data type
    bank_df['Closing Date'] = pd.to_datetime(bank_df['Closing Date'])
    # Extract year from "Closing Date" column
    bank_df['Year'] = bank_df['Closing Date'].dt.year
    # Count the number of failed banks in each year
    year_counts = bank_df['Year'].value_counts()
    st.write('## Number of Failed Banks by Year')
    st.line_chart(year_counts)
    st.markdown("""
        **Number of Failed Banks by Year:** This visualization shows the number of failed banks in each year. From the plot, it is evident that **the year 2010 had the highest number of bank failures,**. This plot helps to identify the years in which the most bank failures occurred.
    """)

elif analysis_type == 'Acquiring Institution Counts':
    # Count the number of failed banks acquired by each institution
    acquiring_inst_counts = bank_df['Acquiring Institution'].value_counts()
    st.write('## Number of Failed Banks by Acquiring Institution')
    # st.bar_chart(acquiring_inst_counts[:10])
    # Create bar chart of top 10 acquiring institutions
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(acquiring_inst_counts[:10].index, acquiring_inst_counts[:10])
    ax.set_xticklabels(acquiring_inst_counts[:10].index, rotation=90)
    ax.set_xlabel('Acquiring Institution')
    ax.set_ylabel('Number of Failures')
    plt.title('Number of Failed Banks by Acquiring Institution')
    st.pyplot(fig)
    st.markdown("""
        **Number of Failed Banks by Acquiring Institution:** This visualization shows the number of failed banks acquired by each institution. From the plot, it is evident that **"No Acquirer" acquired the most number of failed banks,** followed by "State Bank and Trust Company", "First-Citizens Bank & Trust Company" and "Ameris Bank". This plot helps to identify the acquiring institutions that have taken over failed banks.
    """)

# Add a footer with the data source
st.write('Data Source: FDIC')
