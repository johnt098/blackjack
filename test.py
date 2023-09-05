import unittest
import main as b

class TestFunc(unittest.TestCase):

    def test_get_deck(self):
        deck = b.get_deck(b.DECK)
        b.pop(deck)
        self.assertEqual(len(deck), len(b.DECK) - 1)

    def test_pop(self):
        deck = b.get_deck(b.DECK)
        result = b.pop(deck)
        self.assertEqual(len(deck), 51)
        self.assertEqual(result, 'Ace (Spades)')
    
    def test_initial_draw(self):
        deck = b.get_deck(b.DECK)
        player = b.Player('Jack')
        dealer = [None, None]
        deck = b.initial_draw(deck, player, dealer)
        player_deck = player.deck
        self.assertEqual(len(deck), 52 - 4)
        self.assertEqual(player_deck, ['Ace (Hearts)', 'Ace (Clubs)'])
        self.assertEqual(dealer, ['Ace (Spades)', 'Ace (Diamonds)'])

    def test_draw(self):
        deck = b.get_deck(b.DECK)
        player = b.Player('Jack')
        player.deck = []
        dealer = []
        b.draw(deck, player)
        b.draw(deck, dealer)
        self.assertEqual(player.deck[0], 'Ace (Spades)')
        self.assertEqual(dealer[0], 'Ace (Hearts)')
        self.assertEqual(len(deck), 50)
    
    def test_card_name(self):
        self.assertEqual(b.card_name('6 (Clubs)'), '6')
        self.assertEqual(b.card_name('Ace (Clubs)'), 'Ace')

    def test_ace_check(self):
        eg_1 = ['Ace (Hearts)', 'Ace (Clubs)']
        eg_2 = ['2 (Hearts)', '3 (Spades)', '4 (Clubs)']
        eg_3 = ['2 (Hearts)', '3 (Spades)', '4 (Clubs)', 'Ace (Clubs)']
        self.assertTrue(b.ace_check(eg_1))
        self.assertFalse(b.ace_check(eg_2))
        self.assertTrue(b.ace_check(eg_3))

if __name__ == '__main__':
    unittest.main()