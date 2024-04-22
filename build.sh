#!/bin/bash
docker build --network=host -t dperdices/mininet docker-mininet-mac
docker build --network=host -t dperdices/arp-spoofing-mn .