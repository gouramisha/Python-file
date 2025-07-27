  n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Start with total faces from all cubes in this stack
                    area += 6 * grid[i][j]
                    # Subtract 2 faces for each internal cube (vertical connection)
                    area -= 2 * (grid[i][j] - 1)

                    # Check and subtract shared faces with top neighbor
                    if i > 0:
                        area -= 2 * min(grid[i][j], grid[i - 1][j])
                    # Check and subtract shared faces with left neighbor
                    if j > 0:
                        area -= 2 * min(grid[i][j], grid[i][j - 1])

        return area