deposit = int(input())
years = 0
while 50000 < deposit < 700000:
    deposit += (deposit / 100) * 7.1
    years += 1
print(years)
