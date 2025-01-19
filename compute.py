from helper import base_code 


# Define the compressor functions
compressor_variants = ["ahmad", "akbari", "ACFGII_1"]

def generate_code(vector):
    """
    Replaces the compressor calls in column 8 based on the input vector.

    Args:
        vector (list): A list of size 3 indicating which compressor to use for each position.
    Returns:
        str: Modified Python code.
    """
    if len(vector) != 3:
        raise ValueError("Input vector must be of size 3.")
    
    modified_code = base_code
    
    # Replace placeholders with the selected compressors
    modified_code = modified_code.replace("ACFGII_1(L[0][0],L[1][1],L[2][2],L[3][3])",f"{compressor_variants[vector[0]]}(L[0][0],L[1][1],L[2][2],L[3][3])")
    modified_code = modified_code.replace("ACFGII_1(L[4][4],L[5][5],L[6][6],L[7][7])", f"{compressor_variants[vector[1]]}(L[4][4],L[5][5],L[6][6],L[7][7])")
    modified_code = modified_code.replace("ACFGII_1(x4,x5,y1,y2)", f"{compressor_variants[vector[2]]}(x4,x5,y1,y2)")
    
    return modified_code
