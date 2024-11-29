#1st program
result1 = (9 ** 0.5) * 5
print(result1)

#2nd program
result2 = (9.99 > 9.98) and (1000 != 1000.1)
print(result2)

#3th program
result_1 = 2 * 2 + 2
result_2 = 2 * (2 + 2)
print(result_1)
print(result_2)
print(result_1 == result_2)

#4th program
number_str = '123.456'
number = float(number_str)
shifted_number = number * 10
integer_part = int(shifted_number)
first_after_point = integer_part % 10
print(first_after_point)
