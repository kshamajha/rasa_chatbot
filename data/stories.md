## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "kshama0602@gmail.com"}
    - slot{"mail_id": "kshama0602@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "kshama0602@gmail.com"}
    - utter_email_sent
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "American"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_4
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "sjfasfasf"}
    - slot{"location": "sjfasfasf"}
    - action_check_loc
    - slot{"location_resp": false}
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "friendskshama@gmail.com"}
    - utter_email_sent
* goodbye
    - utter_goodbye

## interactive_story_5
* restaurant_search{"cuisine": "Mexican", "location": "Bangalore"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": false}
    - utter_more_help
* affirm
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email{"mail_id": "kshama0602@gmail.com"}
    - slot{"mail_id": "kshama0602@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "kshama0602@gmail.com"}
    - utter_email_sent

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_loc
    - slot{"location_resp": false}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email{"mail_id": "xyz@sth.edu"}
    - slot{"mail_id": "xyz@sth.edu"}
    - action_send_mail
    - slot{"mail_id": "xyz@sth.edu"}
    - utter_email_sent

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email{"mail_id": "ahbcdj@dkj.com"}
    - slot{"mail_id": "ahbcdj@dkj.com"}
    - action_send_mail
    - slot{"mail_id": "ahbcdj@dkj.com"}
    - utter_email_sent

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_loc
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": false}

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "low"}
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"mail_id": "jddk.2jmd@kdl.co.in"}
    - slot{"mail_id": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - slot{"mail_id": "jddk.2jmd@kdl.co.in"}
    - utter_email_sent

## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_loc
    - slot{"location_resp": false}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"price": "low"}
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"mail_id": "jddk.2jmd@kdl.co.in"}
    - slot{"mail_id": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - slot{"mail_id": "jddk.2jmd@kdl.co.in"}
    - utter_email_sent

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Chandigarh"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Chandigarh"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_13
* restaurant_search{"price": "low", "cuisine": "Chinese", "location": "Nashik"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "low"}
    - slot{"location": "Nashik"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "rahuldua.aec@gmail.com"}
    - slot{"mail_id": "rahuldua.aec@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "rahuldua.aec@gmail.com"}
    - utter_email_sent

## interactive_story_14
* stop
    - utter_default

## interactive_story_15
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": false}
* goodbye
    - utter_goodbye

## interactive_story_16
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Gurgaon"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "friendskshama@gmail.com"}
    - utter_email_sent

## interactive_story_17
* restaurant_search{"price": "medium", "location": "Mangalore"}
    - slot{"price": "medium"}
    - slot{"location": "Mangalore"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Mangalore"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "friendskshama@gmail.com"}
    - utter_email_sent

## interactive_story_18
* restaurant_search{"price": "high", "cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_location
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_search_restaurants
    - slot{"location": "Shimla"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"cuisine": "American"}
    - slot{"price": "low"}
* affirm
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"cuisine": "American"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "friendskshama@gmail.com"}
    - utter_email_sent

## interactive_story_21
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## interactive_story_22
* restaurant_search{"price": "medium", "location": "Chennai"}
    - slot{"price": "medium"}
    - slot{"location": "Chennai"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"location": "Faridabad", "price": "medium"}
    - slot{"price": "medium"}
    - slot{"location": "Faridabad"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Faridabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "test@test.co.in"}
    - slot{"mail_id": "test@test.co.in"}
    - action_send_mail
    - slot{"mail_id": "test@test.co.in"}
    - utter_email_sent
* goodbye
    - utter_goodbye

## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Mysore"}
    - slot{"price": "high"}
    - slot{"location": "Mysore"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "North Indian", "location": "Chandigarh"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "low"}
    - slot{"location": "Chandigarh"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_26
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "American"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"location": "gorakhpur"}
    - slot{"location": "gorakhpur"}
    - action_check_loc
    - slot{"location_resp": false}

## interactive_story_28
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_loc
    - slot{"location_resp": false}

## interactive_story_29
* restaurant_search{"location": "Roorkee"}
    - slot{"location": "Roorkee"}
    - action_check_loc
    - slot{"location_resp": false}

## interactive_story_30
* greet
    - utter_greet
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "friendskshama@gmail.com"}
    - utter_email_sent
* affirm
    - utter_goodbye

## interactive_story_32
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "Pune"}
    - slot{"price": "low"}
    - slot{"location": "Pune"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": false}
* goodbye
    - utter_goodbye

## interactive_story_33
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email
* affirm
    - utter_goodbye

## interactive_story_34
* stop
    - utter_default

## interactive_story_35
* greet
    - utter_greet
* stop
    - utter_default

## interactive_story_36
* greet
    - utter_greet
* stop
    - utter_default
* stop
    - utter_default

## interactive_story_37
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_loc
    - slot{"location_resp": false}
* restaurant_search{"location": "delghi"}
    - slot{"location": "delghi"}
    - action_check_loc
    - slot{"location_resp": false}
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "sdhjfhgdsf"}
    - slot{"cuisine": "sdhjfhgdsf"}
    - action_check_cuisine
    - slot{"cuisine_resp": false}
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "fddfdf"}
    - slot{"price": "fddfdf"}
    - action_check_price
    - slot{"price_resp": false}
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_38
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "dfhdsjhfds"}
    - slot{"cuisine": "dfhdsjhfds"}
    - action_check_cuisine
    - slot{"cuisine_resp": false}
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "fdfffdf"}
    - slot{"price": "fdfffdf"}
    - action_check_price
    - slot{"price_resp": false}
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "friendskshama@gmail.com"}
    - slot{"mail_id": "friendskshama@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "friendskshama@gmail.com"}
    - utter_email_sent

## interactive_story_39
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "bhjj"}
    - slot{"cuisine": "bhjj"}
    - action_check_cuisine
    - slot{"cuisine_resp": false}
