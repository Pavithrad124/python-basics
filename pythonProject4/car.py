class car:
    def display(self):
        print("car")
class Tesla(car):
    def display(self):
        #car.display(self)
        print("Tesla")
t=Tesla()
t.display()



try:
    ip = int(input())
    print(5/ip)
except ValueError:
    print("give correct ip")
except ZeroDivisionError:
    print("enter other value")
