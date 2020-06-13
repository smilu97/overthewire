#!/bin/sh
cat data.txt | xxd -r > data.bin
tar -xf data.bin
tar -xf data5.bin
tar -xf data6.bin
mv data8.bin flag.gz
gzip -d flag.gz
rm *.bin
cat flag # 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
rm flag
