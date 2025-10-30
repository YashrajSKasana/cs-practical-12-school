import math, statistics
def main():
  scores = list(map(int, input("Enter 'space saparated' Numbers: ").split(' ')))
  mean = statistics.mean(scores)
  median = statistics.median(scores)
  stdev = statistics.stdev(scores)

  print("Mean:", round(mean, 2))
  print("Median:", median)
  print("Standard Deviation:", round(stdev, 2))
  print("Highest Score (Rounded):", math.ceil(max(scores)))
  print("Lowest Score (Rounded):", math.floor(min(scores)))
if __name__ == "__main__":
  main()
