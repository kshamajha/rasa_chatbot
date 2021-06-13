from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ZomatoData = pd.read_csv('zomato.csv', encoding = "ISO-8859-1")
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
SupportedCuisines = ['chinese', 'mexican', 'italian', 'american', 'south indian', 'north indian']
response_email =""

def RestaurantSearch(City,Cuisine,Budget):
	min_price=0
	max_price=99999
	if Budget == 'low':
		max_price = 299
	elif Budget == 'medium':
		min_price = 300
		max_price = 700
	elif Budget == 'high':
		min_price = 701
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two'].apply(lambda x: (x >= min_price) & (x <= max_price)))].sort_values(by=['Aggregate rating'], ascending=False).head(10)
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def ValidateLocation(loc):
	cities_lower=[x.lower() for x in WeOperate]
	return loc.lower() in cities_lower

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('price')
		print(F'Location is: {loc}, Cuisine is: {cuisine} and budget is: {budget}')
		results = RestaurantSearch(City=loc,Cuisine=cuisine, Budget=budget)
		response="Showing you top rated restaurants: \n\n"
		count=0
		if results.shape[0] == 0:
			restaurant_exist = False
			response= F"There are no restaurants found with City={loc},Cuisine={cuisine}, Price={budget}"
		else:
			restaurant_exist = True
			global response_email
			response_email = "Hi,\nTop Rated restaurants are as follows: \n\n"
			for restaurant in results.iloc[:10].iterrows():
				restaurant = restaurant[1]
				if count < 5:
					response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
				response_email=response_email + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
				count=count+1

		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc), SlotSet('cuisine',cuisine), SlotSet('price',budget), SlotSet('restaurant_exist', restaurant_exist)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		sender_email = 'zomatohelp0602@gmail.com'
		sender_pwd = 'zomato0602'
		location = tracker.get_slot('location')
		cuisine  = tracker.get_slot('cuisine')
		price  = tracker.get_slot('price')
		MailID = tracker.get_slot('mail_id')
		#Setup the MIME
		global response_email
		message = MIMEMultipart()
		message['From'] = sender_email
		message['To'] = MailID
		message['Subject'] = "Zomato Support: Top Resturant list for "  + " " + cuisine.capitalize() + " restaurants in " + str(location).capitalize()
		#The body and the attachments for the mail
		mail_content=response_email
		message.attach(MIMEText(mail_content, 'plain'))
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_email, sender_pwd) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_email, MailID, text)
		session.quit()
		response_email=''
		print('Email Sent successfully')
		return [SlotSet('mail_id',MailID)]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_loc'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		res = ValidateLocation(location)
		if res==False:
			dispatcher.utter_message("Sorry, we don’t operate in this city. Please specify some other location.")
		return [SlotSet('location_resp',res)]

class ActionCheckCuisine(Action):
	def name(self):
		return 'action_check_cuisine'

	def run(self, dispatcher, tracker, domain):
		res = True
		cuisine = tracker.get_slot('cuisine')
		if cuisine.lower() not in SupportedCuisines:
			res = False
			dispatcher.utter_message("Sorry, this cuisine is not supported by our Resturant list. Please specify some other cuisine.")
		return [SlotSet('cuisine_resp', res)]

class ActionCheckPrice(Action):
	def name(self):
		return 'action_check_price'

	def run(self, dispatcher, tracker, domain):
		res = True
		price = tracker.get_slot('price')
		if price.lower() not in ['low', 'medium', 'high']:
			res = False
			dispatcher.utter_message("Please provide a valid price.")
		return [SlotSet('price_resp', res)]
