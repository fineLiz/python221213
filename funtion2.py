# funtion2.py

def setValue(newValue):
    #지역변수
    x = newValue
    print(x)

# 호출
# 디버깅할 때 중단점
retValue=setValue(5)
print(retValue)

# 호출
def swap(x,y):
    return y, x

# 호출
print( swap(3,4))

print("---불변형식---")
a=1.2
print( id(a))
a=2.3
print( id(a))