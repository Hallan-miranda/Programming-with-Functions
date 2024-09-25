import math #import the math 

#simule a database
data = {
    "#1 Picnic": [6.83, 10.16, 0.28 ],
    "#1 Tall": [7.78, 11.91, 0.43],
    "#2": [8.73,	11.59,	0.45],
    "#2.5":	[10.32,	11.91,	0.61],
    "#3 Cylinder":	[10.79,	17.78,	0.86],
    "#5":	[13.02,	14.29,	0.83],
    "#6Z":	[5.40,	8.89,	0.22],
    "#8Z short":	[6.83,	7.62,	0.26],
    "#10":	[15.72,	17.78,	1.53],
    "#211":	[6.83,	12.38,	0.34],
    "#300":	[7.62,	11.27,	0.38],
    "#303":	[8.10,	11.11,	0.42],
}

#read the data line by line, execute the calc volume and surface_area then return the storage_efficiency
def main():

    best_storage_efficiency = ["", 10000]
    best_cost_efficiency = ["", 10000]

    for item in data:
        
        radius = data[item][0]
        height = data[item][1]
        cost_per_can = data[item][2]

        cost_efficiency = compute_cost_efficiency(radius, height, cost_per_can)
        storage_efficiency = compute_storage_efficiency(radius, height)
        print(f'{item} {storage_efficiency:.2f} - {cost_efficiency:.2f} ')

        # save the best storage efficiency value
        if storage_efficiency < best_storage_efficiency[1]:
            best_storage_efficiency =  [item, storage_efficiency]
            
        # save the best cost efficiency value
        if cost_efficiency < best_cost_efficiency[1]:
            best_cost_efficiency = [item, cost_efficiency]

    print(f'The best cost Efficincy is {best_cost_efficiency[0]} with ${best_cost_efficiency[1]:.2f}')
    print(f'The best storage Efficincy is {best_storage_efficiency[0]} with {best_storage_efficiency[1]:.2f}')

#calc the volume 
def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

#calc the surface_area
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# calc the storage eficiency
def compute_storage_efficiency (radius, height):
    volume = compute_volume(radius,height)
    surface_area = compute_surface_area(radius,height)
    storage_efficiency = volume / surface_area
    return storage_efficiency

#calc the const efficiency
def compute_cost_efficiency(radius, height,cost_per_can ):
     volume = compute_volume(radius,height)
     const_effiency = volume / cost_per_can
     return const_effiency

main()