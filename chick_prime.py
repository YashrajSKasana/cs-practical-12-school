def is_prime(num):
  if num == 1: return True
  for i in range(2,num):
    if not num%i:
      return False
  return True

def main():
 num = int(input("Enter a nuber: "))
 if is_prime(num):
    print(f"{num} is a prime number.")
 else:
    print(f"{num} is not a prime number.")

if __name__ == "__main__":
   main()
