#!/usr/bin/python

import argparse

def find_max_profit(prices):

  minPrice = prices[0] #min price set to first number in array

  maxProfit = prices[1] - prices[0] #max profit = second number - first number(min number at the moment)

  for i in range(1, len(prices)): #starts at one -> length of array (starting at zero gives me 0)

    if prices[i] < minPrice: #if price at the current index is smaller than the min price that we start with

      minPrice = prices[i] #the new min price is that price at current index, keeps the lowest price to the left of the max price

    elif prices[i] - minPrice > maxProfit: #instead of looking for max price using the max(), we need to find the the number that gives us the largest difference when subtracted from the min price

      maxProfit = prices[i] - minPrice #max profit = max price - min price



  return maxProfit


print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))