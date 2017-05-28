FROM ubuntu:xenial

MAINTAINER Christian Jauvin <cjauvin@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# install libreoffice, python2, pip2 and supervisor
RUN apt-get update && apt-get install -y libreoffice python python-pip supervisor

COPY app /app
COPY requirements.txt /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# install flask + appy
RUN pip install -r /app/requirements.txt

EXPOSE 12345

# Run both python webserver + soffice
CMD ["/usr/bin/supervisord"]
