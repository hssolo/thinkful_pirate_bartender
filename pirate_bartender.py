def drink_questions():
    questions = {
    'strong': "Do you like your drinks strong?", 
    'salty': "Do you like it with a salty tang?", 
    'bitter': "Do you like it bitter?", 
    'sweet': "Do you like it sweet?", 
    'fruity': "Do you like a fruity finish?"}
    
    print "\nWhat style of drink do you like?"

    preferences = {}
    for x in questions:
        print questions[x]
        user_questions = raw_input().lower()
        if user_questions == "yes" or user_questions == 'y':
            user_questions = True
        else:
            user_questions = False
        preferences[x] = user_questions
    return preferences  
    
def mixalogist():
    import random
    u_preferences = drink_questions()
    drink_contents = []
    
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}

    for x in u_preferences and ingredients: # Question: If these two dictionaries didnt have the same sequential keys then how?
        if u_preferences[x] == True:
            u_preferences[x] = random.choice(ingredients[x])
    for x in u_preferences:
        if u_preferences[x] != False:
            (drink_contents.append(u_preferences[x]))
            
    print "\nYour drink is ready!\n" 
    print "Your drink contains:"
    for v in drink_contents: ## took this idea from the sample code
        print "A " + v 
    #print "The drink contents are {}".format(drink_contents)
    
if __name__ == '__main__':
    drinking = True
    while drinking:
        mixalogist()
        drink_another = raw_input("\nWould you like another?\n").lower()
        if drink_another == "yes" or drink_another == "y":
            drinking = True
        else:
            drinking = False
    print "\nThanks for drinking along, Shall I call you a cab?" 
            
    
    


