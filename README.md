# Sandwich Ordering System
Design and develop a sandwich ordering system that take in a typed customer request for a sandwich, engage in a dialog with the customer to clarify details, and then print out the complete order.

This project helps in understanding logic and how NLP systems would work, using basic regex  and text cleaning than using NLP libraries.

Step 1:

***********Welcome to Sandwich Ordering System***********

Here are options you can choose from:

Pooja'S Veggie Special: contains French bread with ingredients Swiss cheese, tomato, lettuce, onion, carrot, cucumber and spread as mayonnaise

Mustard Chicken Teriyaki: contains wheat bread with ingredients chicken, tomato, lettuce, onion, carrot, cucumber and spread as mustard

Spicy Italian: contains French bread with ingredients tomato, lettuce, onion, cucumber, olives and spread as salsa-sauce

Blt: contains rye bread with ingredients bacon, tomato, lettuce and spread as butter

Veggie Delight: contains wheat bread with ingredients tomato, lettuce, olives and spread as butter

*****************************************************************
Exceptions can be any spread, bread or ingredients.
Options: [ grilled, toasted, extra cheese, salt and pepper]. 
Please note the above menu provides default values for each sandwich 

Step 2:
1. The list of terms you treat as equivalent:

similar_terms = {"mayonnaise":['mayo','mayonnaise'],"veggie":['veg','veggie','vegetarian'],"salsa-sauce":["salsa sauce",'salsa-sauce'],"onion":['onions','onion'],"olives":['olive','olives'],"tomato":["tomato","tomatoes"],"carrot":["carrot","carrots"]}

exception_words = ['hold','no','without','don\'t','not']

ask_menu = ['Menu','menu','choice','Choice','Choices','choices','ask','Ask']

add_on_words = ["with","along","want","along with","add","extra","add extra","on"]

Thus, for similar_terms all values of a Key are equivalent to the Key. For exception words, all of them are treated as 'no'. For add_on_words: all of them are treated as 'with'

2. The list of terms like “Please” etc. that you will ignore.:
stop_words = ['i',"would","like","to","have","please","give","me", "show","i'd like","thanks","you","thank","can","today","the","a","an"]

3. The different ways you will allow customers to specify exceptions:
Hold the mayo, without onion , no lettuce, don't put mayo

Step 3:

