from pwn import *
r = remote("twinpeaks.cs.ucdavis.edu",30001)
i = 0 
while i < 50:
	#You can receive a line at a time
	line = r.recvline()

	#You can receive lines until a word is in the line
	line = r.recvline_contains(b"Question")

	line = line.split()
	print("Extracted two integers:",line[3],line[5])

	#Addition!
	result=int(line[3])+int(line[5])
	print("Result:",result)

	#Send it over! (the encoding thing is to convert a string into bytes
	r.sendline(str(result).encode())
	i+=1

#Did we succeed? Let's go in interactive mode and find out!
r.interactive()
