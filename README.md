## GuessWhoWebIO
A small project to experiment with the PyWebIO library, this web app maximizes the chances of winning at the children's game _Guess Who?_  Using a browser interface, it outputs the best yes-or-no question to ask during each turn, traversing a binary decision tree based on user input responses.   

The algorithm works by maximizing information gain; that is, it transforms the game dataset into a decision tree by splitting nodes into sub-nodes on the unknown variable (a physical feature of the opponent's character) with the greatest entropy in the context of the target variable (the name of the opponent's character).  

The PyWebIO test is implemented in "main.py" and the algorithm is implemented in "guess_who_algorithm.ipynb."  

Note that the game dataset here is based on an old but common version of the game, which has been updated with new characters and traits. An image of the set of compatible character-cards is displayed for reference within the app interface. 

