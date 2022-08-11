import os
import socket
def ping(hostname):
    ping_test = os.system('ping -c 1 '+ hostname)
    if ping_test == 0:
        return True
    else:
        return False


def ping_scan(start, stop, mode='Online'):
    ping_construct = []
    ping_list = []
    start_list = start.split('.')
    stop_list = stop.split('.')
    for i in range(len(start_list)):
        ping_construct.append([int(start_list[i]), int(stop_list[i])])
    def ping_ele_1 (construct):
        if construct[0][1] - construct[0][0] > 0:
            for i in range(construct[0][0] , construct[0][1]+1):
                ping_ele_2(i,construct)
        else:
            ping_ele_2(construct[0][0], construct)
    def ping_ele_2 (ele1, construct):
        if construct[1][1] - construct[1][0] > 0:
            for i in range(construct[1][0] , construct[1][1]+1):
                ping_ele_3(ele1, i,construct)
        else:
            ping_ele_3(ele1, construct[1][0], construct)

    def ping_ele_3 (ele1, ele2, construct):
        if construct[2][1] - construct[2][0] > 0:
            for i in range(construct[2][0] , construct[2][1]+1):
                ping_ele_4(ele1, ele2, i,construct)
        else:
            ping_ele_4(ele1, ele2, construct[2][0], construct)    
    
    def ping_ele_4(ele1, ele2, ele3, construct):
        if construct[3][1] - construct[3][0] > 0:
            for i in range(construct[3][0] , construct[3][1]+1):
                ip = str(ele1)+'.'+str(ele2)+'.'+str(ele3)+'.'+ str(i)
                online_offline = ping(ip)
                if online_offline == True and mode =='Online' or mode == 'Any':
                    ping_list.append([ip,ping(ip)])
                elif online_offline == False and mode =='Offline' or mode == 'Any':
                    ping_list.append([ip,ping(ip)])
        else:
            ip = str(ele1)+'.'+str(ele2)+'.'+str(ele3)+'.'+ str(construct[3][0])
            online_offline = ping(ip)
            if online_offline == True and mode =='Online' or mode == 'Any':
                ping_list.append([ip,ping(ip)])
            elif online_offline == False and mode =='Offline' or mode == 'Any':
                ping_list.append([ip,ping(ip)])
    ping_ele_1(ping_construct)
    return ping_list


def port_test(hostname, port = 80):
    soc = socket.socket()
    soc.settimeout(1)
    try:
        conn = soc.connect_ex((hostname, int(port)))
        if (conn == 0):
            return True
            
    except:
        return False


def port_scan(hostname, start, stop, mode = 'Open'):
    port_list = []
    for i in range(start, stop + 1):
        open_closed = port_test(hostname, i)
        if open_closed == True:
            state = 'Open'
            if mode == 'Open' or mode == 'Any':
                port_list.append([i, state])
        else:
            state = 'Closed'
            if mode == 'Closed' or mode == 'Any':
                port_list.append([i, state])
        
    return port_list

print(port_scan('10.0.0.166', 21, 22, 'Any'))