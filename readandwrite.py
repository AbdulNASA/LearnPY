fw = open('sample.txt', 'w')   # w for writing
fw.write('writing some stuff\n')
fw.write('I like NASA\n')
fw.close()

fr = open('sample.txt', 'r')   # r for reading
text = fr.read()
print(text)
fr.close()