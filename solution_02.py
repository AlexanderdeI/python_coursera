import sys

 
num_steps = int(sys.argv[1])

def create_stairway(stairs):
	sharps = 0
	for st in range(stairs):
		stairs -= 1
		sharps += 1
		print(" " * stairs + "#" * sharps)

if __name__ == "__main__":
	create_stairway(num_steps)
