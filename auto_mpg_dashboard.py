import streamlit as st
import pandas as pd
import seaborn as sns

# set the style for seabornsns.set_style('darkgrid')
# st.write("# This Dashboard is made by Pasha Faisal")
# Title of the dashboard
st.title('Dashboard for Autompg dataset.')

df = pd.read_csv("C:/Users/faisa/Downloads/Streamlit_tutorials-master/Streamlit_tutorials-master/auto-mpg.csv")
@st.cache
def load_data():
    """ Utility function for loading the autompg dataset as a dataframe."""
    df = pd.read_csv("C:/Users/faisa/Downloads/Streamlit_tutorials-master/Streamlit_tutorials-master/auto-mpg.csv")

    return df


# load dataset
data = load_data()
numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns

# checkbox widget
checkbox = st.sidebar.checkbox("Reveal data.")

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

# create scatterplots
st.write("### 1. Representation of data through Scatter plot. ")
st.sidebar.subheader("Scatter plot setup")

st.set_option('deprecation.showPyplotGlobalUse', False)
# add select widget
select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
select_box2 = st.sidebar.selectbox(label="Y axis", options=numeric_columns)
sns.relplot(x=select_box1, y=select_box2, data=data)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# create histograms
st.write("### 2. Representation of data through Histogram. ")
st.sidebar.subheader("Histogram")
select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_columns)
histogram_slider = st.sidebar.slider(label="Number of Bins",min_value=5, max_value=100, value=30)
sns.distplot(data[select_box3], bins=histogram_slider)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# create jointplot
st.write("### 3. Representation of data through Joint plot. ")
st.sidebar.subheader("Joint plot")
select_box3 = st.sidebar.selectbox(label='x', options=numeric_columns)
select_box4 = st.sidebar.selectbox(label="y", options=numeric_columns)
sns.jointplot(x=select_box3, y=select_box4, data=data)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)