import numpy as np
import simpy
import random

# Updated grid generation to simulate population density and customer distribution
def generate_grid(population, num_customers):
    grid = np.zeros((population, population))
    grid[0][0] = 2  # Depot

    customer_locations = []
    for _ in range(num_customers):
        while True:
            x, y = random.randint(0, population - 1), random.randint(0, population - 1)
            if grid[x, y] == 0:
                grid[x, y] = 1  # Mark as customer
                customer_locations.append((x, y))
                break
    return grid, customer_locations

# Example of generating a grid with customers
population = 10  # Grid size
num_customers = 5  # Number of customers
grid, customer_locations = generate_grid(population, num_customers)

print("Grid with Customers (1) and Depot (2):")
print(grid)
print("Customer Locations:", customer_locations)