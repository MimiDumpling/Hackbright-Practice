def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * tip_percentage * 0.01
    return tip


def calculate_total_bill(bill_amount, tip_percentage):
    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_bill = bill_amount + tip_amount
    return total_bill


def split_bill(bill_amount, tip_percentage, number_people):
    total_bill = calculate_total_bill(bill_amount, tip_percentage)
    split = total_bill / number_people
    return split

print split_bill(20, 18, 3)


def main():
    choose_your_adventure = raw_input("Choose: *1* - Calculate Tip or *2* - Split the Bill ")
    if choose_your_adventure == "1":
        bill_amount = int(raw_input("What is the bill amount? "))
        tip_percentage = int(raw_input("What is the tip percentage? "))
        print "The tip amount is", calculate_tip(bill_amount, tip_percentage)
        print "The total bill is", calculate_total_bill(bill_amount, tip_percentage)
        are_you_sure = raw_input("Would you like to split the bill? Yes or No? ")
        if are_you_sure == "Yes":
                number_people = int(raw_input("How many ways would you like to split the bill? "))
                print "Each member of your party owes $", split_bill(bill_amount, tip_percentage, number_people)
        else:
            print "Thanks. Have a nice night. Bye!"
    else:
        bill_amount = int(raw_input("What is the bill amount? "))
        tip_percentage = int(raw_input("What is the tip percentage? "))
        number_people = int(raw_input("How many ways would you like to split the bill? "))
        print "Each member of your party owes $", split_bill(bill_amount, tip_percentage, number_people)


if __name__ == '__main__':
    main()
