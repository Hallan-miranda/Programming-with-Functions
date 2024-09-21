import math # import the module math 
import datetime # import the modeule datetim

#Get the current date
def get_current_date(): 
    return datetime.datetime.now().strftime("%G-%m-%d")

#Prompt the user to enter the width of the tire in mm 
w = int(input('Enter the width of the tire in mm (ex 205): '))
#Prompt the user to enter the ratio of the tire
r = int(input('Enter the aspect ratio of the tire (ex 60): '))
#Prompt the user to enter the diameter in inches
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

#Calculate the volume of the tire based on width (w), ratio(r), and diameter(d) 
def calc_tire_volume(w, r, d):
    volume = (math.pi * (w**2) * r * (2540 * d + w * r)) /10000000000
    return volume

#open the volumes.txt file and appending text values
with open("volumes.txt", "a") as files:
    current_date = get_current_date()

    volume = calc_tire_volume(w,r,d)

    print(f'The approximate volume is {volume:.2f} liters')

    #save the text inputs, date and tire volume on the volumes.txt file
    files.write(f'{current_date}, {w}, {r}, {d}, {volume:.2f}\n' )
    files.close()


#call de functio cal_tire_volume and return the value.
#print(f'The tire Volum is: {calc_tire_volume(w, r, d):.2f}')



