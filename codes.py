import streamlit as st
st.set_page_config(page_title='Code Healthscape App Engine', initial_sidebar_state = 'auto')

# st.image(
#     "hero.png",
#     width=800,
# )

import streamlit.components.v1 as components
import base64

# st.sidebar.title('Navigation')
# nav = st.sidebar.radio("Go To", ('Database Library', 'Predictive', 'Search by project', 'Search Reference', 'Building codes', 'Add a project'), index=0, key=None, help=None, on_change=None, args=None, kwargs=None)

st.title('Code Library')

lib = st.selectbox("Code Library:", ['FGI Guidelines for Design and Construction of Hospitals, 2018'])
col1,col2=st.columns(2)
with col1:
    dept = st.selectbox("Search in Department:", ['Diagnostic and Treatment Facilities'])
with col2:
    search = st.selectbox("Relevant Codes For:", ['Emergency Services'])

if search == 'Emergency Services':
    st.header('Entrance')
    st.image('ed-entrance.png')
    st.write('**Ambulance Entrances** shall provide a minimum of **6 feet (1.83 meters)** in clear width to accomodate gurneys for patients of size, mobile patient lift devices and accompanying attendants.')

    st.header('Provision of bed clearances to support patient safety')
    st.image('bed-clearances.png')
    import pandas as pd
    df = pd.read_csv("bed-clearances.csv")
    df.set_index('Type', inplace=True)
    st.table(df)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        * {font-family: "Rubik";}
        h1, h2, h3, h4, h5, h6 {font-family: "Rubik";}
        /* df cells header row face */
      .css-sc0g0 {font-family: "Rubik";}
        /* df cells font face */
        .css-1l40rdr {font-family: "Rubik";}
        .st-af {font-size: 0.9rem;}
        footer {visibility: hidden;}
        footer:after {content:'Developed with <3 by Ansh Sharma at FivD'; visibility: visible; display: block; position: relative; padding: 5px; top: 2px;}
        th {text-align:left;}
        td {text-align:left;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)