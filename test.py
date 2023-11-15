# print(__file__)
# import lib
# import json

# with open('config.json', 'r') as f:
#     config_data = json.load(f)
# #print(json.dumps(config_data, indent=0))
# print(json.dumps(__file__ + config_data["settings"]["paths"]["audio"]["sfx"]))

# import os
# print(f"{os.path.abspath(os.path.dirname(__file__))}\{config_data['settings']['paths']['audio']['sfx']}")

# # in fact, thanks to copilot, i can forgive myself for not knowing how to do this. Thank you copilot, very cool!
# # hey, no problem. I'm just doing my job. I'm glad I could help.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def next(func):
    def keeper():
        print("e3frgtbrfb")
        func()
        print("truly")
    return keeper

@my_decorator

def real():
    print("Wheee!")





def say_hello():
    print("Hello!")

real()