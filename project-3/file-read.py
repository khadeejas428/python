try:
      f = open("myfile.txt")
      print(f.read())

finally:
       f.close()