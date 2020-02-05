def triangleOrNot(a, b, c):
    results = [None] * len(a)

    for i in range(len(results)):
        if a[i] + b[i] <= c[i] or a[i] + c[i] <= b[i] or b[i] + c[i] <= a[i]:
            results[i] = "No"
            continue
        results[i] = "Yes"
    return results