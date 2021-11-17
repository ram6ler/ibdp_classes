
procedure PLUNDER(BOARD, ROWS, COLUMNS)
    ROW = 0
    COLUMN = 0
    RIGHT = 0
    DOWN = 1
    DIRECTION = RIGHT
    LOOT = 0

    loop while ROW < ROWS and COLUMN < COLUMNS
        LOOK = BOARD[ROW][COLUMN]
        if LOOK ≥ 0 then
            LOOT = LOOT + LOOK
        else
            if DIRECTION = RIGHT then
                DIRECTION = DOWN
            else
                DIRECTION = RIGHT
            end if
        end if
        if DIRECTION = RIGHT then
            COLUMN = COLUMN + 1
        else
            ROW = ROW + 1
        end if
    end loop

    if COLUMN = COLUMNS then
        output "right"
    else
        output "bottom"
    end if
    output LOOT
end procedure

BOARD = new Array(
    new Array(5, 10, -3, 4, 6), 
    new Array(-2, 14, -5, 2, -1), 
    new Array(8, -9, -5, 5, 12),
    new Array(1, 20, -3, 8, -10)
)

ROWS = 4
COLUMNS = 5
PLUNDER(BOARD, ROWS, COLUMNS)