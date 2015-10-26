def drink_questions():
    questions = {
    'strong': "Do you like your drinks strong?", 
    'salty': "Do you like it with a salty tang?", 
    'bitter': "Do you like it bitter?", 
    'sweet': "Do you like it sweet?", 
    'fruity': "Do you like a fruity finish?"}
    print "\nHello " + user_name + ", What style of drink do you like:"
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
            (drink_contents.append(ask_questions[x]))
    for v in drink_contents: 
        print "A " + v 
    
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
        user_name = raw_input().lower()
        returning_customer = user_name in dict_drinking_crowd
        
        if returning_customer == True:
            print "\nWelcome back " + user_name + ", would you like your favorite drink?"
            im_back = raw_input().lower()
            print dict_drinking_crowd.values()
            if im_back == "yes" or im_back == "y":
                print "\nYour " + dict_drinking_crowd[user_name] + " is now ready!\n" 
                
                sober = True
                while sober:
                    print "\n" + user_name + ", would you like another " + dict_drinking_crowd[user_name] +"?"
                    drink_another = raw_input().lower()
                    if drink_another == "yes" or drink_another == "y":
                        print "\nYour " + dict_drinking_crowd[user_name] + " is now ready!\n" 
                    elif drink_another != "yes" or drink_another != "y":
                        print "\nThanks for drinking along " + user_name + ", Have a niec day!\n" 
                        sober = False
                        
        elif returning_customer == False:
            dict_drinking_crowd[user_name] = drink_name()
            ask_questions = drink_questions() 
            print "\nYour drink is now ready!\n" 
            print "testing"
            print user_name +'\n'
            print "It's called the " + dict_drinking_crowd[user_name] ##broken need help
            print dict_drinking_crowd
            print "\nYour drink contains:"
            mixalogist() 
            
            sober = True
            while sober:
                print "\n" + user_name + ", would you like another " + dict_drinking_crowd[user_name] +"?" ##broken need help
                drink_another = raw_input().lower()
                if drink_another == "yes" or drink_another == "y":
                    print "\nYour " + dict_drinking_crowd[user_name] + " is now ready!\n" 
                elif drink_another != "yes" or drink_another != "y":
                    print "\nThanks for drinking along " + user_name + ", Have a niec day!\n" 
                    sober = False
            
    
            
    
    
    
    
    
    


