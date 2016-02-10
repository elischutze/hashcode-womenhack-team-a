# First Attempt will be a lazy attempt to try I/O.
# Traverse the lines, paint individual squares.

rownum = 0;
ROWS = 0;
COLUMNS = 0;
filename = "logo"
with open(filename+"-output.txt",'w') as f:
	nothing=0

def main():
	global rownum, ROWS, COLUMNS

	## Open File
	file = open("logo.txt");

	## Read Line 1
	for line in file:
		if(rownum==0):
			dimline = line.split(' ')
			ROWS = dimline[0]
			COLUMNS = dimline[1]
			with open(filename+"-output.txt",'a') as f:
				f.write(str(ROWS)+" "+str(COLUMNS))
			rownum+=1
		else:
			##Read next ROW lines.
			for i in range(len(line)):
				if line[i] == "#":
					paintSquare(rownum,i+1,0)
					rownum+=1
	file.close

def paintSquare(row,col,size):
	with open(filename+"-output.txt",'a') as f:
		f.write("PAINT_SQUARE "+str(row)+" "+str(col)+" "+str(size)+"\n")

def paintLine(fromRow,fromCol,toRow,toCol):
	print("boop")

def eraseSquare(row,col):
	print("beep")

main()
cells = int(ROWS)*int(COLUMNS)
print("Cells: %d, Solutions: %d, Score: %d") %(cells,rownum,cells/rownum)

