import unittest
from hand import Hand
from score import score_hand


class TestScore(unittest.TestCase):
    def setUp(self):
        self.royal_flush_hand = Hand(["AS", "KS", "TS", "QS", "JS"])
        self.straight_flush_hand = Hand(["9S", "KS", "TS", "QS", "JS"])
        self.flush_hand = Hand(['2C', '3C', 'KC', '5C', '8C'])
        self.straight_hand = Hand(['AC', '2S', '3C', '4H', '5C'])
        self.full_house_hand = Hand(['3C', '3S', '3D', '8D', '8H'])
        self.four_of_a_kind_hand = Hand(['4S', '4C', '4H', '4D', 'JC'])
        self.three_of_a_kind_hand = Hand(['5D', '5H', '9S', '5C', 'AS'])
        self.two_pair_hand = Hand(['5D', '5H', '9S', '9C', 'AS'])
        self.jacks_or_better_hand = Hand(['QH', 'QC', '5C', '3S', '8H'])
        self.non_winning_hand = Hand(['3D', '4C', '6C', 'KC', '8H'])

    def test_royal_flush(self):
        self.assertEqual(score_hand(self.royal_flush_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.flush_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.straight_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Royal Flush')

    def test_straight_flush(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Straight Flush')
        self.assertEqual(score_hand(self.straight_flush_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.flush_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.straight_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Straight Flushh')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Straight Flush')


if __name__ == '__main__':
    unittest.main()
