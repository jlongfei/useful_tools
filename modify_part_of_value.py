zxjt_file = open("zxjt.txt", "r")
new_zxjt_file = open("new_zxjt.txt", "w")
for i in zxjt_file:
    a = str(int(i[-5:-3])+1)
    newline = i[0:18] + a + i[-3:]
    new_zxjt_file.write(newline)
zxjt_file.close()
new_zxjt_file.close()
