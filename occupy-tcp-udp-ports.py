#!/usr/bin/env python
import argparse
import signal
import socket
import sys

def occupy_ports(ports):
  bindings = []
  fail_ports = []

  for port in ports:
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

def parse_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('-r', '--port_range', nargs=2, help='specify port range, e.g.: -r 2000 2003, which means: [2000, 2001, 2002].')
  parser.add_argument('-c', '--custmized_ports', help='specify customized ports by python statements, this argument will be evaluated using eval function, e.g.: -c "[2000, 2005] + list(range(3000, 3003))", which means [2000, 2005, 3000, 3001, 3002]')
  args = parser.parse_args()
  if args.port_range and args.custmized_ports:
    parser.error("Arguments -r and -c can't be used together.")
  return args

def get_ports():
  args = parse_arguments()
  if not args.port_range and not args.custmized_ports:
    ports = [port for port in range(2000, 3000)]
  elif args.port_range:
    ports = [port for port in range(int(args.port_range[0]), int(args.port_range[1]))]
  elif args.custmized_ports:
    ports = eval(args.custmized_ports)
  return ports

def release_ports(bindings):
  for s in bindings:
    try:
      s.close()
    except:
      pass

def release_ports_and_exit(bindings):
  release_ports(bindings)
  sys.exit(0)

def main(ports):
  print 'These ports(both tcp & udp) will be occupied:', ports
  bindings, fail_ports = occupy_ports(ports)
  print_fail_ports(fail_ports)
  print 'Done.'

  signal.signal(signal.SIGTERM, lambda _1, _2: release_ports_and_exit(bindings))

  # Cause the process to sleep until a signal is received;
  # the appropriate handler will then be called.
  # Refer https://docs.python.org/2/library/signal.html#signal.pause
  signal.pause()

if __name__ == "__main__":
  ports = get_ports()
  main(ports)
