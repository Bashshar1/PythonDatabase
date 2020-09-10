import pygame
#Set screen size
pygame.init()
SIZE = (1000,700)
screen = pygame.display.set_mode(SIZE)
pygame.font.init() 
font = pygame.font.Font(None, 20)

#Set colour
RED=(255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
#Set main loop to running
running = True
#Initialize the lists 
firstName = []
lastName = []
birthday = []
age = [] 
sex = []
phone = [] 
instagram = []
people_over_16 = []
#Initialize counters for stats 
IDnumber = 0 
total = 0 
other = 0
code1 = 0
code2 = 0
code3 = 0
code4 = 0
sex1 = 0 
sex2 = 0
other2 = 0
#initialize the strings
title0 = "ID Number"
title1 = "First Name"
title2 = "Last Name"
title3 = "Birthday"
title4 = "Age"
title5 = "Sex"
title6 = "Phone Number"
title7 = "Instagram"
#Opening the file wtih data. 
numFile = open("info.dat", "r")            

while True:
    #Reading the file 
    text = numFile.readline()  
    text = text.rstrip("\n")
    #breaks the text when there is nothing more to read.  
    if (text == ""):
        break        
    datalist = text.split(" ")
    #Adds to each specific string.
    firstName.append(datalist[0])
    lastName.append(datalist[1])
    birthday.append(datalist[2])
    age.append(datalist[3])
    sex.append(datalist[4])
    phone.append(datalist[5])
    instagram.append(datalist[6])
def drawList(inputList, xPos):
    #This is an attempt for Level 4=, this function displays the lists indivisually. 
    yPos = 50
    for i in range(len(inputList)):
        text6 = ("%-10s" % (str(inputList[i])))
        text6 = font.render(text6,True, RED)    
        screen.blit(text6, (xPos, yPos))        
        yPos += 20

def printData():
    screen.fill(BLACK)
    #Prints out the titles
    print("%10s\t%-10s\t%-10s\t%-10s\t%-10s\t%-10s\t%-10s\t%-9s\t" % (title0,title1, title2, title3, title4, title5, title6, title7))
    #Loop for printing out information
    IDnumber = 0
    for x in range (len(firstName)):
        IDnumber += 1
        print(" %-10i\t%-10s\t%-10s\t%-10s\t%-10s\t%-10s\t%-9s\t%-20s\t" % (IDnumber, firstName[x], lastName[x], birthday[x], age[x], sex[x], phone[x], instagram[x]))  
    #Attempt for Level 4+ 
        drawList(firstName, 260)
        drawList(lastName, 350) 
        drawList(birthday, 450)
        drawList(age, 550)
        drawList(sex, 600)
        drawList(phone, 650)
        drawList(instagram,750)

def avgAge():
    #Generates average age of people in the database.
    global total
    u = 0
    for u in range(len(age)):
        total += int(age[u])
    avg = (total/u)
    print("The average age is " + str(avg))


def areaCode():
    #Determines the amount of people in different area codes. 
    global other
    global code1, code2, code3, code4
    for t in range(len(age)):
        phoneNumber =(phone[t])
        areaCode = int(phoneNumber[:3])
        if areaCode == 905:
            code1 += 1 
        elif areaCode == 647: 
            code2 += 1
        elif areaCode == 289:
            code3 += 1 
        elif areaCode == 416: 
            code4 += 1
        else:
            other += 1 
    print("You have %2i people with the area code 905, that's %3.2f%%." % (code1,percentPhone(code1)))
    print("You have %2i people with the area code 647, that's %3.2f%%." % (code2,percentPhone(code2)))
    print("You have %2i people with the area code 289, that's %3.2f%%." % (code3,percentPhone(code3)))    
    print("You have %2i people with the area code 416, that's %3.2f%%." % (code4,percentPhone(code4))) 
    print("You have %2i people with an other area code, that's %3.2f%%." % (other,percentPhone(other)))    


def percentPhone(users):
    #Finds the percentage to the stats above. 
    return float((users/len(firstName))*100)
def overAge():
    #This function determines the specific people above Age 16. 
    global people_over_16
    for c in range(len(age)):
        age2 = int(age[c])
        if age2 >= 16:
            people_over_16 += [firstName[c]]
    for v in range (len(people_over_16)):
        print("%-10s" % (people_over_16[v]))


def sexData():
    #This function determines the demographics and percentages of people in the database and thier genders. 
    global other2
    global sex,sex1,sex2
    for w in range(len(age)):
        sexVar = sex[w]
        if sexVar == "M":
            sex1 += 1
        elif sexVar == "F": 
            sex2 += 1
        else:
            other2 += 1 
    print("You have %2i who identify as male, that's %3.2f%%." % (sex1,percentSex(sex1)))
    print("You have %2i who identify as female, that's %3.2f%%." % (sex2,percentSex(sex2)))
    print("You have %2i who identify as another gender, that's %3.2f%%." % (other2,percentSex(other2)))    

def percentSex(users2):
    #Finds the percentage to the stats above.     
    return float((users2/len(firstName))*100)

def add():
    #This function appends the new inputed item into each list for a new record. 
    print("You will be adding a new record to the data base... We will need some information.")
    newFirstName = input("Please input First Name\n")
    firstName.append(newFirstName)
    newLastName = input("Please input Last Name\n")
    lastName.append(newLastName) 
    newBirthday = input("Please input Birthday\n")
    birthday.append(newBirthday)
    newAge = input("Please input Age\n")
    age.append(newAge)
    newSex = input("Please input Sex\n") 
    sex.append(newSex) 
    newPhone = input("Please input the Phone Number\n") 
    phone.append(newPhone)
    newInstagram = input("Please input their Instagram\n")
    instagram.append(newInstagram)
    printData()

def delete():
    #This function deletes the specific the specific record by deleting every index they hold in each list. 
    recordNumber = (int(input("What record would you like to delete? Select record using the ID Number on the left.\n"))-1)
    print("You have deleted", firstName[recordNumber] + "'s information...")
    del(firstName[recordNumber],lastName[recordNumber],birthday[recordNumber],age[recordNumber],phone[recordNumber],instagram[recordNumber])
    printData()

def modify(): 
    #This function modifies a specific record's field. 
    recordNumber = (int(input("What record would you like to edit? Select record using the ID Number on the left.\n"))-1)
    print("You will be changing", firstName[recordNumber] + "'s information...")
    selectfield = str.lower(input("What field would you like to modify?\n"))
    if selectfield == "first name":
        newValue = input("What would you like to change thier first name too?\n")
        firstName[recordNumber] = newValue
    elif selectfield == "last name":
        newValue = input("What would you like to change thier last name too?\n")
        lastName[recordNumber] = newValue
    elif selectfield == "bithday":
        newValue = input("What would you like to change thier birthday too? Please in put in DD/MM/YYYY\n")
        birthday[recordNumber] = newValue                        
    elif selectfield == "age":
        newValue = input("What would you like to change thier age too?\n")
        age[recordNumber] = newValue  
    elif selectfield == "sex":
        newValue = input("What would you like to change thier sex too?\n")
        sex[recordNumber] = newValue   
    elif selectfield == "phone N=nnumber":
        newValue = input("What would you like to change thier phone number too?\n")
        phone[recordNumber] = newValue        
    elif selectfield == "instagram":
        newValue = input("What would you like to change thier Instagram too?\n")
        instagram[recordNumber] = newValue           
    printData()
    
while running == True:
    #Draws the rectangles in the main menu. 
    pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50, 200, 100 ), 0)  
    pygame.draw.rect(screen, WHITE, pygame.Rect(50,200,200,100),0)
    pygame.draw.rect(screen, WHITE, pygame.Rect(50,350,200,100),0)
    pygame.draw.rect(screen, WHITE, pygame.Rect(50,500,200,100),0)
    pygame.draw.rect(screen, WHITE, pygame.Rect(400,500,500,100),0)    
    #Creates text on the boxes.
    text = "Modify"
    text2 = "Add"
    text3 = "Delete"
    text4 = "Report"
    text5 = "Print"
    text = font.render(text,True, RED)
    text2 = font.render(text2,True, RED)
    text3 = font.render(text3,True, RED) 
    text4 = font.render(text4,True, RED)
    text5 = font.render(text5,True, RED)    
    screen.blit(text, (50, 50)) 
    screen.blit(text2, (50, 200)) 
    screen.blit(text3, (50, 350))      
    screen.blit(text4, (50, 500))      
    screen.blit(text5, (400, 500))   
    
    for evnt in pygame.event.get():#gets the events
        x1, y1 = pygame.mouse.get_pos()#gets the position
        if evnt.type == pygame.QUIT: #to exit       
            running=False
            #Determines which button was clicked and executes the correct funciton. 
        if evnt.type ==pygame.MOUSEBUTTONDOWN:
            if (50<y1<150) and (50<x1<250):
                modify()
            if (200<y1<300) and (50<x1<250):
                add()
            if (350<y1<400) and (50<x1<250):
                delete()
            if (500<y1<600) and (50<x1<250):
                print("Here are the demographics of the genders that people in your Database recognize as:")
                sexData()
                print("Here are some facts about the age of the people in your Database:")
                avgAge()
                print("Here are the number of people above 16 years of age:")
                overAge()
                print("Here are some details about the area codes from the phone numbers:")
                areaCode()                
            if (500<y1<600) and (400<x1<900):
                printData()
            #options = str.lower(input("What would you like to do? Please type one of the following: PRINT, DELETE, MODIFY, REPORT OR ADD. Type EXIT\n"))
            #The user will eventually have to use the console, so here is the code for inputs... 
            #PLEASE COMMENT OUT THE CODE ABOVE (EVERYTHING WITH PYGAME) TO TEST THIS OUT
            #options = str.lower(input("What would you like to do? Please type one of the following: PRINT, DELETE, MODIFY, REPORT OR ADD. Type EXIT\n"))
            #if options == "exit":
                #print("You have exited the program.")
                #running=False
                #break                    
            #elif options == "print":
                #printData()
            #elif options == "delete":
                #delete()
            #elif options == "modify":
                #modify()
            #elif options == "add":
                #add()
            #elif options == "report":
                #print("Here are the demographics of the genders that people in your Database recognize as:")
                #sexData()
                #print("Here are some facts about the age of the people in your Database:")
                #avgAge()
                #print("Here are the number of people above 16 years of age:")
                #overAge()
                #print("Here are some details about the area codes from the phone numbers:")
                #areaCode()
            
                  
    
        pygame.display.flip()
        

#This last for loop rewrited to the function. 
numFile = open ("info.dat", "w")
for x in range(len(firstName)) :
    numFile.write(str(firstName[x])+" "+str(lastName[x])+" "+str(birthday[x])+" "+str(age[x])+" "+str(sex[x])+" "+str(phone[x])+" "+str(instagram[x])+"\n")
numFile.close()
