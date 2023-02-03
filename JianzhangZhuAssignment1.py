# Jianzhang Zhu Assignment1

EU_exchange_rate = 1.02
ER_exchange_rate = 6.97
UR_exchange_rate = 7.11

print('Hello, welcome to the 3-currency calculator!')

From_amount = float(input('Please enter the From amount: '))

Currency_Type = input('Please enter the From Currency (USD, EUR, or RMB): ').upper()

Objective_Type = input('Please enter the To Currency (USD, EUR, or RMB): ').upper()

if Currency_Type == 'USD':

    if Objective_Type == 'RMB':
        outcome = From_amount * UR_exchange_rate

    elif Objective_Type == 'EUR':
        outcome = From_amount * EU_exchange_rate

    elif Objective_Type == 'USD':
        outcome = From_amount

    else:
        print('Please input the valid currency type.')

elif Currency_Type == 'EUR':

    if Objective_Type == 'USD':
        outcome = From_amount/EU_exchange_rate

    elif Objective_Type == 'RMB':
        outcome = From_amount * ER_exchange_rate

    elif Objective_Type == 'EUR':
        outcome = From_amount

    else:
        print('Please input the valid currency type.')

elif Currency_Type == 'RMB':

    if Objective_Type == 'USD':
        outcome = From_amount/UR_exchange_rate

    elif Objective_Type == 'EUR':
        outcome = From_amount/ER_exchange_rate

    elif Objective_Type == 'RMB':
        outcome = From_amount

    else:
        print('Please input the valid currency type.')


else:
    print('This is not an available currency type! Please try again!')

print(f'{From_amount} {Currency_Type} equals {outcome} {Objective_Type}.')