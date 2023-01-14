class Player:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

def find_winner(players):
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

# Create the players
p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charlie")
p4 = Player("Dave")
p6 = Player("semih")
p7 = Player("batuhan")
p8 = Player("ozanksflksdlf")

# Find the winner
winner = find_winner([p1, p2, p3, p4, p6, p7, p8])
print(winner.name)  # Outputs "Charlie"