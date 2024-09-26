# maxProfit
# Linear Programming and Nonlinear Optimization Project

This project demonstrates the application of **Linear Programming (LP)** and **Nonlinear Optimization (NLP)** to solve a business optimization problem involving production and pricing strategies for two products. 

## 1. Problem Setup

### a. Objective:
Maximize the total profit by determining:
- How many units of each product to produce (**Linear Programming**).
- What price to set for each product to maximize demand and profit (**Nonlinear Optimization**).

### b. Inputs:
#### Resources:
- Raw materials available: **200 kg**.
- Labor hours available: **150 hours**.

#### Product Information:
- **Product 1**: Requires **2 kg** of material and **3 hours** of labor per unit.
- **Product 2**: Requires **4 kg** of material and **2 hours** of labor per unit.

#### Cost per Unit:
- **Product 1**: $10 production cost per unit.
- **Product 2**: $15 production cost per unit.

#### Demand Function (Nonlinear):
The demand for the products decreases as the price increases:
- **Product 1**: 𝐷₁(𝑝₁) = 100 - 2𝑝₁
- **Product 2**: 𝐷₂(𝑝₂) = 150 - 3𝑝₂

Where 𝑝₁ and 𝑝₂ represent the prices for products 1 and 2, respectively.

### Profit Calculation:
Profit = (Price - Production Cost) * Units Sold for each product.

## 2. Constraints:

1. **Material Constraint**: 
   - 2x₁ + 4x₂ ≤ 200 (where x₁ and x₂ are the units of Product 1 and Product 2 produced).
   
2. **Labor Constraint**: 
   - 3x₁ + 2x₂ ≤ 150.
   
3. **Demand Constraint**: 
   - x₁ ≤ 𝐷₁(𝑝₁) and x₂ ≤ 𝐷₂(𝑝₂) (units produced cannot exceed demand).

## 3. Formulating the Optimization Problem:

### a. Linear Programming (Production Quantities):
Objective Function: Maximize Profit = (𝑝₁ - 10) * x₁ + (𝑝₂ - 15) * x₂.

**Constraints**:
- 2x₁ + 4x₂ ≤ 200 (Material constraint).
- 3x₁ + 2x₂ ≤ 150 (Labor constraint).
- x₁ ≤ 𝐷₁(𝑝₁) = 100 - 2𝑝₁.
- x₂ ≤ 𝐷₂(𝑝₂) = 150 - 3𝑝₂.

### b. Nonlinear Optimization (Pricing Strategy):
The price affects the demand, and the demand affects the total units sold. The objective is to find the prices 𝑝₁ and 𝑝₂ that maximize the total profit:

Profit = (𝑝₁ - 10) * x₁ + (𝑝₂ - 15) * x₂.

Where x₁ and x₂ are related to demand by the nonlinear functions:
- x₁ = min(𝐷₁(𝑝₁), (200 - 4x₂) / 2).
- x₂ = min(𝐷₂(𝑝₂), (150 - 3x₁) / 2).

## 4. Solving the Problem Using Python

### a. Python Code Example for Linear Programming:

```python
import pulp

# Create an LP maximization problem
lp_prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Define decision variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')  # Product 1 quantity
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')  # Product 2 quantity

# Define prices (can be variables in nonlinear optimization)
p1 = 25  # price for product 1
p2 = 35  # price for product 2

# Objective function: Maximize profit
lp_prob += (p1 - 10) * x1 + (p2 - 15) * x2, "Total Profit"

# Add constraints (Material and Labor)
lp_prob += 2 * x1 + 4 * x2 <= 200, "Material Constraint"
lp_prob += 3 * x1 + 2 * x2 <= 150, "Labor Constraint"

# Solve the linear program
lp_prob.solve()

# Output the results
print(f"Optimal Production for Product 1: {pulp.value(x1)} units")
print(f"Optimal Production for Product 2: {pulp.value(x2)} units")
print(f"Total Profit: ${pulp.value(lp_prob.objective)}")
```

## b. Python Code Example for Nonlinear Optimization

```python
from scipy.optimize import minimize

# Define the demand functions
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
```

### 5. Results & Interpretation:

- **Optimal Production Quantities**: 
  We get the optimal number of units to produce for each product from the linear programming model.

- **Optimal Pricing Strategy**: 
  From the nonlinear optimization, we obtain the optimal prices for the products that maximize the overall profit.

#### Comparison:
- Analyze how pricing affects demand and how production constraints influence profitability.

### 6. Extensions:

- You can extend the model to include:
  - More products.
  - Additional resource constraints (e.g., machine hours).
  - Stochastic demand to handle uncertainty.

- **Introduce competition**: 
  Your pricing strategy could impact competitors' pricing and vice versa, making the model more dynamic and realistic.

