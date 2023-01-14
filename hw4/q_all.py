import math

"##################### Q1 #######################"

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



"##################### Q2 #######################"

def median(array):
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]

    half = len(array) // 2
    left = array[:half]
    right = array[half:]

    median_left = median(left)
    median_right = median(right)

    if len(array) % 2 == 1:
        return array[half]
    else:
        return (array[half - 1] + array[half]) / 2



"##################### Q3 part1 #######################"

class Player:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

def find_winner_ll(players):
    head = players[0]
    current = head
    for i in range(1, len(players)):
        current.next = players[i]
        players[i].prev = current
        current = current.next
    current.next = head
    head.prev = current

    pointer = head

    while pointer.next != pointer:
        to_eliminate = pointer.next
        pointer.next = to_eliminate.next
        to_eliminate.next.prev = pointer

        print(f"{pointer.name} eliminates {to_eliminate.name}")

        pointer = pointer.next

    return pointer



"##################### Q3 part2 #######################"

def find_winner_dc(n: int, k: int) -> int:  
    if n == 2:
        return 2 if k == 1 else 1
    survivor_position_in_subgroup = find_winner_dc(n - n // 2, k)
    if survivor_position_in_subgroup > n // 2:
        return (survivor_position_in_subgroup - 1) * 2
    else:
        return survivor_position_in_subgroup * 2 - 1



def driver():

    print("##################### Q1 #######################")
    num_rows = int(input("Enter the number of rows: "))
    num_columns = int(input("Enter the number of columns: "))
    arr = [[0 for j in range(num_columns)] for i in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_columns):
            arr[i][j] = int(input("Enter the element for row {} and column {}: ".format(i+1, j+1)))

    start = (0, 0)
    end = (num_rows-1, num_columns-1)
    maximum_score, maximum_path = find_maximum_score_path(start, end, arr, arr[0][0], 0, [], [])
    print("Maximum score:", maximum_score)
    print("Maximum score path:", maximum_path)



    print("\n\n##################### Q2 #######################")
    size = int(input("Enter the size of the array: "))
    arr_2 = [0 for i in range(size)]
    for i in range(size):
        arr_2[i] = int(input("Enter the element for index {}: ".format(i)))
    arr_2.sort()
    print("median: ", median(arr_2))



    print("\n\n##################### Q3 part1 #######################")
    count = int(input("Enter count of players: "))
    arr_3 = [0 for i in range(count)]
    for i in range(count):
        arr_3[i] = Player(input("Enter player {} name: ".format(i)))
    winner = find_winner_ll(arr_3)
    print(winner.name,"is the winner")



    print("\n\n##################### Q3 part2 #######################")
    count2 = int(input("Enter count of players: "))
    arr_4 = [0 for i in range(count2)]
    for i in range(count2):
        arr_4[i] = "Enter player p{} name: ".format(i+1)
    winner = find_winner_dc(count2, 1)
    print(arr_4[winner-1],"is the winner")

if __name__ == "__main__":
    driver()