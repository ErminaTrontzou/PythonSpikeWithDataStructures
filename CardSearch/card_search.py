import math

# QUESTION 1: 
# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


#Let's assume that the cards are made up of numbers : cards[20,16,13,10,7,4,2]
#Let's assume that the correct answer is the card with number 10 (at index 3)

cards=[20,16,13,10,7,4,2]
card_to_find = 10


#Answer 1, linear search

def locate_card_with_linear_search(cards,card_to_find):

    print("Implementing linear search")

    index = 0

    print('Cards:', cards)
    print('Card to find:', card_to_find)

    while index < len(cards):
        if(cards[index] == card_to_find):
            return index
        index += 1
    return -1
    


# result = locate_card_with_linear_search(cards,card_to_find)
# if(result==-1):
#     print("Card not found)")
# else:
#     print("The card at location " + str(result) + " is the one, given that the list starts at index 0")


#Answer 2, binary search

def locate_card_with_binary_search(cards,card_to_find):

    print("Implementing binary search")

    print('Cards:', cards)
    print('Card to find:', card_to_find)

    start = 0
    end = len(cards) -1

    while start <= end:
        mid = (start + end)//2
        mid_number = cards[mid]
        if(mid_number == card_to_find):
            while((mid > start) and (cards[mid-1] == cards[mid])):
                mid = mid-1
            return mid
        elif(mid_number < card_to_find):
            end = mid - 1
        elif(mid_number > card_to_find):
            start = mid + 1
    return -1

result = locate_card_with_binary_search(cards,card_to_find)
if(result==-1):
    print("Card not found)")
else:
    print("The card at location " + str(result) + " is the one, given that the list starts at index 0")