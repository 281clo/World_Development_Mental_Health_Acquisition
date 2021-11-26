import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def path(data):
    
    return '/Users/c-losmc-c/Python Projects/Data/' + data

R_names = ['Argentina','Brazil','Chile','Colombia','Ecuador','Paraguay','Uruguay','Guyana','Suriname']
# Data is missing for the following countries in dataset: Bolivia, Peru, Venezuela, French Guiana

def plot_rate_S(df):
    plt.subplots(figsize=(20,10))
    
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
    plt.subplots(figsize=(20,10))
    
    try:
        for name in R_names_N:
            country = df.loc[name]['suicides/100k pop']
            plt.plot(country, label=name)
            plt.xticks(rotation = 45)
            plt.legend();
    except:
        pass
        
    return None


names = ['Argentina','Brazil','Bolivia','Chile','Colombia','Ecuador','Peru','Venezuela','Paraguay','Uruguay','Guyana','Suriname','French Guiana']

def plot_happy_S(df):
    fig, ax = plt.subplots(figsize=(20,10))
    
    for name in names:
        country = df[df['Country name'] == name].set_index('year')['Life Ladder']
        plt.plot(country, label=name)
        plt.xticks(rotation = 45)
        plt.legend();
    return None


names_N = ['United States', 'Mexico', 'Canada', 'Guatemala', 'Honduras', 'Nicaragua', 'Costa Rica', 'Panama', 'El Salvador', 'Belize']

def plot_happy_N(df):
    fig, ax = plt.subplots(figsize=(20,10))
    
    for name in names_N :
        country = df[df['Country name'] == name].set_index('year')['Life Ladder']
        plt.plot(country, label=name)
        plt.xticks(rotation = 45)
        plt.legend();
    return None