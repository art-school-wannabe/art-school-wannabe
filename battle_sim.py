
# import modules
import random
import time 


# set variables

# player health 
player_health=48

# mana
mana=random.randint(2,3)

# distance
distance=1

# inventory
total_experience=0
total_gold=0
number_of_potions=random.randint(0,3)
number_of_arrows=random.randint(12,16)


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


# fight repeat
total_fights=1
while total_fights>0:

    # tavern opening alert
    print('you step into the tavern')
    time.sleep(1)
    # tavern selection menu
    tavern_action=input("""-----------------
1 take a bounty 
2 grab a drink
3 buy items
-----------------""")
    
    # bounty board 
    if tavern_action==('1'):

        # creature a 
        creaturea_health=random.randint(26,42)
        if creaturea_health>34:
            creaturea_size='small'
        else:
            creaturea_size='large'
        creaturea_experience=(creaturea_health*40)
        creaturea_gold=random.randint(20,40)
    
        # creature b
        creatureb_health=random.randint(26,42)
        if creatureb_health>34:
            creatureb_size='small'
        else:
            creatureb_size='large'
        creatureb_experience=(creatureb_health*40)
        creatureb_gold=random.randint(20,40)
    
        # creature c 
        creaturec_health=random.randint(26,42)
        if creaturec_health>34:
            creaturec_size='small'
        else:
            creaturec_size='large'
        creaturec_experience=(creaturec_health*40)
        creaturec_gold=random.randint(20,40)
    
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

        # reward variables 
        reward_arrows=random.randint(6,8)
        reward_potions=random.randint(0,2)
        item_list=['a tattered pelt', 'a broken arrow']
        item_reward=(random.choice(item_list))

        # reward function
        def reward():
            global mana, gold, number_of_potions, number_of_arrows, experience, total_gold, total_experience

            # reward variables 
            reward_arrows=random.randint(6,8)
            reward_potions=random.randint(0,2)
            item_list=['a tattered pelt', 'a broken arrow']
            item_reward=(random.choice(item_list))

            #reward alert and inventory update
            print(f'{gold} gold, {reward_arrows} arrows, {reward_potions} health potions, {item_reward}, and {experience} experience')
            mana=mana+2
            number_of_potions=(number_of_potions+reward_potions)
            number_of_arrows=(number_of_arrows+reward_arrows)
            total_gold=total_gold+gold
            total_experience=total_experience+experience

        # opening alert 
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
4 use a health potion
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
                if number_of_arrows>0:
                    number_of_arrows-1
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
                    mana=mana-1
                    spell_cast=input("""------------------------
1 flame
2 lightening bolt
------------------------""")


                    # flame spell
    
                    # player attack
                    if spell_cast=='1':
                        if (random.randint(1,20))>4:
                            player_attack=(random.randint(4,8))
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
                        if (random.randint(1,20))>4:
                            player_attack=(random.randint(4,8))
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

            # health potion (4)
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

    
        # repeat request selection
        repeat_option=input('would you like to return to the tavern? (y or n)')

        # end game
        if repeat_option==('n'):
            exit()

        # repeat fight
        if repeat_option==('y'):
            total_fights=total_fights+1
            continue
