# Create your own adventure with python here
# Inspo from https://trinket.io/python/6d4371f542 and https://replit.com/@AdamRicks/Epic-Journey#main.py


wins = 0
losses = 0


def intro():
    print('')
    print('Welcome to the dungeon, ' + name + '. Good luck and have fun!')
    pickDoor()


def pickDoor():
    print('')
    answerDoor = input(
        'You enter the dungeon and see three doors. Which one will you enter? Door 1 seems dark. Door 2 smells damp. Door 3 smells fresh. ')
    if (answerDoor == '1' or answerDoor == 'door 1'):
        print('You open the Dark Door...')
        door1()
    elif (answerDoor == '2' or answerDoor == 'door 2'):
        print('You open the Damp Door...')
        door2()
    elif (answerDoor == '3' or answerDoor == 'door 3'):
        print('You open the Fresh Door...')
        door3()
    else:
        print('Unusual answer, try again.')
        pickDoor()


def door1():
    global losses
    print('')
    answerDoor1 = input(
        'You enter the dark room. You are attacked in the dark and hurt. Do you drink your healing potion? (y/n) ').lower()
    if (answerDoor1 == 'yes' or answerDoor1 == 'y'):
        print('You heal yourself, but...')
        orcAttack()
    elif (answerDoor1 == 'no' or answerDoor1 == 'n'):
        print('Your wound is fatal and you die.')
        losses += 1
        lose()
    else:
        print('Unusual answer, try again.')
        door1()


def orcAttack():
    print('You see a hostile orc in the room.')
    answerOrcAttack = input('Do you attack? (y/n) ').lower()
    if (answerOrcAttack == 'y' or answerOrcAttack == 'yes'):
        print('You defeat the orc. There is a prince held prisoner in the room.')
        freePrince()
    elif (answerOrcAttack == 'n' or answerOrcAttack == 'no'):
        print('The orc is confused by your unwillingness to attack.')
        reasonOrc()
    else:
        print('Unusual answer, try again.')
        orcAttack()


def freePrince():
    global wins
    answerPrince = input('Do you free the prince? (y/n) ').lower()
    if (answerPrince == 'y' or answerPrince == 'yes'):
        print('The prince is freed and rewards you. But he returns to becoming a tyrant to the kingdom. Good for you.')
        wins += 1
        win()
    elif (answerPrince == 'n' or answerPrince == 'no'):
        print('You leave the prince to die and leave. The kingdom descends into anarchy. Good for you.')
        wins += 1
        win()
    else:
        print('Unusual answer, try again.')
        freePrince()


def reasonOrc():
    global losses
    global wins
    answerReason = input('Do you seek to reason with her? (y/n) ').lower()
    if (answerReason == 'y' or answerReason == 'yes'):
        print('You both parley and begin to understand each other. You connect your thoughts, feelings, and aspirations. You become friends.')
        wins += 1
        win()
    elif (answerReason == 'n' or answerReason == 'no'):
        print('You decide to keep fighting and you both end up dying.')
        losses += 1
        lose()
    else:
        print('Unusual answer, try again.')
        reasonOrc()


def door2():
    global losses
    global wins
    print('')
    answerPool = input('You enter the damp room and see a pool of water. Do you (a) drink the water, (b) flip the switch by the pool, or (c) talk to the magic koi fish swimming in the pool? (a/b/c) ').lower()
    if (answerPool == 'a' or answerPool == 'drink'):
        print('The water was poisoned, you die')
        losses += 1
        lose()
    elif (answerPool == 'b' or answerPool == 'flip'):
        print('The pool drains to reveal treature and loot, and a dead magic koi fish, odd. You are now rich and win life')
        wins += 1
        win()
    elif (answerPool == 'c' or answerPool == 'talk'):
        print('The magic koi fish convinces you to not flip the switch, and gives you the treasure and loot hidden in the pool. You are now rich, benevolent, and win life.')
        wins += 1
        win()
    else:
        print('Unusual answer, try again.')
        door2()


def door3():
    global losses
    koiname = input('You enter the fresh door and unknowingly pass through a magic portal. You are transformed into a magical talking koi fish and now live in a pool of water. What is your koi name? ')
    print('Welcome to your new forever life, ' + koiname)
    losses += 1
    lose()


def win():
    print('You win')
    replay()


def lose():
    print('You lose, sorry bud')
    replay()


def replay():
    print('Wins: {}'.format(wins))
    print('Losses: {}'.format(losses))
    replay = input('Play again? (y/n) ').lower()
    if (replay == 'y' or replay == 'yes'):
        intro()
    elif (replay == 'n' or 'no'):
        print('Try again later!')
        quit()
    else:
        print('Unusual answer, try again.')
        replay()


name = input('Choose your own dungeon adventure! What is your name? ')
intro()
