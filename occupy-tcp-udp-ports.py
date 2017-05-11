#!/usr/bin/env python
import socket

bindings = []

# Occupy port range from 2000 to 2999
for port in range(2000, 3000):
  tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcp.bind(('', port))
  tcp.listen(1)
  udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp.bind(('', port))
  bindings.extend([tcp, udp])

# Wait for user input
raw_input()
