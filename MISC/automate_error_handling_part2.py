years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
# years.reverse()
#fix this by  using sort
years.sort()
print(years)
#what will happen if you applied wrong assertion/method/logic
assert years[0] <= years[-1], "First element is greater than last element."