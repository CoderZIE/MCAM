from moo import *
import csv
import itertools

range_values = [0, 1, 2]

# Generate all possible configurations
all_configs = list(itertools.product(range_values, repeat=3))
print(all_configs)
# Initialize a list to store the results
results = []

# Iterate through all configurations
for config in all_configs:
    error, latency, area, power = multi_objective_function(config)
    results.append([*config, error, latency, area, power])

# Save the results to a CSV file
csv_filename = "config_results.csv"
header = ["Param1", "Param2", "Param3", "Error", "Latency", "Area", "Power"]

with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(results)

# Find the configuration with the least power
min_power_row = min(results, key=lambda x: x[-1])

# Print the configuration with the least power
print("Configuration with the least power:")
print(f"Params: {min_power_row[:3]}, Error: {min_power_row[3]}, Latency: {min_power_row[4]}, Area: {min_power_row[5]}, Power: {min_power_row[6]}")