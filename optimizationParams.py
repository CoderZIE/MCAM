import yaml

def optimizationParam(x):
    """
    This function calculates the Latency, Area, and Power using the params values in parameter.yaml
    for the compressors corresponding to the indices in x.
    
    :param x: List of indices corresponding to the compressors
    :return: Dictionary with total latency, power, and area
    """
    # Load parameters from parameters.yaml
    with open("parameters.yaml", "r") as file:
        params = yaml.safe_load(file)
    
    # Initialize totals
    total_latency = 0
    total_power = 0
    
    # Iterate through the indices in x
    for index in x:
        if 0 <= index < len(params['compressors']):
            compressor = params['compressors'][index]
            total_latency += compressor['latency']
            total_power += compressor['power']
        else:
            raise ValueError(f"Index {index} is out of range for compressor_variants.")
    
    # Return the calculated totals
    return {
        total_latency,
        total_power
    }
