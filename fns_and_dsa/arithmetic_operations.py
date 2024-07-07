def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operation based on the given inputs.
    
    :param num1: First number (float)
    :param num2: Second number (float)
    :param operation: String specifying the operation ('add', 'subtract', 'multiply', 'divide')
    :return: Result of the operation or an error message
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
