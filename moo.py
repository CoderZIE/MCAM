import numpy as np
from mred import MRED
from optimizationParams import optimizationParam
def multi_objective_function(x):
    """
    This function calculates four objectives: MRED, Latency, Area, and Power.
    The calculation is arbitrary for demonstration purposes. Replace these with your actual equations.
    """
    
    # Replace these with actual formulas for MRED, Latency, Area, and Power
    error = MRED(x)  # Example: Sum of squares
    
    # Calculate Latency, Area, and Power using the optimizationPram function
    Latency, Power, Area = optimizationParam(x)
    print(error, Latency, Area, Power)
    return error, Latency, Area, Power

# multi_objective_function([1, 2, 0])