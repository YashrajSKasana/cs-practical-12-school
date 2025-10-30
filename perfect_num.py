def is_perfect(num):
  p_deviser = []
  for i in range(1,num):
    if not num%i:
      p_deviser.append(i)
  return sum(p_deviser) == num

def main():
  num = int(input("Enter an Integer: "))
  if is_perfect(num):
    print(f"{num} is perfect :> yeeee!")
  else:
    print(f"{num} is not perfect :<")
if __name__ == "__main__":
  main()
