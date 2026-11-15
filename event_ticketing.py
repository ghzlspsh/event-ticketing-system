import time
Events = []
Users = []
def show_Events() :

    for i , item in enumerate(Events):
        print(i+1 , end='')
        print(item.name)
def get_number(message) :

    while True :
        try :
            return int(input(message))
        except ValueError:
            print('please enter number.')
def check_events_num(num):
        return 1 <= num <= len(Events) 

            
class User :
    def __init__(self , name , username , email , password):

        #if not name :
            #raise ValueError('name cant be empty')
        self.name = name 
        self.username = username
        self.password = password
        self.email = email
        self.history = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , new):
        if not new :
            raise ValueError('name can not be empty !')
        
        self.__name = new

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self , new):
        if not new :
            raise ValueError('username can not be empty !')
        self.__username = new
    @property
    def password(self) :
        return self.__password

    @password.setter
    def password(self , new ) :
        if not new : 
            raise ValueError('Password can not be empty !')
        if len(new) >= 8 :
            self.__password = new
        else : 
            raise ValueError('your password must have at least 8 caractes')

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self ,new):
        if not new : 
            raise ValueError('Email can not be empty !')

        if new.endswith('@gmail.com'):
            self.__email = new
        else:
            raise ValueError('mail should be gmail')


    def purchase_history(self) :
        if not self.history :
            print('you did noy buy anything !')
            return 
        print(f'username : {self.username}')
        for item in self.history :
            for event in item[0] :
                print(f'the name : {event[0].name} ')
            print(f'your total tickets : {item[1]}')
            print(f' your total price : {item[2]}')
                        

class Reservation : # می شود یک لیست هر سابجکتش که ان لیست یک یوزرنیم هم دارد
    def __init__(self ,user):
        self.user = user
        self.reserv = []# وقتی که کلاس خود را به صورت یک لیست تعریف می کند سلف های موجود در متد های شما به موجودیت لیست اشاره دارد

    def add(self , e , t):
        if t <= e.left_sit :
            self.reserv.append((e , t))
            e.reserved += t
            e.left_sit -= t 
            print('reserved successfuly.')
            
        else : 
            print('not enough capacity')
            return

    def delet(self):
        self.show_reserv()
        a = get_number('which one do you want to delet? ')
        if a <= 0  or a > len(self.reserv): 
            print('invalid')
            return
        self.reserv[a-1][0].reserved -= self.reserv[a-1][1]
        self.reserv[a-1][0].left_sit += self.reserv[a-1][1]
        del self.reserv[a-1]
        print('deleted successfuly.')
    
        

    def show_reserv(self):
        for i , item in enumerate(self.reserv):
            print(i+1 , end='.')
            print(f'event : {item[0].name} , ticket :  {item[1]}')
        

class Buy :
    count = 0
    def __init__(self , reserv):

        self.reserv = reserv
        self.order = reserv.reserv.copy()

        Buy.count += 1
    def orderlist(self) :
        print(self.reserv.user.name)
        tp = 0 
        tt = 0
        for item in self.order  :  
            print(f'name of event : {item[0].name}\ndate of event : {item[0].date}\nprice of event : {item[0].price}\nYour tickets : {item[1]}')
            tp += item[0].price*item[1]
            tt += item[1]
            item[0].sold += item[1]
            item[0].reserved -= item[1]
        print(f'total price : {tp}')
        print(f'total tickets : {tt}')
    
        self.reserv.user.history.append((self.order.copy() , tt , tp))
        self.reserv.reserv.clear()

          
class Admin(User):
    def __init__(self, name, username, email, password):
        super().__init__(name, username, email, password)



    def creat_Event():
        while True :
            a = input('name : ')
            b = (input('date : '))
            c = input('place : ')
            d = input('capacity : ')
            e = input('price : ')
            try:
                m = Event(a, b, c, d, e,)
                Events.append(m)
                break
            except ValueError as error :
                print(error)
    def statistics():
        print(f'total users : {len(Users)}')
        print(f'total events : {len(Events)}')
        s = 0
        r = 0
        for user in Users :
            for item in user.history : 
                s += item[1]
                r += item[2]
        print(f'total sold tickets : {s} ')
        print(f'total revenue : {r}')

    

    
   
import time 
class Event :
    def __init__(self , name , date , place , capacity , price ):
        self.name = name 
        self.date = date 
        self.place = place
        self.capacity = capacity
        self.price = price
        self.sold = 0
        self.reserved = 0 
        self.left_sit = self.capacity

    @property 
    def date(self) :
        return self.__date

    @date.setter
    def date(self , new) :
            if not new :
                raise ValueError('date cant be empty')
            try :
                n = time.strptime(new , '%Y/%m/%d')
            except ValueError :
                raise ValueError('wrong date format')

            a = time.localtime()
            if n >= a : 
                self.__date = n 
            else :
                raise ValueError('wrong date value')


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self , new):
        try :
            new = int(new)
        except ValueError:
            raise ValueError('capacity should be number')
        if self.check_int(new):
            self.__capacity = new
        else :
            raise ValueError('capacity should more than 0')


    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self , new):
        try :
            new = int(new)
        except ValueError:
            raise ValueError('the price should be number')
        if self.check_int(new) :
            self.__price = new 
        else :
            raise ValueError('your number is not available')

    @staticmethod
    def check_int(a):
        if isinstance(a , int) and a > 0:
            return True
        else :
            return False



    def show_ditails(self) :
        for item in (Events):
            if self == item : 
                print(f'name : {item.name}\ndate : {item.date}\nplace : {item.place}\ncapacity : {item.capacity}\nprice : {item.price}\nsold : {self.sold}\nreserved : {self.reserved}\nleft_sit :{self.left_sit}')

    def change_Event(self):
            Admin.creat_Event()
            h = Events[len(Events)-1]
            Events[self-1] = h
            Events.pop(len(Events)-1)
            print('The event was edited successfully.')
    def delet_Event(self):
            Events.pop(self-1)
            print('The event was deleted successfully')

