#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #find max difference between smallest and largest prices, so we should loop through the array

  for i in range(0, len(prices)-1):
    price = prices[i]


    return maxprofit

  #max profit = some price by another price that comes before it (it can't come after it)

print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))