# 데이터를 저장 할 때마다 변수를 생성해야 한다
# 컬렉션 : 데이터들을 한개의 변수로 저장할 수 있도록 만들어진 자료형
# 기본 컬렉션 4가지 : list, tuple, set, dict

###### list ######
# 리스트에서도 각각의 데이터는 ,를 기준으로 구분한다. 컬렉션에서 저장하고 있는 각각의 데이터는 요소라고도 한다.

li = []
li1 = [1,2,3]
li2=['a','b']
li3=[1,2,'a','b',True]
li4=[1,2,["a","b"]] # 리스트 안의 요소로 이중 리스트를 표현

print(li)
print(li1)
print(li2)
print(li3)
print(li4)

# 컬렉션 데이터들도 데이터(요소)별로 인덱스를 가지게 된다.
print(li1[0])
print(li1[2])
print(li3[4])
print(li4[2])
print(li4[2][0])
# 이중 리스트 안에 존재하는 값에 접근하고자 할 떄는 먼저 요소 리스트를 가져온다. 그 후 요소 리스트의 인덱싱으로 원하는 데이터를 가져올 수 있다.

# 요소의 수정: list에서 인덱싱으로 내가 수정하고 싶은 요소를 가져와서 새로운 요소를 추가 수정 삭제 가능
li =[10,20,30]
li[2] = 40
print(li) #[10, 20, 40]

# append(data)의 형식으로 사용하고, 항상 데이터를 마지막 요소로 추가
# insert(index, data)형식으로 사용, 추가할 데이터의 인덱스를 지정할 수 있다.

score = [40,20,50,90]
print(score) #[40, 20, 50, 90]
score.append(70)
print(score) #[40, 20, 50, 90, 70]
score.append("문자")
print(score) #[40, 20, 50, 90, 70, '문자']

score.insert(2,80)
print(score) #[40, 20, 80, 50, 90, 70, '문자']

#삭제 pop() 메서드, del()함수
# pop(index)형식으로 사용하고, 전달한 인덱스 위치의 데이터를 삭제한다.
# index를 생략하면, 마지막 인덱스에 위치한 데이터를 삭제한다.
score.pop()
print(score)  #[40, 20, 80, 50, 90, 70]

score.pop(1)
print(score)  #[40, 80, 50, 90, 70]

#del()함수: data를 삭제하는 함수
del score[0]
print(score) #[80, 50, 90, 70]

del score[1:3] #del함수는 범위를 지정해서 슬라이싱으로 삭제 가능
print(score) #[80, 70]

del score #변수 자체를 삭제

###### tuple 튜플 ######
# 소괄호()를 사용하고, tuple() 형변환 함수로 생성
# 리스트와 마찬가지로 각 요소에 인덱스가 부여되고, 인덱싱, 슬라이싱이 가능하다.
# 한번 만들어지면 저장된 데이터 값을 변경할 수 없다.

t1 = (1,2,3)
print(t1) #(1, 2, 3)

t2 = 1,2,3
print(t2) #(1, 2, 3)
# 파이썬에서 컴파일 과정에서 데이터 묶음(컬렉션 데이터)을 생성한다면 튜플이 기본형식으로 생성된다.

t3 = (100)
print(t3) #100

t3 = (100,)
print(t3) #(100,) 콤마를 함께 작성해야 컬렌션 데이터라고 인식

#인덱싱 슬라이싱 동일하게 가능
print(t1[2]) #3
print(t1[1:3]) #(2, 3)

# 값의 수정은 불가능

# 컬렉션 연산
li = [1,2,3]
li2 = ['a','b','c']
print(li+li2) #[1, 2, 3, 'a', 'b', 'c']
# 컬렌션 데이터 끼리 + 연산을 진행하면 두 컬렉션의 요소가 하나로 연결된 새로운 컬렉션을 생성한다

print(li *3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# 곱한 횟수 만큼 리스트의 요소를 반복한 새로운 리스트를 생성한다.

print('*'*7) #*******

###### set 세트 ######
# 수학의 집합 개념을 자료형으로 구현한 컬렉션 데이터
# 저장된 값들의 순서(인덱스)를 가지지 않는다. 인덱스가 없으므로 인덱싱과 슬라이싱이 불가능하다
# 중괄호{} 또는 set() 형변환 함수를 이용해서 생성한다.
s = {10, 20, 30}
print(s) #{10, 20, 30}

li = [1,2,3,4,5,3,2,4,2,2,1,1]
print(li) #[1, 2, 3, 4, 5, 3, 2, 4, 2, 2, 1, 1]
s2 = set(li)
print(s2) #{1, 2, 3, 4, 5}

# 요소의 추가 삭제
# 추가
# add(), update()를 사용한다

# add(data) : 입력한 data를 추가한다.
s2.add(6)
print(s2) #{1, 2, 3, 4, 5, 6}

# update  : 여러개의 데이터를 한번에 입력할 때 사용, 기본적으로 list를 많이 사용한다.
s2.update([9,13,15])
print(s2) #{1, 2, 3, 4, 5, 6, 9, 13, 15}

# 요소의 삭제 : remove(data), discard(data)
# *차이점: remove의 경우 없는 요소를 삭제할 경우 오류 발생
s2.remove(6)
print(s2) #{1, 2, 3, 4, 5, 9, 13, 15}

s2.discard(5)
print(s2) #{1, 2, 3, 4, 9, 13, 15}

###### dict 딕셔너리 (dictionary) ---> map ######
# 사전처럼 데이터가 이름(key) 와 의미(value)로 이루어진다. 인덱스가 존재하지 않는다. 대신 key값을 이용해서 인덱싱과 비슷한 결과를 얻는다.

# dict생성
# 중괄호 {}를 사용하고, dict() 형변환 함수
s = {1,2,3}
#dict : {key1: value1, key2 : value2}

di = {"a" : "apple", "b" :"banana"}
# :를 기준으로 왼쪽 data가 key 값이 되고, 오른쪽 data가 value 값이 된다. key와 value 한 쌍의 묶음이 1개의 요소로 취급 된다.
# 값의 접근(사용)
print(di) #{'a': 'apple', 'b': 'banana'}

print(di['a']) #apple

# get() 메서드
print(di.get('c','cat')) #cat
print(di) #{'a': 'apple', 'b': 'banana'}
# key가 없는 데이터 라면 default로 입력한 값을 반환해준다
# default가 지정되지 않았다면, 기본적으로 None을 반환한다.
# default를 지정해도 key값이 dict에 존재하면, key에 맞는 value가 반환된다.

di.setdefault('c','dog')
print(di) #{'a': 'apple', 'b': 'banana', 'c': 'dog'}
di.setdefault('c','cat')
print(di) #{'a': 'apple', 'b': 'banana', 'c': 'dog'}
di.update({'d':"delete",'e':"enter"})
print(di) #{'a': 'apple', 'b': 'banana', 'c': 'dog', 'd': 'delete', 'e': 'enter'}

print(di.keys())   #dict_keys(['a', 'b', 'c', 'd', 'e'])
print(di.values()) #dict_values(['apple', 'banana', 'dog', 'delete', 'enter'])
print(di.items())  #dict_items([('a', 'apple'), ('b', 'banana'), ('c', 'dog'), ('d', 'delete'), ('e', 'enter')])

di.pop('d')
print(di) #{'a': 'apple', 'b': 'banana', 'c': 'dog', 'e': 'enter'}
del di['e']
print(di) #{'a': 'apple', 'b': 'banana', 'c': 'dog'}

di.clear()
print(di) #{}

