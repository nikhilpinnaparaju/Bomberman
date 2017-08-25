#20161118
#Nikhil Pinnaparaju

Hi, Welcome to my custom terminal based game of Bomberman.

###The controls used are normal:-

*W - Move Up
*A - Move Left
*S - Move Down
*D - Move right
*B - Plant Bomb
*Q - Quit

Enemies are spawned at random locations and so are the bricks leading to multiple possible levels in a single level itself.

The game using threading and so it runs multiple parallel process at the same time hence not stopping the game's core mechanics such as enemy movement
or bomb countdown with the user does not provide input. This was the hardest part and took a lot of trials and implementations to make work.

OOPS concepts such as Modularity, Inheritance, Encapsulation and Polymorphism have been used in this project creation along with others.

To run a level enter the respective directory and run **main.py** in **Python3**

Comments have been added to the Level 1 directory files

###Existing classes:-

*Person
*Bomberman
*Bomb
*Enemy
*RepeatedTimer
*Bricks
*KillingFunction
*MovingEnemies

The Code has been run on a terminal of Black Background, Please consider that will running game.

Note: The movement of enemies is based on a random number generated using python random from 0-3. If the enemy is surrounded by 2 or 3 bricks or walls
it might seem like they are not moving however that is not the case so please consider that it could be the case that the random number generated does
not allow motion

###Levels - 

*Level 1 - Regular game of Bomberman. 3 lives for Bomberman and 1 life per Enemy
*Level 2- Enemies move faster. 2 Lives per Enemy and only 2 lives for Bomberman. Bigger Board. Double number of enemies from Level 1. 

Note: Any number of enemies can be added by adding a line in the main.py file (Usage: "**<var name>** = enemy()" and then "enemies.add(**<var name>)**")

###Implementation of OOPS Concepts:- 

#Inheritance - The class *Bomberman* and *Enemy* both inherit properties from the class *Person*
#Polymorphism - *add* to an *enemies* set puts in another enemy into the collection of *enemies* but when calculating distances between our characters (*bomberman* and *enemy*) and the bomb it sums up two integers
#Encapsulation - To avoid accidental accessing of variables encapsulation has been applied to variables like *score* and the *init* functions inside class declarations. The function *_exit* should only be called when certain conditions are met and not improperly to suddenly stop execution. Hence it is also properly encapsulated
#Modularity - The *grid* and our *print_board* functions are all in a file *grid.py*. Similarly, the primary class definitions are all in *classdefs.py* and the python threader we are using for this code is in *threader.py* and so on.
#Abstraction - The attributes to *bomb* and *bomberman* are all abstracted to the user and carefully placed inside the classes and in their respective functions.
# Many Classes and objects have also been used covering many OOPS concepts.

Hope you enjoy the game.
Thanks in Advance.