############## q1 ######################

def sub_match(left, right):
    if left == right:
        return left
    j=0
    result = ""
    for i in range(0, len(left)):
        if left[i] == right[j]:
            result += left[i]
            j += 1
        else:
            return result

def sub_common(strings):
    if len(strings) == 1:
        return strings[0]
    
    half = len(strings) // 2
    left = strings[:half]
    right = strings[half:]
    
    left = sub_common(left)
    right = sub_common(right)
    
    sc = sub_match(left, right)
    return sc

################# q2 a ######################3

def max_profit_divide_conquer(prices):
    if len(prices) <= 1:
        return 0

    mid = len(prices) // 2
    left_prices = prices[:mid]
    right_prices = prices[mid:]

    left_profit = max_profit_divide_conquer(left_prices)
    right_profit = max_profit_divide_conquer(right_prices)

    cross_profit = 0
    left_min = float('inf')
    for price in left_prices:
        left_min = min(left_min, price)
    right_max = 0
    for price in right_prices:
        right_max = max(right_max, price)
    cross_profit = right_max - left_min

    return max(left_profit, right_profit, cross_profit)


####################### q2 b ####################

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

######################## q3 ############################

def longest_increasing_subarray(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)  

########################## q4 a #######################

def max_score_dynamic(map):
    scores = [[0 for j in range(len(map[0]))] for i in range(len(map))]
    
    if len(map) == 1:
        for j in range(len(map[0])):
            scores[0][j] = scores[0][j-1] + map[0][j]
    elif len(map[0]) == 1:
        for i in range(len(map)):
            scores[i][0] = scores[i-1][0] + map[i][0]
    else:
        for i in range(len(map)):
            scores[i][0] = scores[i-1][0] + map[i][0]
        for j in range(len(map[0])):
            scores[0][j] = scores[0][j-1] + map[0][j]
    for i in range(1, len(map)):
        for j in range(1, len(map[0])):
            scores[i][j] = max(scores[i-1][j], scores[i][j-1]) + map[i][j]

    return scores[-1][-1]

########################## q4 b ##########################33


def max_score_greedy(map):
    i = 0
    j = 0
    score = map[i][j]
    
    while (i, j) != (len(map)-1, len(map[0])-1):
        down_score = float('-inf') if i+1 >= len(map) else map[i+1][j]
        right_score = float('-inf') if j+1 >= len(map[0]) else map[i][j+1]
        
        if down_score > right_score:
            i += 1
        else:
            j += 1 
        
        score += map[i][j]
    return score

if __name__ == "__main__":

    print("################# q1 #################")
    inp = []
    n = int(input("Enter size of the array: "))
    print("Enter the elements of array")
    for _ in range(n):
        inp.append(input())
    print("Longest common string: ", sub_common(inp))


    
    print("################# q2 a #################")
    arr = []
    n2 = int(input("Enter size of the array: "))
    print("Enter the elements of array")
    for _ in range(n2):
        arr.append(int(input()))
    print("Maximum profit with divide-and-conquer algorithm:", max_profit_divide_conquer(arr))



    print("################# q2 b #################")
    print("Maximum profit with not divide-and-conquer algorithm:", max_profit(arr))



    print("################# q3 #################")
    lis = []
    n3 = int(input("Enter size of the array: "))
    print("Enter the elements of array")
    for _ in range(n3):
        lis.append(int(input()))
    print("Length of longest increasing subarray: ", longest_increasing_subarray(lis))



    print("################# q4 a#################")
    board = []
    dimens = int(input("Enter first dimension of the board: "))
    print("Enter the board")
    for _ in range(dimens):
        board.append([int(i) for i in input().split()])
    print("\nmaximum score with dynamic programming: ", max_score_dynamic(board))



    print("################ q4 b #################")
    print("\nmaximum score with greedy algorithm: ", max_score_greedy(board))