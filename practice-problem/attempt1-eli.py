# First Attempt will be a lazy attempt to try I/O.
# Traverse the lines, paint individual squares.

rownum = 0;
ROWS = 0;
COLUMNS = 0;
filename = "logo"
commands = 0;
with open(filename+"-output.txt",'w') as f:
	nothing=0

def main():
	global rownum, ROWS, COLUMNS

	## Open File
	file = open(filename+".txt");

	## Read Line 1
	for line in file:
		if(rownum==0):
			dimline = line.split(' ')
			ROWS = dimline[0]
			COLUMNS = dimline[1]
			# with open(filename+"-output.txt",'a') as f:
			# 	f.write(str(ROWS)+" "+str(COLUMNS))
			rownum+=1
		else:
			##Read next ROW lines.
			for i in range(len(line)):
				from = "0,0"
				
				lineflag=false;
				if line[i] == "#":
					if line[i+1] != "#":
						if !lineflag:
							paintSquare(rownum-1,i,0)
						else:					
							paintLine(from.split()[0],from.split()[1],rownum-1,i)
							lineflag=false
					else:
						if !lineflag:
							from = rownum-1+","+i
							lineflag = true
						
			rownum+=1
	
	with open(filename+"-output.txt",'r+') as f:
		text = f.read()
		f.seek(0,0)
		f.write(str(commands)+"\n"+text)

	file.close

def paintSquare(row,col,size):
	global commands
	with open(filename+"-output.txt",'a') as f:
		f.write("PAINT_SQUARE "+str(row)+" "+str(col)+" "+str(size)+"\n")
		commands+=1

def paintLine(fromRow,fromCol,toRow,toCol):
	global commands
	with open(filename+"-output.txt",'a') as f:
		f.write("PAINT_SQUARE "+str(fromrow)+" "+str(fromCol)+" "+str(toRow)+" "+str(toCol)+"\n")
		commands+=1

def eraseSquare(row,col):
	print("beep")

main()
cells = int(ROWS)*int(COLUMNS)
# print("Cells: %d, Solutions: %d, Score: %d") %(cells,rownum,cells/rownum)

