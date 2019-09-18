import sys
import base64

if(len(sys.argv) != 3):
	print("ERROR ! args unknown")
	print("args : <file> <'e'|'d'>")
else:
        fin = open(sys.argv[1],"rb")
        fout = open(sys.argv[1]+sys.argv[-1]+".out.txt","wb")
        for line in fin :
                if(sys.argv[-1] in ['e','encode','Encode','ENCODE','-e'] ):
                        s = base64.b64encode(line.rstrip())
                        print(s)
                        fout.write(s+b"\n")
                elif (sys.argv[-1] in ['d','decode','Decode','DECODE','-d'] ):
                        s = base64.b64decode(line.rstrip())
                        print(s)
                        fout.write(s+b"\n")
        fout.close()
        fin.close()

"""
TODO : powershell/bash script
powershell "[convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(\"$*\"))"
powershell "[Text.Encoding]::UTF8.GetString([convert]::FromBase64String(\"$*\"))"
"""
