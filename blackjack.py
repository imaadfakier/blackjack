'''
Main program of the game BlackJack, which is responsible
for the gameplay logic (of the game).
'''

from classes import Card, Deck, Player, Dealer

print(
    '''

 $$$$$$\ $$$$$$\$$\      $$\$$$$$$$\ $$\      $$$$$$\$$$$$$$$\$$$$$$\$$$$$$$$\$$$$$$$\  
$$  __$$\\_$$  _$$$\    $$$ $$  __$$\$$ |     \_$$  _$$  _____\_$$  _$$  _____$$  __$$\ 
$$ /  \__| $$ | $$$$\  $$$$ $$ |  $$ $$ |       $$ | $$ |       $$ | $$ |     $$ |  $$ |
\$$$$$$\   $$ | $$\$$\$$ $$ $$$$$$$  $$ |       $$ | $$$$$\     $$ | $$$$$\   $$ |  $$ |
 \____$$\  $$ | $$ \$$$  $$ $$  ____/$$ |       $$ | $$  __|    $$ | $$  __|  $$ |  $$ |
$$\   $$ | $$ | $$ |\$  /$$ $$ |     $$ |       $$ | $$ |       $$ | $$ |     $$ |  $$ |
\$$$$$$  $$$$$$\$$ | \_/ $$ $$ |     $$$$$$$$\$$$$$$\$$ |     $$$$$$\$$$$$$$$\$$$$$$$  |
 \______/\______\__|     \__\__|     \________\______\__|     \______\________\_______/ 
                                                                                        

88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
    '''
)

deck = Deck()
    # dealer = Dealer()
dealer = Dealer(deck)
    # -----------------------------------------#
acceptable_title_input = ['Mr', 'Ms', 'Mrs']
player_created_successfully = False
    # -----------------------------------------#
ready_or_not = ''
hit_or_stay = ''
acceptable_input = ['hit', 'stay', 'game over']
    # -----------------------------------------#
game_over = False
    # -----------------------------------------#
play_again = ''
replay = False


def deal_initial_cards():
    global dealer
    global player

    for index in range(0, 2):
        dealer.hand.append(dealer.deal_card())
        handle_card_value(index, 'dealer')
        player.hand.append(dealer.deal_card())
        handle_card_value(index, 'player')


def handle_card_value(index, for_player_or_dealer):
    global dealer
    global player
    dealer.deck_obj.values['Ace'] = {'value_one': 11, 'value_two': 1}

    if for_player_or_dealer == 'dealer':
        if (dealer.hand[index].rank == 'Ace') or (dealer.hand[index].rank == 'ace'):
            if dealer.score + dealer.hand[index].value['value_one'] <= 21:
                dealer.score += dealer.hand[index].value['value_one']
                dealer.hand[index].value = dealer.hand[index].value['value_one']
            else:
                dealer.score += dealer.hand[index].value['value_two']
                dealer.hand[index].value = dealer.hand[index].value['value_two']
        else:
            dealer.score += dealer.hand[index].value
    else:
        if (player.hand[index].rank == 'Ace') or (player.hand[index].rank == 'ace'):
            if player.score + player.hand[index].value['value_one'] <= 21:
                player.score += player.hand[index].value['value_one']
                player.hand[index].value = player.hand[index].value['value_one']
            else:
                player.score += player.hand[index].value['value_two']
                player.hand[index].value = player.hand[index].value['value_two']
        else:
            player.score += player.hand[index].value


def game_has_ended(winner):
    global hit_or_stay
    global player
    global dealer
    global game_over

    if winner == 'player':
        hit_or_stay = 'game over'
            
        print(f'Congratulations! You win {player.title} {player.name}. Enjoy your earnings!\n')

        player.bankroll += player.bet_amount * 2

        game_over = True

        print(player)
    elif winner == 'dealer':
        hit_or_stay = 'game over'
            
        print(f'Bust! My apologies {player.title} {player.name}. You lose. Better luck next time!\n')

        player.bankroll -= player.bet_amount
        dealer.money_collected += player.bet_amount

        game_over = True

        print(player)
    else:
        hit_or_stay = 'game over'

        print(f'Push! You have tied with the dealer for the win {player.title} {player.name}. No money won, but no money lost!\n')

        player.bet_amount = 0

        game_over = True

        print(player)


def do_you_want_to_play_again():
    global play_again
    global replay

    while play_again not in ['yes', 'no']:
        play_again = input('Would you like to play again? (Yes/No) ').lower()

        if play_again not in ['yes', 'no']:
            print('Error. Please try again.\n')
    else:
        if play_again == 'yes':
            replay = True
        else:
            replay = False

            print()


