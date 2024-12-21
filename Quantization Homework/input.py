import sys
import ast

def main():
    if len(sys.argv) > 1:
        vector = ast.literal_eval(sys.argv[1])
        bits = int(sys.argv[2])
        beta = int(sys.argv[3])
        alpha = int(sys.argv[4])
      
        print(quantize(vector, bits, beta, alpha))


# Function to quantize the vector
def quantize(vector, bits, beta, alpha):
    
    # The cases are symmetric
    Zeta = 0;

    # Calculate the scaling factor
    step = (beta - alpha) / (2 ** bits - 1)

    # Quantize the vector
    for r in range(len(vector)):
        vector[r] = int(vector[r]/step) - Zeta
    
    return vector;

main()



