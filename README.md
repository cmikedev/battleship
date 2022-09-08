# Battleship
Battleship is a python version of the classic turn-based guess game. The intention of this [site](https://battleship-cmikedev.herokuapp.com/) is to provide a player with a simple and intuitive interface. 


____


![image]()


## Deployed Website
[Battleship](https://battleship-cmikedev.herokuapp.com/)


## Repository
https://github.com/cmikedev/battleship



## Structure

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/battleship-flowchart.png?raw=true)




## Features

* #


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
[image]()




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