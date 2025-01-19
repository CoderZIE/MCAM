from moo import *
import csv
import itertools

from sko.GA import GA
import csv


# Define the fitness function for optimization
def fitness_function(params):
    # Rounding parameters since they must be integers (1, 2, 3)
    params = [round(x) for x in params]
    _, _, _, power = multi_objective_function(params)
    return power  # Minimize power

# Set up the Genetic Algorithm
ga = GA(
    func=fitness_function,        # Fitness function
    n_dim=3,                      # Number of parameters (3 elements in the array)
    size_pop=10,                  # Population size
    max_iter=5,                  # Number of iterations (generations)
    prob_mut=0.2,                 # Mutation probability
    lb=[0, 0, 0],                 # Lower bounds for each parameter
    ub=[2, 2, 2],                 # Upper bounds for each parameter
    precision=1                   # Precision to restrict to integers
)

# Run the Genetic Algorithm
best_params, best_power = ga.run()

# Get the best parameters as integers
best_params = [round(x) for x in best_params]

# Evaluate the best configuration
error, latency, area, power = multi_objective_function(best_params)

# Save results to CSV
csv_filename = "sko_ga_config_results.csv"
header = ["Param1", "Param2", "Param3", "Error", "Latency", "Area", "Power"]

with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerow([*best_params, error, latency, area, power])

# Print the best configuration
print("Best configuration:")
print(f"Params: {best_params}, Error: {error}, Latency: {latency}, Area: {area}, Power: {power}")

# Plot the convergence of the algorithm
import matplotlib.pyplot as plt

plt.plot(ga.all_history_Y)
plt.xlabel("Iteration")
plt.ylabel("Power")
plt.title("Convergence of Genetic Algorithm")
plt.savefig("ga_convergence.png")
