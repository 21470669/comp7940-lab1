def main():
    print("Hello World")

if __name__ == '__main__':
    main()

#EX 1
# Find the all factors of x using a loop and the operator % 
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
x = 52633
for i in range(1,x+1):
  # your code here
  if x % i == 0:
      print(i)

#EX 2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
  # your code here
    result = []
    for i in range(1,x+1):   
        if x % i == 0:
            result.append(i)
    return print(result)

print_factor(x)

#EX 3
# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here
def print_factor_list(mylist):  
    result = []
    for j in mylist:   
        for i in range(1,j+1): 
            if j % i == 0:
                result.append(i)
    return print(sorted(set(result)))  #return the sorted unique factors

print_factor_list(l)