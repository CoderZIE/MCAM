import numpy as np
from mred import MRED
from optimizationParams import optimizationParam
from accuracy import accuracy

def multi_objective_function(x):
    """
    This function calculates four objectives: MRED, Latency, Area, and Power.
    The calculation is arbitrary for demonstration purposes. Replace these with your actual equations.
    """
    
    # Replace these with actual formulas for MRED, Latency, Area, and Power
    error = MRED(x)  # Example: Sum of squares
    error_workload =  1 - accuracy(x)  
    # Calculate Latency, Area, and Power using the optimizationPram function
    Latency, Power = optimizationParam(x)
    print(error, Latency, Power)
    return error, Latency, Power, error_workload

multi_objective_function([0, 12, 2, 3, 4, 5, 6, 7, 8, 9, 20, 11, 12, 13, 14, 15, 16, 17, 18, 21])