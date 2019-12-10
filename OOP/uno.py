import random

class Uno:
  """
  Lobby room for uno game
  """
  def __init__(self, num_player):
    """
    num_player: number of player in this game
    players: specific player object
    start: if game started
    end: if game end
    deck: the card in this uno
    """
    self._num_player = num_player
    self._players = []
    self._start = False
    self._end = False
    self._deck = []
  
  def start_game(self, parameter_list):
    pass
  
  def end_game(self):
    pass

class Player:
  def __init__(self, player_id):
    self._id = player_id
    self.hand = []

  def play_card(self, idx):
    card = self.hand[idx]
    if isPlayAble(card):
      self.hand.remove(idx)
      return True
    return False
  
  def draw(self, deck):
    self.hand.append(deck.remove_top_card)
  
  def see_hand(self):
    pass

  def getNumOfCardLeft(self):
    return len(self.hand)

class Deck:
  def __init__(self, card_num):
    self.card_num = card_num
    self._cards = []

  def initialize_cards(self):
    raise NotImplementedError

  def insert(self, cards):
    raise NotImplementedError
  
  def remove_top_card(self):
    raise NotImplementedError

  def shuffle(self):
    self.cards = random.shuffle(self.cards)

class UnoDeck(Deck):
  def __init__(self, card_num):
    super().__init__(card_num)

  def initialize_cards(self):
    print("initialize successful")

  def remove_top_card(self):
    self._cards.pop()
  
  def insert(self, cards):
    self._cards.extend(cards)

class Card:

  def __init__(self, number, card_type):
    self.number = number
    self.card_type = card_type
  
  def playable(self, env):
    raise NotImplementedError


    
  