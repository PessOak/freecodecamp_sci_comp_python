class Category:

  def __init__(self, category_name):
    self.category_name = category_name
    self.ledger = []
    self.total = 0

  def __str__(self):
    category_name = self.category_name
    category_str = category_name.center(30, '*')
    for i in self.ledger:
      try:
        ledger_description = i['description'][0:23]
      except TypeError:
        ledger_description = ''

      ledger_amount = str("{:.2f}".format(i['amount']))
      category_str += f"\n{ledger_description:<23}{ledger_amount:>7}"
    category_str += "\nTotal: " + str(self.get_balance())
    return category_str

  def deposit(self, amount, description=""):
    self.total += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return self.total

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.total -= amount
      self.ledger.append({
        "amount": -amount,
        "description": "Transfer to " + category.category_name
      })
      category.total += amount
      category.ledger.append({
        "amount":
        amount,
        "description":
        "Transfer from " + self.category_name
      })
      return True
    return False

  def check_funds(self, amount):
    if amount <= self.total:
      return True
    return False


def create_spend_chart(categories):
  spent_dict = {}
  for i in categories:
    s = 0
    for j in i.ledger:
      if j['amount'] < 0:
        s += abs(j['amount'])
    spent_dict[i.category_name] = round(s, 2)
  total = sum(spent_dict.values())
  percent_dict = {}
  for k in spent_dict.keys():
    percent_dict[k] = int(round(spent_dict[k] / total, 2) * 100)
  output = 'Percentage spent by category\n'
  for i in range(100, -10, -10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percent_dict.values():
      if percent >= i:
        output += 'o  '
      else:
        output += '   '
    output += '\n'
  output += ' ' * 4 + '-' * (len(percent_dict.values()) * 3 + 1)
  output += '\n     '
  dict_key_list = list(percent_dict.keys())
  max_len_category = max([len(i) for i in dict_key_list])

  for i in range(max_len_category):
    for name in dict_key_list:
      if len(name) > i:
        output += name[i] + '  '
      else:
        output += '   '
    if i < max_len_category - 1:
      output += '\n     '

  return output