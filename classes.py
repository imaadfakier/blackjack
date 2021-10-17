'''
Not a proper docstring here, but I just wanted to say that don't
forget you can also have default values in functions if argument
is not passed for the given parameter like so:

    def add(num_one=11, num_two=11):
        return num_one _ num_two
    
    add()

etc.

'''

from random import shuffle, choice

class Card:
    '''
    This class enables you to create a Card instance
    object responsible for housing various data about
    the card (object instance).
    '''
    
    ranks = ['Ace', 'ace', 'Two', 'two', 'Three', 'three', 'Four', 'four', 'Five', 'five', 'Six', 'six', 'Seven', 'seven', 'Eight', 'eight', 'Nine', 'nine', 'Ten', 'ten', 'Jack', 'jack', 'Queen', 'queen', 'King', 'king']
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    values = {
        'Ace': {'value_one': 11, 'value_two': 1}, 
        'Two': 2, 
        'Three': 3, 
        'Four': 4, 
        'Five': 5, 
        'Six': 6, 
        'Seven': 7, 
        'Eight': 8, 
        'Nine': 9, 
        'Ten': 10, 
        'Jack': 10, 
        'Queen': 10, 
        'King': 10
    }

    def __init__(self, rank, suit):
        self.rank = Card.ranks[Card.ranks.index(rank)]
        self.suit = suit
        self.value = Card.values[self.rank.capitalize()] # NOTE: The value of 'Ace'
                                                         #       will return another
                                                         #       dictionary.

    def __str__(self):
        return str(self.rank) + ' of ' + self.suit

class Deck(Card):
    '''
    This class enables you to create a Deck instance
    object responsible for housing 52 Card instances
    (i.e. a full deck), shuffling the deck and dealing
    (out) the various cards (i.e. Card instances) to/
    for the computer and (the) player.
    '''

    # ....

    def __init__(self):
        self.deck = []
        
        for the_suit in self.suits:
            for the_rank in self.ranks[::2]:
                self.deck.append(Card(the_rank, the_suit))

    def __str__(self):
        card_deck = []

        for card in self.deck:
            # card_deck.append(str(card))
            # card_deck.extend(str(card))
            card_deck.append(card.__str__()) # will produce the same result as
                                             # when you casted the card instance
                                             # with the str() function.
        
        return str(card_deck)

    def __len__(self):
        return len(self.deck)

    def get_deck(self):
        return self.deck

    # def set_...(self):
    #     self.<...> = ...

    # Inheritance
# class Dealer(Deck):
#     '''
#     This class represents the dealer in the BlackJack
#     game and enables you to create a Dealer instance
#     that will, in this case, constantly be "hit" with
#     new cards if the player's score is under 21 until
#     the dealer has beaten the player or "busts" himself
#     /herself.
#     '''



#     def __init__(self):
#         self.hand = []
#         self.score = 0

#     def shuffle_deck(self):
#         shuffle(self.deck)

#     def deal_card(self, top_of_deck_index):
#         return self.deck.pop(top_of_deck_index)

#     def show_hand(self):
#         hand = ''

#         for card in self.hand:
#             hand += str(self.hand) + ' | '

#         return hand

    # Composition
class Dealer:
    '''
    This class represents the dealer in the BlackJack
    game and enables you to create a Dealer instance
    that will, in this case, constantly be "hit" with
    new cards if the player's score is under 21 until
    the dealer has beaten the player or "busts" himself
    /herself.
    '''

    # ....

    def __init__(self, deck_obj):
        self.deck_obj = deck_obj
        self.hand = []
        self.score = 0
        self.money_collected = 0.0

    def shuffle_deck(self):
        shuffle(self.deck_obj.deck)

    def deal_card(self):
        return self.deck_obj.deck.pop(0)

    def show_hand(self):
        hand = ''

        for card_index in range(0, len(self.hand)):
            if card_index != len(self.hand) - 1:
                hand += str(self.hand[card_index]) + ' | '
            else:
                hand += str(self.hand[card_index])

        return hand

class Player():
    '''
    This class enables you to create a Player instance
    object responsible for housing various data about
    the player such as his/her name, bankroll and
    amount he's willing to bet on a game he/she is
    (playing) in as well as whether to be "hit" with
    another card or "stay" with his/her current card(s).
    '''

    # ....

    def __init__(self, title, name, bankroll, dealer_obj):
        self.title = title
        self.name = name
        self.bankroll = int(bankroll)
        self.bet_amount = 0
        self.hand = []
        self.score = 0
        self.dealer_obj = dealer_obj

    def __str__(self):
        return 'Player name: {name}\nBankroll: {bankroll}\n'.format(name=self.name, bankroll=self.bankroll)

    def bet(self, amount):
        if self.bankroll < amount:
            print('Sorry {title} {name}, but you do not have sufficient funds to bet that much. Please enter a new wager.\n'.format(title=self.title, name=self.name))
        elif amount <= 0:
            print('Sorry {title} {name}, but you have to place a bet. Please enter a new wager.\n'.format(title=self.title, name=self.name))
        else:
            self.bet_amount = amount

    def hit(self):
        return self.dealer_obj.deal_card()

    def stay(self):
        pass

    def show_hand(self):
        hand = ''

        for card_index in range(0, len(self.hand)):
            if card_index != len(self.hand) - 1:
                hand += str(self.hand[card_index]) + ' | '
            else:
                hand += str(self.hand[card_index])

        return hand

    # Shorthand to print everything from a collection
    # using an asterisk (i.e. *) accompanied by a
    # (defined/specfied) separator (i.e. '\n', ' ',
    # ' | ' etc.)
    # 
    #     BlackJack example:
    #         print('/nDealer\'s Hand: ', *dealer.all_cards,
    #                sep='\n')
    # 
    # A newline will be printed every time you show and
    # print out, in this case, one of the dealer's cards
    # from his hand (i.e. the list of cards in his hand).
    # 
    # Another example is shown below:
    # 
    #     items = [1, 2, 3]
    #     print('Item\'s are: ', *items)
    # 
    #     OR (i.e. separator included)
    # 
    #     print('Item\'s are: ', *items, sep='\n')
