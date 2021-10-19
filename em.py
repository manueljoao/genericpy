import random

lodd = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23)
hodd = (25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49)
leven = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24)
heven = (26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50)
stars = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

lo = (random.sample(lodd, k = 2))
le = (random.sample(leven, k = 1))
ho = (random.sample(hodd, k = 1))
he = (random.sample(heven, k = 1))
st = (random.sample(stars, k = 2))

print("Numbers:", sorted(lo + le + ho + he))
print("Stars:", sorted(st))