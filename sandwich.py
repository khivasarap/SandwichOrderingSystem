# Sandwich Ordering System
import re
from re import search
import copy


class Sandwich:
    def __init__(self, name, bread, spread, ingredients=[], options=[],exceptions=[]):
        self.name = name
        self.bread = bread
        self.spread = spread
        self.ingredients = ingredients
        self.options = options
        self.exceptions = exceptions
        if  self.ingredients is not None and self.spread is not None and self.bread is not None:
            if self.options is not None:
                self.description = "\n"+self.name.title()+": contains "+ self.bread + " bread with ingredients "+', '.join(self.ingredients)+ " and spread as "+ self.spread  +" and options as "+ ', '.join(self.options)
            else:
                self.description = "\n"+self.name.title()+": contains "+ self.bread + " bread with ingredients "+', '.join(self.ingredients)+ " and spread as "+ self.spread
        else:
            self.description = ""
        if self.exceptions is not None:
            self.description = self.description + "along with following exceptions "+ ', '.join(self.exceptions)

    def update_description(self):
        if self.options:
            desc = "\n"+self.name.title()+": contains " + self.bread + " bread with ingredients "+', '.join(self.ingredients)+ " and spread as "+ self.spread + " and options as "+ ', '.join(self.options)
        else:
            desc = "\n"+self.name.title()+": contains " + self.bread + " bread with ingredients "+', '.join(self.ingredients)+ " and spread as "+ self.spread 
        if self.exceptions:
            desc = desc + " along with following exceptions "+ ', '.join(self.exceptions)
        return desc

    def print_reciept(self):
        print("\n\t*******************Receipt*********************\t\n")
        print("\tName of the sandwich:\t", self.name.title())
        print("\n\tUsual ingredients:\t"+', '.join(self.ingredients))
        print("\n\tBread-type:\t",self.bread.title())
        print("\n\tSpreads:\t",self.spread.title())
        if self.options:
            print("\n\tOptions:\t"+', '.join(self.options))
        else:
            print("\n\tOptions:\tNone")
        if self.exceptions:
            print("\n\tExceptions:\t"+', '.join(self.exceptions))
        else:
            print("\n\tExceptions:\tNone")


    def sanitize(self):
        if self.ingredients and self.exceptions:
            exp = self.ingredients
            for e in exp:
                if e.lower() in self.exceptions:
                    self.exceptions.remove(e.lower())
        if self.bread and self.exceptions:
            exp = self.bread
            if exp.lower() in self.exceptions:
                self.exceptions.remove(exp.lower())
        if self.spread and self.exceptions:
            exp = self.spread
            if exp.lower() in self.exceptions:
                self.exceptions.remove(exp.lower())

    def display_description(self):
        self.description = self.update_description()
        print(self.description) 
    
    def display_bread_choice(self):
        print("This sandwich ", self.name.title()," will come with ", self.bread, "bread \n") 
    
    def display_spread_choice(self):
        print("This sandwich ", self.name.title()," will come with spread as ", self.spread, "\n") 
    
    def display_ingredients(self):
        print("This sandwich ", self.name.title()," contains "+', '.join(self.ingredients)+"\n") 

    def display_options(self):
        if self.options:
            print("This sandwich ", self.name.title()," will come with "+', '.join(self.options)+ "\n")
        # else:
        #     print("No options chosen for the sandwich\n")
    
    def build_custom_sandwich(self, bread, spread, ingredients):
        __init__(self, bread, spread, ingredients)

    
    def check_if_sandwich(self):
        if not self.bread or not verification['bread']:
            self.rechoose_bread(None)
        if not self.spread or not verification['spread']:
            self.rechoose_spread(None)
        if not self.ingredients:
            self.rechoose_ingredient()
        self.display_description()
            
    #Process exceptions
    def process_exceptions(self):
        if self.exceptions:
            exception = self.exceptions
            for value in exception:
                if check_if_ingredient(value):
                    verification['ingredients']= False
                    self.replace_ingredient(value, "remove")
                elif check_if_spread(value):
                    verification['spread']= False
                    self.replace_spread(value, "remove")
                elif check_if_bread(value):
                    verification['bread']= False
                    self.replace_bread(value, "remove")



    #Process add ons
    def process_add_ons(self,add_ons):
        if add_ons:
            for value in add_ons:
                if value in ingredients and value not in self.ingredients or not self.ingredients:
                    self.ingredients.append(value)
                if value in options:
                    if not self.options:
                        self.options = [value]
                    elif value not in self.options:
                        self.options.append(value)
                if value in bread_options:
                    self.bread = value
                    verification['bread'] = True
                if value in spread_options:
                    self.spread = value
                    verification['spread'] = True


    def replace_spread(self,value,option):
        print("\nYou have requested to remove "+value+" from sandwich.\n")
        if not self.spread.lower() == value.lower():
            self.rechoose_spread(None) #Let the user rechoose
        else:
            self.spread=value.strip().lower()
            verification['spread'] =True

    def replace_bread(self, value,option):
        print("\nYou have requested to remove "+value+" bread from sandwich.\n")
        if not self.bread.lower() == value.lower():
            self.rechoose_bread(None) #Let the user rechoose
        else:
            self.bread=value.strip().lower()
            verification['bread'] =True

    def rechoose_bread(self,choice):
        self.display_bread_choice() 
        choice = input("Press 'return' to accept this choice of bread, or choose one of the other alternatives: 1. wheat, 2. rye, 3.italian, 4. french\n")
        choice = replace_words(choice)
        if choice == 'return' or choice == "":
            verification['bread'] =True
            self.make_complete_sandwich()
        elif choice == '1' or choice == "wheat" and self.bread != "wheat":
            verification['bread'] =True
            self.bread = "wheat"
            self.description = self.update_description()
            self.make_complete_sandwich()
        elif choice == '2' or choice == "rye" and self.bread != "rye":
            verification['bread'] =True
            self.bread = "rye"
            self.description = self.update_description()
            self.make_complete_sandwich()
        elif choice == '3' or choice == "italian" and self.bread != "italian":
            verification['bread'] =True
            self.bread = "italian"
            self.description = self.update_description()
            self.make_complete_sandwich()
        elif choice == '4' or choice == "french" and self.bread != "french":
            verification['bread'] =True
            self.bread = "french"
            self.description = self.update_description()
            self.make_complete_sandwich()
        else:
            print("No bread modified or Invalid bread selected\n")
            self.display_bread_choice() 
            rechoose_bread = input("Press 'return' to accept this choice of bread, or choose one of the other alternatives: 1. wheat, 2. rye, 3.italian, 4.french\n")
            self.rechoose_bread(rechoose_bread)
        

    # If any mandatory value is missing (bread, spread, name or ingredients); Let the user rechoose.
    def make_complete_sandwich(self):
        for key in verification.keys():
            if verification[key] == False:
                if key == "bread":
                    self.rechoose_bread(None)
                if key == "spread":
                    self.rechoose_spread(None)
                if key == "name":
                    print('We didn\'t find any choice you entered. Please choose from the below menu')
                    display_menu()
                    choose = input("Enter the name of the sandwich you would like to have:")
                    validate_user_input(choose)
                if key == "ingredients":
                    self.rechoose_ingredient()

    def rechoose_spread(self, choice):
        self.display_spread_choice()
        if not choice:
            choice = input("Press 'return' to accept this choice of spread, or choose one of the other alternatives: 1. mayonnaise (mayo), 2. mustard, 3.salsa-sauce, 4. butter.\n")
        choice = replace_words(choice)
        if choice == 'return' or choice == "":
            verification['spread'] = True
            self.make_complete_sandwich()
        elif choice == '1' or choice == 'mayonnaise' or choice == 'mayo' and self.spread != 'wheat':
            verification['spread'] = True
            self.spread = "mayonnaise"
            self.description = self.update_description()
            self.make_complete_sandwich()
        elif choice == '2' or choice == 'mustard' and self.spread != 'mustard':
            verification['spread'] = True
            self.spread = "mustard"
            self.description = self.update_description()
            self.make_complete_sandwich()
        elif choice == '3' or choice == 'salsa-sauce' and self.spread != 'salsa-sauce':
            verification['spread'] = True
            self.spread = "salsa-sauce"
            self.description = self.update_description()
            self.make_complete_sandwich()
        elif choice == '4' or choice == 'butter' and self.spread != 'butter':
            verification['spread'] = True
            self.spread = "butter"
            self.description = self.update_description()
            self.make_complete_sandwich()
        else:
            print("No spread modified or Invalid sread selected\n")
            self.rechoose_spread(None)
        

    def replace_option(self, value, option):
        if option == 'add' and not self.options:
            self.options = [value]
        if option == 'remove' and not self.options:
            self.options = [value]
        if option == "add" and value not in self.options:
            self.options.append(value)
        if option == "remove" and value in self.options:
            self.options.remove(value)

    def add_options(self):
        choice =  input("\nFollowing options are available. Choose to add options:[ grilled, toasted, extra cheese, salt and pepper] \n Press 'return' to make no addition\n")
        option = "add"
        if "grilled" in choice: 
            self.replace_option("grilled",option)
        if "toasted" in choice: 
            self.replace_option("toasted",option)
        if "extra cheese" in choice: 
            self.replace_option("extra cheese",option)
        if "salt and pepper" in choice: 
            self.replace_option("salt and pepper",option)
        if choice == "return" or choice == "":
            self.rechoose_options() # To let user add or remove more

    def remove_options(self):
        if self.options:
            choice =  input("\nFollowing options are available. Choose to remove from: "+ ',',join(self.options)+"\n Press 'return' to make no removals\n")
            option = "remove"
            if not (choice == "return" or choice == ""):
                if "grilled" in choice: 
                    self.replace_option("grilled",option)
                if "toasted" in choice: 
                    self.replace_option("toasted",option)
                if "extra cheese" in choice: 
                    self.replace_option("extra cheese",option)
                if "salt and pepper" in choice: 
                    self.replace_option("salt and pepper",option)
            if choice == "return" or choice =="":
                self.rechoose_options() # To let user add or remove more
        else:
            print('\nNo options available')

    def rechoose_options(self):
        self.display_options()
        if self.options:
            choice = input("\nFollowing options are available.\n [ grilled, toasted, extra cheese, salt and pepper]\nPress 'return' to accept this choice of options "+', '.join(self.options)+ " or press 1. to add 2. to remove. \n")
        else:
            choice = input("\nNo options selected as of now. Following options are available.\n [ grilled, toasted, extra cheese, salt and pepper]\n Press 'return' to accept no choice of options or press 1. to add 2. to remove. \n")
        if choice == "1":
            self.add_options()
        elif choice == "2":
            self.remove_options()
        elif (choice == "return" or choice == ""): return
        else:
            print("No modifications made\n")
            self.rechoose_options()

    def replace_ingredient(self, value, option):
        if option == "add" and value not in self.ingredients:
            self.ingredients.append(value)
        if option == "remove" and value in self.ingredients:
            self.ingredients.remove(value)

    def add_ingredients(self):
        choice = input("\nFollowing ingredients are available. Choose to add new ingredients:\n [ onion , garlic , Swiss cheese, avocado, lettuce, olives, tomato, carrot, cucumber, chicken, bacon] \n Press 'return' to make no addition\n")
        option = "add"
        if not (choice == 'return' or choice == ""):
            if "onion" in choice: self.replace_ingredient("onion",option)
            if "garlic" in choice: self.replace_ingredient("garlic",option)
            if "Swiss cheese" in choice: self.replace_ingredient("Swiss cheese",option)
            if "avocado" in choice: self.replace_ingredient("avocado",option)
            if "lettuce" in choice: self.replace_ingredient("lettuce",option)
            if "olives" in choice: self.replace_ingredient("olives",option)
            if "tomato" in choice: self.replace_ingredient("tomato",option)
            if "carrot" in choice: self.replace_ingredient("carrot",option)
            if "cucumber" in choice: self.replace_ingredient("cucumber",option)
            if "chicken" in choice: self.replace_ingredient("chicken",option) 
            if "bacon" in choice: self.replace_ingredient("bacon",option)        
            self.description = self.update_description()
            self.rechoose_ingredient()

    def remove_ingredients(self):
        if self.ingredients:
            choice = input("\nFollowing ingredients are available on Sandwich. Choose to remove ingredients:\n"+','.join(self.ingredients)+ "\n Press 'return' to make no removals\n")
            option = "remove"
            if not (choice == 'return' or choice == ""):
                if "onion" in choice: self.replace_ingredient("onion",option)
                if "garlic" in choice: self.replace_ingredient("garlic",option)
                if "Swiss cheese" in choice: self.replace_ingredient("Swiss cheese",option)
                if "avocado" in choice: self.replace_ingredient("avocado",option)
                if "lettuce" in choice: self.replace_ingredient("lettuce",option)
                if "olives" in choice: self.replace_ingredient("olives",option)
                if "tomato" in choice: self.replace_ingredient("tomato",option)
                if "carrot" in choice: self.replace_ingredient("carrot",option)
                if "cucumber" in choice: self.replace_ingredient("cucumber",option)
                if "chicken" in choice: self.replace_ingredient("chicken",option)
                if "bacon" in choice: self.replace_ingredient("bacon",option)       
                self.description = self.update_description()
                self.rechoose_ingredient()
        else:
            print('\nNo ingredients to remove')

    def rechoose_ingredient(self):
        self.display_ingredients() 
        choice = input("Press 'return' to accept this choice of ingredients, or press 1. to add 2. to remove.\n")
        if choice == 'return' or choice == "":
            verification['ingredients'] = True
            self.display_description()
        elif choice == "1":
            self.add_ingredients()
        elif choice == "2":
            self.remove_ingredients()
        else:
            print("No ingredients modified\n")
            self.rechoose_ingredient()
        self.rechoose_options()

