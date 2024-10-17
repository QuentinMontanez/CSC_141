
prompt = "\nPlease choose which topping you want and I'll add it."
prompt += "\nEnter 'quit' to end the program"
message= "I will add Pepperoni, Sausage, and Pineapple as toppings to your pizza"
while message != 'quit':
    message = input(message)
    print(f"{message}is on the pizza")
    if message == "Pepperoni":
        print("It's not a healthy topping")
        quit
        break
        
        
    
            