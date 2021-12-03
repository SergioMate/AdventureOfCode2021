def addWindow(depths, window, start=0):
  return sum(depths[start:window+start])

def numberOfIncrements(depths, window=1):
  depths = list(map(int, depths))
  increments = 0
  prevDepth = addWindow(depths, window)
  for i in range(0,len(depths)):
    depth = addWindow(depths, window, i)
    if prevDepth < depth:
      increments += 1
    prevDepth = depth
  return increments

if __name__ == '__main__':
  from app.utils import file2list
  depths = file2list("input.txt")
  print("part 1: " + str(numberOfIncrements(depths)))
  print("part 2: " + str(numberOfIncrements(depths, 3)))
  input()
