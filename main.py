from group import Group
from four_groups_compete import FourGroups
import random


# this is just a demo
# the rest part needs finishing by you

# the infomation of different groups
names_four_groups = [[str(100 * i + j) for j in range(10)] for i in range(1, 5)]
ability_four_groups = [[random.random() for _ in range(10)] for _ in range(1, 5)]

# construct four groups and get the qualifiers
groups = [Group(names_four_groups[i], ability_four_groups[i]) for i in range(4)]
info = list(map(lambda x : x.get_qualifier(2), groups))
print(info)

# the rest part
fg = FourGroups(info)
final_info = fg.compete()
print(final_info)