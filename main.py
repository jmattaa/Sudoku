import pygame as p
from Sudoku import Sudoku

WIN_W = 720
WIN_H = 720

CELL_W = WIN_W // 9
CELL_H = WIN_H // 9

sudoku = Sudoku(CELL_W, CELL_H)


def main():
    p.init()
    p.font.init()
    font = p.font.SysFont("UbuntuMono", 48, italic=True)
    fontbold = p.font.SysFont("UbuntuMono", 48, bold=True)
    screen = p.display.set_mode((WIN_W, WIN_H))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    keysToNums = {
        p.K_0: 0,
        p.K_1: 1,
        p.K_2: 2,
        p.K_3: 3,
        p.K_4: 4,
        p.K_5: 5,
        p.K_6: 6,
        p.K_7: 7,
        p.K_8: 8,
        p.K_9: 9,
    }

    numKeys = [
        p.K_0,
        p.K_1,
        p.K_2,
        p.K_3,
        p.K_4,
        p.K_5,
        p.K_6,
        p.K_7,
        p.K_8,
        p.K_9,
    ]

    running = True
    # So we redraw screen only when needed
    # This saves the CPU usage 
    change = True 
    currentSq = (-1, -1)
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                mousepos = p.mouse.get_pos()

                mouseX = mousepos[0] // CELL_W
                mouseY = mousepos[1] // CELL_H
                change = True

                currentSq = (mouseX, mouseY)
            elif e.type == p.KEYDOWN:
                for k in numKeys:
                    if e.key == k:
                        sudoku.addNumber(currentSq, keysToNums[k])
                        change = True
                        break

        if change:
            screen.fill(p.Color("white"))
            sudoku.draw(screen, fontbold, font)
            sudoku.highlight(screen, currentSq)
            change = False

        if sudoku.win:
            print("Win!!")
            running = False

        clock.tick()
        p.display.flip()


if __name__ == "__main__":
    main()
