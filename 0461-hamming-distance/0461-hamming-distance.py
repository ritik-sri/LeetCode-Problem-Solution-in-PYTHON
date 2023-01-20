class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        # Convert numbers in binary and put them in a list
        x = list(bin(x)[2:])
        y = list(bin(y)[2:])
        
        # Padding if it the case
        if len(x) < len(y):
            x = ["0"]*(len(y)-len(x)) + x
        else:
            y = ["0"]*(len(x)-len(y)) + y
        print("".join(x),"".join(y))
        # Computing the Hamming distance
        hamming_distance = 0
        for x_digit, y_digit in zip(x,y):

            if x_digit != y_digit:
                hamming_distance += 1
        
        return hamming_distance
