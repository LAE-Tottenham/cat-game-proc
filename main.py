import os
import time
import random
cat_attributes = {
    "name": "",
    "breed": "",
    "intelligence": 100,
    "energy": 100,
    "weight": 3000,
    "hunger": 100
}
os.system("clear")
print("Welcome to my cat game!")
name = input("Enter name:\n")
os.system("clear")
cat_attributes.update({"name": name})
breed = input("Enter your cat's desired breed.\n")
cat_attributes.update({"breed": breed})

w = 0
os.system("clear")
while True:
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed 4. Show stats 5. Finished playing\n")

    if option == '1':
        os.system("clear")
        for i in range(random.randint(1,4)):
            time.sleep(1)
            print("...")
        print("Your cat had a great time playing with you! It is very happy.")
        cat_attributes["energy"] += -10
        cat_attributes["hunger"] += -20
        cat_attributes["weight"] += -25
        print(f"Your cat has gotten slightly tired. Its energy is now: {cat_attributes["energy"]}")
        print(f"Your cat has lost a bit of weight from playing and is a little more hungry. Its weight is now: {cat_attributes['weight']}, and its hunger is now: {cat_attributes['hunger']}")
        pass
    elif option == '2':
        os.system("clear")
        for i in range(random.randint(1,4)):
            time.sleep(1)
            print("...")
        print("Your cat learned a new trick! It is happy.")
        cat_attributes["intelligence"] += 2
        cat_attributes["energy"] += -10
        cat_attributes["hunger"] += -5
        print(f"Your cat is now slightly smarter! Its intelligence is now : {cat_attributes["intelligence"]}")
        print(f"Your cat has necome slightly more tired and hungry. Its energy is now {cat_attributes['energy']}, and its hunger is now {cat_attributes["hunger"]}")
        pass
    elif option == '3':
        os.system("clear")
        for i in range(random.randint(3,5)):
            time.sleep(1)
            print("...")
        print("Your cat has eaten a nice meal! It is now full and happy.")
        cat_attributes["weight"] += 50
        cat_attributes["energy"] += 20
        cat_attributes["hunger"] += 20
        print(f"Your cat is now slightly heavier! It now weighs: {cat_attributes["weight"]}")
        print(f"Your cat now has more energy! Its energy is now: {cat_attributes["energy"]}")
        print(f"Your cat is full now! Its hunger is now: {cat_attributes["hunger"]}")
    elif option == '4':
        os.system("clear")
        print(f"These are your cat's stats: {cat_attributes}")
    elif option == '5':
        os.system("clear")
        print("Your cat is satisfied with your session today. It is very happy. It will now go off and do its own thing.")
        break
    else:
        os.system("clear")
        print("That is not an option. Please choose one of the available options.")
        pass

    if cat_attributes['energy'] <= 0:
        os.system("clear")
        print("Your cat is tired. It needs to sleep to regain its energy.")
        for i in range(random.randint(6,10)):
            time.sleep(1)
            print("...")
        cat_attributes.update({'energy': 100})
        print("Your cat has woken up! It is rejuvenated! Its energy is now back to 100.")
        pass
    if cat_attributes['hunger'] <= 0:
        os.system("clear")
        while w < 5:
            feed_option = input("Your cat is absolutely famished! Feed the cat by typing '1'!\n")
            if feed_option == "1":
                os.system("clear")
                for i in range(random.randint(4,7)):
                    time.sleep(1)
                    print("...")
                cat_attributes.update({"hunger": 100})
                cat_attributes.update({"energy": 100})
                cat_attributes["weight"] += 50
                print("Your cat wolfed down a massive meal! Its hunger and energy have gone back to 100.")
                break
            else:
                os.system("clear")
                print("That's not the option to feed the cat! Hurry up and feed it before something bad happens!")
                w += 1
        if w >= 5:
            os.system("clear")
            print("Your cat died of starvation due to your negligence. You can now be liable for up to a year of prison time and up to a £40,000 fine. Well done. I'll see you in court.")
            exit()