immutable_var = (1,3,5,9,"Байкал")
print(immutable_var) # Выводим на консоль

print(type(immutable_var)) # Определяем тип переменной.

print(type(immutable_var[4])) # Показать элемент кортежа

# immutable_var[4] = 'Иркутск' # Попытка изменения элемента кортежа. Пишет TypeError: 'tuple' object does not support item assignment
# print(immutable_var)

mutable_list=1,3,5,9,"Байкал" # Создание нового кортежа
print(mutable_list)

mutable_list=1,3,5,9,"Иркутск" # Замена элемента кортежа
print(mutable_list)