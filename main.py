from prettytable import PrettyTable

print('--------------WELCOME TO smruti Shop--------------\n')
table = PrettyTable(['Item Name', 'Item Price'])
total = 0

while (1):
    name = input('Enter Item name:')

    # 'q' to exit and print the table
    if (name != 'q'):
        price = int(input('Enter the Price:'))

        # store all the prices in 'total'
        total += price
        table.add_row([name, price])
        continue

    elif (name == 'q'):
        break

table.add_row(['\033[1m'+'TOTAL', total])
print(table)
print('\033[0m'+'\nThanks for shopping with us :)')
print('Your total bill amount is :','\033[1m', total, '/-','\033[0m')