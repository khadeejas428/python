def solve(strg):

    output ={} 

    for i in strg:
        if i in output:
            output[i] += 1
    
        else:
            output[i] = 1

    return output 
     
     
     
     
print(solve('mashupstack'))