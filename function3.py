# function3.py
#가변형식인 경우
wordlist = ["J", "A", "M"]

#함수의 정의
def change(x):
    x1 = x[:]
    x1[0] = "H"
    print("내부:", x1)

#호출
change(wordlist)
print(wordlist)

print("---global키워드---")
g =1 
def testScope(a):
    global g
    g = 2
    return g+a

#호출
testScope(1)
print("전역변수 g:", g)

#교집합 문자를 리턴
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result



#호출
print( intersect("HAM", "SPAM"))


#키워드인자(파라미터명을 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print( connectURI("credu.com", "80"))
print( connectURI(port="8080", server="credu.com"))

#가변적인 경우(가변인자 *)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM", "EGG"))
print(union("HAM","EGG", "SPAM"))



#간단하게 함수를 정의하는 문법 (예: def times(x,y): return x*y)
#입력받아서 : 뒤에서 처리
g = lambda x, y:x*y
print ( g(3,4))
print ( g(5,6))

#일회성으로 사용하고 버리기
print( (lambda x:x*x)(3))
print( globals())
