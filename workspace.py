import discreteMath as DIM

def cv01_gcd():
    #největší společný dělitel
    print("Největší společný dělitel")
    variables = [13240210688278768,792388011857606]
    DIM.gcd(variables,[True])

def cv02_functions():
    #Eulerova funkce a součet dělitelů
    print("\nEulerova funkce a součet dělitelů")
    variables = [445815279,19864845]
    gcd = DIM.gcd([DIM.euler_function(variables[0]),DIM.euler_function(variables[1])],[False])
    div_sum = DIM.sum_of_divisors(gcd)
    print(f"GCD(\u03A6({variables[0]}),\u03A6({variables[1]})) = {gcd}\n\u03A3(GCD(\u03A6({variables[0]}),\u03A6({variables[1]}))) = {div_sum}")


def cv03_dioph():
    #Loupežníci, přepadení a hromada mincí - idk nemám zadání
    print("\nLoupežníci, přepadení a hromada mincí")
    variables = [5,7] #[x,y]
    constant=666
    n=0 #x=0, y=1
    print(f"({variables[0]}x) + ({variables[1]}y) = ({constant})")
    vals=DIM.diophantine_equation(variables,constant)
    DIM.extras.print_diophantine_equation(vals)
    k=DIM.extras.diaphantine_min_positive(vals[0][n],vals[1][n])
    xy=DIM.extras.diaphantine_solution(vals,k)
    print(f"x = {xy[0]}\ny = {xy[1]}")
    
def cv04_aproximation():
    print("\nAproximace pomocí aproximace I guess")
    multiplier = 20
    shifter=pow(10,multiplier)
    phi = DIM.math.floor((1 + 5 ** 0.5) / 2*shifter)
    DIM.continued_fraction([phi,shifter],50)
    DIM.continued_fraction([phi,shifter],51)
    DIM.continued_fraction([phi,shifter],52)

def cv05_Zap1():
    print("-------Uloha 1---------------")
    variables = [7,101] #[x,y]
    constant=1001
    n=0 #x=0, y=1
    print(f"({variables[0]}x) + ({variables[1]}y) = ({constant})")
    vals=DIM.diophantine_equation(variables,constant)
    DIM.extras.print_diophantine_equation(vals)

    print("-------Uloha 2---------------")
    number = 16632
    print("Euler = ",DIM.euler_function(number),"\nMoebius = ",DIM.moebius_function(number),"\nSum = ",DIM.sum_of_divisors(number),"\nNum = ",DIM.num_of_divisors(number))
    
    print("-------Uloha 3---------------")
    multiplier = 7
    shifter=pow(10,multiplier)
    phi = DIM.math.floor(27182818)
    DIM.continued_fraction([phi,shifter],1)
    DIM.continued_fraction([phi,shifter],2)
    DIM.continued_fraction([phi,shifter],3)
    DIM.continued_fraction([phi,shifter],4)
    DIM.continued_fraction([phi,shifter],5)
    
    print("-------Uloha 4---------------")
    numbers = [115115,30498]
    DIM.gcd(numbers,[True])
    DIM.lcm(numbers)

if __name__=="__main__":
    #cv01_gcd()
    #cv02_functions()
    #cv03_dioph()
    #cv04_aproximation()
    cv05_Zap1()