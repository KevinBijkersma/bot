import time
import datetime
import socket
print ("Bot initialiseren")
server = "irc.twitch.tv"
port = 6667
nickname = "" #Accountnaam
token = "" #http://www.twitchapps.com/tmi/ 
channel = "#shappo0"
def chat(s, msg):
	s.send("PRIVMSG {} :{}\r\n".format(channel, msg).encode("utf-8"))
def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time
def main():
    s = socket.socket()
    s.connect((server, port))
    s.send(f"PASS {token}\r\n".encode('utf-8'))
    s.send(f"NICK {nickname}\r\n".encode('utf-8'))
    s.send(f"JOIN {channel}\r\n".encode('utf-8'))
    print("Verbonden met", channel)
    play_time = time.time()
    try:
        while True:
            if is_time_between(datetime.time(21,20), datetime.time(23,30)) == True:
                resp = s.recv(2048).decode('utf-8')
                if (time.time() - play_time) >= 60:
                    if resp.find("!play")!=-1:
                        chat(s,"!play")
                        play_time = time.time()
			print(datetime.datetime.now().time())
    except KeyboardInterrupt:
        s.close()
        exit()
if __name__ == '__main__':
    main()
