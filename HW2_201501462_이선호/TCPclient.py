from socket import *
import time

serverName = '192.168.0.102'
serverPort = 12000
#메세지 수신 실패 횟수
fail_num = 0 
#최대 소요 시간
max_time = 0.0
#최소 소요 시간
min_time = 99999.9
#각 ping의 소요 시간
time_arr = []
#ping의 횟수
pingLength = 1000
print('tcp 통신의 경우(%d개의 메세지)'%(pingLength))

for i in range(pingLength):
    try:
        #전송할 메세지
        sentence = str(i) + "번 Ping"        

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.settimeout(1)
        #ping 시작 시간 
        start_time = time.time()       
        clientSocket.connect((serverName,serverPort))
        clientSocket.send(sentence.encode())
        
        modifiedSentence = clientSocket.recv(1024)
        #ping의 소요 시간
        elapsed_time = time.time() - start_time 

        ms = int(elapsed_time * 1000)
        print(serverName, '의 응답 : ', modifiedSentence.decode(), '시간: ', ms, 'ms')
        
        time_arr.append(elapsed_time)
        if elapsed_time > max_time:
            max_time = elapsed_time
        if elapsed_time < min_time:
            min_time = elapsed_time
        

        clientSocket.close()

    
    # 서버로부터 응답이 1초 안에 오지 않을 때S
    except timeout:
        print('요청시간이 만료되었습니다.')
        fail_num += 1

#실패 확률
fail_percentage = (fail_num / pingLength) * 100
#모든 ping의 소요시간 합
total_time = 0
for i in range(len(time_arr)):
    total_time += time_arr[i]


print('TCP')
print(serverName, '에 대한 Ping 통계: ')
print('    패킷: 보냄 = %d, 받음 = %d, 손실 = %d (%0.1f 손실).'%(pingLength, pingLength - fail_num, fail_num, fail_percentage))
print('    최대 소요시간 : %0.3fms, 최소 소요시간 : %0.3fms, 평균 소요시간: %0.3fms, 총 소요시간 : %0.7fms'%(max_time * 1000, min_time * 1000, (total_time/len(time_arr)) * 1000, total_time * 1000))