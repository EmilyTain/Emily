print("""




 ____     _    ____  _     ________  _  
/  __\   / |  /  _ \/ \   /  __/\  \//  
| | //   | |  | / \|| |   |  \   \  /   
| |_\\/\_| |  | |-||| |_/\|  /_  /  \   
\____/\____/  \_/ \|\____/\____\/__/\\  
                                        





""")
print("Welcome to Bj Alex")

player_name = input('What is your name, adventurer\n')

health = 100
damage = 20

print('\Welcome '+ player_name +'!You have'+ str(health)+'health and can do damage'+str(damage))
print('You came across a dragon!! What will you do?')
print('1. Fight')
print('2. Run')

choice = int (input('Enter either 1 or 2:'))

if choice == 1:
    print("You attack the dragon and do "+str(damage)+ 'damage')
    print('the dragon back off, spit some acid does 10 damage')
    health -= 10
elif choice == 2:
    print('You run away from the dragon')
    print('live today for tomorrow')
    print("Dragon manage to throw rocks at you deals with twice the damage you inflict\n")
    health -= (10*2)
    print("Your current health\n"+str(health))
    #dragon manage to throw rocks at you deals with twice the damage you inflict
    #print your current health
else:
    print('\nInvalid choice, the dragon get to eat you alive')
    print("Thanks for playing")
   # print("Dragon run away......")
   # print("Dragon chase you!")


