import Card
import Deck
import Player

def start_game():
    player_one = Player.Player('one');
    player_two = Player.Player('two')

    deck = Deck.Deck()
    deck.Sheffle()

    for d in range(26):
        player_one.add_card(deck.deal_one())
        player_two.add_card(deck.deal_one())

    game_on = True
    round_no = 0

    while game_on:
        round_no += 1
        print(f'Round {round_no}')
        if(len(player_one.all_cards) == 0):
            print('Player two won!')
            game_on = False
            break
        if(len(player_two.all_cards) == 0):
            print('Player one won!')
            game_on = False
            break

        player_one_current_cards = []
        player_one_current_cards.append(player_one.remove_one())

        player_two_current_cards = []
        player_two_current_cards.append(player_two.remove_one())

        at_war = True

        while at_war:
            if(player_one_current_cards[-1].value > player_two_current_cards[-1].value):
                player_one.add_card(player_one_current_cards)
                player_one.add_card(player_two_current_cards)
                at_war = False

            elif (player_one_current_cards[-1].value < player_two_current_cards[-1].value):
                player_two.add_card(player_one_current_cards)
                player_two.add_card(player_two_current_cards)
                at_war = False
            else:
                if len(player_one.all_cards) < 5:
                    print('Player_one unable to declare war!')
                    print(f'Player two {player_two.name} won!')
                    game_on  = False
                    break

                elif len(player_two.all_cards) < 5:
                    print(f'Player two {player_two.name} unable to declare war!')
                    print(f'Player one {player_one.name} won!')
                    game_on = False
                    break
                else:
                    for c in range(5):
                        player_one_current_cards.append(player_one.remove_one())
                        player_two_current_cards.append(player_two.remove_one())





   # print(player_one.all_cards[0])




start_game()