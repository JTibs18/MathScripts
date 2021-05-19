kgoing = 1 

def printPermutation(arr, n): 
    for i in range (0, n): 
        print (arr[i], end = ' ')
    
    print()
    
def binaryStrings(n, arr, i): 
    if i == n: 
        printPermutation(arr, n)
        return 

    arr[i] = 0
    binaryStrings(n, arr, i + 1)

    arr[i] = 1
    binaryStrings(n, arr, i + 1)
    

while kgoing == 1: 
    bitNum = int(input("Enter the number of bits in the string: ")) 

    arr = [None] * bitNum 
    binaryStrings(bitNum, arr, 0)
    print("Number of permutations: ", 2 ** bitNum )
     
    cont = input("Another set of permutations? Y/N: ")

    if cont == "N" or cont == "n":
        kgoing = 0 
    else: 
        kgoing = 1
