import os
import sys
import re

def switchem(line,replacement1,replacement2):
	if replacement1 in line:
		return line.replace(replacement1,replacement2)
	else:
		return line.replace(replacement2,replacement1)

if len(sys.argv) != 3:
	print "Usage: mutator.py [DIRECTORY] [EXTENTION]"
	sys.exit()

replacementpairs = (
	['>=','<='],
	['||','&&'],
	['==','!='],
)

directory = sys.argv[1]
extention = sys.argv[2]

count = 0
for root, dirs, files in os.walk(directory):
	for file in files:
		
		ext = file.split('.')[-1]
		filename = "%s/%s"%(root,file)
		
		if ext == extention:
			print "Mutating... %s"%(filename)
			filecontents = []
			
			try:
				for line in open(filename,'r'):
					line = line.rstrip()+"\n"
					for x in replacementpairs:
						line = switchem(line,x[0],x[1])
					filecontents.append(line)
				
				file = open(filename,'w+')
				file.writelines(filecontents)
				count += 1
			except IOError, ex:
				print "Error Opening/Writing %s - %s"%(filename,str(ex))

print "\n### Finished mutating %s files ###"%(count)