def show_hands():
    global dealer
    global player

    print(f'Dealer\'s cards => [{dealer.show_hand()} ] = {dealer.score}')
    print(f'Your cards => [{player.show_hand()}] = {player.score}\n')


def reset_game():
    global deck
    global player
    global dealer
    global hit_or_stay
    global game_over
    global play_again
    global replay

    dealer.deck_obj.values['Ace'] = {'value_one': 11, 'value_two': 1}
    deck = Deck()
    dealer = Dealer(deck)
    player.bet_amount = 0
    player.hand = []
    dealer.hand = []
    player.score = 0
    dealer.score = 0
    hit_or_stay = ''
    game_over = False
    play_again = ''
    replay = False


while not player_created_successfully:
    title = input('Title (Mr/Ms/Mrs): ').lower().capitalize()

    if title in acceptable_title_input:
        try:
            player = Player(title, input('Name: '), input('Bankroll for the night: '), dealer)
        except:
            print('Error! Please, try again\n')
        else:
            if player.bankroll > 0:
                player_created_successfully = True
            else:
                print('Error! Please, try again\n')
    else:
        print('Error! Please, try again\n')

print(f'Good Evening {title} {player.name}. Welcome to BlackJack ... let the games begin!\n{player}')

while not game_over:
    while ready_or_not != 'yes':
        ready_or_not = input(f'Hi, {player.name}. I\'ll be the dealer for tonight. Are you ready? ').lower()
    else:
        print()

        dealer.shuffle_deck()
        # print(dealer.deck)

        while player.bet_amount == 0 and str(player.bet_amount).isdigit():
            try:
                player.bet(int(input('Enter wager: ')))

                print()
            except:
                print('Error, please try again\n')

        dealer.shuffle_deck()

        player_hand = ''
        dealer_hand = ''

        deal_initial_cards()

        print(f'Dealer\'s cards => [{str(dealer.hand[0])} | (Face Down) ] = {dealer.score - dealer.hand[1].value}')
        print(f'Your cards => [{str(player.hand[0])} | {str(player.hand[1])}] = {player.score}\n')

        if (player.score > 21 and dealer.score <= 21) or (player.score < 21 and dealer.score == 21):
            game_has_ended('dealer')

            do_you_want_to_play_again()
        elif (player.score <= 21 and dealer.score > 21) or (player.score == 21 and dealer.score < 21):
            game_has_ended('player')

            do_you_want_to_play_again()
        elif player.score > 21 and dealer.score > 21:
            game_has_ended('dealer')

            do_you_want_to_play_again()
        elif player.score == dealer.score == 21:
            show_hands()

            game_has_ended('neither')

            do_you_want_to_play_again()
        
        while hit_or_stay not in acceptable_input:
            try:
                while hit_or_stay not in acceptable_input: 
                    hit_or_stay = input('Would you like another "hit" or are you going to "stay"? (hit/stay) ').casefold()

                    if hit_or_stay not in acceptable_input:
                        print('Error! Please try again.\n')

                print()
                # while True: 
                #     hit_or_stay = input('Would you like another "hit" or are you going to "stay"? (hit/stay) ').casefold()

                #     if hit_or_stay not in ['hit', 'stay', 'game_over']:
                #         print('Error! Please try again.\n')
                #     else:
                #         break

                # print()
            except Exception as e:
                print('Error! Please try again.\n')
            else:
                if hit_or_stay == 'hit':
                    player.hand.append(player.hit())

                    handle_card_value(len(player.hand) - 1, 'player')

                    show_hands()

                    if player.score > 21:
                        game_has_ended('dealer')

                        do_you_want_to_play_again()
                    elif player.score == 21:
                        game_has_ended('player')

                        do_you_want_to_play_again()
                    else:
                        if player.score < 21:
                            dealer.hand.append(dealer.deal_card())

                            handle_card_value(len(dealer.hand) - 1, 'dealer')

                            show_hands()

                            if dealer.score > 21:
                                game_has_ended('player')

                                do_you_want_to_play_again()
                            elif dealer.score == 21:
                                game_has_ended('dealer')

                                do_you_want_to_play_again()
                            else:
                                hit_or_stay = ''
                else:
                    if player.score < 21:
                        dealer.hand.append(dealer.deal_card())

                        handle_card_value(len(dealer.hand) - 1, 'dealer')

                        show_hands()

                        if dealer.score > 21:
                            game_has_ended('player')

                            do_you_want_to_play_again()
                        elif dealer.score == 21:
                            game_has_ended('dealer')

                            do_you_want_to_play_again()
                        else:
                            hit_or_stay = ''

        if replay:
            reset_game()
        else:
            print('Bummer! We\'re sad to see you go. Thank you for playing!')
