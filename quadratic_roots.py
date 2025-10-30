
def roots(a,b,c):
    D = (b**2 - 4*a*c)
    alpha = (-b + D**(1/2))/(2*a)
    beta = (-b - D**(1/2))/(2*a)
    return alpha, beta

def main():
    print("plese provide coefficients (a,b,c) in (a)x^2 + (b)x + (c)")
    a,b,c = tuple(map(int, input("Give space saparated input as 'a b c': ").split(' ')))
    alpha,beta = roots(a,b,c)
    print(f"roots of ({a})x^2 + ({b})x + {c} are {alpha}, {beta}")

if __name__ == "__main__":
  main()
