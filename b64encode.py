import sys,base64
usage = \
"""
Usage :
	python b64encode.py inputfile
"""
if len(sys.argv) == 2:
	s = open(sys.argv[1],"r").read()
	b = base64.b64encode(s.encode('utf-8'))
	f = open(f"{sys.argv[1]}.base64encoded.txt","wb")
	f.write(b)
	print(b)
	f.close()
else:
	print(usage)