def build_native_sandwich(option):
    if option.lower() == "Pooja's Veggie Special".lower():
        return Sandwich(bread="French",name = option, spread="mayonnaise",ingredients=['Swiss cheese','tomato', 'lettuce', 'onion', 'carrot','cucumber'], options = None)
    elif option.lower() == "Mustard Chicken Teriyaki".lower():
        return Sandwich(bread="wheat", name = option, spread="mustard",ingredients=['chicken','tomato', 'lettuce', 'onion', 'carrot','cucumber'], options = None)
    elif option.lower() == "Spicy Italian".lower():
        return Sandwich(bread="French",name = option, spread="salsa-sauce",ingredients=['tomato', 'lettuce', 'onion','cucumber','olives'], options = None)
    elif option.lower() == "BLT".lower():
        return Sandwich(bread="rye",name = option, spread="butter",ingredients=['bacon','tomato', 'lettuce'], options = None)
    elif option.lower() == "Veggie Delight".lower():
        return Sandwich(bread="wheat",name = option,spread="butter",ingredients=['tomato', 'lettuce','olives'], options = None)

def initialize_native_sandwich():
    for key in sandwich_options.keys():
        sandwich = build_native_sandwich(key)
        sandwich_options[key] = sandwich


bread_options = ["rye", "wheat", "french", "italian"]
spread_options = [ "butter", "mayonnaise","mustard","salsa-sauce"]
sandwich_options = {"pooja's veggie special":None,"mustard chicken teriyaki": None,"spicy italian":None,"blt":None,"veggie delight":None}
ask_menu = ['Menu','menu','choice','Choice','Choices','choices','ask','Ask']
exception_words = ['hold','no','without','don\'t','not']
ingredients = ['onion' , 'garlic' , 'swiss cheese', 'avocado', 'lettuce', 'olives', 'tomato', 'carrot', 'cucumber', 'chicken', 'bacon']
stop_words = ['i',"would","like","to","have","please","give","me", "show","i'd like","thanks","you","thank","can","today","the","a","an"]
similar_terms = {"mayonnaise":['mayo','mayonnaise'],"veggie":['veg','veggie','vegetarian'],"salsa-sauce":["salsa-sauce",'salsa sauce'],"onion":['onions','onion'],"olives":['olive','olives'],"tomato":["tomato","tomatoes"],"carrot":["carrot","carrots"]}
add_on_words = ["with","along","want","along with","add","extra","add extra","on"]
options = ['grilled', 'toasted', 'cheese', 'salt','pepper']
verification ={'bread':False,'spread':False,'name':False,'ingredients':False}
# Make the native sandwiches
initialize_native_sandwich()
#To display the Menu
def display_menu():
    print("\n***********Welcome to Sandwich Ordering System***********\n")
    print("Here are options you can choose from:")
    for key in sandwich_options.keys():
        (sandwich_options[key]).display_description()
    print("\n*****************************************************************\n")

