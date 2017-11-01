import sys 


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def solve_equation(a, b, c):
	d = b * b - 4 * a * c
	if d > 0:
		x1 = (-b + d ** 0.5) / 2 * a
		x2 = (-b - d ** 0.5) / 2 * a
		return ("{0}\n{1}".format(int(x1), int(x2)))
	elif d == 0:
		x1 = x2 = -b / 2 * a
		return ("{0}\n{1}".format(int(x1), int(x2)))
	else:
		return ("Нет корней")
		
		
if __name__ == "__main__":
	print(solve_equation(a, b, c))
