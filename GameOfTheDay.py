import chess 
import chess.svg as svg
import requests
from bs4 import BeautifulSoup

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

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

    return pgn_page.text

def generateGame():
    #board = chess.Board()

    #board.push_san("e4")
    #board.push_san("e5")
    #board.push_san("Qh5")
    #board.push_san("Nc6")
    #board.push_san("Bc4")
    #board.push_san("Nf6")
    #board.push_san("Qxf7")

    #board = svg.board(board,size=650)

    #graphics_file = open('board.svg', 'w')
    #graphics_file.write(board)
    #graphics_file.close()


    #drawing = svg2rlg('board.svg')

    #renderPDF.drawToFile(drawing, "board.pdf")
    return


print(grabGameOfTheDay())