def get_native_sandwich(choice):
    sandwich = sandwich_options[choice]
    return sandwich

def check_if_ingredient(value):
    if value.lower() in ingredients or (value[-1].lower() == 's' and value[:-1].lower() in ingredients):
        return True
    return False

def check_if_spread(value):
    if value.lower() in spread_options:
        return True
    return False

def check_if_bread(value):
    if value.lower() in bread_options:
        return True
    return False

#Validate if the value is valid or not
def validate_values(values):
    new_value = copy.deepcopy(values)
    if values:
        for v in values:
            v = v.strip()
            v = v.strip('.')
            if not(check_if_spread(v) or check_if_bread(v) or check_if_ingredient(v)):
                new_value.remove(v)
    return new_value


#Check exceptions
def check_exceptions(content):
    exceptions = []
    content  = re.search('no(.*)with', content) or re.search('no(.*)', content)
    if content:
        content = content.group(1)
    new_content = content.replace("no","")
    exceptions = new_content.split(" ")
    while("" in exceptions):
        exceptions.remove("")
    while("," in exceptions):
        exceptions.remove(",")
    for v in exceptions:
        vals = v.split(',')
        for val in vals:   
            if val not in exceptions:
                exceptions.append(val.strip())
    exceptions = validate_values(exceptions)
    return exceptions

