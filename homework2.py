#number_1
my_list=[15, 19, 572, 45.6, 5.1, 'mz', "sdt gugjdeu", ("name", "test"), None, False]
type_list=''
for i in my_list:
    type_list+=(type(i).__name__+' ')
print(type_list)


#number_2
myList=input().split()
myList2=[]
for i in myList: 
    if len(myList2)%2>0:
        myList2.insert(-1, i)
    else:
        myList2.append(i)
print(myList2)

#number_3
month=int(input("Введите месяц в виде целого числа от 1 до 12: "))
while month<1 or month>12:
    month=int(input("Введите месяц в виде целого числа от 1 до 12: "))
dictYear={1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month==12 or month==1 or month==2:
    print(dictYear.get(1))
if 3<=month<=5:
    print(dictYear.get(2))
if 6<=month<=8:
    print(dictYear.get(3))
if 9<=month<=11:
    print(dictYear.get(4))

#number_4
user=str(input()).split()
for id, el in enumerate((user), 1):
    if len(el)>10:
        print(id, el[0:10])
    else:
        print(id, el)

#number_5
my_list=[7, 5, 3, 3, 2]
user_el=int(input())
if user_el<my_list[-1]:
    my_list.append(user_el)
else:
    for i in range(len(my_list)):
        if user_el>=my_list[i]:
            my_list.insert(i, user_el)
            break
print(my_list)

#number_6
products=[]
user_prod2=dict.fromkeys(['название', 'цена', 'количество', 'ед'])
i=0
while True:
    i+=1
    for r in user_prod2:
        user_prod2[r]=input("Заполните "+ r + " ")
    products.append((i, user_prod2.copy()))
    if input('хотите закончить?')=='да':
        break
products

analyticks={'название':[], 'цена':[], 'количество':[], 'ед':[]}
for _, d in products:
    for i in d:
        analyticks[i]+=[d[i]]
print(analyticks)