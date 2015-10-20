def drink_questions():
    questions = {
    'strong': "Do you like your drinks strong?", 
    'salty': "Do you like it with a salty tang?", 
    'bitter': "Do you like it bitter?", 
    'sweet': "Do you like it sweet?", 
    'fruity': "Do you like a fruity finish?"}
    
    print "\nHello " + user_name + ", What style of drink do you like?"

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
    #import random
    user_preferences = drink_questions()
    drink_contents = []
    
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}

    for x in user_preferences and ingredients: # Question: If these two dictionaries didnt have the same sequential keys then how?
        if user_preferences[x] == True:
            user_preferences[x] = random.choice(ingredients[x])
    for x in user_preferences:
        if user_preferences[x] != False:
            (drink_contents.append(user_preferences[x]))
        # Question: Does it matter if if statements do not have an elif or else statement to go with it?
            
    print "\nYour drink is now ready!\n" 
    print "It's called the " + drink_name()
    print "\nYour drink contains:"
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
    user_name = raw_input("Hi there, whats your name?\n")
    while drinking:
        mixalogist()
        drink_another = raw_input("\n" + user_name + ", Would you like another?\n").lower()
        if drink_another == "yes" or drink_another == "y":
            drinking = True
        else:
            drinking = False
    print "\nThanks for drinking along " + user_name + ", Shall I call you a cab?" 
            
    
    


