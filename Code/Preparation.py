import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from plotly.offline import download_plotlyjs, plot, iplot
import streamlit as st

def path(data):
    return '/Users/c-losmc-c/Python Projects/Data/' + data



R_names = ['Argentina','Brazil','Chile','Colombia','Ecuador','Paraguay','Uruguay','Guyana','Suriname']
# Data is missing for the following countries in dataset: Bolivia, Peru, Venezuela, French Guiana

def plot_rate_S(df):
    plt.subplots(figsize=(15,8))
    df = df.groupby(['Country','year']).mean()
    try:
        for name in R_names:
            country = df.loc[name]['suicides/100k pop']
            plt.plot(country, label=name)
            plt.xticks(rotation = 45)
            plt.legend();
    except:
        pass
        
    return None

R_names_N = ['United States', 'Mexico', 'Canada', 'Guatemala', 'Nicaragua', 'Costa Rica', 'Panama', 'El Salvador', 'Belize']
# Data is missing for the following countries in dataset: Honduras

def plot_rate_N(df):
    plt.subplots(figsize=(15,8))
    df = df.groupby(['Country','year']).mean()
    try:
        for name in R_names_N:
            country =  df.loc[name]['suicides/100k pop']
            plt.plot(country, label=name)
            plt.xticks(rotation = 45)
            plt.legend();
    except:
        pass
        
    return None


names = ['Argentina','Brazil','Bolivia','Chile','Colombia','Ecuador','Peru','Venezuela','Paraguay','Uruguay','Guyana','Suriname','French Guiana']

def plot_happy_S(df):
    fig, ax = plt.subplots(figsize=(15,8))
    
    for name in names:
        country = df[df['Country'] == name].set_index('year')['Life Ladder']
        plt.plot(country, label=name)
        plt.xticks(rotation = 45)
        plt.legend();
    return None


names_N = ['United States', 'Mexico', 'Canada', 'Guatemala', 'Honduras', 'Nicaragua', 'Costa Rica', 'Panama', 'El Salvador']

def plot_happy_N(df):
    fig, ax = plt.subplots(figsize=(15,8))
    
    for name in names_N :
        country = df[df['Country'] == name].set_index('year')['Life Ladder']
        plt.plot(country, label=name)
        plt.xticks(rotation = 45)
        plt.legend();
    return None

