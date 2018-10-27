from flask import request
from flask import FLASK
import socket
import time

class Client:
    __socket = 0

    app = Flask(__login__)
    app1 = Flask(__email__)
    app2 = Flask(__phone__)
    app3 = Flask(__fname__)
    app4 = Flask(__lname__)
    app5 = Flask(__password__)

    @app.route('/')
    @app1.route('/')
    @app2.route('/')
    @app3.route('/')
    @app4.route('/')
    @app5.route('/')
    __host__ = 0
    def __init__(self, hostage, port, timeout=None):
        self.__socket = socket.create_connection((hostage, port), timeout)
        __host__ = hostage
        
    @app.route('/', methods=['POST'])
    @app1.route('/', methods=['POST'])
    @app2.route('/', methods=['POST'])
    @app3.route('/', methods=['POST'])
    @app4.route('/', methods=['POST'])
    @app5.route('/', methods=['POST'])
    
    def receive(self):
        if request.method == "GET":
            login = request.form['login']
            email = request.form['email']
            password = request.form['password']
            phone = request.form['phone']
            fname = request.form['fname']
            lname = request.form['lname']
        if len(phone) <= 12 and len(phone) >= 11:
            self.incorrect_input(self)
            return False
        correctless_check(email, phone)
        self.__socket.sendall((' '.join(login, email, phone, fname,
                                        lname, password)).encode('utf-8'))
        main_server_answer = (self.__socket.recv(1024)).decode('utf-8')
        pass

    def incorrect_input(self):
        //то, что передаю обратно
        login = request.args.get('login')
        email = request.args.get('email')
        phone = request.args.get('phone')
        fname = request.args.get('fname')
        lname = request.args.get('lname')
        password = request.args.get('password')
        return render_template(__host__+'.html',
                               login = login,
                               email = email,
                               phone = phone,
                               fname = fname,
                               lname = lname,
                               password = password

    def correctness_check(self, email, phone):
        first = True
        for cur_elem in phone:
            if (not first and (not ('0' <= cur_elem and cur_elem <= '9') or cur_elem == '+')):
                self.incorrect_input(self)
                return False;
            first = False

        domens = ['mail.ru', 'yandex.ru', 'bk.ru', 'list.ru', 'gmail.com']

        special_symb = -1
        for i in range(len(email)):
            if ('0' <= email[i] and email[i] <= '9') or \
                    ('A' <= email[i] and 'Z' <= email[i]) or \
                    ('a' <= email[i] and 'z' <= email[i]) or \
                    (email[i] in {'!', '#', '$', '%', '&',
                                  '*', '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~'}):
                pass
            elif email[i] == '@':
                special_symb = i + 1
                break
            else:
                self.incorrect_input(self)
                return False
        if special_symb <= 0 or email[special_symb:len(email)] not in domens:
            self.incorrect_input(self)
            return False
        return True

    def send(self, data):
        pass
    def close(self):
        self.__socket.close()


a = Client('127.0.0.1', 10001)
host = 1;
while host is not None:
    host = input("Enter an adress (URL):")
    if host == '':
        break
    port = input("Enter a port:")
    a.receive(host, port)
    print("!!:", a.send(f))
