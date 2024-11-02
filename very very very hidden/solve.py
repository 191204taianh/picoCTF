# Define the input strings
string1 = "HEYWherE(IS_tNE)50uP?^DId_YOu(]E@t*mY_3RD()B2g3l?"
string2 = "8,:8+14>Fx0l+$*KjVD>[o*.;+1|*[n&2G^201l&,Mv+_'T_B"

# Ensure both strings have the same length
if len(string1) != len(string2):
    raise ValueError("Both strings must have the same length")

# Perform XOR operation character by character
result = ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(string1, string2)])

# Print the result
print(result)
