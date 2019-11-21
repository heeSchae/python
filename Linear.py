def linear(a_list, string):
    result = ""
    for i in range(len(a_list)):
        if string == a_list[i]:
            result = i
            return result 
    if result == "":
        return False
    
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))

