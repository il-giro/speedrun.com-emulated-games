# speedrun.com-emulated-games

A python program that allows you to understand if a game can be emulated or not, (for speedrun purposes) on [speedrun.com](https://www.speedrun.com/).

- Have you ever wondered if there is a list of games where doing a speedrun with an emulator is legal?
- Are you tired of entering the official page of every game just to find out if the emulated speedrun you made can be verified?

The answer is no unluckily 😢

**but speedrun.com-emulated-games is here to help you**

## The 2 txt files

The two **text** files are not complete yet, but are a tentative list of some games respectively with banned emulators or not. <br>(`no_emu.txt`  &&  `emu.txt`)<br>
The rows are sorted in descending order according to the number of players in the game.<br>
The structure of each row of the file is as follows: { number of players } { game name (found in the link)} { game link }<br>
Each time you use the script the file will automatically update.<br>

> [!IMPORTANT]
> The list will not be ordered automatically, in fact you need to use the second script to do this

## The 2 bat files

The two **bat** files automatically execute the corresponding script, as long as the files are in the same directory.

# How to actually use the script
First make sure that Python 3.0+ is installed on your device, then download the files and run them with the respective .bat file. <br>
Every time we run `speedrun.py` a new random game will be added to the list **but not in order**, whenever we want to read the list or modify it we can run `sort.py`.<br>
You can change the, initially initialized, "cycles" variable to change the number of times the script will run, each time the script will run it will print the loop number in the cmd to keep track of where it arrived.


> pls report any issues ty
