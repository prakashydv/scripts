import sys

infile  = ""
outfile = ""
quality = 0

argc = len(sys.argv)
if argc not in [3,4]:
	print "usage : >> imgq inputfile [outputfile] quality"
	exit()
else:
	infile = sys.argv[1]
	if argc == 4:
		outfile = sys.argv[2]
	else:
		outfile = '.'.join(infile.split('.')[:-1]) + "_." + infile.split('.')[-1]
	try:
		quality = int(sys.argv[-1])
	except:
		print "warning: quality must be a number in [0:100]"
		print "         using default 90"
		quality = 90

from PIL import Image

try:
	image = Image.open(infile)
except:
	print "error! could not open file '%s'"%(infile)
	exit()

try:
	image.save(outfile, quality=quality)
except:
	print "error! could not save file '%s'"%(outfile)
	exit()

print "DONE: saved '%s' @ quality %d %%"%(outfile,quality)
