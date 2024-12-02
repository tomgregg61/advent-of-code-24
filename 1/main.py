file = open("./1/puzzle.txt", "r")
data = [line.strip().split() for line in file]

list1 = [int(row[0]) for row in data]
list2 = [int(row[1]) for row in data]

count = 0

for num in list1:
  for item in list2:
    if(num == item):
      count+= num

print(count)