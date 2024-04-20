# > r
p = print
p("Rifat")
a = int(input("value of a"))
b = int(input("Value of b"))

p(f"Value of {a} and Value {b}:", a + b)
p(f"Value of {a} and Value {b}:", a - b)
p(f"Value of {a} and Value {b}:", a * b)
p(f"Value of {a} and Value {b}:", a // b)

if a < b:
    p(f"{a} is less than {b}")
elif a > b:
    p(f"{a} is grater than {b}")
elif a == b:
    p(f"{a} is equal {b}")
elif a != b:
    p(f"{a} is not equal to {b}")
else:
    p("unvalid")

p("not-a", not a)

m = [10, 20, 30, 40]
p(10 in m)
n = 6.788673373887346
n1 = round(n, 2)
p(n1)

if a==10:
    a+=1;
    p(a);
    if a<20:
        a+=1
        if a<13:
            p(a);
elif a!=10:
    a+=1;
    if a<20:
        a+=2
        if a<=13:
            p(a);
else:
    a+=3
    if a<20:
        a+=7
        if a<17:
            p(a);
        else:
            p(a);

for i in range(1,11,2):
    p(i,".","I am a computer Programmer\n");
    
i=1;
while i<=10:
    if i==7:
        i+=1;
        continue
    p(i);
    i+=1;

n=10;
n1= "Yes" if n==10 else "No";
p(n1);
name='Rifat';
isCheing="YES" if name=='Rifat' else "No";
p(isCheing);

for i in range(1,4):
    for j in range(1,4):
        print((i * j),end='');
        print('')


K=1;
L=1;
while K<=4:
    p('K-',K);
    K+=1;
    while L<=3:
        p('L-',L);
        L+=1;
        K+=1;
        print(' ');

List1=[1,2,3,3,3,4,5,7];
List1.append(100);
List1.pop();
List1[3]=200
p(List1)

for i in range(len(List1)):
    p('List-index',List1[i]);
    
List1.insert(1,67);
List1.remove(3);
List1.remove(67);
List1.pop(2)
p(List1);
List1=[1,2,3,3,3,4,5,7];
myCountig=0;
for i in List1:
    if i==3:
        myCountig+=1;
p(myCountig );
List1=[1,2,3,3,3,4,5,7];
L1=[8,65,87,1,90,75]
s1=sorted(L1);
print('Using-sorted',s1);
L1.sort();
print("Using sort",L1);
s1=sorted(L1 ,reverse=True);
print('Using-sorted and reverse',s1);
L1.sort( reverse=True);
print("Using sort and reverse ",L1);

    

