players = ['bob', 'steve', 'michael', 'tom', 'eli', 'bill', 'dave']
#slice and print the names of the first 3 players
print("Here are the names of the first three players on my team:")

for player in players[:3]:
    print(player.title())


print("Here are the names of the third to the 5th player:")
for player in players[2:5]:
    print(player.title())