import pydealer


class Deck:
    def __init__(self):
        self.total_players = None
        self.game_deck = None
        self.discarded_pile = None
        self.cards_dealt_map = None
        self.num_cards = 2

    def get_cards_stats(self):
        print("Total number of cards in the deck: {0}".format(len(self.game_deck)))
        print("Total number of cards in discarded pile: {0}".format(len(self.discarded_pile)))

    def setup_board(self, total_players=2):
        self.game_deck = pydealer.Deck()
        self.discarded_pile = pydealer.Stack()
        self.game_deck.shuffle()
        self.game_deck.shuffle()
        self.cards_dealt_map = dict()
        self.total_players = total_players
        for i in range(self.total_players):
            cards_dealt = self.game_deck.deal(self.num_cards)
            self.discarded_pile.add(cards_dealt)
            cards_list = list()
            for each_card in cards_dealt:
                cards_list.append(each_card.name)
            self.cards_dealt_map["player_{0}".format(i)] = cards_list

        self.get_cards_stats()
        return self.cards_dealt_map

    def deal_cards(self, player_id, num=1):
        player_name = "player_{0}".format(player_id)
        if player_name in self.cards_dealt_map:
            cards_dealt = self.game_deck.deal(num)
            self.discarded_pile.add(cards_dealt)
            for each_card in cards_dealt:
                self.cards_dealt_map[player_name].append(each_card.name)
        else:
            print("ERROR: {0} does not exist".format(player_name))

        self.get_cards_stats()
        return self.cards_dealt_map

    def get_player_cards(self):
        return self.cards_dealt_map
