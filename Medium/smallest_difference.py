"""
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

Examples : 

Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8} 
Output : 3  
That is, the pair (11, 8) 

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80} 
Output : 10
That is, the pair (40, 50)

"""
def smallest_difference(arrayOne: list, arrayTwo: list) -> list:
    """
    """
    # sort both array to start with

    arrayOne.sort()
    arrayTwo.sort()
    diff = 1000000
    i=j=0
    result = [0,0]

    while i < len(arrayOne) and j<len(arrayTwo):
        # calculate difference
        temp = abs(arrayOne[i]-arrayTwo[j])
        # update diff if temp is less than existing
        if temp < diff:
            diff = temp
            result = [arrayOne[i], arrayTwo[j]]
        
        # update value of i, j based on value present at that index
        if arrayOne[i] > arrayTwo[j]: # keep incrementing j
            j+=1
        else:
            i+=1
        
    return result


if __name__ == "__main__":

    arrayOne = [-1, 5, 10, 30, 40]
    arrayTwo = [26, 130 ,25, 15, 55]

    result = smallest_difference(arrayOne, arrayTwo)
    print(result)
