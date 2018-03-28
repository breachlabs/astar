from copy import copy # Copy lists

class Node:
    def __init__(self):
        self.value = None		# Node value
        self.g = 0				# Cost to reach the node
        self.h = 0				# Heuristic value to end state
        self.path = []			# Path to reach the value
        
    def __str__(self):
        return 'value:' + str(self.value) + '\ng: ' + str(self.g) + '\nh: ' + str(self.h) + '\npath: ' + str(self.path)

class Astar:
    def __init__(self, debug = False):
        self.start = None		                # Start state
        self.end = None			                # End state checker function
        self.operators = []		                # Zipped list (opcode, operator)
        self.safe = None		                # Safety check function
        self.g = None			                # Cost function
        self.h = None			                # Heuristic function
        self.comparator = lambda a, b : a == b  # Function to compare 2 states. Uses the equality by default
        self._debug = debug		                # Set debug mode

    def _descendants(self, node):
        result = []
        for op in self.operators:
            descendantNode = self._descendant(node, op)
            if descendantNode != None:
                result.append(descendantNode)
        return result

    def _isBetter(self, node, list):
        if len(list) == 0:
            return True

        for n in list:
            if self.comparator(n.value, node.value) and node.g + node.h >= n.g + n.h:
                return False
        return True

    def _descendant(self, node, operator):
        newValue = operator[1](node.value)
        if self.safe(newValue):
            newNode = Node()
            newNode.value = newValue
            newNode.path = copy(node.path)
            newNode.path.append(operator[0])
            newNode.g = node.g + self.g(operator[0], node.value)
            newNode.h = self.h(newValue)
            return newNode
        return None

    def search(self):
        # Make sure that all the needed functions have been assigned
        if self.g == None:
            raise NotImplementedError('Cost function not implemented')
        if self.h == None:
            raise NotImplementedError('Heuristic function not implemented')
        if self.end == None:
            raise NotImplementedError('End checking function not implemented')
        if self.safe == None:
            raise NotImplementedError('Safety checking function not implemented')

        startNode = Node()
        startNode.value = self.start
        startNode.h = self.h(self.start)

        openNodes = [startNode]
        closedNodes = []

        while len(openNodes) > 0:
            currentNode = openNodes.pop(0)
            closedNodes.append(currentNode)
            if self._debug:
                print "[DEBUG] Current node: " + str(currentNode.value)
            if self.end(currentNode.value):
                if self._debug:
                    print "[DEBUG] The end has been successfully reached."
                return currentNode
            else:
                descendantNodes = self._descendants(currentNode)
                descendantNodes = filter(lambda node : self._isBetter(node, openNodes) and self._isBetter(node, closedNodes), descendantNodes)
                descendantNodes.reverse()
                openNodes += descendantNodes
                openNodes = sorted(openNodes, key = lambda n : n.g + n.h)
        if self._debug:
            print "[DEBUG] The search has finished without finding an optimal solution."
        return None