f = open('newfile.txt', 'a')
lines = ['Hello','World','Welkom','To','File I/O']
text = '\n' .join(lines)
f.writelines(text)
f.close()