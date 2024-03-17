print("no 1")
a = 1
for i in range(3):
    print(a, end = ".Aku cinta indonesia\n") 
    a +=2
print("no 2")
a = 2
b = 2
for i in range(6):
    print(a, end = " ") 
    a +=b
    b +=1   

print("no 3")
for i in range(1,4):
    print(f'1 x {i} = {1 *i}')   

print("no 4")
for i in range(6,11):
    print(f'7 x {i} = {7 *i}') 
    
print("no 5")
baris = 3
kolom = 3
for i in range(baris):
    for j in range( kolom):
        print('*',end='')
    print()  

print("no 6")
baris = 3
kolom = 4
for i in range(1, baris +1):
    for j in range( kolom):
        print(i,end='')
    print() 
print("no 7")
a = 1
b = 1
c = b
for i in range(10):
    print(a, end = " ") 
    c = a + b
    a = b
    b = c

print("\n")
print("no 8")
a = 1
b = 2
c = 3
print(a, end =" ")
print(b, end =" ")
print(c, end =" ")
for i in range(7):
    next_num = a + b +c
    print(next_num, end = " ")  
    a = b
    b = c
    c = next_num
    
print("\n")
print("no 9")
baris = 4
kolom = 4
for i in range(baris):
    for j in range( kolom -i):
        print('1',end='')
    print()

print("no 10")

for i in range(5):
    for j in range(5,i,-1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(3, end=" ")
            else:
                print(2, end=" ")
        else :
            if j % 2 == 1:
                print(3, end=" ")
            else :
                print(2, end=" ")
    print()                        
