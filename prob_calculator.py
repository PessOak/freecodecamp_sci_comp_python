import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for color in range(value):
        self.contents.append(key) 
  
  def draw(self, num_balls_drawn):
    removed_balls = []
    if num_balls_drawn > len(self.contents):
      return self.contents
    else: 
      for ball in range(num_balls_drawn):
        removed = self.contents.pop(random.randrange(len(self.contents)))
        removed_balls.append(str(removed))
    return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for x in range(num_experiments):
    hat_copy = copy.deepcopy(hat) 
    expected_copy = copy.deepcopy(expected_balls)   
    balls_drawn = hat_copy.draw(num_balls_drawn) 
    count = 0
    for color in balls_drawn:
      if color in expected_copy:
        expected_copy[color] += -1  
    for color in expected_copy.values(): 
      if color <= 0:
        count += 1
    if count == len(expected_copy): 
      success += 1

  draw_chance_prob = success / num_experiments 

  return draw_chance_prob