# first_sum = input("Ты ввёл: ")
# sum_int = int(first_sum)
# conv_sum = round(sum_int / 65)
# print("конвертированная сумма в USD = ", conv_sum)
# print(type(conv_sum))

inp_sum = input("Введите сумму в рублях: ")

if inp_sum == "" or inp_sum == " ":
    print("Вы ввели пустое поле. Введите число")
elif type(inp_sum) == 'str':
    print("Вы ввели не число. Введите число")
elif int(inp_sum) < 0:
    print("Введите положительное число")
else :
    new_sum = int(inp_sum)
conv_sum_usd = round(new_sum / 68)
conv_sum_eur = round(new_sum / 74)
conv_sum_chf = round(new_sum / 75)
conv_sum_gbp = round(new_sum / 85)
conv_sum_chy = round(new_sum / 10)
print("конвертированная сумма в USD = ", conv_sum_usd)
print("конвертированная сумма в EUR = ", conv_sum_eur)
print("конвертированная сумма в CHF = ", conv_sum_chf)
print("конвертированная сумма в GBP = ", conv_sum_gbp)
print("конвертированная сумма в CHY = ", conv_sum_chy)
# print(type(inp_sum))

