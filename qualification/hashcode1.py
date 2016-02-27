#hashcode
import math

filename = "busy_day"
file = open(filename+".txt");
input = file.read().split('\n')
file.close()
with open(filename+"-output.txt",'w') as f:
	nothing=0

#line1: rows, columns, # drones, # turns, max payload
ROWS = int(input[0].split(" ")[0])
COLUMNS = int(input[0].split(" ")[1])
NUM_DRONES = int(input[0].split(" ")[2])
NUM_TURNS = int(input[0].split(" ")[3])
MAX_PAYLOAD =int(input[0].split(" ")[4])

commands = 0;
#print("ROWS: %s, COLUMNS: %s, ")

#line2: # products
NUM_PRODUCTS = int(input[1])
# print("# Products: "+NUM_PRODUCTS)
#line3: weight of product types
weights_array = input[2].split(" ")
#[100,5,450]

#line4: # warehouses
NUM_WH = int(input[3])

#Warehouses
warehouses_loc = []
warehouses_prod = []

for i in range(4,(NUM_WH*2)+4,2):
	warehouses_loc.append(input[i])
	warehouses_prod.append(input[i+1])

line = (NUM_WH*2)+4
#Orders
NUM_ORDERS = int(input[line])

orders = []
order_number = 0
###               order 1                   order 2
### [ ["0 0","# prods", "per item"], ["0 0","# prods", "per item" ]   ]
#### within order: [0]: coordinates, [1]: num products, [2]: # products per type

for i in range(line+1,(NUM_ORDERS*3)+line+1,3):
	orders.append([input[i],input[i+1],input[i+2]])
	order_number+=1

#input: "0 0", "1 3"
def distance(cell1,cell2):
	cell1 = cell1.split(" ")
	cell2 = cell2.split(" ")
	distance = math.sqrt( abs(int(cell1[0])-int(cell2[0]))**2 + abs(int(cell1[1])-int(cell2[1]))**2  )
	return round(distance)

#print(distance("0 0","3 3"))

#save drone locations
drones_location = []
for i in range(NUM_DRONES):
	drones_location.append("0 0")

def findClosestWH(drone):
	array=[]
	for wh in warehouses_loc:
		array.append(distance(wh,drones_location[drone]))
	return array.index(min(array))



def orderDroneTime(order,drone,wh):
	return distance(drones_location[drone],warehouses_loc[wh])+2+distance(warehouses_loc[wh],orders[order][0])

times=[]
for order in range(len(orders)): 
	temp=[]
	ind_min=[]
	for drone in range(NUM_DRONES):
		temp.append(orderDroneTime(order,drone,findClosestWH(drone)))
	min_temp=min(temp)
	#print(min_temp)
	ind_min.append((temp.index(min_temp),min_temp))
	times.append(ind_min)
#print(times[0])
dr=min(times, key= lambda t: t[0])[0][0]
ordr=times.index(min(times, key= lambda t: t[0]))

def load(drone,wh,product,numitems):
	global commands
	with open(filename+"-output.txt",'a') as f:
		f.write(drone+" L "+wh+" "+product+" "+numitems+"\n")
	commands+=1;

def deliver(drone,order,product,numitems):
	global commands
	with open(filename+"-output.txt",'a') as f:
		f.write(drone+" L "+order+" "+product+" "+numitems+"\n")
	commands+=1;

def checkProduct(order,wh):
	num_product_types=orders[order][2]
	wh_prods = warehouses_prod[wh]
	for item in num_product_types.split(" "):
		if(wh_prods[int(item)]>0):
			return True
		else:
			return False


if(checkProduct(ordr,findClosestWH(drone))):
	list_of_prods = orders[ordr][2].split(" ")
	list_of_prods.sort()
	weight=0
	while(weight<=MAX_PAYLOAD):
		counteritems = 0;
		for x,item in enumerate(list_of_prods):
			if(MAX_PAYLOAD-weight>weights_array[int(item)]):
				weight += weights_array[int(item)]
				if(list_of_prods[x+1]!=item):
					load(str(dr),str(findClosestWH(dr)),str(item),str(counteritems))
					# deliver(str(dr),str(ordr),str(item),str(counteritems))
				else:
					counteritems+=1
			load(str(dr),str(findClosestWH(dr)),str(item),str(counteritems))
			deliver(str(dr),str(ordr),str(item),str(counteritems))
		break


				
with open(filename+"-output.txt",'r+') as f:
		text = f.read()
		f.seek(0,0)
		f.write(str(commands)+"\n"+text)



#dr=times.index(min(times))











