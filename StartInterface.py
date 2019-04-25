def order_input():
    order = input("Please enter the order of your function: (1) for first order, or (2) for second order: ")
    if order == str(1):
        print('First Order')
    elif order == str(2):
        print('Second Order')
    else:
        print('Please type either 1 or 2')
        order_input()
    return order

order_input()
