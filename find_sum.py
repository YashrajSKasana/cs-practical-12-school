def main():
  nums = input("Enter 'space saperated' Numbers: ").split(' ')
  print(f"SUM: {sum(map(int, nums))}")
if __name__ == "__main__":
  main()
