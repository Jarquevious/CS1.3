#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_recursive(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests
    
    #One is the number factorial begins with
    result = 1
    #create a for loop using variable 'i' in range of 2 to n+1. we use two because...and n+1 to get the entire length of the array
    for i in range(2, n+1): 
    #we multiply result by i to get the result. Result changes based on each interation.
        result *= i 
    #return the final result of all factorial numbers multipkied together
    return result 
  

    

def factorial_recursive(n):
    #check if n is one of the base cases. The base case returns a value without making any subsequent recursive calls, if any of these are chosen, return 1
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        #if n is greater than 1, call function recursively
        return n * factorial_recursive(n - 1)



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
