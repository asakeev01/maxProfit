import pulp

lp_prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')

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