def get_country_overview(country, df1, df2, df3):
    df1 = df1.groupby(['Country','year']).mean()
    
    df_1 = df1.loc[country]['suicides/100k pop']
    df_2 = df1.loc[country]['gdp_per_capita ($)']
    
    df_3 = df2[df2['Country'] == country].set_index('year')['Life Ladder']
    df_4 = df2[df2['Country'] == country].set_index('year')['Perceptions of corruption']
    df_5 = df2[df2['Country'] == country].set_index('year')['Freedom to make life choices']
    df_6 = df2[df2['Country'] == country].set_index('year')['Generosity']
    df_7 = df2[df2['Country'] == country].set_index('year')['Healthy life expectancy at birth']
    df_8 = df2[df2['Country'] == country].set_index('year')['Social support']
    
    df_9 = df3[df3.Country == country].set_index('year')
    df_10 = df_9[df_9.IndicatorName == 'Multilateral debt (% of total external debt)']['Value']
    df_11 = df_9[df_9.IndicatorName == 'Urban population growth (annual %)']['Value']
    df_12 = df_9[df_9.IndicatorName == 'Rural population growth (annual %)']['Value']
    df_13 = df_9[df_9.IndicatorName == 'Mobile cellular subscriptions (per 100 people)']['Value']/10
    df_14 = df_9[df_9.IndicatorName == 'Fixed broadband subscriptions (per 100 people)']['Value']
    df_15 = df_9[df_9.IndicatorName == 'Foreign direct investment, net inflows (% of GDP)']['Value']
    df_16 = df_9[df_9.IndicatorName == 'GNI per capita, Atlas method (current US$)']['Value']
    df_17 = df_9[df_9.IndicatorName == 'Primary education, duration (years)']['Value']
    df_18 = df_9[df_9.IndicatorName == 'Inflation, consumer prices (annual %)']['Value']
    df_19 = df_9[df_9.IndicatorName == 'Adequacy of social safety net programs (% of total welfare of beneficiary households)']['Value']
    df_20 = df_9[df_9.IndicatorName == 'Access to electricity (% of population)']['Value']
    df_21 = df_9[df_9.IndicatorName == 'People using at least basic drinking water services (% of population)']['Value']
    
    fig, ax = plt.subplots(figsize=(15,8))
    ax.plot(df_1, label='Suicide Rate', linewidth=3)
    ax.plot(np.sqrt(np.sqrt(df_2)), label='√GDP Per Capita')
    ax.plot(df_3, label='Happiness Score')
    ax.plot(np.sqrt(df_10), label='√Multilateral Dept')
    ax.plot(df_13, label='Mobile Subscriptions Scaled')
    ax.plot(df_14, label='Broadband Sub')
    ax.plot(df_15, label='Foreign Investment % of GDP')
    ax.plot(df_17, label='Primary Education')
    ax.plot(np.sqrt(df_18), label='√Inflation')
    ax.plot(np.sqrt(np.sqrt(df_20)), label='√Electricity Usage')
    
    
    print(f'Life Expectancy at Birth Average: {df_7.mean()}')
    print(f'Happiness Score Average (0-10): {df_3.mean()}')
    print(f'Suicide Rate Average Per 100K: {df_1.mean()}')
    print(f'Log GDP Per Capita Average: {mean([np.log(n) for n in df_2])}')
    print(f'Log GNI Per Capita Average: {mean([np.log(n) for n in df_16])}')
    print(f'Inflation Annual % Average: {df_18.mean()}')
    print(f'Foreign Investment % of GDP: {df_15.mean()}')
    print('-------------------------------------------')
    print(f'Perceptions of corruption: {df_4.mean()}')
    print(f'Freedom to make life choices: {df_5.mean()}')
    print(f'Generosity: {df_6.mean()}')
    print(f'Social Support: {df_8.mean()}')
    print(f'Rural Pop Growth % Average: {df_12.mean()}')
    print(f'Urban Pop Growth % Average: {df_11.mean()}')
    print(f'Social Safety Net Programs Adequacy Average: {df_19.mean()}')
    print(f'Access to Electricity): {df_20.mean()}')
    print(f'Access to Basic Water Services: {df_21.mean()}')
    plt.title(country + ' Overview', fontsize=20)
    plt.xticks(rotation = 45)
    plt.legend();
    
    return pd.DataFrame(df_1).merge(pd.DataFrame(df_2), how='outer', on='year').merge(pd.DataFrame(df_3), how='outer', on='year').merge(pd.DataFrame(df_4), how='outer', on='year').merge(pd.DataFrame(df_5), how='outer', on='year').merge(pd.DataFrame(df_6), how='outer', on='year').merge(pd.DataFrame(df_7), how='outer', on='year').merge(pd.DataFrame(df_8), how='outer', on='year').merge(pd.DataFrame(df_10), how='outer', on='year').rename(columns={'Value': 'Multilateral Dept'}).merge(pd.DataFrame(df_11), how='outer', on='year').rename(columns={'Value': 'Urban Pop Growth'}).merge(pd.DataFrame(df_12), how='outer', on='year').rename(columns={'Value': 'Rural Pop Growth'}).merge(pd.DataFrame(df_13), how='outer', on='year').rename(columns={'Value': 'Mobile Subscriptions'}).merge(pd.DataFrame(df_14), how='outer', on='year').rename(columns={'Value': 'Broadband Subscriptions'}).merge(pd.DataFrame(df_15), how='outer', on='year').rename(columns={'Value': 'Foreign Investment'}).merge(pd.DataFrame(df_16), how='outer', on='year').rename(columns={'Value': 'GNI Per Capita'}).merge(pd.DataFrame(df_17), how='outer', on='year').rename(columns={'Value': 'Primary Education'}).merge(pd.DataFrame(df_18), how='outer', on='year').rename(columns={'Value': 'Inflation'}).merge(pd.DataFrame(df_19), how='outer', on='year').rename(columns={'Value': 'Social Safety Net Programs'}).merge(pd.DataFrame(df_20), how='outer', on='year').rename(columns={'Value': 'Access to Electricity'}).merge(pd.DataFrame(df_21), how='outer', on='year').rename(columns={'Value': 'Basic Sanitation Services'})

