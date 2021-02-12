import os
import sys
from pprint import pprint

def createChessBoardWithPieces(whites, blacks, verbose):
    chessBoard = {
        'A1': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'A2': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'A3': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'A4': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'B1': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'B2': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'B3': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'B4': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'C1': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'C2': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'C3': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'C4': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'D1': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'D2': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'D3': {
            'chessPiece': 'empty',
            'colour': 'empty'
        },
        'D4': {
            'chessPiece': 'empty',
            'colour': 'empty'
        }
    }

    for piece in whites:
        chessBoard[str(piece[1] + piece[2])]['chessPiece'] = piece[0]
        chessBoard[str(piece[1] + piece[2])]['colour'] = 'white'

    for piece in blacks:
        chessBoard[str(piece[1] + piece[2])]['chessPiece'] = piece[0]
        chessBoard[str(piece[1] + piece[2])]['colour'] = 'black'

    if verbose:
        pprint(chessBoard)

    return chessBoard


def convertBoardCoordinateToMatrixCoordinate(boardCoordinate):
    # Example: 'A4' => [0, 0]

    rowMapping = {
        '4': 0,
        '3': 1,
        '2': 2,
        '1': 3
    }

    columnMapping = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3
    }

    row = rowMapping[boardCoordinate[1]]
    column = columnMapping[boardCoordinate[0]]
    return [row, column]


def createChessMatrixWithPieces(whites, blacks, verbose):
    chessMatrix = [
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0']
    ]

    for piece in whites:
        matrixCoordinate = convertBoardCoordinateToMatrixCoordinate(str(piece[1] + piece[2]))

        chessMatrix[matrixCoordinate[0]][matrixCoordinate[1]] = 'W' + piece[0]

    for piece in blacks:
        matrixCoordinate = convertBoardCoordinateToMatrixCoordinate(str(piece[1] + piece[2]))

        chessMatrix[matrixCoordinate[0]][matrixCoordinate[1]] = 'B' + piece[0]
    
    if verbose:
        pprint(chessMatrix)

    return chessMatrix

def getPossibleMovements(chessMatrix, piece, location):
    # Setting rules
    rowMovements = 0
    columnMovements = 0
    if piece == 'Q':
        print('f')


#
# Complete the simplifiedChessEngine function below.
#
def simplifiedChessEngine(whites, blacks, moves):
    '''
        The board looks like the following:

        4   0   0   0   0
        3   0   0   0   0
        2   0   0   0   0
        1   0   0   0   0
            A   B   C   D

    '''
    # createChessBoardWithPieces(whites, blacks)
    createChessMatrixWithPieces(whites, blacks, verbose=True)
    


if __name__ == '__main__':

    whites = [
        ['N', 'B', '2'],
        ['Q', 'B', '1']
    ]

    blacks = [
        ['Q', 'A', '4']
    ]

    m = 1

    result = simplifiedChessEngine(whites, blacks, m)

