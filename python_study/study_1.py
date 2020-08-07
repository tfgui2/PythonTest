print('Begin python')
print('파이선 파일에서 실행')
a=1
b=2
print(a+b)
c=3; d=4; print(c+4)
print('공백')
#이거는 주석
print('주석')#이거는 주석
a=1.1
print(a)
a=0x11
print(a)

print('he\nhello')
print('he\thello')
a='''
my name
is
hoee
'''
print(a)
print(a.find('i'))
print(a.upper())

while True:
    print('while')
    break
for c in a:
    print(c)
    
b=[[1,2],[3,4],[5,6]]
for i,j in b:
    print(i, end=':')
    print(j)


def main():
    print(a)
    return [100,200]
    

k=main()
if __name__ == '__main__':
    print(k)

import mymodule
k=mymodule.sum(1,2,'-')
k=mymodule.varg(1,2,3,4)
def testfunc():
    global k
    k=1
    print(k)
testfunc()
print(k)