import math # import the moduel math to use math.pi(number pi)

#Calclate the volume of the tire based on width (w), ratio(r), and diameter(d)
def calc_tire_volume(w, r, d):
    volume = (math.pi * (w**2) * r * (2540 * d + w * r)) /10000000000
    return volume

#Prompt the user to enter the width of the tire in mm 
w = int(input('Enter the width of the tire in mm (ex 205): '))
#Prompt the user to enter the ratio of the tire
r = int(input('Enter the aspect ratio of the tire (ex 60): '))
#Prompt the user to enter the diameter in inches
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

#call de functio cal_tire_volume and return the value.
print(f'The tire Volum is: {calc_tire_volume(w, r, d):.2f}')



