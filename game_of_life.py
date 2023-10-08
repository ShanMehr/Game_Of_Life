import random
import os
import time
# CSAI Meeting 10/8/2023

directions = [
    [-1, -1],  # top left
    [-1, 0],  # top
    [-1, 1],  # top right
    [0, -1],  # left
    [0, 1],  # right
    [1, -1],  # bottom left
    [1, 0],  # bottom
    [1, 1],  # bottom right
]

# randomly intialize the grid
def initialize_grid(grid, grid_size):
    for row_index in range(grid_size):
        for col_index in range(grid_size):
            grid[row_index][col_index] = random.randint(0, 1)
    return grid

def print_grid(grid, grid_size):
    for row_index in range(grid_size):
        for col_index in range(grid_size):
            print(
                "*" if grid[row_index][col_index] == 1 else ".",
                end=" ",
            )
        print()
    return grid

### THE PATTERN WILL BE USED TO DEMONSTRATE BRANCHES
def create_glider_pattern(grid, grid_size):
    grid[0][1] = 1
    grid[1][2] = 1
    grid[2][0] = 1
    grid[2][1] = 1
    grid[2][2] = 1
    return grid

def run_game(grid, grid_size):
    for row_index in range(grid_size):
        for col_index in range(grid_size):
            current_cell_val = grid[row_index][col_index]
            neighors_count = count_neighbors(grid, grid_size, row_index, col_index)

            """
                Perform in-place memory updates to the grid
                We use the code 2 to represent a cell that was once dead but is now alive
                We use the code 3 to represent a cell that was once alive but is now dead
            """
            if current_cell_val == 0:
                if neighors_count == 3:
                    grid[row_index][col_index] = 2
            # we use the code 3 to represent a cell that was once alive but is now dead
            elif current_cell_val == 1:
                if neighors_count < 2 or neighors_count > 3:
                    grid[row_index][col_index] = 3
    
    # reupdate the grid to reflect the changes
    for row_index in range(grid_size):
        for col_index in range(grid_size):
            current_cell_val = grid[row_index][col_index]
            if current_cell_val == 2:
                grid[row_index][col_index] = 1
            elif current_cell_val == 3:
                grid[row_index][col_index] = 0


def count_neighbors(grid, grid_size, x, y):
    count = 0
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if (
            # validate that the new x and y are within the grid
            new_x >= 0
            and new_x < grid_size
            and new_y >= 0
            and new_y < grid_size
            # validate that the new x and y are 1 or 3
            and (grid[new_x][new_y] == 1 or grid[new_x][new_y] == 3)
        ):
            count += grid[new_x][new_y]
    return count
        

def main():
    # we want to run the game for 1000 iterations
    game_iterations = 1000

    # we want to start with a 10x10 grid
    grid_size = 100
    grid = [[0] * grid_size for y in range(grid_size)]
    # grid = create_glider_pattern(grid, grid_size)
    grid = initialize_grid(grid,grid_size)

    iteration = 0
    for iteration in range(game_iterations):
        run_game(grid=grid, grid_size=grid_size)
        print_grid(grid, grid_size)
        time.sleep(0.3)
        os.system("clear")
        

if __name__ == "__main__":
    main()

