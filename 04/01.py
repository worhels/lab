
PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}

def infix_to_postfix(expression):
    """
    Перетворення інфіксного математичного виразу у зворотний польський запис (ЗПН).
    :param expression: str - математичний вираз (з пробілами між операндами та операторами)
    :return: str - вираз у ЗПН
    """
    stack = []
    output = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric(): 
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while stack and stack[-1] != '(' and PRIORITY.get(token, 0) <= PRIORITY.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)

   
    while stack:
        output.append(stack.pop())

    return ' '.join(output)

def evaluate_postfix(postfix_expression):
    """
    Обчислення математичного виразу у ЗПН.
    :param postfix_expression: str - вираз у ЗПН
    :return: float - результат обчислення
    """
    stack = []
    tokens = postfix_expression.split()

    for token in tokens:
        if token.isnumeric():  
            stack.append(float(token))
        else:  
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]  
    
if __name__ == "__main__":
    print("Введіть математичний вираз з пробілами між числами та операторами.")
    expression = input("Наприклад: 3 + 4 * 2 / ( 1 - 5 ) ^ 2\nВведіть вираз: ")
    postfix = infix_to_postfix(expression)
    print(f"Зворотний польський запис: {postfix}")
    result = evaluate_postfix(postfix)
    print(f"Результат обчислення: {result}")
