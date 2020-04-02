import socket, argparse, sys

def Main(ip, port):
    print('-' * 120)
    print(f'Scanning target: {args.ip}')
    print(f'Checking port: {args.port}')
    print('-' * 120)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((args.ip, args.port))
        if result == 0:
            print(f'Open Port: {args.port}')
        else:
            print(f'Port: {args.port} is closed')
        s.close()
    except KeyboardInterrupt:
        print('\nExiting program.')
        sys.exit()
    except socket.gaierror:
        print('Hostname could not be resolved.')
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan a port on given hostname or ip')
    ap = argparse.ArgumentParser(prog='port_scanner.py', usage='%(prog)s [options] -ip "ip or hostname" -port "port to scan"')
    ap.add_argument('-ip', help='ip or hostname')
    ap.add_argument('-port', type=int, help='Port to scan')
    args = ap.parse_args()
    ip = args.ip
    port = args.port
    Main(ip, port)
