import dimUtils as extras
import math

def LCMn(values:list):
    """Lowest Common Multiple for arbitrary number of integers

    Args:
        values (list): list of integers for which to find LCM
    """
    def LCM(a:int,b:int):
        """LCM of two numbers
        Args:
            a (int): Number 1
            b (int): Number 2
        """
        return int(a*b/GCDn([a,b],[False]))    
    
    if len(values)<2:
        return None
    multiple=LCM(values[0],values[1])
    for i in range(2,len(values)):
        multiple=LCM(values[i],multiple)
    print(f"LCM({values}) = {multiple}")
    return multiple
def GCDn(values:list,flags:list):
    """Greatest Common Divisor for arbitrary number of integers

    Args:
        values (list): list of integers for which to find GCD
        dFlag (bool): Flag to print the steps of the Euclidean algorithm
        hFlag (bool): Flag to return the steps of the Euclidean algorithm
    """
    def GCD(a:int,b:int):
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
        if a<b:
            num1=b
            num2=a
        while(num2!=0):
            tmp = divmod(num1,num2)
            history.append([num1, num2, tmp])
            num1=num2
            num2=tmp[1]
        return [abs(num1),history]

    if len(values)<2:
        return None
    [divisor,tmp]=GCD(values[0],values[1])
    history=[tmp]
    for i in range(2,len(values)):
        [divisor,tmp]=GCD(divisor,values[i])
        history.append(tmp)
    if flags[0]:
        extras.print_GCD_history(history,values)
    if len(flags)>1 and flags[1]:
        return divisor,history
    return divisor

def getPrimeFactors(number:int):
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
    
    primes = getPrimeFactors(number)
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
    primes = getPrimeFactors(number)
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
    primes = getPrimeFactors(number)
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
    primes = getPrimeFactors(number)
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
    def getParticular(values:list,variables:list,gcd:int):
        """Particular solution of DE

        Args:
            values (list): [P0,Q0]
            variables (list): Diophantine input
            gcd (int): Greatest Common Divisor

        Returns:
            list: Partial particular solution, not multiplied
        """
        maxVal=max(values)
        minVal=min(values)
        maxVar=max(variables)
        minVar=min(variables)
        arr=[]
        if minVar*maxVal+maxVar*minVal == gcd:
            arr=[maxVal,minVal]
        if minVar*maxVal-maxVar*minVal == gcd:
            arr=[maxVal,-minVal]
        if -minVar*maxVal+maxVar*minVal == gcd:
            arr=[-maxVal,minVal]
        if -minVar*maxVal-maxVar*minVal == gcd:
            arr=[maxVal,minVal]
        
        if minVar*minVal+maxVar*maxVal == gcd:
            arr=[minVal,maxVal]
        if minVar*minVal-maxVar*maxVal == gcd:
            arr=[minVal,-maxVal]
        if -minVar*minVal+maxVar*maxVal == gcd:
            arr=[-minVal,maxVal]
        if -minVar*minVal-maxVar*maxVal == gcd:
            arr=[minVal,maxVal]
        
        if variables[0]==minVar:
            return arr
        return [arr[1],arr[0]]
    def getGeneric(particular_solution:list,variables:list,gcd:int):
        """Generic Solution of DE

        Args:
            particular_solution (list): Multiplied partial particular solution
            variables (list): Diophantine input
            gcd (int): Greatest Common Divisor

        Returns:
            list: Generic solution
        """
        maxVar=abs(max(variables))//gcd
        minVar=abs(min(variables))//gcd
        if variables[0]<variables[1]:
            return [int(math.copysign(1,-particular_solution[0]))*maxVar,int(math.copysign(1,-particular_solution[1]))*minVar]
        return [int(math.copysign(1,-particular_solution[0]))*minVar,int(math.copysign(1,-particular_solution[1]))*maxVar]
    
    gcd,hist=GCDn(variables,[False,True])
    if GCDn([gcd,constant],[False])!=gcd:
        return [[None,None],[None,None]]
    p0=[1,0]
    q0=[0,1]
    for step in hist[0]:
        mul=step[2][0]
        p0=[p0[1],p0[0]+mul*p0[1]]
        q0=[q0[1],q0[0]+mul*q0[1]]
        
    particular_p_solution=getParticular([p0[0],q0[0]],variables,gcd)
    particular_solution=[particular_p_solution[0]*constant//gcd,particular_p_solution[1]*constant//gcd]
    generic_solution=getGeneric(particular_solution,variables,gcd)
    return particular_solution, generic_solution


if __name__=="__main__":
    print(GCDn([13240210688278768,792388011857606],[False],))
