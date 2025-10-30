def is_leap_year(year):
  if year%4:
    return False
  elif year%100:
    return True
  else:
    if year%400:
      return False
    else:
      return True

def main():
  year = int(input("Give a year: "))
  if is_leap_year(year):
    print(f"{year} is a leap year :>")
  else:
    print(f"{year} is not a leap year :<")
if __name__ == "__main__":
   main()
