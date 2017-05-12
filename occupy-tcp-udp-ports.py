#!/usr/bin/env python
import socket
import time

def occupy_ports():
  bindings = []
  fail_ports = []

  # Occupy port range from 2000 to 2999
  for port in range(2000, 3000):
    try:
      tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      tcp.bind(('', port))
      tcp.listen(1)
    except:
      fail_ports.append(('tcp', port))

    try:
      udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      udp.bind(('', port))
    except:
      fail_ports.append(('udp', port))
    bindings.extend([tcp, udp])

  return (bindings, fail_ports)

def print_fail_ports(fail_ports):
  if len(fail_ports) == 0:
    return
  print 'Failed to bind these ports:'
  for port_info in fail_ports:
    print port_info

def main():
  bindings, fail_ports = occupy_ports()
  print_fail_ports(fail_ports)

  # Pause program
  # Plan A, Wait for user input
  raw_input()
  # Plan B, sleep 3600 seconds
  # time.sleep(3600)

if __name__ == "__main__":
  main()
