# A* search algorithm for Python

A generic implementation of the A* search algorithm in Python

## Usage example: Maze

### Import the library
Download and import Astar
```
from astar import Astar
mySearch = Astar()
```

### Define the operators
The operators are the functions which will be used to create the new nodes
```
up    = lambda p : [p[0], p[1] - 1] # Go up
down  = lambda p : [p[0], p[1] + 1]	# Go down
left  = lambda p : [p[0] - 1, p[1]]	# Go left
right = lambda p : [p[0] + 1, p[1]]	# Go right
```

### Set the operators
The operators must be passed as a list of lists or tuples, where the first element of each tuple is the operator description and the second element the function
```
descriptions = ['go up', 'go down', 'go left', 'go right']
operators = [up, down, left, right]
mySearch.operators = zip(descriptions, operators)
```

### Set the cost and heuristic functions
The cost function penalizes the usage of an operator. It should always have 2 parameters, the operator name and the node value before calling the operator.

The heuristic function calculates the estimate distance to the final state. It should always have a single parameter (the state)
```
mySearch.g = lambda o, p : 1 if o == 'go up' else 0 # 0 cost for all operators except 'go up'
mySearch.h = lambda p : abs(p[0] - 8 + p[1] - 1) # Heuristic: Manhattan distance to the destination point
```

### Set the status restrictions
In this example we want to avoid the walls, so we use the following function:
```
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
wsc.safe = safe
```

### Set the end checking function
We have to check whether the final state has been reached or not. This function must have a parameter (the current state) and must return _True_ if the current state is the final state and _False_ otherwise
```
wsc.end = lambda p : p == [8, 1]
```

### Set the equality function (Optional)
Some structures cannot be compared using '==', so we have to provide a function allowing us to compare such structures. By default the function is
```
mySearch.comparator = lambda a, b : a == b
```

### Search
Call the search() method on your instance of Astar
```
result = mySearch.search()
```
If the search has been successful, it will return a instance of the Node class with the following fields:

> **value:** The final state value

> **g:** The total cost

> **h:** The heuristic of the final state, always 0

> **path:** A list containing the description for all the operators called to reach the state

If the search has failed, it will return _None_

## License

This project is licensed under [GNU GPL v3.0](LICENSE)
