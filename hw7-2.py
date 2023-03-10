# Задача 2. Напишите функцию print_operation_table

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns+1):
            print(operation(row, column), end = '\t')
        print()

print_operation_table(lambda x, y: x + y)