import random

# Initialize variables
party_members = []
party_health = [10, 10, 10, 10]
miles_remaining = 360
days_until_showdown = 68
dollars = 0
horses = 0
rations = 0
emergency_supplies = 0
horse_price = 20
rations_price = 2
emergency_supplies_price = 5
party_dead = False
dead = 'tough luck'

# Introduction
print("Howdy partner! Welcome to 'Cowboy Trail'!")

# Choose occupation
answer = ""
while answer.lower() not in ['a', 'b', 'c']:
    answer = input("What would you like to be? A) Sheriff (a), B) Outlaw (b), or C) Rancher (c)\n")

if answer.lower() == 'a':
    dollars = 100
elif answer.lower() == 'b':
    dollars = 70
else:
    dollars = 55

# Choose party leader
party_leader = input("What is your leader's name?\n")
party_members.append(party_leader)

# Choose party members
count = 0
while count < 3:
    new_member = input("What are your other members' names?\n")
    party_members.append(new_member)
    count += 1

# Main game loop
while dollars >= 2 and not party_dead:
    # Shopping
    answer = ""
    while answer.lower() not in ['a', 'b', 'c']:
        answer = input("What would you like to buy? A) Horses, B) Rations, or C) Emergency Supplies\n")

    if answer.lower() == 'a':
        amount = input("How many horses would you like to buy?\n")
        if amount.isdigit():
            amount = int(amount)
            total = amount * horse_price
            if dollars >= total:
                horses += amount
                dollars -= total
            else:
                print("Not enough dollars")
        else:
            print("Invalid amount entered. Try again.")
    elif answer.lower() == 'b':
        amount = input("How many rations would you like to buy?\n")
        if amount.isdigit():
            amount = int(amount)
            total = amount * rations_price
            if dollars >= total:
                rations += amount
                dollars -= total
            else:
                print("Not enough dollars")
        else:
            print("Invalid amount entered. Try again.")
    elif answer.lower() == 'c':
        amount = input("How many emergency supplies would you like to buy?\n")
        if amount.isdigit():
            amount = int(amount)
            total = amount * emergency_supplies_price
            if dollars >= total:
                emergency_supplies += amount
                dollars -= total
            else:
                print("Not enough dollars")
        else:
            print("Invalid amount entered. Try again.")

    # Traveling
    answer = ""
    while answer.lower() not in ['a', 'b', 'c', 'd', 'e']:
        answer = input("Here are your options: A) Ride hard, B) Ride normal, C) Rest, D) Check party status, or E) Quit\n")

    if answer.lower() == 'a':
        if rations > 0:
            rations -= 1
            if days_until_showdown <= 0:
                party_health[0] += 1.5
                party_health[1] += 1.5
                party_health[2] += 1.5
                party_health[3] += 1.5
            else:
                party_health[0] += 3
                party_health[1] += 3
                party_health[2] += 3
                party_health[3] += 3
        else:
            print("You can't ride hard without rations")

        days = random.randint(5, 15)
        miles = random.randint(20, 40)
        miles_remaining -= miles
        days_until_showdown -= days

    elif answer.lower() == 'b':
        if horses > 0:
            days = random.randint(10, 20)
            party_health[0] -= 2
            party_health[1] -= 2
            party_health[2] -= 2
            party_health[3] -= 2
            random_percent = random.randint(0, 100)
            if random_percent <= 10:
                horses -= 1
        else:
            days = random.randint(20, 30)
            party_health[0] -= 4
            party_health[1] -= 4
            party_health[2] -= 4
            party_health[3] -= 4

        miles = random.randint(10, 30)
        miles_remaining -= miles
        days_until_showdown -= days

    elif answer.lower() == 'c':
        if horses > 0:
            days = random.randint(5, 10)
            party_health[0] += 2
            party_health[1] += 2
            party_health[2] += 2
            party_health[3] += 2
            random_percent = random.randint(0, 100)
            if random_percent <= 5:
                horses -= 1
        else:
            days = random.randint(10, 20)
            party_health[0] -= 2
            party_health[1] -= 2
            party_health[2] -= 2
            party_health[3] -= 2

        miles = 0
        days_until_showdown -= days

    elif answer.lower() == 'd':
        print("Party status:")
        print("Health: ", party_health)
        print("Rations: ", rations)
        print("Horses: ", horses)
        print("Emergency supplies: ", emergency_supplies)
        print("Miles remaining: ", miles_remaining)
        print("Days until showdown: ", days_until_showdown)

    elif answer.lower() == 'e':
        answer = input("Are you sure you want to quit? ")
        if 'y' in answer.lower():
            print("You have chosen to quit. Goodbye.")
            break

    # Random events
    rand_num = random.randint(1, 20)
    if rand_num == 1:
        print("A wild mustang has been spotted! You can try to catch it.")
        answer = input("Do you want to try to catch the mustang? ")
        if 'y' in answer.lower():
            random_percent = random.randint(0, 100)
            if random_percent <= 50:
                print("You caught the mustang!")
                horses += 1
            else:
                print("You failed to catch the mustang.")
        else:
            print("You decided not to try to catch the mustang.")

    elif rand_num == 20:
        print("You found a hidden waterhole! You can rest and recover.")
        party_health[0] += 5
        party_health[1] += 5
        party_health[2] += 5
        party_health[3] += 5

    # Check for dead party members
    for i in range(len(party_health)):
        if party_health[i] <= 0:
            party_health[i] = dead
            print(party_members[i], "has died!")

    # Check for game over
    if miles_remaining <= 0:
        print("Congratulations, you have reached the end of the trail!")
        break
    elif all(health == dead for health in party_health):
        print("Unfortunately, your entire party has died. Game over.")
        party_dead = True


