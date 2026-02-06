## tax.no_function.py
"""
done = False
while not done:
    sentinel = str.upper(input(f'Enter Q for quit or any otherkey to compute tax '))
    if sentinel == 'Q':
        done = True
        print(sentinel,done)
        continue
    else:
        print("Compute tax")
    price = float(input('What is the price '))
    tax = float(input('What is the tax rate? '))
    calculated_price = price * (100 + tax) / 100
    print(f'The calculated price is {calculated_price}')

## tax.with_function.py

while True:
    sentinel = str.upper(input(f'Enter Q for quit or any otherkey to compute tax '))
    if sentinel == 'Q':
        break
    else:
        print("Compute tax")

        ## input function
        def get_inputs():
            price = float(input('What is the price '))
            tax = float(input('What is the tax rate? '))
            return price, tax
        
        ## price with tax calculation function
        def calculate_price_with_tax(tax, price):
            price_with_tax = price * (100 + tax) / 100
            return price_with_tax
        price, tax = get_inputs()
        calculated_price = calculate_price_with_tax(tax, price)
        print(f'The calculated price is {calculated_price}')
"""
## add_multi_function.py
def add_multi(x,y):
    sum_xy = x + y
    multi_xy = x * y
    return sum_xy, multi_xy

sum, multi = add_multi(10,20)
print(f'Sum is {sum} and Multiplication is {multi}')

## add_multi_lambda.py
add_multi = lambda x, y: (x + y, x * y)

sum, multi = add_multi(10,20)
print(f'Sum is {sum} and Multiplication is {multi}')
