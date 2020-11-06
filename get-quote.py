import random
def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd], end = '')
  print(quotes[rnd], end = '')

if __name__== "__main__":
  main()
