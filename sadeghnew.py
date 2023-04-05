# https://quera.org/problemset/616/

a = int(input())
for i in range(1, 1000000000):
    x = 2**i
    if a < x:
        print(2**(i))    
        break
    elif a == x:
         print(2**(i+1))
         break

        
