import random

print("\033[35m", "-------> Infinite Dice <----------", "\033[0m")
print("\033[34m", "        ----------------", "\033[0m")


def crazzy_dise():
  '''this is the crazzy dice many the number of sides which are given
  by the user and same number of sides are == in all side same number of values
  are there which user had give
  
  Example
  if user had input 46 it mean that throw a dice which are having 46 side
  and all 46 side will have 46 number of dots not less or not more evey 
  side is equal to 46 side
  numberof_sides = number of dots per sides
  
  it's not like a normal dice where we got 6 dice had evey side there is different number
  from 1 to 6'''

  while True:
    side = (input("\n\nHow many side of dice you want to throw ? ---> "))
    if not side.isdigit():
      print("\033[31m",
            "logical errro\nyou can only put integer positive numbers.",
            "\033[0m")
      continue
    print("\033[32m", "\nyou roll the dice of", side, "sides 😮 and got",
          random.randint(1, int(side)), "as number", "\033[0m")
    break

    # else:


# print(crazzy_dise.__doc__)
crazzy_dise()
while True:
  decide = input("\n\n\ndo you want to play again ? ----> ")
  if decide == "yes":
    crazzy_dise()
  elif decide == "no":
    print("\033[35m", "\n-----------> by my buddy 🥲 <-------------", "\033[0m")
    break
  else:
    print("\033[31m", "you can only enter yes or no", "\033[0m")
    continue
