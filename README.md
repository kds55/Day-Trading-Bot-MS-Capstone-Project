# Day-Trading-Bot-MS-Capstone-Project

Summary:
This project represents a model built to day trade the stock markets. It uses extensive data feature creation and machine learning to predict the stock market direction over short periods of times.
It then uses this indicator to determine entry and exit points to produce a profit in the market.

See "DTSC 691 - Day Trading Bot" notebook for the code and all documentation over the project.
See "Project Overview" to get a condensed summary of the project.

General Notes:
Flask user interface folder is missing the saved models to run it. This is due to certain models being too large to store on here. 
As such if you wan't to run the interface you will need to re-run the notebook and save the models.
Note due to the size of the data, this will likely take several hours at least.

Project Intro:
The stock market has been around for decades and has proven to be an enormous opportunity 
for generating wealth. Through the years data has been maintained on all the transactions that 
have occurred, generally summarized in time intervals (Ex yearly, monthly, daily). The markets 
themselves consist of trending markets, whether that is upwards, sideways or downwards. 
Given these trends and the significant amount of data available I am hoping to build a 
supervised machine learning model to predict the direction of the overall stock market. By 
overall stock market I am referring to the S&P 500 and more specifically the ES (S&P 500 mini 
futures). While the data maintained for the basics of the stock market is fairly simple, I believe 
with strong feature engineering it will be possible to create a model to take advantage of this 
opportunity.

To take it a step further, not only do I want to predict the direction of the stock market but I 
want to determine if you should buy, and subsequently what price you should sell at. To do so a 
strategy will need to be developed for when to enter and exit the market. The base strategy will 
include the market direction prediction from the machine learning model as well as a few other 
criteria and filters. Additionally, 3 key price points will need to be determined for the strategy 
(Note that these prices will be determined using a general algorithm and not machine learning):
1) The price to enter the market 
2) The price to exit the market if your position is winning (Referred to as the "target")
3) The price to exit the market if your position is losing (Referred to as the "stop").
4) 
By determining these price points, the hope is to build an application that will determine if you 
should enter into the market at any given time to generate a profit. Due to this using intraday 
data (see below in data description) the trades will be short term, likely opened and closed 
within an hour.

In other words, with the above information I hope to create a bot that will be able to day trade 
the market. I believe this will be beneficial as it will help empower the individuals to make 
consistent profits off the market, without being reliant on a trained professional broker.
