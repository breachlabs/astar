from astar import Astar

# Operator definitions
up    = lambda p : [p[0], p[1] - 1] # Go up
down  = lambda p : [p[0], p[1] + 1]	# Go down
left  = lambda p : [p[0] - 1, p[1]]	# Go left
right = lambda p : [p[0] + 1, p[1]]	# Go right

# Set list values
opcodes   = ['^', 'v', '<', '>']
operators = [up, down, left, right]

# Location safety checker function. Tests whether the new location is possible or not
def safe(pt):
	# If the point is out of bounds, it is not safe
	if pt[0] < 0 or pt[0] > 13:
		return False
	if pt[1] < 0 or pt[1] > 11:
		return False
	
	# Test if the new location is a wall
	map = [#  0    1    2    3    4    5    6    7    8    9    10   11   12   13
			['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],	# 0
			['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],	# 1
			['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],	# 2
			['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],	# 3
			['#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],	# 4
			['#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],	# 5
			['#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#'],	# 6
			['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],	# 7
			['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],	# 8
			['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],	# 9
			['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],	# 10
			['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']	# 11
		  ]
	return map[pt[1]][pt[0]] == ' '

# Create new instance
wsc = Astar()

# Set attributes
wsc.operators  = zip(opcodes, operators) 							# Operator and operator description list
wsc.safe       = safe				     							# Check whether a state is safe or not
wsc.start      = [1, 10]                  							# Start point
wsc.end        = lambda p    : p == [8, 1] 							# Lambda function used to check if the destination point has been reached
wsc.g          = lambda o, p :  1 if o == '^' else 0               	# 0 cost for all operators except '^'
wsc.h          = lambda p    : abs(p[0] - 8 + p[1] - 1)	            # Heuristic: Manhattan distance
wsc.comparator = lambda l1, l2 : l1 == l2							# Function used to compare points

# Search the shortest path
result = wsc.search()
if result == None:
    print 'Could not find the shortest path'
else:
    print 'The shortest path is: ' + str(result.path)
