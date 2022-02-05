#!/usr/bin/env python3
import os 
import shutil

import chess 
import chess.svg as svg
import chess.pgn 

import requests
from bs4 import BeautifulSoup

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF,renderPM
from pdf2image import convert_from_path

import imageio

def grabGameOfTheDay():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

    URL = "https://www.chessgames.com"
    pgn_URL_template = "https://www.chessgames.com/perl/nph-chesspgn?text=1&gid="

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,"html.parser")

    game_of_the_day_ID = soup.find(string="begingameotd")
    game_of_the_day_String=str(game_of_the_day_ID.find_parent("p"))

    parts = game_of_the_day_String.split(">")
    gotd_specifier = parts[2].split('"')[1]
    game_ID = gotd_specifier.split("gid=")[1]

    # Once the game_ID has been captured the pgn can be extracted 
    pgn_URL = pgn_URL_template + game_ID
    pgn_page = requests.get(pgn_URL, headers=headers)

    pgn_file = open('game.pgn', 'w')
    pgn_file.write(pgn_page.text)
    print(pgn_page.text)
    pgn_file.close()

    return 

def generateGame():
    pgn = open("game.pgn")

    game = chess.pgn.read_game(pgn)
    board = game.board()

    dir = "images"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    
    ply = 0 
    for move in game.mainline_moves():
        board.push(move)
        board_SVG = svg.board(board,size=120000)
        graphics_file = open('board.svg', 'w')
        graphics_file.write(board_SVG)
        graphics_file.close()
        drawing = svg2rlg('board.svg')
        renderPDF.drawToFile(drawing, dir +f"/board{ply}.pdf")
        ply = ply + 1
    os.remove("board.svg")

    return dir,ply

def convertPDFs2GIF(dir,ply):
    images = []
    for i in range(ply):
        page = convert_from_path(dir +f"/board{i}.pdf",1)[0]
        page.save(dir +f"/board{i}.png","PNG")
        os.remove(dir +f"/board{i}.pdf")
        images.append(imageio.imread(dir +f"/board{i}.png"))
        os.remove(dir +f"/board{i}.png")
    os.rmdir(dir)
    imageio.mimsave('game.gif', images, duration = 0.6)
    
    return

def main():
    grabGameOfTheDay()

    directory, ply = generateGame()

    convertPDFs2GIF(directory,ply)

if __name__ == "__main__":
        main()