Programming language you used: Python
List the commands required to run the system : sandwich.py
Files : sandwich.py 
This file consists of 2 parts (Sandwich class along with it's validations and the application which has various helper methods to reformat the user input.)


Step 4: Working:
Example 1:
C:\Users\Modak\Desktop\NEU\Term 3-Fall 2020\CS 5100-AI>sandwich.py

Hello, Welcome to the online Sandwich Ordering System

What would you like to have today? OR Would you like to see the Menu?
Veggie Delight don't put mayo

Preparing customized sandwich

You have requested to remove mayonnaise from sandwich.

This sandwich  Veggie Delight  will come with spread as  butter

Press 'return' to accept this choice of spread, or choose one of the other alternatives: 1. mayonnaise (mayo), 2. mustard, 3.salsa-sauce, 4. butter.
salsa-sauce
This sandwich  Veggie Delight  will come with  wheat bread

Press 'return' to accept this choice of bread, or choose one of the other alternatives: 1. wheat, 2. rye, 3.italian, 4. french
rye
This sandwich  Veggie Delight  contains tomato, lettuce, olives

Press 'return' to accept this choice of ingredients, or press 1. to add 2. to remove.
1

Following ingredients are available. Choose to add new ingredients:
 [ onion , garlic , Swiss cheese, avocado, lettuce, olives, tomato, carrot, cucumber, chicken, bacon]
 Press 'return' to make no addition
garlic
This sandwich  Veggie Delight  contains tomato, lettuce, olives, garlic

Press 'return' to accept this choice of ingredients, or press 1. to add 2. to remove.


Veggie Delight: contains rye bread with ingredients tomato, lettuce, olives, garlic and spread as salsa-sauce along with following exceptions mayonnaise

No options selected as of now. Following options are available.
 [ grilled, toasted, extra cheese, salt and pepper]
 Press 'return' to accept no choice of options or press 1. to add 2. to remove.
1

Following options are available. Choose to add options:[ grilled, toasted, extra cheese, salt and pepper]
 Press 'return' to make no addition
toasted
This sandwich  Veggie Delight  will come with toasted


Following options are available.
 [ grilled, toasted, extra cheese, salt and pepper]
Press 'return' to accept this choice of options toasted or press 1. to add 2. to remove.


Veggie Delight: contains rye bread with ingredients tomato, lettuce, olives, garlic and spread as salsa-sauce and options as toasted along with following exceptions mayonnaise

        *******************Receipt*********************
    
        Name of the sandwich:    Veggie Delight
    
        Usual ingredients:      tomato, lettuce, olives, garlic
    
        Bread-type:      Rye
    
        Spreads:         Salsa-sauce
    
        Options:        toasted
    
        Exceptions:     mayonnaise

Example 2:

C:\Users\Modak\Desktop\NEU\Term 3-Fall 2020\CS 5100-AI>sandwich.py

Hello, Welcome to the online Sandwich Ordering System

What would you like to have today? OR Would you like to see the Menu?
Pooja's veggie special on whole wheat please no onions and carrots

Preparing customized sandwich

This sandwich  Pooja'S Veggie Special  will come with spread as  mayonnaise

Press 'return' to accept this choice of spread, or choose one of the other alternatives: 1. mayonnaise (mayo), 2. mustard, 3.salsa-sauce, 4. butter.
butter
This sandwich  Pooja'S Veggie Special  contains Swiss cheese, tomato, lettuce, cucumber

Press 'return' to accept this choice of ingredients, or press 1. to add 2. to remove.
2

Following ingredients are available on Sandwich. Choose to remove ingredients:
Swiss cheese,tomato,lettuce,cucumber
 Press 'return' to make no removals
cucumber
This sandwich  Pooja'S Veggie Special  contains Swiss cheese, tomato, lettuce

Press 'return' to accept this choice of ingredients, or press 1. to add 2. to remove.
1

Following ingredients are available. Choose to add new ingredients:
 [ onion , garlic , Swiss cheese, avocado, lettuce, olives, tomato, carrot, cucumber, chicken, bacon]
 Press 'return' to make no addition
avocado
This sandwich  Pooja'S Veggie Special  contains Swiss cheese, tomato, lettuce, avocado

Press 'return' to accept this choice of ingredients, or press 1. to add 2. to remove.


Pooja'S Veggie Special: contains wheat bread with ingredients Swiss cheese, tomato, lettuce, avocado and spread as butter along with following exceptions onion, carrot

No options selected as of now. Following options are available.
 [ grilled, toasted, extra cheese, salt and pepper]
 Press 'return' to accept no choice of options or press 1. to add 2. to remove.
1

Following options are available. Choose to add options:[ grilled, toasted, extra cheese, salt and pepper]
 Press 'return' to make no addition
grilled
This sandwich  Pooja'S Veggie Special  will come with grilled


Following options are available.
 [ grilled, toasted, extra cheese, salt and pepper]
Press 'return' to accept this choice of options grilled or press 1. to add 2. to remove.

This sandwich  Pooja'S Veggie Special  will come with grilled


Following options are available.
 [ grilled, toasted, extra cheese, salt and pepper]
Press 'return' to accept this choice of options grilled or press 1. to add 2. to remove.


Pooja'S Veggie Special: contains wheat bread with ingredients Swiss cheese, tomato, lettuce, avocado and spread as butter and options as grilled along with following exceptions onion, carrot

        *******************Receipt*********************
    
        Name of the sandwich:    Pooja'S Veggie Special
    
        Usual ingredients:      Swiss cheese, tomato, lettuce, avocado
    
        Bread-type:      Wheat
    
        Spreads:         Butter
    
        Options:        grilled
    
        Exceptions:     onion, carrot

Above examples, let the user have choice to reslect since user has not specifically given bread/spread. Thus, we get the details and user may or maynot change it.

Example 3: (User directly specifies the name of the sandwich)
Hello, Welcome to the online Sandwich Ordering System

What would you like to have today? OR Would you like to see the Menu?
Can you show me the menu please

***********Welcome to Sandwich Ordering System***********

Here are options you can choose from:

Pooja'S Veggie Special: contains French bread with ingredients Swiss cheese, tomato, lettuce, onion, carrot, cucumber and spread as mayonnaise

Mustard Chicken Teriyaki: contains wheat bread with ingredients chicken, tomato, lettuce, onion, carrot, cucumber and spread as mustard

Spicy Italian: contains French bread with ingredients tomato, lettuce, onion, cucumber, olives and spread as salsa-sauce

Blt: contains rye bread with ingredients bacon, tomato, lettuce and spread as butter

Veggie Delight: contains wheat bread with ingredients tomato, lettuce, olives and spread as butter

*****************************************************************


Enter the name of the sandwich you would like to have:spicy italian

Found your sandwich!

        *******************Receipt*********************
    
        Name of the sandwich:    Spicy Italian
    
        Usual ingredients:      tomato, lettuce, onion, cucumber, olives
    
        Bread-type:      French
    
        Spreads:         Salsa-sauce
    
        Options:        None
    
        Exceptions:     None

Example 4: (User asks for something which is not present in the system)
C:\Users\Modak\Desktop\NEU\Term 3-Fall 2020\CS 5100-AI>sandwich.py

Hello, Welcome to the online Sandwich Ordering System

What would you like to have today? OR Would you like to see the Menu?
sandwich club

You have not selected a sandwich we provide. Please select one from the menu.


***********Welcome to Sandwich Ordering System***********

Here are options you can choose from:

Pooja'S Veggie Special: contains French bread with ingredients Swiss cheese, tomato, lettuce, onion, carrot, cucumber and spread as mayonnaise

Mustard Chicken Teriyaki: contains wheat bread with ingredients chicken, tomato, lettuce, onion, carrot, cucumber and spread as mustard

Spicy Italian: contains French bread with ingredients tomato, lettuce, onion, cucumber, olives and spread as salsa-sauce

Blt: contains rye bread with ingredients bacon, tomato, lettuce and spread as butter

Veggie Delight: contains wheat bread with ingredients tomato, lettuce, olives and spread as butter

*****************************************************************

Enter the name of the sandwich you would like to have:I would like blt

Found your sandwich!

        *******************Receipt*********************
    
        Name of the sandwich:    Blt
    
        Usual ingredients:      bacon, tomato, lettuce
    
        Bread-type:      Rye
    
        Spreads:         Butter
    
        Options:        None
    
        Exceptions:     None

In this scenario, since user had not initially specified the name of sandwich (provided by the system), we tell user "You have not selected a sandwich we provide. Please select one from the menu." and let user re-select from the menu.


Example 5: 

(User has specified bread and spread both, with sandwich name. Thus, don't ask anything else.)
C:\Users\Modak\Desktop\NEU\Term 3-Fall 2020\CS 5100-AI>sandwich.py

Hello, Welcome to the online Sandwich Ordering System

What would you like to have today? OR Would you like to see the Menu?
I would like blt with wheat bread and mayo sauce

Preparing customized sandwich


Blt: contains wheat bread with ingredients bacon, tomato, lettuce and spread as mayonnaise

        *******************Receipt*********************
    
        Name of the sandwich:    Blt
    
        Usual ingredients:      bacon, tomato, lettuce
    
        Bread-type:      Wheat
    
        Spreads:         Mayonnaise
    
        Options:        None
    
        Exceptions:     None


Regex usage was simple. Creating an object of sandwich class makes it easier to set and validate the values.

Learnings from the project:
1. How to understand a requirement and balance it in terms of assumptions and re-verifications.
2. Nice way to know how user systems would work! The way user interact with system can be in various different ways. Thus, handling various cases was important and a good learning to think of them. A good learn in terms of processing the natural language and understanding it.