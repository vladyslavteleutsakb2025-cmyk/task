# number_input = 5670
number_input = int(input("Введіть 4-значне число: "))
if len(str(number_input)) > 4:
    print("Завелике число")
else:
    number_input_one = int(number_input / 1000) #5
    number_input_two = int(number_input / 100) % 10 #6
    number_input_tree = int(number_input / 10) % 10 #7
    number_input_four = int(number_input % 10) #0

    sum_number = int(number_input_one + number_input_two + number_input_tree + number_input_four)
    res = (f"{number_input_one} + {number_input_two} + {number_input_tree} + "
           f"{number_input_four} = {sum_number}")
    print(res)