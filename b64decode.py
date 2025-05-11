import sys,base64
usage = \
"""
Usage :
	python b64decode.py "theBase64EncodedString"
"""
if len(sys.argv) == 2:
	print(base64.b64decode(sys.argv[1]))
else:
	print(usage)