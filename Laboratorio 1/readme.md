# Laboratorio 1: ICMP + Cesar

Descripcion de los archivos:

- cesar.py: cifrar el mensaje utilizando la consola

    ```python3 cesar.py "mensaje a cifrar" [corrimiento]```

- pingv4.py: enviar un mensaje por medio de paquetes ICMP, utilizando localhost como destino. Se enviara un paquete por cada carecter del mensaje.

    ```python3 pingv4.py "mensaje cifrado"```

- readv2.py: lee una captura .pcapng con paquetes ICMP, los cuales podrian contener un mensaje cifrado en el campo data. Entrega el mensaje con 26 corrimientos aplicados (de 0 a 25), indicando en verde el mensaje mas probable basado en las frecuencias de las letras en espanol.

    ```python3 readv2.py captura.pcapng```

- datacifrada.pcapng: una captura de mensajes ICMP realizada con un mensaje encriptado.