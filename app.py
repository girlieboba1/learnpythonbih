print("Enter the strike price: ")
strike_price_str = input()
strike_price = float(strike_price_str)

print("Enter the amount of vested options you want to exercise: ")
options_str = input()
options = int(options_str)

total_price = options * strike_price

print("Total exercise price is ", total_price)
