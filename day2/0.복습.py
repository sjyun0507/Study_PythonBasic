a='hello world'
b='phyton is easy'

# 1. a 변수의 문자열 중에 hello만  출력
print(a[0:5])
print(a[:5])

# 2. b 변수의 저장된 문자열 중에 'is'만 출력
print(b[7:9])
print(b[-7:-5])

# 3. a 변수와 b 변수의 문자를 조합해서 'Hello phyton'이 출력될 수 있도록 하세요
print(a[0:6]+b[0:6])
print(a[0:5], b[:6])

# 4. 슬라이싱을 이용해서 'is easy'만 출력
print(b[7:])
print(b[-7:])

# 5. 슬라이싱을 이용해서 'world'만 출력
print(a[-5:])

# 6. 슬라이싱을 이용해서 'world is easy'만 출력
print(a[6:],b[7:])