def get_world_overview(df1, df2, df3):
    
    df_1 = df1[(df1['year'] >= 2005) & (df1['year'] <= 2017)].set_index(['Country','year'])['suicides/100k pop']
    df_2 = df1[(df1['year'] >= 2005) & (df1['year'] <= 2017)].set_index(['Country','year'])['gdp_per_capita ($)']

    df_3 = df2[(df2['year'] >= 2005) & (df2['year'] <= 2017)].set_index(['Country','year'])['Life Ladder']
    df_4 = df2[(df2['year'] >= 2005) & (df2['year'] <= 2017)].set_index(['Country','year'])['Perceptions of corruption']
    df_5 = df2[(df2['year'] >= 2005) & (df2['year'] <= 2017)].set_index(['Country','year'])['Freedom to make life choices']
    df_6 = df2[(df2['year'] >= 2005) & (df2['year'] <= 2017)].set_index(['Country','year'])['Generosity']
    df_7 = df2[(df2['year'] >= 2005) & (df2['year'] <= 2017)].set_index(['Country','year'])['Healthy life expectancy at birth']
    df_8 = df2[(df2['year'] >= 2005) & (df2['year'] <= 2017)].set_index(['Country','year'])['Social support']

    df_9 = df3[(df3['year'] >= 2005) & (df3['year'] <= 2017)].set_index(['Country','year'])
    df_10 = df_9[df_9.IndicatorName == 'Multilateral debt (% of total external debt)']['Value']
    df_11 = df_9[df_9.IndicatorName == 'Urban population growth (annual %)']['Value']
    df_12 = df_9[df_9.IndicatorName == 'Rural population growth (annual %)']['Value']
    df_13 = df_9[df_9.IndicatorName == 'Mobile cellular subscriptions (per 100 people)']['Value']
    df_14 = df_9[df_9.IndicatorName == 'Fixed broadband subscriptions (per 100 people)']['Value']
    df_15 = df_9[df_9.IndicatorName == 'Foreign direct investment, net inflows (% of GDP)']['Value']
    df_16 = df_9[df_9.IndicatorName == 'GNI per capita, Atlas method (current US$)']['Value']
    df_17 = df_9[df_9.IndicatorName == 'Primary education, duration (years)']['Value']
    df_18 = df_9[df_9.IndicatorName == 'Inflation, consumer prices (annual %)']['Value']
    df_19 = df_9[df_9.IndicatorName == 'Adequacy of social safety net programs (% of total welfare of beneficiary households)']['Value']
    df_20 = df_9[df_9.IndicatorName == 'Access to electricity (% of population)']['Value']
    df_21 = df_9[df_9.IndicatorName == 'People using at least basic drinking water services (% of population)']['Value']



    print(f'Life Expectancy at Birth Average: {df_7.mean()}')
    print(f'Happiness Score Average (0-10): {df_3.mean()}')
    print(f'Suicide Rate Average Per 100K: {df_1.mean()}')
    print(f'Log GDP Per Capita Average: {mean([np.log(n) for n in df_2])}')
    print(f'Log GNI Per Capita Average: {mean([np.log(n) for n in df_16])}')
    print(f'Inflation Annual % Average: {df_18.mean()}')
    print(f'Foreign Investment % of GDP: {df_15.mean()}')
    print('-------------------------------------------')
    print(f'Perceptions of corruption: {df_4.mean()}')
    print(f'Freedom to make life choices: {df_5.mean()}')
    print(f'Generosity: {df_6.mean()}')
    print(f'Social Support: {df_8.mean()}')
    print(f'Rural Pop Growth % Average: {df_12.mean()}')
    print(f'Urban Pop Growth % Average: {df_11.mean()}')
    print(f'Social Safety Net Programs Adequacy Average: {df_19.mean()}')
    print(f'Access to Electricity: {df_20.mean()}')
    print(f'Access to Basic Water Services: {df_21.mean()}')
    

    return pd.DataFrame(df_1).merge(pd.DataFrame(df_2), how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_3), how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_4),how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_5), how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_6), how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_7), how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_8), how='outer', on=(['Country','year'])).merge(pd.DataFrame(df_10), how='outer',  on=(['Country','year'])).rename(columns={'Value': 'Multilateral Dept'}).merge(pd.DataFrame(df_11), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Urban Pop Growth'}).merge(pd.DataFrame(df_12), how='outer',on=(['Country','year'])).rename(columns={'Value': 'Rural Pop Growth'}).merge(pd.DataFrame(df_13), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Mobile Subscriptions'}).merge(pd.DataFrame(df_14), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Broadband Subscriptions'}).merge(pd.DataFrame(df_15), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Foreign Investment'}).merge(pd.DataFrame(df_16), how='outer', on=(['Country','year'])).rename(columns={'Value': 'GNI Per Capita'}).merge(pd.DataFrame(df_17), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Primary Education'}).merge(pd.DataFrame(df_18), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Inflation'}).merge(pd.DataFrame(df_19), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Social Safety Net Programs'}).merge(pd.DataFrame(df_20), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Access to Electricity'}).merge(pd.DataFrame(df_21), how='outer', on=(['Country','year'])).rename(columns={'Value': 'Access to Improved Water'})   



