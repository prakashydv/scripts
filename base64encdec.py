import sys
import base64

if(len(sys.argv) != 3):
	print "ERROR ! args unknown"
	print "args : <string> <'e'|'d'>"
else:
	if(sys.argv[-1] in ['e','encode','Encode','ENCODE'] ):
		print base64.b64encode(sys.argv[1])
	elif (sys.argv[-1] in ['d','decode','Decode','DECODE'] ):
		print base64.b64decode(sys.argv[1])


"""
TODO : powershell/bash script
powershell "[convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(\"$*\"))"
powershell "[Text.Encoding]::UTF8.GetString([convert]::FromBase64String(\"$*\"))"
"""