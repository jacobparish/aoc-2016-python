from aocd import lines
from parse import parse
import collections as col
import bisect


transfers = []
outputs = {}
bot_rules = {}
bot_vals = col.defaultdict(list)
outputs = {}


for line in lines:
    if line.startswith("value"):
        val, bot = parse("value {:d} goes to bot {:d}", line)
        transfers.append((val, bot))
    elif line.startswith("bot"):
        src, dst_low_type, dst_low, dst_high_type, dst_high = parse(
            "bot {:d} gives low to {} {:d} and high to {} {:d}", line
        )
        bot_rules[src] = ((dst_low_type, dst_low), (dst_high_type, dst_high))


while transfers:
    val, bot = transfers.pop(0)
    bisect.insort(bot_vals[bot], val)
    if len(bot_vals[bot]) == 2:
        if bot_vals[bot] == [17, 61]:
            p1 = bot
        for (dst_type, dst), dst_data in zip(bot_rules[bot], bot_vals[bot]):
            if dst_type == "bot":
                transfers.append((dst_data, dst))
            elif dst_type == "output":
                outputs[dst] = dst_data


p2 = outputs[0] * outputs[1] * outputs[2]
