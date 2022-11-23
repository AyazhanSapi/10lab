#super - Кейінірек қажет болатын функциялар
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

# Если создать дочерний класс `Laptop`, то будет доступ 
# к свойству базового класса благодаря функции super().
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model


asus = Laptop('asus', 2, 512, 'l420')

print('This computer is:', asus.computer)
print('This computer has ram of', asus.ram)
print('This computer has ssd of', asus.ssd)
print('This computer has this model:', asus.model)

#next - Кейінірек қажет болатын функциялар
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
 
#sorted - Жаңадан бастаушылар үшін түсініксіз функциялар
# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Ayazhan'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

#enumerate, zip - Жаңадан бастаушылар үшін түсініксіз функциялар
names = ['Ayazhan', 'Arman', 'Aisha']
ages = [21, 22, 17]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

#tuple
for i, t in enumerate(zip(names, ages)):
    print(i, t)

#any - Жаңадан бастаушылар үшін түсініксіз функциялар
# initializing list
test_list = [4, 5, 8, 9, 10, 17]
print("Список : ", test_list)
res = any(ele > 10 for ele in test_list)
print("Удовлетворяет ли какой-либо элемент указанному условию? : ", res)

#frozenset - Сізге олардың қажеті жоқ болуы мүмкін
setCat = set('Аяжан')
frozenCat = frozenset('Аяжан')
print(setCat == frozenCat)

print(type(setCat))    # set
print(type(frozenCat)) #frozenset

setCat.add('с') # можем добавить
print(setCat)

frozenCat.add('с') # эта строка вызовет ошибку при компиляции

#round - Кез келген уақытта үйренуге болатын функциялар
# for integers
print(round(15))
 
# for floating point
print(round(51.6))
print(round(51.5))
print(round(51.4))

#slice - Сізге олардың қажеті жоқ болуы мүмкін
py_string = 'Ayazhan' 
# stop = 3 
# contains 0, 1 and 2 indices 
slice_object = slice(3) 
print(py_string[slice_object]) 
# Pyt 
# start = 1, stop = 6, step = 2 
# contains 1, 3 and 5 indices 
slice_object = slice(1, 6, 2) 
print(py_string[slice_object])
