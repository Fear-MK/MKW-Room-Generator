import random
import math

def distribution(x, y):
    a = x//y
    b = x%y
    r = [a+1]*b + [a]*(y-b)
    return r

f=open("players.txt", "r", encoding="utf-8")
all_players=f.read().split("\n")
player_amount=len(all_players)

room_string=""

if player_amount%12 != 0:
    invalid_room_str=input(f"Invalid amount of players, you have {str(player_amount%12)} extra. Please type in the room sizes manually: ")
    room_sizes=[int(x) for x in invalid_room_str.split(", ")]
else:
    room_sizes=[]
    for x in range(1, (player_amount//12)+1):
        room_sizes.append(12)


hosts=[]
for player in all_players:
    if "host" in player.split(" ")[-1]:
        hosts.append(player)

all_players=[el for el in all_players if el not in hosts]

host_distribution=distribution(len(hosts), len(room_sizes))

for x in range(0, len(room_sizes)):
    room_sizes[x]-=host_distribution[x]

for x in range(0,len(room_sizes)):
    hosts_in_room=random.sample(hosts, host_distribution[x])
    hosts=[el for el in hosts if el not in hosts_in_room]
    non_hosts_in_room=random.sample(all_players, room_sizes[x])
    all_players=[el for el in all_players if el not in non_hosts_in_room]
    non_hosts_in_room="\n".join(non_hosts_in_room)
    hosts_in_room="\n".join(hosts_in_room) #I have to add a separate line for this due to how f strings work and that I have to store the players
    room=f"\nROOM {str(x+1)}\n\n{hosts_in_room}\n{non_hosts_in_room}"
    print(room)