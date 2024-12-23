

def print_diophantine_equation(solutions:list):
    print(f"x = ({solutions[0][0]}) + ({solutions[1][0]}k)\ny = ({solutions[0][1]}) + ({solutions[1][1]}k)")
def print_GCD_history(history:list,values:list):
    """Print of all the steps of calculating GCD
    Args:
        history (list): Steps of GCD calculation
        values (list): Numbers whose GCD is calculated
    """
    divisor = None
    for _,step in enumerate(history):
        print("")
        for _, step2 in enumerate(step):
            print(f"{step2[0]}/{step2[1]} => {step2[2]}")
            divisor=step2[1]
    print(f"\nGCD({values}) = {divisor}")

def diaphantine_min_positive(particular, generic):
    k=0
    if generic==0:
        return k
    k=particular//abs(generic)
    if k<0:
        k=(-k)
    return k

def diaphantine_solution(solution,k):
    particular_solution, generic_solution = solution
    xy=[particular_solution[0]+k*generic_solution[0],particular_solution[1]+k*generic_solution[1]]
    return xy

def congruence_fix(variables):
    if type(variables[0])==list:
        return [variables[0][0],variables[0][1]-variables[0][0]]
    return variables

def congruence_print(cong):
    if len(cong)==2:
        print(f"x ≡ {cong[0]} ({cong[1]})")
    elif len(cong)==3:
        print(f"{cong[0]}x ≡ {cong[1]} ({cong[2]})")
    else:
        print("No solution")

if __name__=="__main__":
    print("Running wrong script")
