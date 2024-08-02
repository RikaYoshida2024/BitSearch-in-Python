def bit_search(list,number):
    for i,val in enumerate(list):
        if (val & number)==number:
            return i
    return -1

list=[1,2,3,4,5 ,6,7,8,9,10,11,12,13]
number = 9
result = bit_search(list,number)

if result != -1:
    print(f"Number {bin(number)} found at index {result}")
else:
    print(f"Number {bin(number)} not found in the list.")