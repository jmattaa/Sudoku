local DIM = 9

---@class Sudoku
---@field cw number
---@field ch number
---@field offsetX number
---@field offsetY number
---@field gridW number
---@field gridH number
---@field grid number[][]
---@field initial number[][]
---@field solved number[][]
---@field won boolean
local Sudoku = {}
Sudoku.__index = Sudoku

---@return Sudoku
function Sudoku.new()
    ---@type Sudoku
    local self = setmetatable({}, Sudoku)

    local mindim = math.min(love.graphics.getWidth(), love.graphics.getHeight())
    self.cw = mindim / DIM
    self.ch = self.cw

    self.gridW = self.cw * DIM
    self.gridH = self.ch * DIM
    self.offsetX = (love.graphics.getWidth() - self.gridW) / 2
    self.offsetY = (love.graphics.getHeight() - self.gridH) / 2

    self.grid = {}
    for i = 1, DIM do
        self.grid[i] = {}
        for j = 1, DIM do
            self.grid[i][j] = 0
        end
    end

    self.initial = {}
    self.solved = {}
    self.won = false

    -- self:generate()

    return self
end

function Sudoku:draw()
    local thickline = 5
    love.graphics.setLineWidth(thickline)
    love.graphics.rectangle("line",
        self.offsetX,
        self.offsetY,
        self.gridW,
        self.gridH
    )

    -- the lines at 0 and 9 are drawn as the square sides
    for i = 1, 8 do
        local thck = i % 3 == 0 and thickline or 0

        love.graphics.setLineWidth(thck)
        love.graphics.line(
            self.offsetX + self.cw * i,
            self.offsetY,
            self.offsetX + self.cw * i,
            self.offsetY + self.gridH
        )
        love.graphics.line(
            self.offsetX,
            self.offsetY + self.ch * i,
            self.offsetX + self.gridW,
            self.offsetY + self.ch * i
        )
    end
end

function Sudoku:resize(w, h)
    local mindim = math.min(w, h)
    self.cw = mindim / DIM
    self.ch = self.cw

    self.gridW = self.cw * DIM
    self.gridH = self.ch * DIM
    self.offsetX = (w - self.gridW) / 2
    self.offsetY = (h - self.gridH) / 2
end

return Sudoku
