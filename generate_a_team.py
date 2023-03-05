import random #we need this library to draw a teams
from termcolor import colored
def createTeams(all):

    number_to_random=len(all)
    drawed_numbers=[]
    while len(drawed_numbers)<number_to_random:
        number=random.randint(0,number_to_random-1)
        if number not in drawed_numbers:    #we want to be sure that our list with generated numbers doesn't contain two same numbers
            drawed_numbers.append(number)

    support_var='' #we need support variable to replace names in list
    half_of_all=int(number_to_random/2)
    for i in range(half_of_all): #generate first team
        support_var=all[i]
        all[i]=all[drawed_numbers[i]]
        all[drawed_numbers[i]]=support_var
    # now list 'all' have shuffeld names

    team1=[]
    team2=[]
    k=half_of_all
    for j in range(half_of_all): 
        team1.append(all[j])
        team2.append(all[k])
        k+=1

    team1=' '.join(team1) #make a string of team lists
    team2=' '.join(team2) 
    return [team1,team2] # return a list which contains two teams (in strings)

statement=0
while(True): #the loop will repeat itself as long as the user wants it to draw more teams

    if statement>0: print('') #every next time when we have already generated a teams we want to make an endlina after it

    print('Give me the names to create teams (a number of names must be even , example: Jack Johny Jacob Julia): ') 
    all=input('') #\n will make endline after a text

    all=all.split() #make a list of names


    if len(all)<2: #number of names can't be 1
        print("Not enough people to create teams!") 

    elif len(all)%2!=0: #numeber of names have to be even
        print("Number of names must be even!")

    else:
        teams=createTeams(all)
        team1=teams[0]  # the function returns a list of two teams so we can use index to get them
        team2=teams[1]
        print('\nTeam',colored('red','red'),':',team1)
        print('Team',colored('blue','blue'),':',team2,'\n')

        print('Do you want to draw next team? Y/n')
        if_continue=input('')
        if if_continue=='n': 
            break    #break the loop if user wants to end program
    statement=1
