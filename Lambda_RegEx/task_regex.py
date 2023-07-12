"""
We have a list of mock trade ids that need to be processed, so that we
extract the date string from each id
"""
import re

trade_ids = [
    "ghjd-gfjv-20220615-12345",
    "vbfd-dusi-20181103-11111",
    "pomm-xxsa-20041222-22222",
]

regex = "\w{4}-\w{4}-(\d{8})-\d{4}"
pattern = re.compile(regex)

print(pattern)

for trade_id in trade_ids:
    match = pattern.search(trade_id)
    if match:
        print(match.group(1))

result = [pattern.search(_id).group(1) for _id in trade_ids]
print(result)

