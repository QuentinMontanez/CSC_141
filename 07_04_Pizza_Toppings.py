
prompt = "\nPlease choose which topping you want and I'll add it."
prompt += "\nEnter 'quit' to end the program"
message= "I will add Pepperoni, Sausage, and Pineapple as toppings to your pizza"
while message != 'quit':
    message = input(prompt)
    print(f"{message}is on the pizza")
            