#Validate add-ons
def validate_add_ons(content):
    add_ons = []
    new_content = content.replace("with","")
    add_ons = new_content.split(" ")
    while("" in add_ons):
        add_ons.remove("")
    while("," in add_ons):
        add_ons.remove(",")
    for a in add_ons:
        if ',' in a:
            add_ons.remove(a)
            add_ons.append(a.strip(",")) 
        if '.' in a:
            add_ons.remove(a)
            add_ons.append(a.strip("."))
    validate_values(add_ons)
    return add_ons

def tokenize_and_process(choice):
    found = False
    #Get the sandwich name
    for key in sandwich_options.keys():
        pattern = key.lower()
        match = (re.search(pattern, choice))
        if match:
            found = True
            start, end = match.span()
            name = choice[start:end]
            # Make the sandwich
            sandwich = build_native_sandwich(name)
            verification['name'] = True # Mark that the name is set
            new_choice = choice[0: start:]+ choice[end+1::]
            match = (re.search("no",new_choice))
            #Exceptions exists thus, check-process-and validate them
            if match:
                exceptions = check_exceptions(new_choice)
                sandwich.exceptions = exceptions
                sandwich.process_exceptions()
                #Once exceptions are processes before processing add-ons, remove what is processed.
                for x in exceptions:
                    new_choice = new_choice.replace(x,"")
            new_choice = new_choice.replace("no","")  
            #Add-ons are given thus, process add-ons and validate them
            match_add = (re.search("with",new_choice))
            if match_add:
                add_choices_content = new_choice.partition('with')[2]
                add_ons = validate_add_ons(add_choices_content)
                sandwich.process_add_ons(add_ons)
            # Verify that all values are set
            sandwich.check_if_sandwich()
            sandwich.sanitize()
            # Display receipt to the user
            sandwich.print_reciept()
    #User has not selected with a sandwich name, Thus, let use decide from menu
    if not found:
        print('We didn\'t find any choice you entered. Please choose from the below menu')
        display_menu()
        choose = input("\nEnter the name of the sandwich you would like to have:")
        validate_user_input(choose)

