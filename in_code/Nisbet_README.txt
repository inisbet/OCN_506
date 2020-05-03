######################################################################################

This README describes the processing of reading Traffic Data from a CSV, 
cleaning the data, and performing a Multinomial Logit Model ananlysis on 
certain factors in the data.

The files used in this workflow are saved under Documents/UW/CET521/Final_Project

The process has been broken down into different R files for different steps in the 
analysis process for ease of repeating certain steps if errors occur somewhere in the
process.

######################################################################################

*   US_Accidents_Dec19.csv contains the raw data obtained from an online database.
	It includes collision data from over 3,000,000 auto collisons from the US.

######################################################################################

* Nisbet_Sea_LA_data.R will read US_Accidents_Dec19.csv as the input and create a 
	data frame of the CSV data, including headers.It will then filter the raw 
	data to only include data from accidents that occured in a specific city,
	in this case it is Seattle and Los Angeles. It will save the resulting data
	frame to a CSV for future use.
Input: US_Accidents_Dec19.csv
Output: df_sea_la_raw.csv

There are about 45 columns of data in the raw CSV file. The original CSV file is 
	about 1 GB, so it takes a few minutes to load into R.

######################################################################################

* Project_SEA_LA_data.R will take the new CSV file and filter out data columns that we
	are not intersted in and columns or rows with many null values. Atter this has
	been completed, many multinomial logit models are ran for various factors we 
	are intersted in, and a final model is found by comparing the AIC values for 
	each model. Again, a csv is exported for a seperate R file for visualization
	of the data.
Input: df_sea_la_raw.csv
Output: df_sea_la_final.

This process cuts the data columns to about 20.

######################################################################################

* Project_SEA_LA_vis.R will take the final csv used for the multinomial logit model 
	and run a few lines of code to create plots and diagrams that show how the 
	different factors we were interested in interact with eachother, such as 
	temperature vs severity of crash.
Input: df_sea_la_final.csv
Output: multple jpeg files of data visuals

######################################################################################

Any updates to the original CSV file