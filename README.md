# airbnb_hackathon

## Summary

This repo looks at airbnb listings and calendars from [insideairbnb.com](http://insideairbnb.com/get-the-data.html). Converting the calendar scrapes from days to month and imputing average monthly prices per listing, a dynamic pricing model is performed using Gradient Boosting using sklearn library in Python. The user inputs the following variables: month, number of bedrooms, neighborhood, number of reviews, and rating. These are the inputs into the pricing model. The result is the expected price from the model. 

Based on the month and bedroom inputs, the min, max, median, and mean neighborhood prices are also calculated, giving the user prices for other neighborhoods. Adding in neighborhood input, the listings for all three inputs (month, bedroom, neighborhood) are shown.

Please see the airbnb_app.py file to see how flask routing. The airbnb_pricing_model_2016.csv is the data for the algorithm, while neighborhood_prices_2016.csv is for the neighborhood average prices, and listings_agg.csv is the listings for the month,bedrooms, and neighborhood inputs.

The following people collaborated on this project:
* Tenzin Changchup - Web Development
* Nico Cucciniello - Web Development
* Amish Dalal - Data Science
* Donald Highe - Web Development
* [Andrew Jeong - Data Science](https://github.com/AndrewJeong89)
* Samuel Na - Web Development
* Janelle Rosario - Web Development