def remove_stop_words(choice):
    choice = choice.lower()
    choices = choice.split(" ")
    for word in stop_words:
        if word.lower() in choices:
            choices.remove(word)
    return ' '.join(choices)

def replace_exception_words(choice):
    choice = choice.lower()
    for word in exception_words:
        if word.lower() in choice:
            #choice = choice.replace(word.lower(), "no")
            choice = re.sub(r"\b%s\b" % word.lower() , "no", choice)
    return choice
    
def replace_add_on_words(choice):
    choice = choice.lower()
    for word in add_on_words:
        if word.lower() in choice:
            choice = re.sub(r"\b%s\b" % word.lower() , "with", choice)
    return choice

def replace_similar_words(choice):
    choice = choice.lower()
    for key in similar_terms.keys():
        terms = similar_terms[key]
        for word in terms:
            if word.lower() in choice:
                choice = re.sub(r"\b%s\b" % word.lower() , key, choice)
    return choice

# Cleans up the input and replaces similar words, exception words, add-on words and removes stop words
def replace_words(choice):
    choice = remove_stop_words(choice)
    choice = replace_exception_words(choice)
    choice = replace_add_on_words(choice)
    choice = replace_similar_words(choice)
    return choice

# Split on with and append whatever is given
def split_on_with(choice, sandwich):
    match = (re.search("with",choice))
    if match:
        words = print(choice.split("with"))
        for word in words:
            if(check_if_ingredient(word)):
                if sandwich.ingredients:
                    sandwich.ingredients.append(word)
                else:
                    sandwich.ingredients = [word]
                verification['ingredients'] = True
            if(check_if_bread(word)):
                if not sandwich.bread:
                    sandwich.bread = word
                    verification['bread'] = True
            if(check_if_spread(word)):
                if not sandwich.spread:
                    sandwich.spread = word
                    verification['spread'] = True

