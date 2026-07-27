# for i in range (1,101):
#     if i % 3 == 0:
#         print(i)

m = int(input('enter a start number'))
n = int(input('enter an end number'))

num = int(input('select the number'))

for i in range(m, n):
    if i % num == 0:
        print(i)