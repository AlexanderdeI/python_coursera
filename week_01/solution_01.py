import sys


digit_string = sys.argv[1]
digits_sum = 0

for digit in digit_string:
	digits_sum += int(digit)
	
if __name__ == "__main__":
	print(digits_sum)
