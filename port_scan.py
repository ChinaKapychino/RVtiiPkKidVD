import socket
import json
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor

with open("port_list.json", "r") as file:
    data = json.load(file)
    ports = data["ports"]

target_ip = input("TargetIP: ")

def scan_port(ip, port, protocol):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, int(port)))
        if result == 0:
            print(f"{Fore.GREEN}Порт {port} открыт ({protocol}){Style.RESET_ALL}")
            return f"IP: {ip} Порт {port} открыт ({protocol})"
        else:
            print(f"Порт {port} закрыт")
            return None
    except Exception as e:
        print(f"Ошибка при сканировании порта {port}: {e}")
        return None

def scan_ports(ip, ports):
    open_ports = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_port = {executor.submit(scan_port, ip, port, protocol): (port, protocol) for port, protocol in ports.items()}

        for future in future_to_port:
            port, protocol = future_to_port[future]
            result = future.result()
            if result:
                open_ports.append(result)

    with open("open_ports.txt", "w") as output_file:
        for entry in open_ports:
            output_file.write(f"{entry}\n")

scan_ports(target_ip, ports)
