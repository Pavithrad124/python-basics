try:
    ip = int(input())
    print(5/ip)
    if(ip>0):
        print(p)
except ValueError:
    print("give correct ip")
except ZeroDivisionError:
    print("enter other value")
except:
    print("check code")
