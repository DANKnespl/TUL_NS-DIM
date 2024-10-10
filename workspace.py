import discreteMath as DIM

def cv01_gcd():
    #největší společný dělitel
    variables = [13240210688278768,792388011857606]
    DIM.gcd(variables,[True])

def cv02_functions():
    #Eulerova funkce a součet dělitelů
    variables = [445815279,19864845]
    gcd = DIM.gcd([DIM.euler_function(variables[0]),DIM.euler_function(variables[1])],[False])
    div_sum = DIM.sum_of_divisors(gcd)
    print(f"GCD(\u03A6({variables[0]}),\u03A6({variables[1]})) = {gcd}\n\u03A3(GCD(\u03A6({variables[0]}),\u03A6({variables[1]}))) = {div_sum}")


def cv03_dioph():
    #Loupežníci, přepadení a hromada mincí - idk nemám zadání
    variables = [5,7] #[x,y]
    constant=666
    n=0 #x=0, y=1
    print(f"({variables[0]}x) + ({variables[1]}y) = ({constant})")
    vals=DIM.diophantine_equation(variables,constant)
    DIM.extras.print_diophantine_equation(vals)
    k=DIM.extras.diaphantine_min_positive(vals[0][n],vals[1][n])
    xy=DIM.extras.diaphantine_solution(vals,k)
    print(f"x = {xy[0]}\ny = {xy[1]}")

if __name__=="__main__":
    cv01_gcd()
    cv02_functions()
    cv03_dioph()
