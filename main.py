#!/usr/bin/python3

from rich.prompt import Prompt
from manage_docker import *

while True:
    colour_print("green", f"{'_'*20}MENU{'_'*20}")
    colour_print("green", "[1] Status of containers")
    colour_print("green", "[2] Download new Image")
    colour_print("green", "[3] Run container")
    colour_print("green", "[4] Delete container")
    colour_print("green", "[5] Network details of container")
    colour_print("red", "[6] Exit")

    ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,7)])
    
    if ch == '1':
        container_status()
    elif ch == '2':
        dwnld_new_image()
    elif ch == '3':
        run_container()
    elif ch == '4':
        delete_container()
    elif ch == '5':
        display_docker_network()
    elif ch == '6':
        break
    else:
        colour_print("red", "Wrong option!! Try again")