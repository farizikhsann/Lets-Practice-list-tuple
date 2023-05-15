def func( var1, var2):
    output = []
    for i in range(len(var1)):
        for j in range(len(var2)):
            if(var1[i] == var2[j]):
                output.append(var2[j])
    return output
if __name__ == '__main__':
    l1 = [3, 2, 4, 5, 1] 
    l2 = [7, 4, 5, 2]
    
    print(func(l1,l2))
