n = int(input("Введите количество элементов: "))
list = []
for i in range(n):
    num = int(input("Введите число в массиве: "))
    list.append(num)
X = int(input("Введите искомое число: "))
num = abs(list[0]-X)
index = 0
for i in range(1,len(list)):
    if abs(list[i]-X)<num:
        num = abs(list[i]-X)
        index = i
print(list[index])
