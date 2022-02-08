from sys import argv

print('Hey! Вы написали сколько часов проработал ваш сотрудник, сколько он получает в час и какую премию вы собираетесь ему заплатить!! Мы расчитали все!')

def sallary_count(hours,rate, bonus):
    return hours * rate + bonus
print(argv)

print(sallary_count(int(argv[1]),int(argv[2]),int(argv[3])))




