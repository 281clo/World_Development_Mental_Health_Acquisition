# World_Development_Mental_Health_Acquisition

## Overview

The goal is to find contributing factors to mental health worldwide and make predictions on these features to see where the World Health Organization can divert reasorces to assist in the mental health of people worldwide. This project will primarily be focusing on North and South America as there are many contries with the contributing factors varying in complexity accross different cultures so utilizing a more focused approch will produce more accurate results to the countries in question. The data comes from multipule sorces.  Methods include combining datasets, preprocessing, testing significant features and predictive modeling. Results show some the significant features that affect suicide rates are multilateral debt, access to clean water and electricity, education. Recommendations would vary from country to country but ovarall recommendation is Universal Mental Health care, better adequacy of social safety net programs to those experiencing hardship. 


## Business Problem

Finding the contributing factors to suicide rates by country using, happiness scores, world development indicators and suicide rates from three different datasets. There is a vast amount of data contained in these datasets so the challange is going to be narrowing down which features to work with. With that we can use these features to combined with happiness scores and suicide rates to determine what leads to a happier population and how to reduce suicide rates. 


## Data Understanding

Multipule sorces of data, the first being from the World Bank containing over a thousand indicators of economic development worldwide. The second comes from the Gallup World Poll containing the World Happiness Report and is a survey of the state of global happiness. The last is a dataset contains the suicide rates by country referecned from United Nations Development Program, World Health Organization, and the World Bank. The two target variables are 'Life Ladder' (happiness score) from the World Happiness Report and 'suicides/100k pop' from the Suicide Rates dataset. The world development dataset is only being used as a reference to find contributing features to either suicide rates or happiness scores becuase it has over a thousand indicators by year. With these three datasets combined we 


## Methods

After cleaning, preprocessing, and combining our data, we start with a F_regressor to find the F-statistic and P-values of all our features compared to our target to find which features are most significant for our model. We then utilize Gradiant boost, and RandomForestRegressor to build a inferential model. 



## Results



***

Here is an example of how to embed images from your sub-folder:

### Visual 1
![graph1](./images/viz1.png)

## Conclusions

Mental health is a very complex subject but the conclusions the models concludes 


***

## For More Information

## Repository Structure


```

