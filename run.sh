escaped_display="host.docker.internal:0"
docker run -it --rm --privileged -e DISPLAY=${escaped_display} \
    -v /lib/modules:/lib/modules \
    -v ${PWD}:/root \
    dperdices/arp-spoofing-mn $@