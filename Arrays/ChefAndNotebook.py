""" Chef likes to write poetry. Today, he has decided to write a X pages long poetry, but unfortunately his notebook has only Y pages left in it. 
Thus he decided to buy a new CHEFMATE notebook and went to the stationary shop. 
Shopkeeper showed him some N notebooks, where the number of pages and price of the ith one are Pi pages and Ci rubles respectively. 
Chef has spent some money preparing for Ksen's birthday, and then he has only K rubles left for now.
Chef wants to buy a single notebook such that the price of the notebook should not exceed his budget and he is able to complete his poetry.
Help Chef accomplishing this task. You just need to tell him whether he can buy such a notebook or not.
Note that Chef can use all of the Y pages in the current notebook, and Chef can buy only one notebook because Chef doesn't want to use many notebooks. """

""" Input
The first line of input contains an integer T, denoting the number of test cases. Then T test cases are follow.
The first line of each test case contains four space-separated integers X, Y, K and N, described in the statement.
The ith line of the next N lines contains two space-separated integers Pi and Ci, denoting the number of pages and price of the ith notebook respectively. """

import array, math

#X 3 1 2 2
poetry_length = 3 #X
pages_remaining = 1 #Y
money_left = 2 #K
num_of_notebooks = 2 #N
pages_required = poetry_length - pages_remaining
for notebook in range(num_of_notebooks):
  notebook_spec = [int(i) for i in input().split()]
  num_of_pages = notebook_spec[0]
  price_of_notebook = notebook_spec[1]
  print("Hello", num_of_pages, price_of_notebook)
  if num_of_pages >= pages_remaining and price_of_notebook <= money_left:
      print("Lucky")
  else:
      print("Unlucky")