import struct, binascii , codecs
findRMD = codecs.decode("F000F0F002".encode(), "hex_codec")
tmx_number = 0
rmdStart = 0
rmd_number = 0
firstLocation = 0
epl_data = open(input("What EPL do you want to extract from? "), "rb").read()
epl_entries = int(codecs.encode(epl_data[128:129], "hex_codec"))
tmx_count = epl_data.count(b"TMX0")
rmd_count = epl_data.count(findRMD)

if tmx_count > 0:
    while tmx_count > tmx_number:
        tmx_number = tmx_number + 1
        firstLocation = epl_data.find("TMX0", firstLocation + 1)
        read_size = firstLocation - 4
        read_size = epl_data[read_size : read_size + 4].encode("hex")
        read_size = int(read_size, 16)
        read_size = int(struct.pack('<I', read_size).encode("hex"), 16)
        tmx_data = firstLocation - 8
        tmx_data = epl_data[tmx_data:tmx_data + read_size]
        tmxWriter = open(str(tmx_number) + ".tmx", "wb")
        tmxWriter.write(tmx_data)
        tmxWriter.close()

if rmd_count > 0:
    while rmd_count > rmd_number:
        rmd_number = rmd_number + 1
        rmdStart = epl_data.find(findRMD, rmdStart + 1)
        rmdSize = rmdStart - 172
        rmdSize = codecs.encode(epl_data[rmdSize : rmdSize + 4], "hex_codec")
        rmdSize = int(rmdSize, 16)
        rmdSize = int(codecs.encode(struct.pack('<I', rmdSize), "hex_codec"), 16)
        rmdWriter = open(str(rmd_number) + ".RMD", "wb")
        rmdWriter.write(epl_data[rmdStart:rmdStart+rmdSize])
        rmdWriter.close()
        
input("Done extracting, press enter to close. ")
exit(0)
        

