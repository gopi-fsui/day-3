import random
import art

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "K": 10,
    "Q": 10
}

# TODO-1 Create function for score calculation;
def score_calc(score_list):
    score = 0
    for key in score_list:
        score += cards[key]
    if ("A" in score_list) and (score > 21):
        for char in score_list:
            if (char == "A") and (score > 21):
                score -= 10
    return score


#Todo-2 Create function for Game result:
def game_result(player_cards, dealer_cards):
    print(f"Your final hand: {player_cards} , final score: {score_calc(player_cards)}\n"
          f"Computer's final hand: {dealer_cards}, final score: {score_calc(dealer_cards)}")
    if score_calc(player_cards) > 21:
        print("You Lose")
    elif score_calc(dealer_cards) > 21:
        print("You Win")
    elif score_calc(player_cards) == score_calc(dealer_cards):
        if (score_calc(player_cards) == 21) and ((len(player_cards) > 2) and (len(dealer_cards) == 2)):
            print("Dealer get black jack in first attempt, You Lose")
        else:
            print("Draw")
    elif score_calc(player_cards) > score_calc(dealer_cards):
        print("You Win")
    elif score_calc(player_cards) < score_calc(dealer_cards):
        print("You Loss")
    print(f"--------------------------------------------")


# todo-3 Create function for score_card
def score_card(player_cards,dealer_cards):
    print(f"Your cards: {player_Cards}, current score: {score_calc(player_Cards)} \n"
          f"Dealer's first card: ['{dealer_Cards[0]}','-']\n"
          f"--------------------------------------------")




game_Continue = True
if not input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    game_Continue = False

while game_Continue:
    print(art.logo)
    player_Cards = []
    dealer_Cards = []

    for x in range(2):
        player_Cards.append(random.choice(list(cards.keys())))
        dealer_Cards.append(random.choice(list(cards.keys())))

    score_card(player_Cards,dealer_Cards)

    if score_calc(player_Cards) == 21:
        game_result(player_Cards,dealer_Cards)
        if not input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
            game_Continue = False

    else:
        card_loop = input("Type 'y' to get another card, type 'n' to pass:").lower()
        while card_loop == "y":
            player_Cards.append(random.choice(list(cards.keys())))
            score_card(player_Cards,dealer_Cards)

            if score_calc(player_Cards) < 21:
                card_loop = input("Type 'y' to get another card, type 'n' to pass:").lower()
            else:
                card_loop = "n"

        if (score_calc(player_Cards) <= 21) and (score_calc(dealer_Cards) < 17):
            while score_calc(dealer_Cards) < 17:
                dealer_Cards.append(random.choice(list(cards.keys())))
        game_result(player_Cards, dealer_Cards)
        if not input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
            game_Continue = False

