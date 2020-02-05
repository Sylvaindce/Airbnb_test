def consecutive(num):
    result = 0

    for i in range(1, num + 1):
        j = (num - (i * (i + 1)) / 2) / i
        if j - int(j) == 0.0:
            result += 1
        if i * (i + 1) > (2 * num) - 1:
            break
    return result - 1


if __name__ == "__main__":
    print(consecutive(10))