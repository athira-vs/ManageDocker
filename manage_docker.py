#!/usr/bin/python3

from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import os

console = Console()


def colour_print(colour, string):
    console.print(string, style = f'bold {colour}')


def execute_shell(cmd):
    return os.popen(cmd).read()


def container_status():
    colour_print("#FF00FF", os.system("docker container stats"))


def dwnld_new_image():
    image_name = Prompt.ask("Enter image name (image_name:tag)")
    colour_print("#FF00FF", execute_shell(f"docker pull {image_name}"))


def docker_image_list():
    cmd = "docker images | wc -l"
    count = int(execute_shell(cmd).strip())
    cmd = f"docker images | tail -n {count-1}| tr -s ' ' | cut -d' ' -f1,2 --output-delimiter=':'"
    return execute_shell(cmd).split()


def docker_container_list():
    cmd = "docker ps -a | wc -l"
    count = int(execute_shell(cmd).strip())
    cmd = f"docker ps -a | tail -n {count}| tr -s ' ' | rev |cut -d' ' -f1 | rev"
    return execute_shell(cmd).split()


def run_container():
    image_name = Prompt.ask("Enter image name", choices = docker_image_list())
    container_name = Prompt.ask("Enter name for container")
    cmd = f"docker run --name {container_name} {image_name}"
    colour_print("#FF00FF", execute_shell(cmd))


def delete_container():
    container_name = Prompt.ask("Enter name of the container", choices = docker_container_list())
    colour_print("#FF00FF", execute_shell(f"docker rm {container_name}"))


def display_docker_network():
    colour_print("#FF00FF", execute_shell("docker network ls"))


def modify_docker_network_menu():
    colour_print("green", f"{'_'*10}MODIFY NETWORK MENU{'_'*10}")
    colour_print("green", "[1] Disconnect application from bridge")
    colour_print("green", "[2] Show conection from bridge to app")
    colour_print("red", "[3] Exit")


def modify_docker_network():
    while True:
        modify_docker_network_menu()
        ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,5)])
        display_docker_network()
        if ch == '1': 
            connect_bridge()
        elif ch == '2':
            disconnect_bridge()
        elif ch == '3':
            show_connection_bridge()
        elif ch == '4':
            break
        else:
            colour_print("red", "Wrong option!! Try again")


def connect_bridge():
    status_container()
    container_name = Prompt.ask("\tEnter the container name ")
    bridge_name = Prompt.ask("\tEnter the bridge name")
    execute_shell(f"docker network connect {bridge_name} {container_name}")
    wait_status("\t\t Bridge Connected!!!")

    
def show_connection_bridge():
    bridge_name = Prompt.ask("\tEnter the bridge name")
    cmd = execute_shell(f"docker network inspect {bridge_name}")
    yprint("---------------------------------------------------------------")
    yprint(cmd)
    yprint("---------------------------------------------------------------")

    
def disconnect_bridge():
    container_name = Prompt.ask("\tEnter the container name ")
    bridge_name = Prompt.ask("\tEnter the bridge name")
    cmd = execute_shell(f"docker network disconnect {bridge_name} {container_name}")
    wait_status("\t Bridge Disconnected!!!")



if __name__ == "__main__":
    docker_image_list()
