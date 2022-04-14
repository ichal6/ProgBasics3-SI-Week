is_good_value = False

while is_good_value == False:
    try:
        T_f = float(input('Give a temperatures in Farenheit degress: '))
    except:
        print("Please insert a number value")
    else:
        is_good_value = True

T_c = (5/9)*(T_f - 32)

print("Celsius degress = %.2f" %T_c)