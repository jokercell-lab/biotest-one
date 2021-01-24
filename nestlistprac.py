# state_of_taiwan = ["Taipei", "Taichung", "Changhua", "Kaushung"]
# print(len(state_of_taiwan))

#game of chess

row1 = ["x","x","x","x","x","x","x","x"]
row2 = ["x","x","x","x","x","x","x","x"]
row3 = ["x","x","x","x","x","x","x","x"]
row4 = ["x","x","x","x","x","x","x","x"]
row5 = ["x","x","x","x","x","x","x","x"]
row6 = ["x","x","x","x","x","x","x","x"]
row7 = ["x","x","x","x","x","x","x","x"]
row8 = ["x","x","x","x","x","x","x","x"]
map = [row1,row2,row3,row4,row5,row6,row7,row8]
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")
position = input("where do you want to put? ")

x = int(position[0])
y = int(position[1])
# xp = map[x-1]
# yp = map[y-1]
map[y-1][x-1] = "0"
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")