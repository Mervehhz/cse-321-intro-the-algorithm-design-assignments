def topologicalSort(neighbors):
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


graph = {
		'CSE 102': ['CSE 241'],
		'CSE 241': ['CSE 222'],
		'CSE 211': ['CSE 321'],
		'CSE 222': ['CSE 321'],
		'CSE 321': ['CSE 422'],
		'CSE 422': []
	}
# Obtain a topological sorting of the tasks in the project
sorting = topologicalSort(graph)

# Print the topological sorting
print(sorting)

# Output: ['task1', 'task3', 'task2', 'task4', 'task5']

