from scipy.optimize import minimize

def demand_p1(price):
    return max(100 - 2 * price, 0)

def demand_p2(price):
    return max(150 - 3 * price, 0)

# Define the objective function (profit to maximize)
def objective(prices):
    p1, p2 = prices
    x1 = demand_p1(p1)
    x2 = demand_p2(p2)
    return -(p1 - 10) * x1 - (p2 - 15) * x2  # Negative for minimization

# Set initial guesses for prices
initial_guess = [20, 30]

# Optimize the pricing strategy
result = minimize(objective, initial_guess, bounds=[(10, 50), (15, 50)])

# Output the optimized prices and profit
optimal_p1, optimal_p2 = result.x
print(f"Optimal Price for Product 1: ${optimal_p1}")
print(f"Optimal Price for Product 2: ${optimal_p2}")
print(f"Maximized Profit: ${-result.fun}")
