import streamlit as st
import pandas as pd
import Preparation as prep
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import download_plotlyjs, plot, iplot

header = st.container()
dataset = st.container()
features = st.container()
countries = st.container()
modeltraining = st.container()

st.markdown("""
<style>
.deploy {
background-color: #F5F5F5;
}
<style>
""", unsafe_allow_html=True
           )

@st.cache(allow_output_mutation=True)
def get_data(filename):
    RateDf = pd.read_csv(filename)
    return RateDf

@st.cache(allow_output_mutation=True)
def get_data2(filename):
    HappyDf = pd.read_csv(filename)
    return HappyDf

@st.cache(allow_output_mutation=True)
def get_data3(filename):
    WorldDf = pd.read_csv(filename)
    return  WorldDf

with header:
    st.title('Welcome to my World Development Mental Health Acquisition!')
    st.markdown('The goal is to find contributing factors to mental health worldwide and make predictions on these features to see where the World Health Organization can divert resources to assist in the mental health of people worldwide. ')
    
with dataset:
    st.header('World Suicide Rates Preview ')
    st.markdown('This data contains the suicide rates by country referenced from United Nations Development Program, World Health Organization, and the World Bank.')
    
    RateDf = get_data(prep.path('sucide.csv'))
    RateDf = RateDf.rename(columns={'country': 'Country'}).drop(columns='HDI for year')
    HappyDf = get_data2(prep.path2('CleanedHappy.csv'))
   
    WorldDf = get_data3(prep.path2('WorldDf.csv'))


    
    fig = px.choropleth(RateDf.sort_values(by='year'),
                    locations="Country",
                    locationmode = 'country names',
                    color="suicides/100k pop", 
                    hover_name="Country",
                    animation_frame="year", 
                    range_color=[20,80],
                    )
    st.plotly_chart(fig)
    st.header('World Happiness Scores Preview ')
    
    fig = px.choropleth(HappyDf.sort_values(by='year'),
                    locations="Country",
                    locationmode = 'country names',
                    color="Life Ladder", 
                    hover_name="Country",
                    animation_frame="year", 
                    range_color=[2,8],
                    )
    st.plotly_chart(fig)
    
with countries:
    sel_col, disp_col = st.columns(2)
    
    st.header('Explore Data by Country')
    country = sel_col.selectbox('Pick a country to preview:', options=['United States', 'Japan', 'Russia Federation', 'Mexico', 'Canada', 'Colombia', 'Brazil', 'Chile', 'Argentina', 'Ukraine'], index=0)
    disp_col.write(prep.get_country_overview(country, RateDf, HappyDf, WorldDf))
    
    
with features:
    st.header('Min & Max Preview')
    st.subheader('Top value counts')
    st.write(RateDf[['Country','suicides/100k pop']].groupby(['Country']).mean().sort_values(by = 'suicides/100k pop', ascending = False).head(10).style.background_gradient(cmap='seismic')), st.write(RateDf[['Country','suicides/100k pop']].groupby(['Country']).mean().sort_values(by = 'suicides/100k pop', ascending = True).head(10).style.background_gradient(cmap='seismic'))
 
  
    
with modeltraining:
    st.header('Training my model')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes.')
    
    sel_col, disp_col = st.columns(2)
    
    max_depth = sel_col.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)
    data = sel_col.selectbox('Which Dataset would you like?', options=[(HappyDf), (RateDf)], index=0)
    features = sel_col.selectbox('What feature would you like to preview?', options=['Life Ladder', 'suicides/100k pop'], index=0)
    
    input_feature = sel_col.text_input('Which feature should be used as the input feature?', 'suicides_no')
   
    
    