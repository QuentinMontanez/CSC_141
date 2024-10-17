name= input("\nWhat is your name?")
prompt= input("If you had the choice to go somewhere special, where would it be?")
prompts=(name) = prompt
repeat= input("Does anyone else have somewhere in mind if you had the option to go there? (yes/no)")
if repeat == 'no':
    polling_active = False
print("\n---Poll Results---")
for name, prompt in prompts/iter():
    print(f"{name} would like to go to {prompt}")
