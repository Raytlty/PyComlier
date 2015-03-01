__author__ = 'Benco'
from Scanner import *

def test_scanner():
   test_scanner=Scanner(filename='a.txt')
   print(len(test_scanner.items))
   for item in test_scanner.items:
       print(item)

if __name__ == '__main__':
   test_scanner()



