def find_maximum_score_path(current_coordinate, destination_coordinate, map, current_score, maximum_score, current_path, maximum_path):
    if current_coordinate == destination_coordinate:
        if current_score > maximum_score:
            maximum_score = current_score
            maximum_path = current_path.copy()
        return maximum_score, maximum_path

    if current_coordinate[0] < destination_coordinate[0]:
        new_coordinate = (current_coordinate[0] + 1, current_coordinate[1])
        new_score = current_score + map[new_coordinate[0]][new_coordinate[1]]
        current_path.append(new_coordinate)
        maximum_score, maximum_path = find_maximum_score_path(new_coordinate, destination_coordinate, map, new_score, maximum_score, current_path, maximum_path)
        current_path.pop()
    
    if current_coordinate[1] < destination_coordinate[1]:
        new_coordinate = (current_coordinate[0], current_coordinate[1] + 1)
        new_score = current_score + map[new_coordinate[0]][new_coordinate[1]]
        current_path.append(new_coordinate)
        maximum_score, maximum_path = find_maximum_score_path(new_coordinate, destination_coordinate, map, new_score, maximum_score, current_path, maximum_path)
        current_path.pop()
    
    return maximum_score, maximum_path


def find_maximum_score(map, start, end):
    maximum_score, maximum_path = find_maximum_score_path(start, end, map, map[0][0], 0, [], [])
    print("Maximum score:", maximum_score)
    print("Maximum score path:", maximum_path)

map = [[25, 30, 25], [45, 15, 11], [1, 88, 15], [9, 4, 23]]
start = (0, 0)
end = (3, 2)
find_maximum_score(map, start, end)