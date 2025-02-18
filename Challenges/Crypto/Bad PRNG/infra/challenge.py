import sys
import errno
import socket
import threading

def handleConnection(conn, addr) -> bool:
    print('Handling connection')
    try:
        with conn:
            print('Connected by', addr)

            import bad_prng
            flag = "bronco{0k_1ts_n0t_gr34t}"
            output = []
            random = bad_prng.generate_seed()
            for c in flag:
                random = bad_prng.rand_word()
                output.append(random ^ ord(c))

            conn.sendall(bytes(output).hex().encode())
            conn.close()
            return True

    except ConnectionResetError:
        print(f'Connection reset. Connection by {addr} closing...')
        return False


def connect(s):
    try:
        print('connected')
        while True:
            try:
                conn, addr = s.accept()
            except ConnectionAbortedError:
                print(f'Client disconnected')
                return

            thread = threading.Thread(target=handleConnection, args=(conn, addr))
            thread.start()
            print(f'# Active threads: {threading.active_count()}')

    except KeyboardInterrupt:
        s.close()
        print('Exiting...')
        sys.exit(130)


def bind() -> bool:
    HOST = '0.0.0.0'
    PORT = 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f'Listening on {PORT}')
        connect(s)
        s.close()
    return False

def main():
    try:
        bind()
    except OSError as error:
        if error.errno == errno.EBADF:
            print(error)
            print('Continuing...')


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('Exiting...')
            sys.exit(130)
