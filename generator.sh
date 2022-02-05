#!/usr/bin/env bash

source $PWD/chessEnv/bin/activate

chmod +x GameOfTheDay.py

./GameOfTheDay.py

xdg-open game.gif
