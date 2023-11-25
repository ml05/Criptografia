FROM ubuntu:20.10
COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install openssh-client openssh-server net-tools -y
RUN echo 'root:password' | chpasswd
RUN mkdir /var/run/sshd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

