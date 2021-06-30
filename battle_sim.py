
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

# inventory
total_experience=0
total_gold=80
total_health_potions=random.randint(0,3)
total_mana_potions=random.randint(0,3)
total_arrows=random.randint(12,16)


# define functions

# fire damage function
def fire_damage():
    global enemy_health
    
    player_attack=(random.randint(2,4))
    enemy_health=enemy_health-player_attack
    print(f'The creature is on fire. It takes {player_attack} damage.')
    if enemy_health<0:
        enemy_health=0
    time.sleep(1)


# game start
print('you step into the tavern')
time.sleep(1)

# fight repeat
total_fights=1
while total_fights>0:

    # tavern selection menu
    tavern_action=input("""-----------------
1 take a bounty 
2 grab a drink
3 buy items
4 leave the tavern 
-----------------""")

    
    # 1 bounty board 
    if tavern_action==('1'):

        # creature a 
        creaturea_health=random.randint(26,42)
        if creaturea_health<34:
            creaturea_size='small'
        else:
            creaturea_size='large'
        creaturea_experience=(creaturea_health*40)
        creaturea_gold=creaturea_health*2
    
        # creature b
        creatureb_health=random.randint(26,42)
        if creatureb_health<34:
            creatureb_size='small'
        else:
            creatureb_size='large'
        creatureb_experience=(creatureb_health*40)
        creatureb_gold=creatureb_health*2
    
        # creature c 
        creaturec_health=random.randint(26,42)
        if creaturec_health<34:
            creaturec_size='small'
        else:
            creaturec_size='large'
        creaturec_experience=(creaturec_health*40)
        creaturec_gold=creaturec_health*2
    
        # bounty board selection menu
        print(f""" ______________    ______________    ______________
|  Creature A  |  |  Creature B  |  |  Creature C  |
|  size: {creaturea_size} |  |  size: {creatureb_size} |  |  size: {creaturec_size} |
|  exp: {creaturea_experience}   |  |  exp: {creatureb_experience}   |  |  exp: {creaturec_experience}   |
|    Reward    |  |    Reward    |  |    Reward    |
|   {creaturea_gold}  gold   |  |   {creatureb_gold}  gold   |  |   {creaturec_gold}  gold   |
 ______________    ______________    ______________ """)
        time.sleep(1)
        enemy_selection=input('Choose a bounty.')

        if enemy_selection==('a') or ('A'):
            enemy_health=creaturea_health
            enemy_size=creaturea_size
            experience=creaturea_experience
            gold=creaturea_gold

        if enemy_selection==('b') or ('B'):
            enemy_health=creatureb_health
            enemy_size=creatureb_size
            experience=creatureb_experience
            gold=creatureb_gold

        if enemy_selection==('c') or ('C'):
            enemy_health=creaturec_health
            enemy_size=creaturec_size
            experience=creaturec_experience
            gold=creaturec_gold


        # enemy attack function
        def enemy_action():
            global player_health
            global distance

            if distance==1:
                attack_chance=(random.randint(1,20))
            else:
                attack_chance=(random.randint(1,10))
            if attack_chance>4:
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

        # reward function
        def reward():
            global mana, gold, total_health_potions, total_arrows, experience, total_gold, total_experience

            # reward variables 
            reward_arrows=random.randint(6,8)
            reward_potions=random.randint(0,2)
            item_list=['a tattered pelt', 'a broken arrow']
            item_reward=(random.choice(item_list))

            #reward alert and inventory update
            print(f'{gold} gold, {reward_arrows} arrows, {reward_potions} health potions, {item_reward}, and {experience} experience')
            mana=mana+2
            total_health_potions=(total_health_potions+reward_potions)
            total_arrows=(total_arrows+reward_arrows)
            total_gold=total_gold+gold
            total_experience=total_experience+experience
            time.sleep(1)
            print('you return to the tavern')

        # opening alert 
        print(f'a {enemy_size} creature has approached you. It appears hostile.')
        time.sleep(1)
        print("""------------------------
1 attack with sword
2 attack with crossbow
3 cast a spell
4 check inventory
5 move
------------------------""")
        time.sleep(1)


        # round repeat
        while 1>0:

            # action selection menu
            player_action=input('What do you do next?')

    
            # controls info pannel (0)
            if player_action=="0":
                print("""------------------------
1 attack with sword
2 attack with crossbow
3 cast a spell
4 check inventory
5 move
------------------------""")
                time.sleep(1)
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
                        print(f'you swung you sword at the creature dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                        time.sleep(1)
                        if enemy_health==0:
                            print('The creature died.')
                            time.sleep(1)
                            reward()
                            time.sleep(1)
                            break
                    else:
                        print('You missed the attack.')
                        time.sleep(1)
                else:
                    print('You are to far from the creature.')
                    time.sleep(1)
                    continue

                # enemy attack
                enemy_action()
                if player_health==0:
                    time.sleep(1)
                    exit()
                continue


            # attack with crossbow (2)

            # player attack
            if player_action=="2":
                if total_arrows>0:
                    total_arrows=total_arrows-1
                    if distance==1:
                        attack_chance=(random.randint(1,20))
                    else:
                        attack_chance=(random.randint(1,8))
                    if attack_chance>4:
                        player_attack=(random.randint(4,8))
                        enemy_health=(enemy_health-player_attack)
                        if enemy_health<0:
                            enemy_health=0
                        print(f'You shot the creature with your crossbow doing {player_attack} damage. The creature is at {enemy_health} hp.')
                        time.sleep(1)
                        if enemy_health==0:
                            print('The creature died.')
                            time.sleep(1)
                            reward()
                            time.sleep(1)
                            break
                    else:
                        print('You missed the attack.')
                        time.sleep(1)

                    # enemy attack
                    enemy_action()
                    if player_health==0:
                        time.sleep(1)
                        exit()
                    continue

                else:
                    print('you are out of arrows')

    
            # cast a spell (3)

            # spell selection menu
            if player_action=="3":
                if mana>0:
                    spell_cast=input(f"""------------------------
mp                  {mana}
------------------------
1 flame             10
2 lightening bolt   30
------------------------""")


                    # flame spell
    
                    # player attack
                    if spell_cast=='1':
                        mana=mana-10
                        if (random.randint(1,20))>4:
                            player_attack=(random.randint(8,12))
                            enemy_health=enemy_health-player_attack
                            if enemy_health<0:
                                enemy_health=0
                            print(f'You cast flame dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                            if enemy_health==0:
                                print('The creature died.')
                                time.sleep(1)
                                reward()
                                time.sleep(1)
                                break
                            fire_damage()
                            if enemy_health==0:
                                print('The creature died.')
                                time.sleep(1)
                                reward()
                                time.sleep(1)
                                break
                        else:
                            print('You missed the spell.')
                            time.sleep(1)

                        # enemy attack
                        enemy_action()
                        if player_health==0:
                            time.sleep(1)
                            exit()
                        continue

    
                    # lightening bolt spell

                    # player attack
                    if spell_cast=='2':
                        mana=mana-30
                        if (random.randint(1,20))>4:
                            player_attack=(random.randint(8,12))
                            enemy_health=enemy_health-player_attack
                            if enemy_health<0:
                                enemy_health=0
                            print(f'You cast lightening bolt dealing {player_attack} damage. The creature is at {enemy_health} hp.')
                            if enemy_health==0:
                                print('The creature died.')
                                time.sleep(1)
                                rewrad()
                                time.sleep(1)
                                break
                            time.sleep(1)
                            print('The creature is temporarly paralyzed. It does not attack.')
                            continue
                    
                    # enemy attack
                        else:
                            print('You missed the spell.')
                            time.sleep(1)
                            enemy_action()
                            if player_health==0:
                                time.sleep(1)
                                exit()
                            continue
                else:
                    print('You are out of mana.')
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
                            health_from_potion=(random.randint(1,6))
                            player_health=player_health+health_from_potion
                            total_health_potions=total_health_potions-1
                            print(f'You took a potion of health. You recovered {health_from_potion} hp. You are at {player_health} hp. You have {total_health_potions} potions left.')
                            continue
                        else:
                            print('You are out of health potions.')
                            continue
                        
                    # use mana potion  
                    if inventory_action=='2':
                        if total_mana_potions>0:
                            mana=mana+20
                            total_mana_potions=total_mana_potions-1
                            print(f'You took a potion of mana. You recovered 20 mp. You are at {mana} hp. You have {total_mana_potions} potions left.')
                            continue
                        else:
                            print('You are out of health potions.')
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
                        print('You cant step any closer to the creature.')
                        time.sleep(1)
                        continue
                    else:
                        distance=distance-1
                        print('you stepped toward the creature.')
                        time.sleep(1)
                        continue


                # step backward
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


                # run away 
                if move_action=='3':
                    print('You ran away.')
                    time.sleep(1)
                    break

    
        #game repeat
        total_fights=total_fights+1
        continue


    # 2 smiley interaction
    if tavern_action=='2':
        print('\"Hunter, I see the monsters haven\'t gotten you yet. Can\'t say the same for all your peers.\"')
        time.sleep(1)
        player_action=input('\"I take it you want a drink?\" (y or n)')
        if player_action=='n':
            print('\"To early for some I guess\"')
            time.sleep(1)
            print('\"Well I\'ll see you later. And be safe\"')
            time.sleep(1)
            continue
        if player_action=='y':
            print('\"Ah, one to have some fun in battle I see. I knew I liked you\"')
            health_from_potion=random.randint(8,15)
            player_health=player_health+health_from_potion
            time.sleep(1)
            print(f'you gained {health_from_potion} hp')
            time.sleep(1)
            print('\"Have fun, and remeber, be safe\"')
            time.sleep(1)
            continue

    # 3 shop 
    if tavern_action=='3':
        print('Smiley offers a few small items for sale')
        time.sleep(1)
        print(f"""------------------------------
you have             {total_gold} gold
------------------------------
1 potion of health   50 gold
2 potion of mana     30 gold
3 arrows (4 count)   10 gold
     4 check inventory
------------------------------
     5 finish shopping""")
        while 1>0:
            purchase=input('')

            # buy health potion 
            if purchase==('1'):
                if total_gold>=50:
                    total_gold=total_gold-50
                    total_health_potions=total_health_potions+1
                    print('you purchased a health potion')
                    time.sleep(1)
                    continue
                else:
                    print('you do not have enough gold')
                    time.sleep(1)
                    continue

            # buy mana potion
            if purchase==('2'):
                if total_gold>=30:
                    total_gold=total_gold-30
                    total_mana_potions=total_mana_potions+1
                    print('you purchased a potion of mana')
                    time.sleep(1)
                    continue
                else:
                    print('you do not have enough gold')
                    time.sleep(1)
                    continue

            # buy arrows
            if purchase==('3'):
                if total_gold>=10:
                    total_gold=total_gold-10
                    total_arrows=total_arrows+4
                    print('you purchased a bundle of arrows')
                    time.sleep(1)
                    continue
                else:
                    print('you do not have enough gold')
                    time.sleep(1)
                    continue

            # check inventory
            if purchase==('4'):
                print(f"""------------------------------
1) potion of health       {total_health_potions}
2)   potion of mana       {total_mana_potions}
3)           arrows       {total_arrows}
4)             gold       {total_gold}

   {mana} mana   {total_experience} experience
------------------------------""")

            # exit shop
            if purchase==('5'):
                print('Smiley puts the items back under the bar')
                time.sleep(1)
                break

    # 4 leave the tavern
    if tavern_action==('4'):
        print('you step out of the tavern and take a deep breathe of fresh air after a long days work')
        time.sleep(1)
        exit()
