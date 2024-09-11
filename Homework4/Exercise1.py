#1
# slices =  int(input("how many pieces"))
# friends = slices // 4
# leftover_pizza_slices = slices % 4
#
# print(f"for every friend {friends} slice")
# print(f"leftover slices {leftover_pizza_slices}")

#2
friends: int = int(input("how many friends come?"))
slices: int = int(input("how many pieces order"))
slices_for_friends: int = slices // friends
leftover = slices % friends
print(f"every friend get {slices_for_friends}")
print(f"leftover slices {leftover}")

