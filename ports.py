import sys, socket

ip = f"{sys.argv[1]}"
open_ports = []
ports = range(1, 65535)


def probe_port(ip, port, result=1):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    r = sock.connect_ex((ip, port))
    if r == 0:
      result = r
    sock.close()
  except Exception as e:
    pass
  return result


for port in ports:
  sys.stdout.flush()
  response = probe_port(ip, port)
  if response == 0:
    open_ports.append(port)
    print("\033[32mport {} is open\033[0m".format(port))
  else:
    print("port {} is closed".format(port))

if open_ports:
  print("\033[32mOpen Ports are:\033[0m")
  print("\033[32m", sorted(open_ports), "\033[0m")
  # push the ports to a file
  with open('open_ports.txt', 'w') as f:
    for port in sorted(open_ports):
      f.write(str(port) + '\n')
else:
  print("\033[32mLooks like no ports are open :(\033[0m")