* restaurant_search{"cuisine": "jhhh"}
    - slot{"cuisine": "jhhh"}
    - action_check_cuisine
    - slot{"cuisine_resp": false}
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email

## interactive_story_40
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "dsdsd"}
    - slot{"cuisine": "dsdsd"}
    - action_check_cuisine
    - slot{"cuisine_resp": false}
* restaurant_search{"cuisine": "bhhjj"}
    - slot{"cuisine": "bhhjj"}
    - action_check_cuisine
    - slot{"cuisine_resp": false}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email
* goodbye
    - utter_goodbye

## interactive_story_41
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "Mexican", "location": "New Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "low"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email{"mail_id": "kshama0602@gmail.com"}
    - slot{"mail_id": "kshama0602@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "kshama0602@gmail.com"}
    - utter_email_sent

## interactive_story_42
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "Mexican", "location": "New Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "low"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email
* goodbye
    - utter_goodbye

## interactive_story_43
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "Nashik"}
    - slot{"price": "low"}
    - slot{"location": "Nashik"}
    - action_check_loc
    - slot{"location_resp": true}
    - action_check_price
    - slot{"price_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - slot{"cuisine": "American"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": false}
* goodbye
    - utter_goodbye

## interactive_story_44
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "low"}
    - slot{"restaurant_exist": false}

## interactive_story_45
* greet
    - utter_greet
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "high"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"mail_id": "test@email.co.in"}
    - slot{"mail_id": "test@email.co.in"}
    - action_send_mail
    - slot{"mail_id": "test@email.co.in"}
    - utter_email_sent

## interactive_story_46
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* stop
    - utter_default
* stop
    - utter_default

## interactive_story_47
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* stop
    - utter_default
* stop
    - utter_default
* stop
    - utter_default
* stop
    - utter_default
* stop
    - utter_default
* stop
    - utter_default
* stop
    - utter_default
* stop
    - utter_default

## interactive_story_48
* greet
    - utter_greet
* restaurant_search{"location": "gwalior"}
    - slot{"location": "gwalior"}
    - action_check_loc
    - slot{"location_resp": false}
* goodbye
    - utter_goodbye

## interactive_story_49
* greet
    - utter_greet
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_check_loc
    - slot{"location_resp": false}
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_check_price
    - slot{"price_resp": true}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "medium"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* donot_send_email
    - utter_do_not_sent_email
* goodbye
    - utter_goodbye

## interactive_story_50
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye

## interactive_story_51
* greet
    - utter_greet
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_loc
    - slot{"location_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine_resp": true}
    - utter_ask_price
* goodbye
    - utter_goodbye
