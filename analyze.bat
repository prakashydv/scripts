@echo off
cdb -z %1 -y srv*C:\nvsymbols*http://dispsym/sym;srv*C:\nvsymbols*http://msdl.microsoft.com/download/symbols;srv*C:\nvsymbols*\\some\location -logo %1.analyze.txt -lines -c "!analyze -v;lmDvmnvspcaps*;q"
rem cdb -z %1 -y srv*C:\nvsymbols*http://dispsym/sym -logo %1.analyze.txt -lines -c "!analyze -v;lmDvmnvspcaps*;q"
echo %1, >> log.txt
findstr /B FAILURE_BUCKET_ID %1.analyze.txt >> log.txt
echo , >> log.txt
findstr /B BUCKET_ID %1.analyze.txt >> log.txt
echo , >> log.txt
findstr /C:"File version" %1.analyze.txt >> log.txt
echo , >> log.txt
@echo on
