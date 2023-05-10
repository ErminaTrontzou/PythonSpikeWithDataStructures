import math

# QUESTION 1: 
# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

#Answer 1:
#Let's assume that the cards are made up of numbers : cards[20,16,13,10,7,4,2]
#Let's assume that the correct answer is the card with number 10 (at index 3)


def locate_card(cards,cardToFind):
    index = 0
    while True:
        if(cards[index] == cardToFind):
            return index
        index += 1
        if(index==len(cards)):
           return "Card not found"
    

cards=[20,16,13,10,7,4,2]
cardToFind = 10

result = locate_card(cards,cardToFind) + 1
print("The card at location " + str(result) + " is the one.")

