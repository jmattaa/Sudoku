local Grid = require("sudoku")

---@type Grid
local grid

function love.load()
    grid = Grid.new()
end

function love.resize(w, h)
end

function love.update(dt)
end

function love.draw()
    grid:draw()
end
