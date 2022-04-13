import pygame
#import your controller


def main():
    pygame.init()

mylist = []
for i in range(4):
  var = int(input("Enter an integer: "))
  mylist.append(var)



print(mylist[3])
print(mylist[1])
print(mylist[2])
print(mylist[0])

mylist[0], mylist[-1] = mylist[-1], mylist[0]

print(mylist)

  
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
