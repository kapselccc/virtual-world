# Virtual world
The game allows to control human, walking on the map and interacting with other
organisms. The game is implemented in Python and for graphical interface
`pygame` library is used. 
## Starting
To start the game type command below in the terminal or run main.py in IDE.
```sh
python main.py
```
| ⚠️ **Warning!** pygame library is required to start the game | 
|---|

To install pygame type command below in the terminal
```sh
pip install pygame
```

## Game
There are 2 kinds of organisms on the map: plants and animals. Every organism
has 2 main attributes: strength and initiative. Initiative indicates which
creature moves first. Strength indicates wchich creature would win in the fight.
### Animals
Animals are the creatures that can move and attack. There are 7 types of animal
which have different features. For example `turtle` moves only once a few turns
and can repel an attack. 

### Plants
Plants don't move but can propagate. Each turn there is a certain chance of
propagating for every plant. Plants can be eaten by animals and some of them
have special effects. For example after eating `guarana`, animal will recieve
additional strength points.

### Human
Human is an animal controlled by player. To move human you should press the
arrow on the keyboard indicating the direction that you want to go. The goal of
this game is to survive on the map for as long as you can.