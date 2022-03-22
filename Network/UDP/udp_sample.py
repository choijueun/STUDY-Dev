import sys      # 터미널에서 실행
import socket   # 소켓 연결
import json     # json 변환

ECHO_PORT = 20001   # port 미입력시 기본 PORT
BUFSIZE = 1024      # 최대 수신가능 데이터 크기

# main    
def main():
    # argv 2개 미만
    if len(sys.argv) < 2:
        usage()
    # server 함수 호출
    if sys.argv[1] == '-s':
        udpServer()
    # client 함수 호출
    elif sys.argv[1] == '-c':
        udpClient()
    else:
        usage()
    
# 사용 방법 안내
def usage():
    sys.stdout = sys.stderr
    print('Usage: udp -s [port]             (server)')
    print('or:    udp -c host [port] <file  (client)')
    sys.exit(2) # 종료

'''
ex:
    [term1]
    python3 udp_sample.py -s 8001
    [term2]
    python3 udp_sample.py -c 127.0.0.1 8001
'''

# server
def udpServer():
    # port
    if len(sys.argv) > 2:
        port = eval(sys.argv[2])    # port 지정
    else:
        port = ECHO_PORT            # port 미지정
        
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    print('UDP ECHO SERVER READY')
    
    # Loop
    while True:
        # client msg 도착하면 다음 줄로 넘어가고 그렇지 않으면 대기(Blocking)
        data, clAddr = sock.recvfrom(BUFSIZE)
        
        # Print
        print('SERVER RECEIVED %r from %r' % (data, clAddr))
        
        # Parsing
        data = data.decode('utf-8')                     # bytes to string
        parsedMSG = 'UDP >>'+data+'<< UDP'
        # Send to client
        sendMSG = json.dumps(parsedMSG).encode('utf-8') # string to bytes
        sock.sendto(sendMSG, clAddr)

# client
def udpClient():
    if len(sys.argv) < 3:
        usage() # exit
    
    # Addr
    ip = sys.argv[2]
    if len(sys.argv) > 3:
        port = eval(sys.argv[3])    # port 지정
    else:
        port = ECHO_PORT            # port 미지정
    addr = ip, port
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 0))
    print('UDP ECHO CLIENT READY')
    
    # Loop
    while True:
        # Input
        line = sys.stdin.readline()
        if not line:
            break
        
        # Send text
        line = str.encode(line)
        sock.sendto(line, addr)
        
        # Return 대기
        data, servAddr = sock.recvfrom(BUFSIZE)
        # Print
        print('CLIENT RECEIVED %r FROM %r' % (data, servAddr))

main()