def user_panel(u):
            reserv1 = Reservation(u)

                
            while True :
                    a = get_number('1.show events\n2.reserve\n3.cancel reservation\n4.show reservation\n5.buy\n6.purchase history\n0.exit ')
                    if a < 0 or a > 6 :
                        print('out of range.')    
                        continue                
                    if a == 1 :
                        show_Events()
                        b = get_number('which one do you want its ditails? 0.back : ')
                        if b == 0 : 
                            continue
                        if check_events_num(b):
                            Events[b-1].show_ditails()
                            print('--------------')

                        else :
                            print('out of range.')
                            
                    if a == 2 :
                        show_Events()
                        b = get_number('Which Event do you want to reserv ? 0.back ')
                        if b == 0 : 
                            continue
                        if not check_events_num(b):
                            print('out of range.')
                            continue
                        c = get_number('How many tickets do you want ? ')
                        if c <= 0 : 
                            print('invalid , only positive number.')
                            continue
                        reserv1.add(Events[b-1] , c )

                        print('--------------')
                        
                    if a == 3 :
                        if  not reserv1.reserv :
                            print('you did not reserv anything yet.')
                            continue
                        reserv1.delet()
                        
                        print('--------------')
                    if a == 4 :
                        print('Your reservation : ')
                        reserv1.show_reserv()
                        print('--------------')
                    if a == 5 :
                        while True : 
                            warm = get_number('Are you sure about your reservation ? 1.Yes\n2.No')
                            if warm == 2 :
                                break
                            if warm == 1 : 
                                if not reserv1.reserv : # اگر لیست بود همین رزرو کفایت می کرد ولی این در واقع یک شی است که به شکل لیست است
                                    print('you should reserv first !')
                                    break
                                else :
                                    o = Buy(reserv1)
                                    o.orderlist()
                                    break
                            else :
                                print('invalid')
                    if a == 6 : 
                        u.purchase_history()

                    if a == 0 : 
                        break


                    
                            
                            

admin1 = Admin('admin1' , 'admin1' , 'example@gmail.com' , '123456789')
while True :
    first = get_number('Welcom...\n1.Login\n2.Register\n0.exite')
    if first < 0 or first > 2 : 
        print('out of range')
    if first == 0 : 
        break

    if first == 1 :
        b = input('Enter your username : ')
        d = input('Enter your email :  ')
        c = input('Enter your password for this account : ')
        flag = False
        for user in Users : 
            if user.email == d and user.username == b and user.password == c : 
                flag = True
                user_panel(user)
                break

        if flag == False :
            if d == admin1.email and c == admin1.password :
                print(f'Welcom {admin1.name}')
                while True :
                    a = get_number('1.add event , 2.show events , 3.Edit , 4.delet , 5.system statistics , 6.most populer event , 0.exit ')
                    if a < 0 or a > 6 : 
                        print('out of range')
                    if a == 1 :
                        Admin.creat_Event() 
                        while True :
                            ask = input('do you want to creat more ? [Y/N]')
                            if ask == 'Y' :
                                Admin.creat_Event() 
                            elif ask == 'N' :
                                break
                            else :
                                print('invalid only Y or N')
                        
                    if a == 2 : 
                        show_Events()
                        while True :
                            b = get_number('give the number for more ditailes :\nif you want to back to Homepage Enter 0 :')
                        
                            if b == 0 :
                                break
                            if check_events_num(b) :
                                Event.show_ditails(Events[b-1])

                            else :
                                print('invalid value')


                    if a == 3 : 
                        show_Events()
                        while True :
                            q =get_number('which one do you want to edit ?\nif you want to back to Homepage Enter 0 :')
                            if q == 0 :
                                break
                            if not check_events_num(q) :
                                print('out of range')
                                continue

                            if Events[q-1].sold > 0  or Events[q-1].reserved > 0 :
                                print('sorry , this event has sold out so you cant edit it')
                                
                            else:
                                Event.change_Event(q)
                            
                    if a == 4 :
                        show_Events()
                        while True :
                            q = get_number('which one do you want to delet ?\nif you want to back to Homepage Enter 0 :')
                            if q == 0 :
                                break
                            if not check_events_num(q) :
                                print('out of range')
                                continue
                            if Events[q-1].sold > 0  or Events[q-1].reserved > 0  :
                                print('sorry , this event has sold out so you cant delet it')
                                
                            else :
                                Event.delet_Event(q)

                    if a == 5 : 
                        Admin.statistics()


                    if a == 6 :
                        m = 0
                        n = []
                        for event in Events:
                            if event.sold > 0 : 
                                if event.sold > m : 
                                    m = event.sold 
                                    n = [event.name]
                                elif event.sold == m :
                                    n.append(event.name)

                                

                        print(f'the most populer event is {n} ')
                            


                    if a == 0 :
                        break




            else :

                print('there is no user or admin with these information')
    if first == 2 :
            while True :
                a = input('name : ')
                b = input('username : ')
                c = input('emial : ')
                d = input('password : ')
                m = False
                for user in Users :
                    if user.username == b or user.email == c : 
                        m = True
                        break
                if m : 
                        print('this user has already exsit')
                        continue

                    
                        
                try:
                    u = User(a, b, c, d)
                    print(f'welcome {a}')
                    Users.append(u)
                    break
                except ValueError as error :
                    print(error)



            user_panel(u)


               
  


                    
                            
                            


                
            


    
    





                


    

    
