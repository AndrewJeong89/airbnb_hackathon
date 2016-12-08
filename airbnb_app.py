import flask
app = flask.Flask(__name__)

#-------- MODEL GOES HERE -----------#

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

data = pd.read_csv('/Users/amishdalal/airbnb_hackathon/airbnb_model.csv',index_col=0)
X1 = data.iloc[:,:5]
y1 = data['avg_price']

X1_train,X1_test,y1_train,y1_test = train_test_split(X1,y1, random_state = 25,test_size=0.33)

PREDICTOR = GradientBoostingRegressor(n_estimators=1000).fit(X1_train,y1_train)


#------ ROUTES GO HERE -------#
@app.route('/predict', methods=["GET"]) # Two main methods = "GET" & "POST"
def predict():
   month = flask.request.args['month']
   bedrooms = flask.request.args['bedrooms']
   number_of_reviews = flask.request.args['number_of_reviews']
   review_scores_rating = flask.request.args['review_scores_rating']
   neighborhood = flask.request.args['neighborhood']

   item = [month, bedrooms, number_of_reviews, review_scores_rating, neighborhood]
   score = PREDICTOR.predict(item)
   price = score[0]
   results = {'Average Price': price}
   return flask.jsonify(results)
   

#---------- CREATING AN API, METHOD 2 ----------------#

# This method takes input via an HTML page
@app.route('/page')
def page():
  with open("page.html", 'r') as viz_file:
      return viz_file.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
   '''Gets prediction using the HTML form'''
   if flask.request.method == 'POST':

      inputs = flask.request.form

      month = inputs['month'][0]
      #print month
      bedrooms = inputs['bedrooms'][0]
      #print bedrooms
      number_of_reviews = inputs['number_of_reviews'][0]
      #print number_of_reviews
      review_scores_rating = inputs['review_scores_rating'][0]
      #print review_scores_rating
      neighborhood = inputs['neighborhood'][0]
      #print neighborhood

      item = np.array([month, bedrooms, number_of_reviews, review_scores_rating, neighborhood])
      score = PREDICTOR.predict(item)
      price = round(score,2)
      results = {'Average Price': price}
      return flask.jsonify(results)

@app.route('/neighborhoods', methods=['POST', 'GET'])
def neighborhoods():
	'''Returns dataframe based on month and bedroom input'''
	if flask.request.method == 'POST':

		inputs = flask.request.form
        month = inputs['month'][0]
        bedrooms = inputs['bedrooms'][0]

        df = pd.read_csv('/Users/amishdalal/airbnb_hackathon/neighborhood_prices_2016')
        df = df[(df['month']==month) & (df['bedrooms']==bedrooms)].sort_values('median_price')
        
        return flask.jsonify(df)

if __name__ == '__main__':
    '''Connects to the server'''
    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)