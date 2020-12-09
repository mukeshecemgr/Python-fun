import socket
import _thread
import time
import json
import pickle
import utility
import tkinter
from utility import *

userID = '7091728998'
userName = 'Mukesh'



MAIN_TABLE_NAME = 'usr_'+userID
DB_NAME = 'clientDB'
CONTACT_TABLE_NAME='contacts'
#table Schema
MAIN_TABLE_DISCRIPTON = (
    "CREATE TABLE `"+MAIN_TABLE_NAME+"` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `time` varchar(128) ,"
    "  `contacts` varchar(16) NOT NULL,"
    "  `status` enum('Online','Offline') NOT NULL,"
    "  `reply_status` enum('no','yes') NOT NULL,"
    "  `message` varchar(2048) ,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

CONTACT_TABLE_DISCRIPTON = (
    "CREATE TABLE `"+CONTACT_TABLE_NAME+"` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `contacts` varchar(16) NOT NULL,"
    "  `name` varchar(20) ,"
    "  `status` enum('Offline','Online') NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

#serverDB = 'serverDB'
ip = '127.0.0.1'
port = 2222
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#client.bind((ip,port))
chat_box={}
enable_msgList = 1

def menu():
    print("+--------------------+")
    print("1. Add Buddies ")
    print("2. Delete Buddy")
    print("3. Show New Messages")
    print("4. Show Online Buddies ")
    print("5. Go Offline")
    op = input("Option :")
    if op == '':
        return 0
    return int(op)
    

def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    my_msg = chat_box['myMsg']
    msg = my_msg.get()
    lTime = time.asctime()
    #print(msg)
    msg_list = chat_box['msgList']
    box_msg="{:<8}[{}]:{}".format(userName,lTime,msg)
    msg_list.insert(tkinter.END, box_msg)
    my_msg.set("")  # Clears input field.
    msg_send = {
        'type':'MessageSend',
        'sender':userID,
        'receiver':chat_box['receiver'],
        'time':lTime,
        'message':msg
    }
    payLoad =  pickle.dumps(msg_send)
    client.send(payLoad)



def chatBox(title):
    top = tkinter.Tk()
    top.title(title)
    chat_box['top'] = top
    messages_frame = tkinter.Frame(top)
    my_msg = tkinter.StringVar()  # For the messages to be sent.
    my_msg.set("Type your messages here.")
    chat_box['myMsg'] = my_msg
    scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
    # Following will contain the messages.
    msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    chat_box['msgList'] = msg_list
    messages_frame.pack()

    entry_field = tkinter.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send)
    send_button.pack()


def msg_sender(mydb,cursor,userID,clientObj,receiverID):
    while True:
        lTime = time.asctime()
        print("{}[{}]:".format(userID,lTime))
        #message = input()
        data = {
            'type':'MessageSend',
            'time':lTime,
            'sender':userID,
            'receiver':receiverID,
            'message':"Hello"
        }
        payLoad = pickle.dumps(data)
        clientObj.send(payLoad)



def add_buddies(mydb,cursor):
    'Adding the buddies based on their mobile number'
    while True:
        number=input("Enter Mobile Number:")
        name=input("Name:")
        
        insert_contact = ("INSERT INTO {} (contacts, name) VALUES (%(contacts)s, %(name)s)".format(CONTACT_TABLE_NAME))
        print(insert_contact)
        contact_params={
            'contacts':number,
            'name':name
        }
        insert_data(mydb,cursor,insert_contact, contact_params)
        op = input("Wish to add more y/n:")
        if op == 'y':
            continue
        else:
            return

def delete_buddies():
    'deleting buddies from the contact list'



def newMessages(mydb,cursor,userID):
    'Show New Messages'
    query = ("SELECT contacts,count(reply_status) FROM {} WHERE reply_status=1 group by contacts".format(MAIN_TABLE_NAME))

    result = query_table(mydb,cursor,query,MAIN_TABLE_NAME)
    if len(result) is not 0:
        # Print the names of the columns. 
        print ("{:<3} {:<15} {:<11}".format('Id','Contacts', 'New Message')) 
  
        # print each data item. 
        id = 1
        for i in result:  
            print ("{:<3} {:<15} {:<11}".format(id,i[0],i[1])) 
            id += 1
        select = int(input("Select Id to See the message:"))
        count = 1
        for i in result:
            if count == select:
                print("Match Found for <{}>".format(i[0]))
                chatBox(i[0])
                query = ("SELECT contacts,time,message FROM {} WHERE contacts={} ".format(MAIN_TABLE_NAME,i[0]))
                result = query_table(mydb,cursor,query,i[0])
                msg_list = chat_box['msgList'] 
                chat_box['receiver'] = i[0]
                for idx in result:
                    msg="{:<8}[{}]:{}".format(idx[0],idx[1],idx[2])
                    msg_list.insert(tkinter.END, msg)
                    #print("{}[{}]: {}".format(idx[0],idx[1],idx[2]))
                    
            count += 1




def onlineBuddies(mydb,cursor,userID):
    'Check who is online'
    query="select * from {} where status=2".format(CONTACT_TABLE_NAME)
    result = query_table(mydb,cursor,query,CONTACT_TABLE_NAME)
    if len(result) is not 0:
        print("{:<3} {:<15} {:<15} {:<11}".format('Id','Contacts','Name', 'Status'))

        id = 1
        for i in result:
            print ("{:<3} {:<15} {:<15} {:<11}".format(id,i[1],i[2],i[3]))
            id += 1
        select = int(input("Select Id to Chat with..:"))
        count = 1
        for i in result:
            if count == select:
                print("Match Found for <{}>".format(i[1]))
                chatBox(i[2])
                chat_box['receiver'] = i[1]
                query = ("SELECT contacts,time,message FROM {} WHERE contacts={} ".format(MAIN_TABLE_NAME,i[1]))
                result = query_table(mydb,cursor,query,i[1])
                msg_list = chat_box['msgList']  
                #print("yahoooooooo",msg_list,result)
                for idx in result:
                    msg="{:<8}[{}]:{}".format(i[2],idx[1],idx[2])
                    msg_list.insert(tkinter.END, msg)
                   # print("{}[{}]: {}".format(idx[0],idx[1],idx[2]))
            count += 1



def goOffline(userID):
    'Adio Amigos'
    offline_msg={
        'type':'Offline',
        'sender':userID
    }
    data = pickle.dumps(offline_msg)
    client.send(data)


def msg_receiver(mydb,cursor,userID,clientObj, chat_box):
    'This thread will keep receiving message from server'
    while True:
        data = clientObj.recv(2048)
        #print("Message Received..")
        msg = pickle.loads(data)
        if msg.get('type') == 'Status':
            contacts = msg.get('contacts')
            for cont,status in contacts.items():
                if status == 'Offline':
                    user_status = "UPDATE {} SET status = {} WHERE  contacts={}".format(CONTACT_TABLE_NAME,1,cont)
                else:
                    user_status = "UPDATE {} SET status = {} WHERE  contacts={}".format(CONTACT_TABLE_NAME,2,cont)
                update_data(mydb,cursor,user_status)
        if msg.get('type') == 'MessagRecv':
            user = str(msg.get('sender'))
            print("Message Received from <{}>".format(user))


            msg_list = chat_box['msgList']
            sender_info = ("INSERT INTO usr_7091728998 (time,contacts, status, reply_status, message) VALUES (%(time)s, %(contacts)s, %(status)s,%(reply_status)s, %(message)s)")

            sender_params = {
                'time':str(msg.get('time')),
                'contacts':user,
                'status':'Online',
                'reply_status':'no',
                'message':msg.get('message')
            }
            insert_data(mydb,cursor,sender_info, sender_params)
            #msg="{:<8}[{}]:{}".format(msg['sender'],msg['time'],msg['message'])
            #msg_list.insert(tkinter.END, msg)
            
            print("{}[{}]:{}".format(msg['sender'],msg['time'],msg['message']))

def contacts_status(mydb,cursor,userID,client):
    print('Keep running and checking about all contacts Online Status')
    while True:
        query="select contacts,status from {}".format(CONTACT_TABLE_NAME)
        result = query_table(mydb,cursor,query,CONTACT_TABLE_NAME)
        online_check={
            'type':'Status',
            'sender':userID
            }
        contacts={}
        if len(result) != 0:
            for i in result:
                contacts[i[0]] = i[1]
            online_check['contacts'] = contacts
            data=pickle.dumps(online_check)
            client.send(data)

        time.sleep(3)



def connectServer(mydb,cursor,userID):
    serverIP = '127.0.0.1'
    serverPort = 1234
    try:
        client.connect((serverIP, serverPort)) 
    except:
        print("Server connection is not established")
        return
    
    #Notify to server you are online now :)
    lTime = time.asctime()
    helloMsg = {'type':'Online','user':userID, 'time':lTime}
    data = pickle.dumps(helloMsg)
    client.send(data)
    # Create two threads as follows
    try:
        _thread.start_new_thread( msg_receiver, (mydb,cursor,userID, client,chat_box) )
        _thread.start_new_thread( contacts_status, (mydb,cursor,userID, client ) )
    except:
        print ("Error: unable to start thread")
    

def client_start(mydb,cursor,userID):
    connectServer(mydb,cursor,userID)
    while True:
        op = menu()
        if op == 1:
            add_buddies(mydb,cursor)
        elif op == 2:
            delete_buddies()
        elif op == 3:
            newMessages(mydb,cursor,userID)
        elif op == 4:
            onlineBuddies(mydb,cursor,userID)
        elif op == 5:
            goOffline(userID)



if __name__ == '__main__':
    try:
        mydb = mysql.connector.connect(host='127.0.0.1',user='root',database=DB_NAME)
        cursor = mydb.cursor()
    except mysql.connector.Error as err:
        mydb = mysql.connector.connect(host='127.0.0.1',user='root')
        cursor = mydb.cursor()
        create_database(cursor,DB_NAME)
    
    db_init(mydb,cursor,MAIN_TABLE_DISCRIPTON,MAIN_TABLE_NAME,DB_NAME)
    #Create Contact Table where all contacts entries are made
    createTable(cursor,CONTACT_TABLE_DISCRIPTON,CONTACT_TABLE_NAME)
    client_start(mydb,cursor,userID)

    while True:
        pass