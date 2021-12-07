from mip import Model, MAXIMIZE, CONTINUOUS

model = Model(sense=MAXIMIZE)

# Variables
x1 = model.add_var(var_type=CONTINUOUS, lb=0, ub=7)
x2 = model.add_var(var_type=CONTINUOUS, lb=0, ub=6)

# Constraints
model += x1 + x2 <= 9
model += 3 * x1 + x2 <= 18

# Objective function
model.objective = 3 * x1 + 2 * x2

# Solve
model.optimize()

# Print results, should be 4.5
print(x1.x)
print(x2.x)