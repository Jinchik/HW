byte = float(input("Please enter the correct value of bytes, you want to convert : "))
bit = byte*8
kbyte=byte/1024
mbyte=kbyte/1024
gbyte=mbyte/1024
#print(f'It is an amount in {bit} bits,\n it is an amount in {kbyte} kbytes,\n it is an amount in {mbyte} mbytes,\n it is an amount in {gbyte} gbytes')
#print(f"It is an amount in {bit} bits,\n"f" it is an amount in {kbyte} kbytes, \n" f" it is an amount in {mbyte} mbytes, \n" f" it is an amount in {gbyte} gbytes")
print("Hey my friend \n" "Here are the", bit , " bits\n" "The", kbyte , " kbytes and many, many more")