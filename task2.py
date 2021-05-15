my_file = open("../exam/alfa.txt", "r")
file_contents = my_file.read()
b = file_contents.split()
b = ''.join(b)
b = b.replace('.', '').replace(',', '').replace('!', '').replace('\n', '').replace('?', '').replace('-', '').replace('‘', '').replace('’', '')
new_letter = b.lower()
start = -1
count = 0
while True:
    start = new_letter.find("s", start+1)
    if start == -1:
        break
    count += 1
print("Букв s: ", count)

while True:
    start = new_letter.find("t", start+1)
    if start == -1:
        break
    count += 1
print('Букв t: ', count)
