#1  choice random number given range
'''
import random

for i in range(4):
     print(random.randint(1, 50))
'''

#2  name from given list
'''
import random

members = ["Rakib", "Anik", "Sifat", "Sakib"]
leader = random.choice(members)
print(leader)
'''

#exercise
#pic 2 numbers from dice and print it like (1, 2) (3, 1)
'''
import random

class dice:
     def roll(self):
          first = random.randint(1, 6)
          second = random.randint(1, 6)
          return (first, second)


dice = dice()
print(dice.roll())
'''

#we will work here with directory
#1
'''
from pathlib import Path

path = Path("ecommerce")
print(path.exists())    #we can check existance of a directory


#2
from pathlib import Path

path = Path("email")
print(path.mkdir())      #we can make directory

#2
from pathlib import Path

path = Path("email")
print(path.rmdir())      #we can remove directory

'''

#we can show all files in current directory

from pathlib import Path

path = Path()
for file in path.glob("*.py"):   #we can also show all file,director ("*") with this
    print(file)