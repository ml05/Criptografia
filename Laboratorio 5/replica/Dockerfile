# Usa la imagen base de Ubuntu 20.10
FROM ubuntu:20.10

ENV DEBIAN_FRONTEND=noninteractive

COPY sources.list /etc/apt/sources.list

RUN apt update && apt install sudo -y

RUN apt-get update && apt-get install openssh-client openssh-server net-tools -y

RUN sudo apt install git gcc make libssl-dev zlib1g-dev autoconf vim -y

# Habilitar el inicio del servicio
RUN mkdir /var/run/sshd

# Abre el puerto 22 para las conexiones SSH
EXPOSE 22

# Define el comando por defecto que se ejecutará al iniciar el contenedor
CMD ["/usr/sbin/sshd", "-D"]