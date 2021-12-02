from mip import Model, INTEGER, maximize

# Create the model
model = Model("Timmerman")

# Create the variables x and y of type INTEGER
x = model.add_var(var_type=INTEGER)
y = model.add_var(var_type=INTEGER)

# Add the constraints
model += 5 * x + 4 * y <= 80
model += 10 * x + 20 * y <= 200
model += x >= 0
model += y >= 0

# Set the objective function of the model
model.objective = maximize(180 * x + 200 * y)

# Optimize
model.optimize()

# Print the values
print(f"Found the optimal value on ({x.x}, {y.x}), optimal value: {model.objective_value}")
