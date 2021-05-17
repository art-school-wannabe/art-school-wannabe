
#import modules
import random
import time 


#set variables

#player health 
player_health=28

#enemy health
enemy_health=random.randint(26,42)
#player size for the intro text
if enemy_health>28:
    enemy_size='large'
else:
    enemy_size='small'

#number of health potions
number_of_potions=random.randint(0,3)

#mana
mana=random.randint(3,4)

#distance
distance=1

#reward function
experience=(enemy_health*40)
gold=random.randint(3,16)
item_list=['a tattered pelt', 'three arrows', 'a broken arrow']
item_reward=(random.choice(item_list))
reward=(f'{gold} gold, {item_reward}, and {experience} experience')


#define functions

#enemy attack
def enemy_action():
    global player_health
    global distance
    
    if distance==1:
        attack_chance=(random.randint(1,20))
    else:
        attack_chance=(random.randint(1,16))
    if attack_chance>8:
        enemy_attack=(random.randint(4,8))
        player_health=(player_health-enemy_attack)
        if player_health<0:
            player_health=0
        print(f'The creature attacked dealing {enemy_attack} damage. You are at {player_health} hp.')
        time.sleep(2)
        if player_health==0:
            print('You died.')
    else:
        print('The creature missed the attack.')
        time.sleep(1)
        
#fire damage
def fire_damage():
    global enemy_health
    
    player_attack=(random.randint(2,4))
    enemy_health=enemy_health-player_attack
    print(f'The creature is on fire. It takes {player_attack} damage.')
    if enemy_health<0:
        enemy_health=0
    time.sleep(1)


#alerts

#opening alert 
print(f'a {enemy_size} creature has approached you. It appears hostile.')
time.sleep(1)
print("""------------------------
1 attack with sword
2 attack with crossbow
3 cast a spell
4 use a health potion
5 move
------------------------""")
time.sleep(1)


#repeat
while 1>0:

    #selection menu
    player_action=input('What do you do next?')
    
    
    #controls info pannel
    if player_action=="0":
        print("""------------------------
1 attack with sword
2 attack with crossbow
3 cast a spell
4 use a health potion
5 move
------------------------""")
        time.sleep(1)
        continue
    
    
    #attack with sword
    
    #player attack
    if player_action=="1":
        if distance==1:
            if random.randint(1,20)>6:
                player_attack=(random.randint(4,8))
                enemy_health=(enemy_health-player_attack)
                if enemy_health<0:
                    enemy_health=0
                print(f'you swung you sword at the creature dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                time.sleep(1)
                if enemy_health==0:
                    print('The creature died.')
                    time.sleep(1)
                    print(reward)
                    time.sleep(1)
                    break
            else:
                print('You missed the attack.')
                time.sleep(1)
        else:
            print('You are to far from the creature.')
            time.sleep(1)
            continue

        #enemy attack
        enemy_action()
        if player_health==0:
            time.sleep(1)
            break
        continue


    #attack with crossbow
    
    #player attack
    if player_action=="2":
        if distance==1:
            attack_chance=(random.randint(1,20))
        else:
            attack_chance=(random.randint(1,16))
        if attack_chance>8:
            player_attack=(random.randint(4,8))
            enemy_health=(enemy_health-player_attack)
            if enemy_health<0:
                enemy_health=0
            print(f'You shot the creature with your crossbow doing {player_attack} damage. The creature is at {enemy_health} hp.')
            time.sleep(1)
            if enemy_health==0:
                print('The creature died.')
                time.sleep(1)
                print(reward)
                time.sleep(1)
                break
        else:
            print('You missed the attack.')
            time.sleep(1)

        #enemy attack
        enemy_action()
        if player_health==0:
            time.sleep(1)
            break
        continue

    
    #cast a spell
    
    #spell selection menu
    if player_action=="3":
        spell_cast=input("""------------------------
1 flame
2 lightening bolt
------------------------""")


        #flame
        
        #player attack
        if spell_cast=='1':
            if (random.randint(1,20))>8:
                player_attack=(random.randint(4,8))
                enemy_health=enemy_health-player_attack
                if enemy_health<0:
                    enemy_health=0
                print(f'You cast flame dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                if enemy_health==0:
                    print('The creature died.')
                    time.sleep(1)
                    print(reward)
                    time.sleep(1)
                    break
                fire_damage()
                if enemy_health==0:
                    print('The creature died.')
                    time.sleep(1)
                    print(reward)
                    time.sleep(1)
                    break
            else:
                print('You missed the spell.')
                time.sleep(1)
        
            #enemy attack
            enemy_action()
            if player_health==0:
                time.sleep(1)
                break
            continue
    
    
        #lightening bolt
        
        #player attack
        if spell_cast=='2':
            if (random.randint(1,20))>8:
                player_attack=(random.randint(4,8))
                enemy_health=enemy_health-player_attack
                if enemy_health<0:
                    enemy_health=0
                print(f'You cast lightening bolt dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                if enemy_health==0:
                    print('The creature died.')
                    time.sleep(1)
                    print(reward)
                    time.sleep(1)
                    break
                time.sleep(1)
                print('The creature is temporarly paralyzed. It does not attack.')
                continue
            
        #enemy attack
            else:
                print('You missed the spell.')
                time.sleep(1)
                enemy_action()
                if player_health==0:
                    time.sleep(1)
                    break
                continue

                
    #health potion
    if  player_action=="4":
        if number_of_potions>=0:
            health_from_potion=(random.randint(1,6))
            player_health=player_health+health_from_potion
            print(f'You took a health potion. You recovered {health_from_potion} hp. You are at {player_health} hp. You have {number_of_potions} potions left.')
            number_of_potions=number_of_potions-1
            continue
        else:
            print('You are out of health potions.')
            continue
    
    
    #move
    if player_action=='5':
        move_action=input("""------------------------
1 step forward
2 step back
3 run away
------------------------""")


        #step forward
        if move_action=='1':
            if distance==1:
                print('You cant step any closer to the creature.')
                time.sleep(1)
                continue
            else:
                distance=distance-1
                print('you stepped toward the creature.')
                time.sleep(1)
                continue

               
        #step backward
        if move_action=='2':
            if distance==1:
                distance=distance+1
                print('You stepped from the creature.')
                time.sleep(1)
                continue
            else:
                move_action=input('You are already stepped away from the creature. Do you want to run away? (Y/N)')
                if move_action=='Y':
                    print('You ran away.')
                    time.sleep(1)
                    break
                else:
                    time.sleep(1)
                    continue

        
        #run away 
        if move_action=='3':
            print('You ran away.')
            time.sleep(1)
            break
                    