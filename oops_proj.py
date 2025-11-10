class chatbook:

    __user_id = 0

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Default User'
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()


    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value


    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value    

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()

    
    def signup(self):
        email = input("Enter your email here")
        pwd = input("Enter your password here")
        self.username = email
        self.password = pwd
        print("You have signed up succesfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username here: ")
            pwd = input("Enter your password here: ")
            if self.username == uname and self.password == pwd:
                print("You have successfully logged in")
                self.loggedin = True
            else:
                print("Please entre valid credentials")
        print("\n")
        self.menu()   


    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here")
            print(f"Your message {txt} has been posted successfully ")
        else:
            print("You need to sign-in to post content")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin == True:
            txt = input("Enter your message here ")
            frnd = input("Whom to send the msg ")
            print(f"Your msg has been sent to {frnd}")
        else:
            print("You need to sign-in to post something")
        print("\n")
        self.menu()        

    







