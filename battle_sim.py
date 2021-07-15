
# import modules
import random
import time 


# set variables

# player health 
player_health=48

# mana
mana=40

# distance
distance=1

# amount of drinks
drink=1

# inventory
total_experience=0
total_gold=80
total_health_potions=random.randint(0,3)
total_mana_potions=random.randint(0,3)
total_arrows=random.randint(12,16)


# define functions

# slow print function
def sprint(str):
    print(str)
    time.sleep(1)

# fire damage function
def fire_damage():
    global enemy_health
    
    player_attack=(random.randint(2,4))
    enemy_health=enemy_health-player_attack
    sprint(f'The creature is on fire. It takes {player_attack} damage.')
    if enemy_health<0:
        enemy_health=0


# game start
sprint('You step into the tavern.')

# fight repeat
while 1>0:

    # tavern selection menu
    tavern_action=input("""-----------------
1 take a bounty
2 grab a drink
3 buy items
0 end game
-----------------""")

    
    # 1 take a bounty
    if tavern_action==('1'):

        # define creature a 
        creaturea_health=random.randint(26,68)
        if creaturea_health<54:
            creaturea_size='small'
        else:
            creaturea_size='large'
        creaturea_experience=(creaturea_health*40)
        creaturea_gold=creaturea_health

        # define creature b
        creatureb_health=random.randint(26,68)
        if creatureb_health<54:
            creatureb_size='small'
        else:
            creatureb_size='large'
        creatureb_experience=(creatureb_health*40)
        creatureb_gold=creatureb_health
    
        # define creature c 
        creaturec_health=random.randint(26,68)
        if creaturec_health<54:
            creaturec_size='small'
        else:
            creaturec_size='large'
        creaturec_experience=(creaturec_health*40)
        creaturec_gold=creaturec_health
    
        # bounty board selection menu
        sprint(f""" ______________    ______________    ______________
|  Creature A  |  |  Creature B  |  |  Creature C  |
|  size: {creaturea_size} |  |  size: {creatureb_size} |  |  size: {creaturec_size} |
|  exp: {creaturea_experience}   |  |  exp: {creatureb_experience}   |  |  exp: {creaturec_experience}   |
|    Reward    |  |    Reward    |  |    Reward    |
|   {creaturea_gold}  gold   |  |   {creatureb_gold}  gold   |  |   {creaturec_gold}  gold   |
 ______________    ______________    ______________ """)
        enemy_selection=input('Choose a bounty.')

        # leave bounty board
        if enemy_selection=='0':
            continue

        # set creature a
        if enemy_selection=='a':
            enemy_health=creaturea_health
            enemy_size=creaturea_size
            experience=creaturea_experience
            gold=creaturea_gold

        # set creature b
        if enemy_selection=='b':
            enemy_health=creatureb_health
            enemy_size=creatureb_size
            experience=creatureb_experience
            gold=creatureb_gold

        # set creature c
        if enemy_selection=='c':
            enemy_health=creaturec_health
            enemy_size=creaturec_size
            experience=creaturec_experience
            gold=creaturec_gold
            

        # enemy attack function
        def enemy_action():
            global player_health, distance

            if distance==1:
                attack_chance=(random.randint(1,20))
            else:
                attack_chance=(random.randint(1,10))
            if attack_chance>4:
                enemy_attack=(random.randint(4,8))
                player_health=(player_health-enemy_attack)
                if player_health<0:
                    player_health=0
                sprint(f'The creature attacked dealing {enemy_attack} damage. You are at {player_health} hp.')
                if player_health==0:
                    sprint('You died.')
            else:
                sprint('The creature missed the attack.')

        # reward function
        def reward():
            global mana, gold, total_health_potions, total_arrows, experience, total_gold, total_experience, distance, drink

            # reward variables 
            reward_arrows=random.randint(6,8)
            reward_potions=random.randint(0,2)
            item_list=['a tattered pelt', 'a broken arrow']
            item_reward=(random.choice(item_list))

            #reward alert and inventory update
            time.sleep(1)
            sprint(f'You got {gold} gold, {reward_arrows} arrows, {reward_potions} health potions, and {experience} experience.')
            distance=1
            mana=mana+20
            total_health_potions=(total_health_potions+reward_potions)
            total_arrows=(total_arrows+reward_arrows)
            total_gold=total_gold+gold
            total_experience=total_experience+experience
            drink=1
            sprint('You return to the tavern.')


        # opening alert 
        sprint(f'You step out onto the dirt trail outside the tavern and journey off deep into the forest ahead.')
        sprint(f'A short walk later, a {enemy_size} creature has approached you. It appears hostile.')
        sprint("""------------------------
1 attack with sword
2 attack with crossbow
3 cast a spell
4 check inventory
5 move
------------------------""")

        # round repeat
        while 1>0:

            # action selection menu
            player_action=input('What do you do next?')

    
            # controls info pannel (0)
            if player_action=="0":
                sprint("""------------------------
1 attack with sword
2 attack with crossbow
3 cast a spell
4 check inventory
5 move
------------------------""")
                continue
    
    
            # attack with sword (1)
    
            # player attack
            if player_action=="1":
                if distance==1:
                    if random.randint(1,20)>4:
                        player_attack=(random.randint(4,8))
                        enemy_health=(enemy_health-player_attack)
                        if enemy_health<0:
                            enemy_health=0
                        sprint(f'You swung you sword at the creature dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                        if enemy_health==0:
                            sprint('The creature died.')
                            reward()
                            break
                    else:
                        sprint('You missed the attack.')
                else:
                    sprint('You are to far from the creature.')
                    continue

                # enemy attack
                enemy_action()
                if player_health==0:
                    exit()
                continue


            # attack with crossbow (2)

            # player attack
            if player_action=="2":
                if total_arrows>0:
                    total_arrows=total_arrows-1
                    if distance==1:
                        attack_chance=(random.randint(1,8))
                    else:
                        attack_chance=(random.randint(1,20))
                    if attack_chance>4:
                        player_attack=(random.randint(4,12))
                        enemy_health=(enemy_health-player_attack)
                        if enemy_health<0:
                            enemy_health=0
                        sprint(f'You shot the creature with your crossbow doing {player_attack} damage. The creature is at {enemy_health} hp.')
                        if enemy_health==0:
                            sprint('The creature died.')
                            reward()
                            break
                    else:
                        sprint('You missed the attack.')

                    # enemy attack
                    enemy_action()
                    if player_health==0:
                        exit()
                    continue

                else:
                    sprint('You are out of arrows.')
                    continue

    
            # cast a spell (3)

            # spell selection menu
            if player_action=="3":
                    spell_cast=input(f"""------------------------
mp                  {mana}
------------------------
1 flame             10
2 lightening bolt   30
------------------------""")


                    # flame spell
    
                    # player attack
                    if spell_cast=='1':
                        if mana>=10:
                            mana=mana-10
                            if (random.randint(1,20))>4:
                                player_attack=(random.randint(8,12))
                                enemy_health=enemy_health-player_attack
                                if enemy_health<0:
                                    enemy_health=0
                                sprint(f'You cast flame dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                                if enemy_health==0:
                                    sprint('The creature died.')
                                    reward()
                                    break
                                fire_damage()
                                if enemy_health==0:
                                    sprint('The creature died.')
                                    reward()
                                    break
                            else:
                                sprint('You missed the spell.')

                            # enemy attack
                            enemy_action()
                            if player_health==0:
                                exit()
                            continue
                                
                        else:
                            sprint('You do not have enough mana')
                            continue

    
                    # lightening bolt spell

                    # player attack
                    if spell_cast=='2':
                        if mana>=30:
                            mana=mana-30
                            if (random.randint(1,20))>4:
                                player_attack=(random.randint(8,12))
                                enemy_health=enemy_health-player_attack
                                if enemy_health<0:
                                    enemy_health=0
                                sprint(f'You cast lightening bolt dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                                if enemy_health==0:
                                    sprint('The creature died.')
                                    rewrad()
                                    break
                                continue

                            # enemy attack
                            else:
                                sprint('You missed the spell.')
                                enemy_action()
                                if player_health==0:
                                    exit()
                                continue
                        else:
                            sprint('You do not have enough mana.')
                            continue


            # check inventory (4)
            if player_action=='4':
                print(f"""------------------------------
1) potion of health       {total_health_potions}
2)   potion of mana       {total_mana_potions}
3)           arrows       {total_arrows}
4)             gold       {total_gold}
   {mana} mana   {total_experience} experience
------------------------------
         (0) exit""")

                # inventory repeat
                while 1>0:
                    inventory_action=input('')
                    
                    # exit inventory
                    if inventory_action=='0':
                        break
                    
                    # use health potion 
                    if  inventory_action=='1':
                        if total_health_potions>0:
                            health_from_potion=(random.randint(4,8))
                            player_health=player_health+health_from_potion
                            total_health_potions=total_health_potions-1
                            sprint(f'You took a potion of health. You recovered {health_from_potion} hp. You are at {player_health} hp. You have {total_health_potions} potions left.')
                            continue
                        else:
                            sprint('You are out of health potions.')
                            continue
                        
                    # use mana potion  
                    if inventory_action=='2':
                        if total_mana_potions>0:
                            mana=mana+20
                            total_mana_potions=total_mana_potions-1
                            sprint(f'You took a potion of mana. You recovered 20 mp. You are at {mana} mp. You have {total_mana_potions} potions left.')
                            continue
                        else:
                            sprint('You are out of potions of mana.')
                            continue
                    
                    # use nonusable item
                    if inventory_action=='3' or '4':
                        sprint('This item is not usable')
                        continue

    
            # move (5)
            if player_action=='5':
                move_action=input("""------------------------
1 step forward
2 step back
3 run away
------------------------""")


                # step forward
                if move_action=='1':
                    if distance==1:
                        sprint('You cant step any closer to the creature.')
                        continue
                    else:
                        distance=distance-1
                        sprint('You stepped toward the creature.')
                        continue


                # step backward
                if move_action=='2':
                    if distance==1:
                        distance=distance+1
                        sprint('You stepped from the creature.')
                        continue
                    else:
                        move_action=input('You are already stepped away from the creature. Do you want to run away? (y or n)')
                        if move_action=='y':
                            sprint('You ran away.')
                            break
                        else:
                            time.sleep(1)
                            continue


                # run away 
                if move_action=='3':
                    sprint('You ran away.')
                    break

    
        #game repeat
        total_fights=total_fights+1
        continue


    # 2 get a drink interaction
    if tavern_action=='2':
        if drink<=2:
            sprint('\"Hunter, I see the monsters haven\'t gotten you yet. Can\'t say the same for all your peers.\"')
            player_action=input('\"I take it you want a drink?\" (y or n)')
            if player_action=='n':
                sprint('\"To early for some I guess\"')
                sprint('\"Well I\'ll see you later. And be safe\"')
                continue
            if player_action=='y':
                sprint('\"Ah, one to have some fun in battle I see. I knew I liked you\"')
                health_from_potion=random.randint(8,15)
                player_health=player_health+health_from_potion
                mana=mana+10
                drink=drink+1
                sprint(f'you gained {health_from_potion} hp')
                sprint('\"Have fun, and remeber, be safe\"')
                continue
        else:
            sprint('\"Careful, you gotta slow down before I gotta take that sword from you.\"')
            sprint('you can not have any more drinks right now')
            continue

    # 3 shop 
    if tavern_action=='3':
        sprint('Smiley offers a few small items for sale')
        print(f"""------------------------------
you have             {total_gold} gold
------------------------------
1 potion of health   50 gold
2 potion of mana     30 gold
3 arrows (4 count)   10 gold
     4 check inventory
------------------------------
     0 finish shopping""")
        while 1>0:
            purchase=input('')

            # buy health potion 
            if purchase==('1'):
                if total_gold>=50:
                    total_gold=total_gold-50
                    total_health_potions=total_health_potions+1
                    sprint('You purchased a health potion.')
                    continue
                else:
                    sprint('You do not have enough gold.')
                    continue

            # buy mana potion
            if purchase==('2'):
                if total_gold>=30:
                    total_gold=total_gold-30
                    total_mana_potions=total_mana_potions+1
                    sprint('You purchased a potion of mana.')
                    continue
                else:
                    sprint('You do not have enough gold.')
                    continue

            # buy arrows
            if purchase==('3'):
                if total_gold>=10:
                    total_gold=total_gold-10
                    total_arrows=total_arrows+4
                    sprint('You purchased a bundle of arrows.')
                    continue
                else:
                    sprint('You do not have enough gold.')
                    continue

            # check inventory
            if purchase==('4'):
                print(f"""------------------------------
1) potion of health       {total_health_potions}
2)   potion of mana       {total_mana_potions}
3)           arrows       {total_arrows}
------------------------------""")

            # exit shop
            if purchase==('0'):
                sprint('Smiley puts the items back under the bar.')
                break


    # 4 exit game
    if tavern_action==('0'):
        sprint('You step out of the tavern and take a deep breathe of fresh air after a long days work.')
        exit()
