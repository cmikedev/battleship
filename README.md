# Battleship
Battleship is a single-player python version of the classic turn-based guess game.</br >
</br > 

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/am-i-responsive.png?raw=true)</br >
</br >
Image created using [Am I responsive](https://ui.dev/amiresponsive)</br >
</br >

### Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://battleship-cmikedev.herokuapp.com/).


### Repository
The GitHub repository can be found [here](https://github.com/cmikedev/battleship).


____



## 1. Design

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/battleship-flowchart.png?raw=true)


## 2. Features

### 2.1 The Introduction Screen
When the page loads the user is presented with an introduction providing a brief background story. The purpose of this is to provide a sense of immersion in the game.
* The text loading is staggered in order to make it look like the user is awaiting receipt of a message from fleet Command. This is done to create a further sense of immersion by linking the user with an imaginery third party, a Fleet Command.</br >
</br >

![image]()</br >
</br >

* The user is then provided with a prompt move on to the next screen allowing them as much time as is required to read the introduction screen.</br >
</br >

### 2.2 The Instructions Screen
* The game instructions are laid out for the user. Again, they will be provided with a prompt to move onto the next screen in their own time.
* The user will not need to come back to this screen as simplified instructions will be provided on the game screen.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/instructions.png?raw=true)</br >
</br >

### 2.3 The Difficulty Screen
* The Difficulty Screen provides the user the opportunity to provide input into the game. The four difficuly levels are explained and the user is prompted to choose.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/difficulty.png?raw=true)</br >
</br >

* Depending on the difficulty level chosen, from 'Easy' to 'Insane', the board size will increase as will the number of enemy vessels. The number of missiles, while increasing in number, will either decrease proprotionately to the board size or remain the same (in the case of 'Medium' and 'Hard').</br >
</br >

### 2.4 The Game Board
When the user has selected their desired difficulty level, the game board will be generated with its size corresponding to the diffficulty chosen.
* The user is once again provided with instructions on how to play.
* The game board grids are visualised (the image below shows a 9x9 grid as per 'Insane' difficulty level).
* The number of enemy ships and the number destroyed will be displayed (again, based on difficulty level chosen).
* The missiles (turns).</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/gameboard.png?raw=true)</br >
</br >

* The user is asked to input their guess by way of selected the numerical row and aphabetical column. These coordinates represent a place on the grid.
* An enemy ship occupies one grid space. If the user's guess corresponds to the coordinates of the enemy ship, the enemy ship is destroyed.
* The board will then be reprinted displaying an "X" in the grid where a ship was destroyed or a "-" to denote a miss.
* The number of enemy ships and missiles remaining displays are then updated as the board reprints.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/ships-missiles-remaining.png?raw=true)</br >
</br >

* If the user has failed to destroy all ships by the time their missiles remaining reaches 5, the missiles remaining message will update to warn the user that they are running low on ammo.</br >
</br >

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/low-ammo-warning.png?raw=true)</br >
</br >

## Testing

### Responsiveness Testing

* to be included...<br />
<br />

### Validator Testing

* #### PEP8
    * HTML
        * To be included<br />
        <br />


## Deployment

### Deploying the repository via Heroku
* The app was created using Heroku via the following steps:
    * On the https://dashboard.heroku.com/apps page, click <mark style="background-color: grey">New</mark> and then select <mark style="background-color: grey">Create New App</mark> from the drop-down menu.
    * When the next page loads insert the <mark style="background-color: grey">App name</mark> and <mark style="background-color: grey">Choose a region</mark>. The click <mark style="background-color: grey">Create app</mark>
    * In the settings tab click on <mark style="background-color: grey">Reveal Config Vars</mark> and add the key <mark style="background-color: grey">Port</mark> and the value <mark style="background-color: grey">8000</mark>. There were no credentials required for this app.
    * Below this click <mark style="background-color: grey">Add buildpack</mark> and choose <mark style="background-color: grey">python</mark> and <mark style="background-color: grey">nodejs</mark> in that order.</br >
    </br >
* To deploy the Heroku app:
    * Click on the <mark style="background-color: grey">Deploy</mark> tab and select <mark style="background-color: grey">Github-Connect to Github</mark>.
    * Enter the repository name and click <mark style="background-color: grey">Search</mark>.
    * Choose the repository that holds the correct files and click <mark style="background-color: grey">Connect</mark>.
    * A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub. For this app automatic was selected.
    * Once the deployment method has been chosen the app will be built and can be launched by clicking the <mark style="background-color: grey">Open app</mark> button at the top of the page.<br />
    <br />
![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/heroku-deployment.png?raw=true)




## Credits

### Research and Guidance
* [stackoverflow](https://stackoverflow.com/questions/60405812/can-you-put-a-operator-into-a-list-comprehension) was referenced for guidance on using operators within list comprehension.
* [stackoverflow](https://stackoverflow.com/questions/68716514/python-sleep-function-not-working-as-expected) was referenced for guidance on the sleep function from the time import.
* [scaler](https://www.scaler.com/topics/how-to-clear-screen-in-python/) provided a solution to the issue of clearing the board depending on whether the user's os was MAC, Windows or Linux.
* [trinket](https://trinket.io/python/051179b6d3) provided research on simple Battleship game-logic and creating enemy ships.
* [Austin Montgomery](https://bigmonty12.github.io/battleship) provided examples for creating the board, enemy ships and game logic.
* [codecademy](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605) Example of a Battleship game using classes.
* [mailpraveens](https://gist.github.com/mailpraveens/6167921) Example of a Battleship game code created from a CodeCademy tutorial.
* [gbrough](https://github.com/gbrough/battleship/blob/main/single_player.py) provided a solution to the create board problem with the rows numbered and creating the ship locations. Code from gbrough has been referenced in the run.py file.
* [programiz](https://www.programiz.com/article/flowchart-programming) for guidance on creating the flowchart.

----

## Acknowledgements
I would like to thank my course mentor Harry Dhillon for providing guidance on this project as well as Alysha Johnson for providing styling inspiration for the README.