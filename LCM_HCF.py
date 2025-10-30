from math import gcd, lcm
from functools import reduce
def main():
  mode = int(input("Press (1) for LCM and (2) for HCF mode: "))
  if mode not in {1,2}:
    print("invalid mode :<")
  else:
    nums = map(int, input("Give 'space saparated' Integers: ").split(' '))
    if mode == 1:
      print(reduce(lambda x,y: lcm(x,y), nums))
    elif mode == 2:
      print(reduce(lambda x,y: gcd(x,y), nums))
if __name__ == "__main__":
  main()
