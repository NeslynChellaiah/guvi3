class main():                      
    def func():                    
        N = int(input())           
        a = []                     
        count = 0                  
        a = input().split()        
        a.sort()                   
        k = len(a) - 1             
        if a[k]=="0":              
            count+=1               
        else:                      
            for i in range (0,N):  
                print (a[k],end="")
                k-=1  
        if count != 0:
            print (0)
ob = main            
ob.func()            
