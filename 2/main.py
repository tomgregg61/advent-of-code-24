file = open("./2/puzzle.txt", "r")
data = [line.strip().split() for line in file]
reports = [(list(map(int, row))) for row in data]

count = 0

def f(report):
  diffs = [a - b for a, b in zip(report, report[1:])]
  return all(1 <= a <= 3 for a in diffs) or all(-1 >= a >= -3 for a in diffs)

for report in reports:
  if any(f(report[:i] + report[i+1:]) for i in range(len(report))):
    count+=1

print(count)