def DFS(graph):
    visited = set()
    ans = []
    def DFSUtil(v):
        visited.add(v)
        for neighbour in graph[v]:
            if neighbour not in visited:
                DFSUtil(neighbour)
        ans.insert(0, v)

    for v in graph:
        if v not in visited:
            DFSUtil(v)

    return ans

######################################################
def pow(a, n):
    if n == 0:
        return 1
    half = pow(a, n//2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half


##########################################################

def BFS(neighbors):
	# Initialize a dictionary to store the in-degree of each node
	in_degrees = {}
	
	# Initialize the in-degree of each node to zero
	for neighbor in neighbors.keys():
			in_degrees[neighbor] = 0

	# For each node in the graph
	for node, neighbor_list in neighbors.items():
		# For each neighbor of the node
		for neighbor in neighbor_list:
			# Increment the in-degree of the neighbor
			in_degrees[neighbor] += 1

	
	# Initialize a queue with all nodes that have no incoming edges
	queue = [node for node in in_degrees if in_degrees[node] == 0]


	
	# Initialize a list to store the topological sorting
	topological_sorting = []
	
	# Repeat the following until the queue is empty
	while queue:
		# Remove a node from the queue
		node = queue.pop(0)
		
		# Add the node to the list of sorted nodes
		topological_sorting.append(node)
    
		# For each outgoing edge from the removed node
		for neighbor in neighbors[node]:
			# Decrement the in-degree of the neighbor
			in_degrees[neighbor] -= 1
			
			# If the neighbor's in-degree becomes zero, add it to the queue
			if in_degrees[neighbor] == 0:
				queue.append(neighbor)
	
	return topological_sorting

#########################################################################################

def findNextEmptyCell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def isValid(grid, cell):
    row, col = cell
    value = grid[row][col]
    for i in range(9):
        if i != col and grid[row][i] == value:
            return False

    for j in range(9):
        if j != row and grid[j][col] == value:
            return False

    for i in range(3):
        for j in range(3):
            r = row - row % 3 + i
            c = col - col % 3 + j
            if r != row and c != col and grid[r][c] == value:
                return False
    return True

def solve_sudoku(grid):
    empty_cell = findNextEmptyCell(grid)
    if empty_cell is None:
        return True

    row, col = empty_cell

    for value in range(1, 10):
        grid[row][col] = value
        if isValid(grid, empty_cell) and solve_sudoku(grid):
            return True

    grid[row][col] = 0
    return False

######################################################################

if __name__ == "__main__":
    print("##### Q1 #####\n")
    print("Enter nodes of DAG:")
    nodes = input().split()
    graph = {}
    for node in nodes:
        print("Enter adjacents of " + node + ": ")
        adj = input().split()
        graph[node] = adj
    
    print("#### DFS ####\n")
    print(DFS(graph))
    print("#### BFS ####\n")
    print(BFS(graph))

    print("##### Q2 #####")
    print("Base:")
    base = int(input())
    print("Power:")
    power = int(input())
    print(pow(base, power))

    print("##### Q3 #####")
    board = []
    print("Enter the board")
    for _ in range(9):
        board.append([int(i) for i in input().split()])
    
    print("Solved board:")
    for l in solve_sudoku(board):
        print(l)
    