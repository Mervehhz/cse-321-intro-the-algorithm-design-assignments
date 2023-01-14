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
	print(ans)


if __name__ == "__main__":
	graph = {
		'CSE 102': ['CSE 241'],
		'CSE 241': ['CSE 222'],
		'CSE 211': ['CSE 321'],
		'CSE 222': ['CSE 321'],
		'CSE 321': ['CSE 422'],
		'CSE 422': []
	}
	DFS(graph)
