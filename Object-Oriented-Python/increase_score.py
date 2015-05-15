class Game:
  def __init__(self):
    self.current_score = [0, 0]

  def score(self, player):
    if player == 1:
      self.current_score[0] += 1  # increase the 1st item in the self.current_score list by 1
    if player == 2:
      self.current_score[1] += 1  # increase the 2nd item in the self.current_score list by 1
