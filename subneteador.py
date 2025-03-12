import ipaddress
import sys
import math

def calcular_subred(ip, cantidad_hosts):
    # Calcular la cantidad de bits necesarios para los hosts
    bits_necesarios = math.ceil(math.log2(cantidad_hosts + 2))  # +2 por la red y el broadcast
    cidr = 32 - bits_necesarios  # CIDR resultante
    subred = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)

    # Mostrar detalles de la subred
    print("\n📌 **Detalles de la subred:**")
    print(f"🔹 Dirección de Red: {subred.network_address}")
    print(f"🔹 Máscara de Subred: {subred.netmask}")
    print(f"🔹 CIDR: /{cidr}")
    print(f"🔹 Dirección de Broadcast: {subred.broadcast_address}")
    print(f"🔹 Rango de Hosts: {list(subred.hosts())[0]} - {list(subred.hosts())[-1]}")
    print(f"🔹 Hosts utilizables: {len(list(subred.hosts()))}")

if __name__ == "__main__":
    print("\n📖 **Manual de Uso:**")
    print("Este script calcula la subred óptima para una dirección IP dada y un número de hosts.")
    print("🔹 Uso: python script.py <IP> <Cantidad de Hosts>")
    print("🔹 Ejemplo: python script.py 192.168.1.10 50")
    print("🔹 El script determinará la mejor máscara de subred, CIDR y el rango de direcciones.")

    if len(sys.argv) < 3:
        print("\n❌ Error: Debes ingresar una IP y la cantidad de hosts.")
        print("Ejemplo: python script.py 192.168.1.10 50")
        sys.exit(1)

    ip = sys.argv[1]
    cantidad_hosts = int(sys.argv[2])

    calcular_subred(ip, cantidad_hosts)
