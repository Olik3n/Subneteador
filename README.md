# 📡 IP Subnet Calculator

🚀 IP Subnet Calculator es un script en Python diseñado para calcular de forma rápida y precisa la mejor subred para una dirección IP dada y una cantidad específica de hosts.

Este script te proporciona información detallada sobre la máscara de subred, el CIDR, la dirección de red, el broadcast y el rango de hosts utilizables, ayudándote a optimizar la administración de redes.

📌 Características
✅ Calcula la máscara de subred óptima según el número de hosts.
✅ Muestra la dirección de red y la dirección de broadcast.
✅ Indica el rango de direcciones IP utilizables.
✅ Fácil de usar y sin dependencias externas (usa solo la librería estándar de Python).

🛠️ Instalación
````
git clone https://github.com/tuusuario/IP-Subnet-Calculator.git
cd IP-Subnet-Calculator
`````

⚡ Uso
Ejecuta el script pasando una dirección IP y la cantidad de hosts que necesitas
````
python script.py <IP> <Cantidad de Hosts>
```
🏗️ Cómo Funciona
Calcula los bits necesarios para la cantidad de hosts.
Obtiene la máscara de subred óptima usando la notación CIDR.
Genera la dirección de red y broadcast para definir el rango.
Muestra la cantidad de hosts utilizables dentro de la subred.

📜 Licencia
Este proyecto está bajo la Licencia MIT, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente.

✨ Autores
@CraZyZkoLL
