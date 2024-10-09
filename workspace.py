import discreteMath as DIM

if __name__=="__main__":
    variables = [5,7]
    constant=666
    n=0
    print(f"({variables[0]}x) + ({variables[1]}y) = ({constant})")
    vals=DIM.diophantine_equation(variables,constant)
    DIM.extras.print_diophantine_equation(vals)
    k=DIM.extras.diaphantine_min_positive(vals[0][n],vals[1][n])
    xy=DIM.extras.diaphantine_solution(vals,k)
    print(f"x = {xy[0]}\ny = {xy[1]}")