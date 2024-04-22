FROM dperdices/mininet

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    dsniff \
    arping \
    wireshark \
    dnsmasq-base \
    dnsutils \
    netcat \
 && rm -rf /var/lib/apt/lists/*
 
