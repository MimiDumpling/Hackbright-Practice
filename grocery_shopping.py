# Program to add & remove, and display items in a shopping list

from time import sleep

def add_to_list(shopping_list):
    print " "
    item = raw_input("What would you like to add? ").lower()
    sleep(1)

    if item in shopping_list:

        print " "
        print "This item is already in your list, so we didn't add a second one."
        sleep(2)

    else:

        shopping_list.append(item)
        shopping_list.sort()

    print " "
    print "Here's your updated list: " 
    print shopping_list


def order_list(shopping_list):
    shopping_list.sort()


def remove_item(shopping_list):
    print " "
    item2 = raw_input("What do you want to remove? ").lower()
    sleep(1)

    if item2 in shopping_list:
        shopping_list.remove(item2)

    else:

        print " "
        print "That item is not in the shopping list, so we couldn't remove it."
        sleep(2)

    shopping_list.sort()

    print " "
    print "Here's your updated list: " 
    print shopping_list    
    print " "
    sleep(2)

    
def main():
    shopping_list = ["toothpaste", "soap", "tampons", "lotion"]

    print " "
    print "Let's make a shopping list!"
    sleep(1)
    
    add_to_list(shopping_list)
    sleep(1)

    order_list(shopping_list)

    remove_item(shopping_list)
    sleep(1)

    print "Thanks! See you next time!"
    print " "

    # shopping_list.extend(["floss", "shampoo", "conditioner", "facewash"])
    # print shopping_list
    # sleep(2)

    # shopping_list.remove("floss")
    # print shopping_list

if __name__ == '__main__':
    main()
