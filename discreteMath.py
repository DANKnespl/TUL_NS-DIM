import dimUtils as extras
import math

def lcm(values:list):
    """Lowest Common Multiple for arbitrary number of integers

    Args:
        values (list): list of integers for which to find LCM
    """
    def lcm2(a:int,b:int):
        """LCM of two numbers
        Args:
            a (int): Number 1
            b (int): Number 2
        """
        return int(a*b/gcd([a,b],[False]))    
    
    if len(values)<2:
        return None
    multiple=lcm2(values[0],values[1])
    for i in range(2,len(values)):
        multiple=lcm2(values[i],multiple)
    print(f"LCM({values}) = {multiple}")
    return multiple
def gcd(values:list,flags:list=[False,False]):
    """Greatest Common Divisor for arbitrary number of integers

    Args:
        values (list): list of integers for which to find GCD
        dFlag (bool): Flag to print the steps of the Euclidean algorithm
        hFlag (bool): Flag to return the steps of the Euclidean algorithm
    """
    def gcd2(a:int,b:int):
        """GCD of two integers
        Args:
            a (int): Number 1 
            b (int): Number 2
        Returns:
            list: [value of GCD, steps taken]
        """
        num1=a
        num2=b
        history = []
        #if a<b:
        #    num1=b
        #    num2=a
        while(num2!=0):
            tmp = divmod(num1,num2)
            history.append([num1, num2, tmp])
            num1=num2
            num2=tmp[1]
        return [abs(num1),history]

    if len(values)<2:
        return None
    [divisor,tmp]=gcd2(values[0],values[1])
    history=[tmp]
    for i in range(2,len(values)):
        [divisor,tmp]=gcd2(divisor,values[i])
        history.append(tmp)
    if flags[0]:
        extras.print_GCD_history(history,values)
    if len(flags)>1 and flags[1]:
        return divisor,history
    return divisor

def get_prime_factors(number:int):
    """Function for calculating prime factors of integer

    Args:
        number (int): Factorised number

    Returns:
        dict: Prime factor:Exponent
    """
    primes = {}
    current_prime = 2
    tmp = number
    while tmp > 1:
        if tmp % current_prime == 0:
            if current_prime in primes:
                primes[current_prime] += 1
            else:
                primes[current_prime] = 1
            tmp //= current_prime  # Use integer division
        else:
            current_prime += 1
    return primes
def euler_function(number:int):
    """Function for Euler phi function\n
    phi(n) = EulerFunction(number)
    Args:
        number (int): argument n of phi function
    Returns:
        int: Number of integers k <= n, for which GCD(k,n) > 1
    """
    
    primes = get_prime_factors(number)
    product=1
    for key,max_exponent in primes.items():
        product *= (pow(key,max_exponent)-pow(key,max_exponent-1))
    return product
def sum_of_divisors(number:int):
    """Function to get sum of all divisors of number
    
    Args:
        number (int): number whose divisor are meant to sum
    Returns:
        int: sum of divisors
    """
    primes = get_prime_factors(number)
    tmp_sum=0
    product=1
    for key,max_exponent in primes.items():
        tmp_sum=0
        for exponent in range(0,max_exponent+1):
            tmp_sum+=pow(key,exponent)
        product *= tmp_sum
    return product
def num_of_divisors(number:int):
    """Function to get number of all divisors of number
    Args:
        number (int): numbers whose divisors are meant to be enumerated
    Returns:
        int: number of divisors
    """
    primes = get_prime_factors(number)
    nDiv=1
    for exponent in primes.values():
        nDiv=nDiv*(1+exponent)
    return nDiv
def moebius_function(number:int):
    """Moebius Function\n 
    mu(n) = { if n=1 => 1,\n
    if n is product of k DISTINCT primes => (-1)^k ,\n
    if (x^2)|n, where x>1  => 0 }

    Args:
        number (int): argument of Moebius function

    Returns:
        int: {-1,0,1} 
    """
    primes = get_prime_factors(number)
    for val in primes.values():
        if val > 1:
            return 0
    return pow(-1,len(primes))