def validate_user_input(choice):
    # Cleans up the input and replaces similar words, exception words, add-on words and removes stop words
    choice = replace_words(choice)
    sandwich_options_lower = [x.lower() for x in sandwich_options.keys()]
    #Direct name given prepare and return
    if choice in sandwich_options_lower:
        print("\nFound your sandwich!")
        sandwich = get_native_sandwich(choice)
        sandwich.print_reciept()
    # Case when sandwich name with options given. Ask clarification questions too. (Better user interface)
    elif(any(x in y or y in x for y in choice.split() for x in sandwich_options_lower)):
        print("\nPreparing customized sandwich\n")
        tokenize_and_process(choice)      
    #For menu generation
    elif(any(s in l for l in choice.split() for s in ask_menu)):
        display_menu()
        choose = input("\nEnter the name of the sandwich you would like to have:")
        validate_user_input(choose)
    else:
        print("\nYou have not selected a sandwich we provide. Please select one from the menu.\n")
        display_menu()
        choose = input("Enter the name of the sandwich you would like to have:")
        validate_user_input(choose)

def sandwich_system_start():
    print("\nHello, Welcome to the online Sandwich Ordering System\n")
    user_choice = input("What would you like to have today? OR Would you like to see the Menu?\n")
    # Check if the name matches exactly
    validate_user_input(user_choice)

#Stating Point of the Program
sandwich_system_start()
