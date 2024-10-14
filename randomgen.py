# Your first name: Tracy Xing
# Your section:

import random
import matplotlib.pyplot as plt

# Write your functions with their docstrings here

# nextMiddleSquare
def nextMiddleSquare(iSeed):
    # print("nextMiddleSquare:", iSeed)
    iRet = 0
    iSquare = iSeed * iSeed
    sSquare = str(iSquare)
    # If the square is not a four-digit number, insert "0" at the beginning as leading zeros
    if len(sSquare) == 1:
        sSquare = "000" + sSquare
    elif len(sSquare) == 2:
        sSquare = "00" + sSquare
    elif len(sSquare) == 3:
        sSquare = "0" + sSquare

    iRet = int(sSquare[1:3])
    # print("nextMiddleSquare: iSeed =", iSeed, ", iRet =", iRet)
    return iRet

# listMiddleSquare
def listMiddleSquare(iSeed):
    # print("ilistMiddleSquare: iSeed = ", iSeed)
    lList = []
    iMiddleSquare = nextMiddleSquare(iSeed)
    lList.append(iMiddleSquare / 100.0)
    for iIter in range(499):
        iMiddleSquare = nextMiddleSquare(iMiddleSquare)
        lList.append(iMiddleSquare / 100.0)
    return lList
   
# nextLehmer
def nextLehmer(a, m, iRandom):
    return a * iRandom % m

# listLehmer
def listLehmer(iSeed):
    lList = []
    a = 17
    m = 101
    iLehmer = nextLehmer(a, m, iSeed)
    lList.append(iLehmer / float(m))
    for iIter in range(499):
        iLehmer = nextLehmer(a, m, iLehmer)
        lList.append(iLehmer / float(m))
    return lList

# listRandom
def listRandom():
    lList = []
    for iIter in range(500):
        # Generate a random float between 0 and 1 using Mersenne Twister algorithm
        fRandom = random.random()
        lList.append(fRandom)
        # print("random = ", fRandom)
    return lList

def chartRandomNumbers(mid, lehmer, rand):
  '''
  This function draws a histogram of the three lists on the same plot
  :param mid: a list of random numbers from middle squares
  :param lehmer: a list of random numbers from lehmer
  :param rand: a list of random numbers from Python random module
  '''
  multi = [mid, lehmer, rand]
  plt.hist(multi, histtype='bar', label=['middle square', 'lehmer', 'random module'])
  plt.legend(prop={'size': 10})
  plt.show()
  


def main():
  start = 29
  list1 = listMiddleSquare(start)
  list2 = listLehmer(start)
  list3 = listRandom()
  chartRandomNumbers(list1, list2, list3)

if __name__ == "__main__":
  main()
