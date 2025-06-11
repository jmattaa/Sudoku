local DIM = 9

---@class Grid
---@field cw number
---@field ch number
---@field grid number[][]
---@field initial number[][]
---@field solved number[][]
---@field won boolean
local Grid = {}
Grid.__index = Grid

---@return Grid
function Grid.new()
    ---@type Grid
    local self = setmetatable({}, Grid)
    self.cw = love.graphics.getWidth() / DIM
    self.ch = love.graphics.getHeight() / DIM

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

function Grid:draw()
    for i = 1, DIM do
        for j = 1, DIM do
            local x = self.cw * (j - 1)
            local y = self.ch * (i - 1)
            love.graphics.rectangle("line", x, y, self.cw, self.ch)
        end
    end
end


return Grid
