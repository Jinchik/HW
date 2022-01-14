print ("The itsy bitsy spider\nclimbed up the waterspout.")
print ("\\")
print ("Down came the rain\nand washed the spider out.")
print ("The itsy bitsy spider","climbed up","the waterspout.")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Programming","Essentials","in",sep="***",end="...")
print("Python")
print("    *","\n   * *","\n  *   *","\n *     *","\n***   ***","\n  *   *","\n  *   *","\n  *****")
print("    *","\n   * *","\n  *   *","\n *     *","\n***   ***","\n  *   *","\n  *   *","\n  *   *","\n  *   *","\n  *****")
print("    *","\n   * *","\n  *   *","\n *     *","\n***   ***","\n  *   *","\n  *   *","\n  *   *","\n  *   *","\n  *****")
print("Hey,","Hey,",end="")
print("Hey!")
print(2 ** 2 ** 3)
print(9 % 6 % 2)
print("Hey, hey")
print("Alex")
print("My name is Alex.\t2021\nI live in Somewhere.\t2222")
# variables
# conditions
# loops

a='Hello'
print(a)
# str string  '5' 'Andrey' - строка
# int integer 5 120 - целые числа
# float float 5.0 12.4 -1.5 - тип данных с плавующей точкой
# bool bolean True False - 1,0
name="Odessa"
terrain='near the sea'
temperature='25'
color= "black"
pet='cat'
print("Hello, my name is",name)
print("I have a little",color,pet)
print("I have a little"+" "+str(color)+" "+str(pet))
print("I have a little {} {}" .format(color,pet)) #<python 3.6
print(f"I have a little {color} {pet}")
print(f"I live in {name}, It is the beautiful city {terrain}. We have summer with {temperature}C")
about_me = f"I live in {name}, It is the beautiful city {terrain}. We have summer with {temperature}C."
print(about_me)