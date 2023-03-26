#Задание №1

#На вход подается 1 строка без пробелов. По данной строке определите, является ли она палиндромом 
#(то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш").Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном
#случае.


choice = input('Что Вы хотете ввести? \n 1. слово \n 2. строку? \n ')

if (choice == str('Слово')) or (choice == str('слово')) or (choice == str('Cлова')) or (choice == str('слова')) or (choice == str('1')) or (choice == str('1.')):
    string = input('Введите слово: ')
    n_string = string.lower()
    palidrom = n_string[::-1]

    if n_string == palidrom:
        print(f'Вывод: {palidrom} = {string}.')
        print('Yes!')

    else:
        print(f'Вывод: {palidrom} != {string}.')
        print('No!')



if (choice == str('Строку')) or (choice == str('строку')) or (choice == str('Страка')) or (choice == str('страка')) or (choice == str('2')) or (choice == str('2.')):    
    string = input('Введите стороку без пробелов: ')
    palidrom = string[::-1]

    if choice == palidrom:
        print(f'Вывод: {palidrom} = {string}.')
        print('Yes!')

    else:
         print(f'Вывод: {palidrom} != {string}.')
         print('No!')

