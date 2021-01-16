import mysql.connector
USI = input("Press any key to start:")

XC = input("Need to connect specific DB? y / n ")

if XC == 'y':
    mysqle = mysql.connector.connect(host=input("Enter Host Name:"),
                                     user=input("Enter User Name:"),
                                     passwd=input("Enter Password:"),
                                     database=input("Enter DB name to connect"))
    mycurs = mysqle.cursor()
else:
    mysqle = mysql.connector.connect(host=input("Enter Host Name:"),
                                     user=input("Enter User Name:"),
                                     passwd=input("Enter Password:"))
    mycurs = mysqle.cursor()

class SDBC:
    def __init__(self):
        self.choices()

    def choices(self):
        while True:
            User_Choices = input('''Choose One Choice To Controle The DB:
                Press[cbd] : Create a new DB           Press[sh] : Show all DBS
                Press[ct] : Create a new Table         Press[dt] : Drop a taple               
                Press[ddb] : Drop a DB                 Enter a Choice...''')

            if User_Choices == 'cbd':
                self.cbd()

            elif User_Choices == 'sh':
                self.sh()

            elif User_Choices == 'ct':
                self.ct()

            elif User_Choices == 'dt':
                self.dt()

            elif User_Choices == 'ddb':
                self.ddb()

            else:
                print("Enter A valid choice")

    def cbd(self):
        data = input("Enter Your DB Name:")
        sqle = " CREATE DATABASE {} ".format(data)
        mycurs.execute(sqle, data)
        mysqle.commit()

    def sh(self):
        mycurs.execute("SHOW DATABASES")
        for Db in mycurs:
            print(Db)

    def ct(self):
        data = input("Enter Table name:")
        sqle = " CREATE TABLE {}( A VARCHAR(100), B VARCHAR(200), C VARCHAR(300))".format(data)
        mycurs.execute(sqle, data)
        mysqle.commit()

    def dt(self):
        data = input("Enter A Table To delete:")
        sqle = "DROP TABLE {}".format(data)
        mycurs.execute(sqle,data)
        mysqle.commit()

    def ddb(self):
        data = input("Enter A DB To delete")
        sqle = "DROP DATABASE {}".format(data)
        mycurs.execute(sqle,data)
        mysqle.commit()

SDBC()