def diophantine_equation(variables:list,constant:int):
    """Diophantine equation solver
    Args:
        variables (list): [q_x,q_y]
        constant (int): right side value
    """
    def get_particular(values:list,variables:list,greatest_common_divisor:int):
        """Particular solution of DE

        Args:
            values (list): [P0,Q0]
            variables (list): Diophantine input
            greatest_common_divisor (int): Greatest Common Divisor

        Returns:
            list: Partial particular solution, not multiplied
        """
        maxVal=max(values)
        minVal=min(values)
        maxVar=max(variables)
        minVar=min(variables)
        arr=[]
        if minVar*maxVal+maxVar*minVal == greatest_common_divisor:
            arr=[maxVal,minVal]
        if minVar*maxVal-maxVar*minVal == greatest_common_divisor:
            arr=[maxVal,-minVal]
        if -minVar*maxVal+maxVar*minVal == greatest_common_divisor:
            arr=[-maxVal,minVal]
        if -minVar*maxVal-maxVar*minVal == greatest_common_divisor:
            arr=[maxVal,minVal]
        
        if minVar*minVal+maxVar*maxVal == greatest_common_divisor:
            arr=[minVal,maxVal]
        if minVar*minVal-maxVar*maxVal == greatest_common_divisor:
            arr=[minVal,-maxVal]
        if -minVar*minVal+maxVar*maxVal == greatest_common_divisor:
            arr=[-minVal,maxVal]
        if -minVar*minVal-maxVar*maxVal == greatest_common_divisor:
            arr=[minVal,maxVal]
        
        if variables[0]==minVar:
            return arr
        return [arr[1],arr[0]]
    def get_generic(particular_solution:list,variables:list,greatest_common_divisor:int):
        """Generic Solution of DE

        Args:
            particular_solution (list): Multiplied partial particular solution
            variables (list): Diophantine input
            greatest_common_divisor (int): Greatest Common Divisor

        Returns:
            list: Generic solution
        """
        maxVar=abs(max(variables))//greatest_common_divisor
        minVar=abs(min(variables))//greatest_common_divisor
        
        
        if variables[0]<variables[1]:
            if particular_solution[0]==particular_solution[1]:
                return [-maxVar,minVar]
            return [int(math.copysign(1,-particular_solution[0]))*maxVar,int(math.copysign(1,-particular_solution[1]))*minVar]
        if particular_solution[0]==particular_solution[1]:
                return [-minVar,maxVar]
        return [int(math.copysign(1,-particular_solution[0]))*minVar,int(math.copysign(1,-particular_solution[1]))*maxVar]
        
    greatest_common_divisor,hist=gcd(variables,[False,True])
    if gcd([greatest_common_divisor,constant],[False])!=greatest_common_divisor:
        return [[None,None],[None,None]]
    p0,q0 = continued_fraction(variables,len(hist[0]))

    particular_p_solution=get_particular([p0[0],q0[0]],variables,greatest_common_divisor)
    particular_solution=[particular_p_solution[0]*constant//greatest_common_divisor,particular_p_solution[1]*constant//greatest_common_divisor]
    generic_solution=get_generic(particular_solution,variables,greatest_common_divisor)
    return particular_solution, generic_solution
def continued_fraction(variables:list, terminator:int, flags:list=[False,True]):
    """Contunued Fraction solver\n
    
    Args:
        variables (list): [1. starting numerator, 2. starting denumerator]
        terminator (int): maximum number of iterations
        flags (list, optional): [add number of iterations to output]. Defaults to [False,True].

    Returns:
        list: [last two numerators, last two denumerators, ?number of iterations]
    """
    _,hist=gcd(variables,[False,True])
    p0=[1,hist[0][0][2][0]]
    q0=[0,1]
    n=0
    for step in hist[0]:
        mul=step[2][0]
        if n!=0:
            p0=[p0[1],p0[0]+mul*p0[1]]
            q0=[q0[1],q0[0]+mul*q0[1]]
        if n==terminator:
            break
        n+=1
    if flags[1]:
        print(f"{p0[1]}/{q0[1]}")
    if flags[0]:
        return p0,q0,n
    return p0,q0

def congruence(variables:list):
    """Linear congruence solver\n
    a*x congruent b (modulo)

    Args:
        variables (list): [a,b,m]
        a (int): a in equation
        b (int): b in equation
        m (int): modulo in equation

    Returns:
        None|list|int: value of x which solve the congruence
                        None - no x solves
                        int - 1 x solves
                        list - multiple x solve
    """
    
    m=variables[2]
    a=variables[0]
    b=variables[1]
    d = gcd([a,m])
    if d==1:
        fraction_data = continued_fraction([m,a],100,[True,False])
        n = fraction_data[2]
        return (pow(-1,n-1)*fraction_data[0][0]*b)%m
    if b%d==0:
        a_1=a/d
        b_1=b/d
        m_1=m/d
        x_0=int(congruence([a_1,b_1,m_1]))
        outputs=[]
        for i in range(0,d):
            outputs.append(int((x_0+i*m_1)%m))
        return outputs
    return None
def congruence_system(variables:list):
    """Solves system of n linear congruences like ax congruent b (m)
    
    Args:
        variables (list): [[a_0,b_0,m_0],...,[a_n,b_n,m_m]]
    Returns:
        list: [int,int] [b,m] (congruence)
        None: 0 solutions
    """
    
    def congruence_system_setup():
        """Transforms list of generic ax congruent b (m) equations [a,b,m]
        to x congruent b (m) [b,m]

        Returns:
            list: [int,int]      [[b_0,m_0],...,[b_n,m_n]]
        """
        new_variables = []
        for cong in variables:
            new_cong = congruence(cong)
            if new_cong==None:
                return None
            new_variables.append(extras.congruence_fix([new_cong,cong[2]]))
        return new_variables
    
    def congruence_system_2(variables:list):
        """Solves system of 2 linear congruences like x congruent b (m)

        Args:
            variables (list): [[b_0,m_0],[b_1,m_1]]

        Returns:
            list: [b,m] new congruence
        """
        c1 = variables[0]
        c2 = variables[1]
        c_temp = [c1[1],c2[0]-c1[0],c2[1]]
        c_new = extras.congruence_fix([congruence(c_temp),c2[1]])
        if c_new[0]==None:
            return None
        return [c1[0]+c1[1]*c_new[0],c1[1]*c_new[1]]
    
    
    new_variables = congruence_system_setup()
    if new_variables == None:
        return None
    fin_congruence = new_variables[0]
    
    for i in range(1,len(new_variables)):
        fin_congruence=congruence_system_2([fin_congruence,new_variables[i]])
        if fin_congruence == None:
            return None
    
    return fin_congruence
    
if __name__=="__main__":
    print("Running wrong script")
    continued_fraction([1618033988749895,1000000000000000],5)

