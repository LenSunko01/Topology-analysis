def even():
    print("Even")


def odd():
    print("Odd")


j = 3
while j <= 100:
    for i in range(0, 10):
        if i % 2 == 0:
            even()
            j -= 5
        else:
            odd()
            j += 10
    if j < 0:
        break
