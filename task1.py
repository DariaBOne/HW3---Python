n = int(input("Введите количество элементов: "))
list = []
count = 0
for i in range(n):
    num = int(input("Введите число в массиве: "))
    list.append(num)
X = int(input("Введите искомое число: "))
for i in range(len(list)):
    if list[i]==X:
        count+=1
print(count)
