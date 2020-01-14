import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

#можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
#print (flats_list)

#TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
#и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:

i = 0
n = 0
print('Новостройки:')
for flat in flats_list:
    if "новостройка" in flat[2]:
        n +=1
        print('number {} , ID'.format(i), flat[0])
    i += 1 
print ('Всего новостроек',n)
# 2) добавьте в код подсчет количества новостроек


#TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
flat_info = {"ID":flat[0], "Количество комнат":flat[1], "Новостройка/вторичка":flat[2], "Цена. (руб)":flat[11]}
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1 
header = flats_list.pop(0)
subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace("м.", "")
  if subway not in subway_dict.keys():
    subway_dict[subway] = list()
  subway_dict[subway].append(flat_info)
print(subway_dict)

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.

print ('Количество квартир у метро:')

for st in subway_dict:
    q = subway_dict[st] 
    print (st, len(q)) 

