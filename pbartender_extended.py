def drink_questions():
    questions = {
    'strong': "Do you like your drinks strong?", 
    'salty': "Do you like it with a salty tang?", 
    'bitter': "Do you like it bitter?", 
    'sweet': "Do you like it sweet?", 
    'fruity': "Do you like a fruity finish?"}
    print "\nHello " + users_name + ", What style of drink do you like:"
    preferences = {}
    for x in questions:
        print questions[x]
        user_answers = raw_input().lower()
        if user_answers == "yes" or user_answers == 'y':
            user_answers = True
        else:
            user_answers = False
        preferences[x] = user_answers
    return preferences  
    
def mixalogist():
    drink_contents = []
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}
    for x in ask_questions and ingredients: # Question: If these two dictionaries didnt have the same sequential keys then how?
        if ask_questions[x] == True:
            ask_questions[x] = random.choice(ingredients[x])
    for x in ask_questions:
        if ask_questions[x] != False:
            (drink_contents.append(ask_questions[x]))# Question: Does it matter if if statements do not have an elif or else statement to go with it?
    for v in drink_contents: ## took this idea from the sample code
        print "A " + v 
    #print "The drink contents are {}".format(drink_contents) Question: hos do we remove commas and parentheses when using this format?
    
def drink_name():
    list1 = ["Crazy", "Insane", "Fuzzy", "Buzzy", "Wuzzy"]
    list2 = ["Dog", "Bear", "Lion", "Tiger", "Hippo"]
    name = '"' + random.choice(list1) + ' ' + random.choice(list2) + '"'
    return name
    
if __name__ == '__main__':
    import random
    drinking = True
    dict_drinking_crowd = {}
    
    while drinking:
        print "Hi there, whats your name?"
        users_name = raw_input()
        returning_customer = users_name in dict_drinking_crowd
        
        if returning_customer == True:
            print "Hey there " + users_name + ", would you like your favorite drink?"
            im_back = raw_input().lower()
            if im_back == "yes" or im_back == "y":
                print "\nYour " + dict_drinking_crowd.values()[0] + " is now ready!\n" 
                
                sober = True
                while sober:
                    print "\n" + users_name + ", would you like another " + dict_drinking_crowd.values()[0] +"?"
                    drink_another = raw_input().lower()
                    if drink_another == "yes" or drink_another == "y":
                        print "\nYour " + dict_drinking_crowd.values()[0] + " is now ready!\n" 
                    elif drink_another != "yes" or drink_another != "y":
                        print "\nThanks for drinking along " + users_name + ", Have a niec day!\n" 
                        sober = False
                        
        elif returning_customer == False:
            dict_drinking_crowd[users_name] = drink_name()
            ask_questions = drink_questions() ## Call to the drink_questions function 
            print "\nYour drink is now ready!\n" 
            print "It's called the " + dict_drinking_crowd.values()[0]
            print dict_drinking_crowd
            print "\nYour drink contains:"
            mixalogist() ##call to the mixalogist function why does it work somietimes and somwtimes not when you add an argument?
            
            sober = True
            while sober:
                print "\n" + users_name + ", would you like another " + dict_drinking_crowd.values()[0] +"?"
                drink_another = raw_input().lower()
                if drink_another == "yes" or drink_another == "y":
                    print "\nYour " + dict_drinking_crowd.values()[0] + " is now ready!\n" 
                elif drink_another != "yes" or drink_another != "y":
                    print "\nThanks for drinking along " + users_name + ", Have a niec day!\n" 
                    sober = False
            
    
            
    
    
    
    
    
    


