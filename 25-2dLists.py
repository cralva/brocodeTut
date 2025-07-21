#2d list (tuple since its faster)
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# will print with parentheses
# for row in num_pad:
#     print(row)


#will print without parentheses
for row in num_pad:
    for num in row:
        print(num, end=" " )
    print()

