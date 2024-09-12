import streamlit as st
import requests

# Creating a list of all the neighbourhoods
NEIGHBOURHOODS = ['Blmngtn', 'Blueste', 'BrDale', 'BrkSide', 'ClearCr',
                  'CollgCr', 'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR',
                  'MeadowV', 'Mitchel', 'NAmes', 'NoRidge', 'NPkVill',
                  'NridgHt', 'NWAmes', 'OldTown', 'SWISU', 'Sawyer',
                  'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker']

# Title and subtitle
st.markdown('# House Prices Calculator 🏠')
st.markdown('### Enter the following details and click the "Calculate" button')
st.write("")
st.write("")

# Splitting into 2 columns
col1, col2 = st.columns(2)

# Getting all the inputs in the left column
lot_area = col1.number_input('Lot Area in square feet', step=1, format="%d")
built_area = col1.number_input('Built Area in square feet', step=1, format="%d")
bedrooms = col1.number_input('Number of Bedrooms', step=1, format="%d", min_value=1)
neighbourhood = col1.selectbox('Neighbourhood', NEIGHBOURHOODS)
overall_condition = col1.slider('Overall Condition', min_value=1, max_value=10)

# Getting all the inputs in the right column
pool = col2.selectbox('Has Pool', ["Yes", "No"])
if pool == "Yes":
    pool = 1
else:
    pool = 0

garage = col2.selectbox('Has Garage', ["Yes", "No"])
if garage == "Yes":
    garage = 1
else:
    garage = 0

basement = col2.selectbox('Has Basement', ["Yes", "No"])
if basement == "Yes":
    basement = 1
else:
    basement = 0

air_conditioning = col2.selectbox('Has AC', ["Yes", "No"])
if air_conditioning == "Yes":
    air_conditioning = 1
else:
    air_conditioning = 0

fireplace = col2.selectbox('Has Fireplace', ["Yes", "No"])
if fireplace == "Yes":
    fireplace = 1
else:
    fireplace = 0


# Calling the api
url = 'https://houses-api-image-v7n7mb57hq-ew.a.run.app/predict'

params = {
    'lot_area': lot_area,
    'built_area': built_area,
    'bedrooms': bedrooms,
    'neighbourhood': neighbourhood,
    'overall_condition': overall_condition,
    'pool': pool,
    'garage': garage,
    'basement': basement,
    'air_conditioning': air_conditioning,
    'fireplace': fireplace
}

response = requests.get(url, params).json()

st.write("")
st.write("")

if st.button("Calculate"):
    st.write('Your estimated house price is', response['house_price'], '$')
