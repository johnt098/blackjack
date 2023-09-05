import numpy as np

DECK = ['Ace (Spades)', 'Ace (Hearts)', 'Ace (Diamonds)', 'Ace (Clubs)', 
        '2 (Spades)', '2 (Hearts)', '2 (Diamonds)', '2 (Clubs)', 
        '3 (Spades)', '3 (Hearts)', '3 (Diamonds)', '3 (Clubs)', 
        '4 (Spades)', '4 (Hearts)', '4 (Diamonds)', '4 (Clubs)',
        '5 (Spades)', '5 (Hearts)', '5 (Diamonds)', '5 (Clubs)',
        '6 (Spades)', '6 (Hearts)', '6 (Diamonds)', '6 (Clubs)',
        '7 (Spades)', '7 (Hearts)', '7 (Diamonds)', '7 (Clubs)',
        '8 (Spades)', '8 (Hearts)', '8 (Diamonds)', '8 (Clubs)',
        '9 (Spades)', '9 (Hearts)', '9 (Diamonds)', '9 (Clubs)',
        '10 (Spades)', '10 (Hearts)', '10 (Diamonds)', '10 (Clubs)',
        'Jack (Spades)', 'Jack (Hearts)',  'Jack (Diamonds)',  'Jack (Clubs)',
        'Queen (Spades)', 'Queen (Hearts)', 'Queen (Diamonds)', 'Queen (Clubs)',
        'King (Spades)', 'King (Hearts)', 'King (Diamonds)', 'King (Clubs)']

DECK_DICT = {
    'Ace (Spades)':1, 'Ace (Hearts)':1, 'Ace (Diamonds)':1, 'Ace (Clubs)':1, 
    '2 (Spades)':2, '2 (Hearts)':2, '2 (Diamonds)':2, '2 (Clubs)':2, 
    '3 (Spades)':3, '3 (Hearts)':3, '3 (Diamonds)':3, '3 (Clubs)':3, 
    '4 (Spades)':4, '4 (Hearts)':4, '4 (Diamonds)':4, '4 (Clubs)':4,
    '5 (Spades)':5, '5 (Hearts)':5, '5 (Diamonds)':5, '5 (Clubs)':5,
    '6 (Spades)':6, '6 (Hearts)':6, '6 (Diamonds)':6, '6 (Clubs)': 6,
    '7 (Spades)':7, '7 (Hearts)':7, '7 (Diamonds)':7, '7 (Clubs)':7,
    '8 (Spades)':8, '8 (Hearts)':8, '8 (Diamonds)':8, '8 (Clubs)':8,
    '9 (Spades)':9, '9 (Hearts)':9, '9 (Diamonds)':9, '9 (Clubs)':9,
    '10 (Spades)':10, '10 (Hearts)':10, '10 (Diamonds)':10, '10 (Clubs)':10,
    'Jack (Spades)':10, 'Jack (Hearts)':10,  'Jack (Diamonds)':10,  'Jack (Clubs)':10,
    'Queen (Spades)':10, 'Queen (Hearts)':10, 'Queen (Diamonds)':10, 'Queen (Clubs)':10,
    'King (Spades)':10, 'King (Hearts)':10, 'King (Diamonds)':10, 'King (Clubs)':10
}

def get_deck(deck): #passed
    return DECK.copy()

def shuffle(deck): #passed
    '''Shuffle the deck'''
    np.random.shuffle(deck)
    return deck

def pop(deck): #passed
    '''Pop first card from deck'''
    popped = deck.pop(0)
    return popped

def initial_draw(deck, player, dealer): #passed
    '''Initiate first round of draws'''
    dealer[0] = pop(deck)
    player.deck[0] = pop(deck)
    dealer[1] = pop(deck)
    player.deck[1] = pop(deck)
    return deck 

def draw(deck, player_or_dealer): #passed
    '''Draw a card for the player or dealer'''
    if type(player_or_dealer) == Player:
        player_or_dealer.deck.append(pop(deck))
    else:
        player_or_dealer.append(pop(deck))

def card_name(card): #passed
    '''Return the card name'''
    return card.split(' ')[0]

def ace_check(hand): #passed
    '''Check if there is an ace in the hand'''
    for card in hand:
        if card_name(card) == 'Ace':
            return True
    return False

def hand_score(hand): #FIXME
    '''Return the score of the hand'''
    if ace_check(hand) == True:
        if card_name(hand[0]) == 'Ace' and card_name(hand[0]) == 'Ace':
            return 21
        if len(hand) == 2:
            score_10 = 10
            score_1 = 1
            for card in hand:
                if card != 'Ace':
                    val = DECK_DICT[card]
                    score_10 += val
            for card in hand:
                if card != 'Ace':
                    val = DECK_DICT[card]
                    score_1 += val
            return [score_10, score_1]
        else:
            pass
    else:
        score = 0
        for card in hand:
            val = DECK_DICT[card]
            score += val
        return score

def player_score(player):
    '''Return the player score'''
    hand = player.deck
    if ace_check(hand) == True:
        if len(hand) == 2 and hand_score(hand) == 21:
            player.win_bj
            return 'blackjack'
    else:
        return hand_score(hand)
    
def dealer_score(dealer):
    '''Return the dealer score'''

    
# def play_round():
#     print()

class Player:

    deck = [None, None]

    def __init__(self, name):
        self.name = name
        self.balance = 1000
        self.bet_amount = 0
    
    def bet(self, amount):
        '''Choose the amount of money to bet'''
        self.balance -= amount
        self.bet_amount = amount
    
    def lose_round(self):
        '''Subtract the amount that the player bets from balance'''
        self.balance -= self.bet_amount
        print('You lost ' + str(self.bet_amount))
        print('Your balance is now: ' + str(self.balance))
        self.bet_amount = 0

    def win_round(self):
        '''Add the amount that the player bets to balance'''
        self.balance += self.bet_amount
        print('You won ' + str(self.bet_amount))
        print('Your balance is now ' + str(self.balance))
        self.bet_amount = 0

    def win_bj(self):
        '''Add the amount * 1.5 the amount that the player bets to balance'''
        self.balance += self.bet_amount * 1.5
        print('You won ' + str(self.bet_amount * 1.5))
        print('Your balance is now ' + str(self.balance))
        self.bet_amount = 0
    

def main():
    name = str(input('Hello, welcome to Deez N Casino. What is your name? ' ))
    print() #blank space
    player = Player(name)
    print('Welcome Mr./Ms. ' + str(player.name))
    print('Your starting balance is $1000.')
    print() #blank space
    play = 'yes'
    dealer = [None, None]
    while play == 'yes':
        amount = int(input('How much Nmoney would you like to wager? '))
        print() #blank space
        player.bet(amount)
        deck = shuffle(DECK)
        deck = initial_draw(deck, player, dealer)
        print('Your cards are ' + str(player.deck[0]) + ' and ' + 
              str(player.deck[1]) + '.')
        
        print('The first card of the dealer is ' + dealer[0])
        print() #blank space
        h_or_s = input('Would you like to hit or stand? ')
        if h_or_s == 'hit':
            deck = draw(deck, player)
        else:
            pass 

if __name__ == '__main__':
    main()