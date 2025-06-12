local Sudoku = require("sudoku")

---@type Sudoku
local grid

function love.load()
    grid = Sudoku.new()
end

function love.resize(w, h)
    grid:resize(w, h)
end

function love.update(dt)
end

function love.draw()
    love.graphics.setBackgroundColor(0.1, 0.1, 0.1)
    love.graphics.setColor(0.7, 0.7, 0.7)
    grid:draw()
end
