#!/usr/bin/env bash

source ~/environments/chessEnv/bin/activate

chmod +x GameOfTheDay.py

./GameOfTheDay.py

xdg-open game.gif
