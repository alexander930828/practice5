a = [1,2,3,4,5]

print(a)

a.append("안녕")
a.append('True')

print(a)

print("이번 단어는" +" "+ a[5])

try:
    print(a[9])
except IndexError:
    print('아니 이건 없는거야')

print(a[9])
