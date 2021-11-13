import requests 
import random
import pyfiglet
from colorama import init
from termcolor import colored
init()
banner = pyfiglet.figlet_format("BAD JOKES BY HARSH")
banner = colored(banner, color = "cyan")
print(banner)
running = "TRUE"
while running:
    inputt = input("want to hear a  joke??")
    if inputt != "no":
        user_input = input(f"choose a topic for a joke: ")
        url = "https://icanhazdadjoke.com/search"
        reply = requests.get(url, headers = {"Accept": "application/json"}, params = {"term": user_input}).json()
        num_jokes = reply["total_jokes"]
        results = reply["results"]
        if num_jokes > 1:
            print(f"I have {num_jokes} jokes about {user_input} This one is really funny XD : ")
            print(random.choice(results)["joke"])
            more = input(f"Do I tell you another joke on {user_input}??")
            if more == "yes":
                run = "True"
            elif more == "no":
                run = "False"    
            while run:
                one_more = input("one more?")
                if one_more == "yes":
                    print(random.choice(results)["joke"])
                elif one_more == "no":
                    exit()
        elif num_jokes == 1:
            print(f"I have only one joke about {user_input} here it is : ")
            print(results[0]["joke"])    
        else:
            print(f"sorry, I dont have any jokes about {user_input}")
            print(results)
    elif inputt == "no":
        print("ok bye :) Call me when you need me ;)")
        exit()    