def stationarity_check(TS):
    
    # Import adfuller
    from statsmodels.tsa.stattools import adfuller
    
    # Calculate rolling statistics
    roll_mean = TS.rolling(window=8, center=False).mean()
    roll_std = TS.rolling(window=8, center=False).std()
    
    # Perform the Dickey Fuller Test
    dftest = adfuller(TS)
    
    # Plot rolling statistics:
    fig = plt.figure(figsize=(12,6))
    plt.plot(TS, color='blue',label='Original')
    plt.plot(roll_mean, color='red', label='Rolling Mean')
    plt.plot(roll_std, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    # Print Dickey-Fuller test results
    print('Results of Dickey-Fuller Test: \n')

    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', 
                                             '#Lags Used', 'Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)
    
    return None

def get_country_overview2(country, df1, df2, df3):
    df1 = df1.groupby(['Country','year']).mean()
    
    df_1 = df1.loc[country]['suicides/100k pop']
    df_2 = df1.loc[country]['gdp_per_capita ($)']
    
    df_3 = df2[df2['Country'] == country].set_index('year')['Life Ladder']
    df_4 = df2[df2['Country'] == country].set_index('year')['Perceptions of corruption']
    df_5 = df2[df2['Country'] == country].set_index('year')['Freedom to make life choices']
    df_6 = df2[df2['Country'] == country].set_index('year')['Generosity']
    df_7 = df2[df2['Country'] == country].set_index('year')['Healthy life expectancy at birth']
    df_8 = df2[df2['Country'] == country].set_index('year')['Social support']
    
    df_9 = df3[df3.Country == country].set_index('year')
    df_10 = df_9[df_9.IndicatorName == 'Multilateral debt (% of total external debt)']['Value']
    df_11 = df_9[df_9.IndicatorName == 'Urban population growth (annual %)']['Value']
    df_12 = df_9[df_9.IndicatorName == 'Rural population growth (annual %)']['Value']
    df_13 = df_9[df_9.IndicatorName == 'Mobile cellular subscriptions (per 100 people)']['Value']/10
    df_14 = df_9[df_9.IndicatorName == 'Fixed broadband subscriptions (per 100 people)']['Value']
    df_15 = df_9[df_9.IndicatorName == 'Foreign direct investment, net inflows (% of GDP)']['Value']
    df_16 = df_9[df_9.IndicatorName == 'GNI per capita, Atlas method (current US$)']['Value']
    df_17 = df_9[df_9.IndicatorName == 'Primary education, duration (years)']['Value']
    df_18 = df_9[df_9.IndicatorName == 'Inflation, consumer prices (annual %)']['Value']
    df_19 = df_9[df_9.IndicatorName == 'Adequacy of social safety net programs (% of total welfare of beneficiary households)']['Value']
    df_20 = df_9[df_9.IndicatorName == 'Access to electricity (% of population)']['Value']
    df_21 = df_9[df_9.IndicatorName == 'People using at least basic drinking water services (% of population)']['Value']
    
    return pd.DataFrame(df_1).merge(pd.DataFrame(np.sqrt(np.sqrt(df_2))), how='outer', on='year').merge(pd.DataFrame(df_3), how='outer', on='year').merge(pd.DataFrame(df_4), how='outer', on='year').merge(pd.DataFrame(df_5), how='outer', on='year').merge(pd.DataFrame(df_6), how='outer', on='year').merge(pd.DataFrame(np.sqrt(df_7)), how='outer', on='year').merge(pd.DataFrame(df_8), how='outer', on='year').merge(pd.DataFrame(df_10), how='outer', on='year').rename(columns={'Value': 'Multilateral Dept'}).merge(pd.DataFrame(df_11), how='outer', on='year').rename(columns={'Value': 'Urban Pop Growth'}).merge(pd.DataFrame(df_12), how='outer', on='year').rename(columns={'Value': 'Rural Pop Growth'}).merge(pd.DataFrame(df_13), how='outer', on='year').rename(columns={'Value': 'Mobile Subscriptions'}).merge(pd.DataFrame(np.sqrt(df_14)), how='outer', on='year').rename(columns={'Value': 'Broadband Subscriptions'}).merge(pd.DataFrame(df_15), how='outer', on='year').rename(columns={'Value': 'Foreign Investment'}).merge(pd.DataFrame(np.sqrt(np.sqrt(df_16))), how='outer', on='year').rename(columns={'Value': 'GNI Per Capita'}).merge(pd.DataFrame(df_17), how='outer', on='year').rename(columns={'Value': 'Primary Education'}).merge(pd.DataFrame(df_18), how='outer', on='year').rename(columns={'Value': 'Inflation'}).merge(pd.DataFrame(df_19), how='outer', on='year').rename(columns={'Value': 'Social Safety Net Programs'}).merge(pd.DataFrame(np.sqrt(df_20)), how='outer', on='year').rename(columns={'Value': 'Access to Electricity'}).merge(pd.DataFrame(np.sqrt(df_21)), how='outer', on='year').rename(columns={'Value': 'Basic Sanitation Services'})