import chess 
import chess.svg as svg

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

board = chess.Board()

board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
board.push_san("Qxf7")

board = svg.board(board,size=650)

graphics_file = open('board.svg', 'w')
graphics_file.write(board)
graphics_file.close()


drawing = svg2rlg('board.svg')

renderPDF.drawToFile(drawing, "board.pdf")

