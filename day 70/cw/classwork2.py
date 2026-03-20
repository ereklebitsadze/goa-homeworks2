def e(y):
    if y % 2 == 0:
        return "ლუწი"
    else:
        return None

random = [1,2,3,4,5,6,6,7,8,9,9,9,0,99,9,9,9,9,9,9,9,12312123,123,123,123,5,123,4,5,5,4]

result = map(e, random)

clean = filter(None, result)

print(list(clean))