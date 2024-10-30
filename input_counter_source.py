number_limit = 0
adder = 0
values_1_10 = []
values_11_20 = []
values_21_30 = []
values_31_40 = []
values_41_50 = []

while True:
    while True:
        try:
            adder = int(input('Input a number that greater than or equals to 1 and less than or equals to 50'))
            
            if adder < 1 and adder > 50:
                print('Input is not within acceptable range')
                adder = 0
                break
        except:
            print('Input has caused an error')
        
        break
    
    number_limit = number_limit + adder
    if number_limit > 50:
        print('Range\t\t Amount')
        print('01 - 10 =\t', len(values_1_10))
        print('11 - 20 =\t', len(values_11_20))
        print('21 - 30 =\t', len(values_21_30))
        print('31 - 40 =\t', len(values_31_40))
        print('41 - 50 =\t', len(values_41_50))
        break
    
    if adder >= 1 and adder <= 10:
        values_1_10.append(number_limit)
    if adder >= 11 and adder <= 20:
        values_11_20.append(number_limit)
    if adder >= 21 and adder <= 30:
        values_21_30.append(number_limit)
    if adder >= 31 and adder <= 40:
        values_31_40.append(number_limit)
    if adder >= 41 and adder <= 50:
        values_41_50.append(number_limit)