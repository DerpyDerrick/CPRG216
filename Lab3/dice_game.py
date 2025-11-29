import random
NUM_DICE_TO_ROLL = 5
SEED = 2183

def roll_dice(rolls):
    '''
    receives the number of dice being rolled as a parameter and returns a list of
    that many elements holding random integers between 1 and 6 inclusive.
    '''
    list = [] 
    # rolls dice as many times as the user wanted
    for i in range (rolls):
        list.append(random.randint(1,6))
    # prints results to user
    print("Your roll of", list, "contains", most_repeats(list), "of a kind.") # calls function most_repeats
def most_repeats(list):
    '''
    receives a list of integers (representing dice values) as the parameter and
    returns the highest number of repeated values. E.g. if the received list contains 
    [1, 1, 4, 4, 4], the returned value would be 3.
    '''
    # stores the number of times the number appeared in the lsit
    one = int(list.count(1))
    two = int(list.count(2))
    three = int(list.count(3))
    four = int(list.count(4))
    five = int(list.count(5))
    six = int(list.count(6))
    highest = one
    # checks to see which which number appeared the most in the list
    for i in range (1,6):
        if i == 0:
            count = one
        elif i == 1:
            count = two
        elif i == 2:
            count = three
        elif i == 3:
            count = four
        elif i == 4:
            count = five
        elif i == 5:
            count = six
        if count > highest:
            highest = count
    return highest
def main():
    '''
    establishes the random generator seed, performs user input/output, and controls
    the overall flow of the game.
    Start with this skeleton code:
    '''
    random.seed(SEED)
    # implement remaining logic here!

    # loops as long as the user wants
    while(True) :
        roll_dice(NUM_DICE_TO_ROLL)

        # taking in user input as well as error handling
        userCont = input("Do you want to roll again (Y/N)? ").upper()
        if userCont.startswith('Y') :
            pass
        elif userCont.startswith('N') :
            break
        else :
            print("That is not a valid input. Please input a proper input.")
main()