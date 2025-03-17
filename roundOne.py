
    
def daimond(m):
    
    n = m + 2
    for i in range(1,n+1,2):
        space = (n-i)//2
        l = ''.join(chr(65+j) for j in range(i))
        print(" "*space + l)
        
        
    for i in range(n-2,0,-2):
        space = (n-i)//2
        l = ''.join(chr(65+j) for j in range(i))
        print(" "*space + l)
        
        
   
 
a = input()
b = int(a)
daimond(b)
       
        
