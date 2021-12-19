import streamlit as st
import pandas as pd
import numpy as np
import Code.Preparation as prep
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import download_plotlyjs, plot, iplot
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from statsmodels.tsa.stattools import acf, pacf, adfuller
from datetime import datetime
from time import time
from datetime import timedelta
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()




header = st.container()
dataset = st.container()
features = st.container()
countries = st.container()
modeltraining = st.container()
time_series = st.container()


with header:
    st.title('Welcome to the World Development Mental Health Acquisition!')
    st.markdown(
    """
    <style>
   .sidebar .sidebar-content {
        background: #FFED91;
    }
    </style>
    """,
    unsafe_allow_html=True
)



    st.markdown('The goal is to find contributing factors to mental health worldwide and make predictions on these features to see where the World Health Organization can divert resources to assist in the mental health of people worldwide. ')
    
with dataset:
    
    st.header('World Suicide Rates Preview ')
    st.markdown('This data contains the suicide rates by country referenced from United Nations Development Program, World Health Organization, and the World Bank.')
    
    RateDf = pd.read_csv('Data/sucide.csv')
    RateDf = RateDf.rename(columns={'country': 'Country'}).drop(columns='HDI for year')
    HappyDf = pd.read_csv('Data/CleanedHappy.csv')
    WorldDf = pd.read_csv('Data/WorldCleanedDf.csv')

    type_map = st.selectbox('Pick either flat map or 3D map. (Optional)', options=['equirectangular', 'orthographic'], index=0)
    
    fig = px.choropleth(RateDf.sort_values(by='year'),
                    locations="Country",
                    locationmode = 'country names',
                    color="suicides/100k pop", 
                    hover_name="Country",
                    animation_frame="year", 
                    range_color=[20,80],
                    projection= type_map,
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
                    projection = type_map 
                    )
    st.plotly_chart(fig)
    
with countries:
    
    
    st.header('Explore Data by Country')
    country = st.selectbox('Pick a country to preview:', options=['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Cabo Verde', 'Canada', 'Chile', 'Colombia', 'Costa Rica',
 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Dominica', 'Ecuador', 'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
 'Grenada', 'Guatemala', 'Guyana', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania', 'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Netherlands', 'New Zealand', 'Nicaragua', 'Norway', 'Oman',
 'Panama', 'Paraguay', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saint Kitts and Nevis',
 'Saint Lucia', 'Saint Vincent and Grenadines', 'San Marino', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Suriname',
 'Sweden', 'Switzerland', 'Thailand', 'Trinidad and Tobago', 'Turkey', 'Turkmenistan', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
 'Uzbekistan'], index=0)
    st.line_chart(prep.get_country_overview2(country, RateDf, HappyDf, WorldDf))
    st.sidebar.write('Feature Averages: \n\n 1. Suicide Rate Per 100k \n 2. Happiness Score \n 3. Healthy Life Expectancy at Birth \n 4. GDP Per Capita Log \n 5. GNI Per Capita Log \n 6. Inflation \n 7. Foreign Investment \n 8. Perceptions of Corruption % \n 9. Freedom To Make Life Choices \n 10. Generosity \n 11. Social Suport \n 12. Social Safety Net Programs \n 13. Access to Electricity \n 14. Access to Basic Water Services')
    st.sidebar.write(prep.get_country_overview3(country, RateDf, HappyDf, WorldDf))

    
with features:
    st.header('Min & Max Preview')
    st.subheader('Top value counts')
    col, col2  = st.columns(2)
    col.write(RateDf[['Country','suicides/100k pop']].groupby(['Country']).mean().sort_values(by = 'suicides/100k pop', ascending = False).head(10).style.background_gradient(cmap='seismic'))
    col2.write(RateDf[['Country','suicides/100k pop']].groupby(['Country']).mean().sort_values(by = 'suicides/100k pop', ascending = True).head(10).style.background_gradient(cmap='seismic'))
 
  
    
with modeltraining:
    AllThree = pd.read_csv(('Data/Combined_df.csv'), index_col=['Country', 'year'])
    
    st.header('Modeling')
    st.markdown('Infurential model explaining how well our features can predict our target. Here you get to choose the hyperparameters of the model and see how the performance changes.')
    
    sel_col, disp_col = st.columns(2)
    feat = sel_col.selectbox('Pick a target variable for the model to train on. ("Life Ladder" is the same as Happiness Score)', options=['Life Ladder', 'suicides/100k pop'], index=0)
    max_depth = sel_col.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)
    n_estimator = sel_col.selectbox('How many estimators should we use?', options=[1000,10,50,200,500,10000], index=0)
    
    rf = RandomForestRegressor(random_state=789, n_estimators=n_estimator, min_samples_split=2, max_depth=max_depth)

    y = AllThree[feat]

    X = AllThree.drop(feat, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=789)
    rmodel = rf.fit(X_train, y_train)
    disp_col.text('Accuracy Score')
    disp_col.write(rmodel.score(X_train, y_train))
    disp_col.text('Test Score')
    disp_col.write(rmodel.score(X_test, y_test))



with time_series:
    st.header('Time Series')
    sel_col, disp_col = st.columns(2)

    feature = sel_col.selectbox('Which feature would you like to predict?', options=['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'], index=0)
    


mask = HappyDf.copy()
mask.reset_index(inplace=True)
mask.year = mask.year.astype(str)
mask.year = pd.to_datetime(mask.year)
mask.set_index('year', inplace=True)
ts_happ = mask[feature].groupby('year').mean().sort_index().interpolate().loc['2006':'2021']
ts_happ = ts_happ.resample('M').mean().interpolate()
world_happ = ts_happ.asfreq(pd.infer_freq(ts_happ.index))

start_date = datetime(2006,1,1)
end_date = datetime(2021,1,1)
lim_world_happ = world_happ[start_date:end_date]

train_end = datetime(2018,1,1)
test_end = datetime(2021,1,1)

train_data = lim_world_happ[:train_end]
test_data = lim_world_happ[train_end + timedelta(days=1):test_end]

order = (0,1,0)
seasonal_order = (0, 0, 1, 4)

rolling_predictions = test_data.copy()
for train_end in test_data.index:
    train_data = lim_world_happ[:train_end-timedelta(weeks=4)]
    model = SARIMAX(train_data, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit()

    pred = model_fit.forecast()
    rolling_predictions[train_end] = pred
rolling_residuals = test_data - rolling_predictions


plt.figure(figsize=(10,5))
st.subheader('Original Values')
st.line_chart(lim_world_happ)
st.subheader('Predicted Values')
st.line_chart(rolling_predictions)
plt.legend(('Data', 'Predictions'), fontsize=16)
plt.title('World Happiness Scores', fontsize=20)
plt.ylabel('Scores', fontsize=16)
for year in range(start_date.year,end_date.year):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)
st.markdown('Mean Absolute Percent Error:')
st.write(round(np.mean(abs(rolling_residuals/test_data)),4))
st.markdown('Root Mean Squared Error')
st.write(np.sqrt(np.mean(rolling_residuals**2)))
        
st.markdown('6 Month Prediction')
st.write(model_fit.forecast(6))
