
dfile=open(r'docf.txt','r')
vowels=list('aeiouAEIOU')
vc=0
text=dfile.read()
for a in text:
    if (a in vowels):
        vc+=1
        vowels[vc]='#'
print(vc,vowels)
dfile.close()

file=open(r'letters.txt')

txt=file.readlines()
print(len(txt))
file.close()

def fn(lst):
    lst.insert(3,4)
    lst.insert(2,3)

lst1=[10,15,20,30]
fn(lst1)
print(lst1[:4])

def d(n1,n2=10):
    di=n2-n1
di=0
di=d(9)
print(di)

def dis(n):
    global var
    var=var-2
    if n%3==0:
        var=var*n
    else:
        var=var/n
    print(n,var,sep='&',end='@')
var=5
dis(10)
print(var)


def c(y):
    print(country[y-1],end='#')
import random
country=['india','aus','cana','usa']
for y in range(4):
    x=random.randint(1,3)
    c(x)






    
