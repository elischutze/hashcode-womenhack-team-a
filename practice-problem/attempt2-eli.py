# First Attempt will be a lazy attempt to try I/O.
# Traverse the lines, paint individual squares.

rownum = 0;
ROWS = 0;
COLUMNS = 0;
filename = "right_angle"
commands = 0;
with open(filename+"-output2.txt",'w') as f:
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
			lineflag=False;
			start = "0,0"
			for i in range(len(line)):
				if line[i] == "#":
					# print("it's a #! Let's check ahead...")
					if not i == len(line)-1:
						if not line[i+1] == "#":
							# print("Ahead is a . ")
							if not lineflag:
								# print("not in a line so let's paint!")
								paintSquare(rownum-1,i,0)
							else:
								# print("End of our Line! Paint it!")					
								paintLine(start.split(',')[0],start.split(',')[1],rownum-1,i)
								lineflag = False
								start = "0,0"
						else:
							# print("Ahead is a #")
							if not lineflag:
								# print("Ooh we're starting a line, let's save..")
								start = str(rownum-1)+","+str(i)
								lineflag = True
					else:
						if lineflag:
							paintLine(start.split()[0],start.split()[1],rownum-1,i)
							lineflag = False
							start = "0,0"
						else:
							paintSquare(rownum-1,i,0)	
				else:
					nothing=0# print("I'm a . BYE")
						
			rownum+=1
	
	with open(filename+"-output2.txt",'r+') as f:
		text = f.read()
		f.seek(0,0)
		f.write(str(commands)+"\n"+text)

	file.close

def paintSquare(row,col,size):
	global commands
	with open(filename+"-output2.txt",'a') as f:
		f.write("PAINT_SQUARE "+str(row)+" "+str(col)+" "+str(size)+"\n")
		commands+=1

def paintLine(fromRow,fromCol,toRow,toCol):
	global commands
	with open(filename+"-output2.txt",'a') as f:
		f.write("PAINT_LINE "+str(fromRow)+" "+str(fromCol)+" "+str(toRow)+" "+str(toCol)+"\n")
		commands+=1

def eraseSquare(row,col):
	print("beep")

main()
cells = int(ROWS)*int(COLUMNS)
# print("Cells: %d, Solutions: %d, Score: %d") %(cells,rownum,cells/rownum)

