def ascend(numbers):
    for b in range(len(numbers)):
        for a in range(len(numbers)-1):
            temp = numbers[a+1]
            if numbers[a] > numbers[a+1]:
                numbers[a+1] = numbers[a]
                numbers[a] = temp
    return numbers


def descend(numbers):
    for b in range(len(numbers)):
        for a in range(len(numbers)-1):
            temp = numbers[a+1]
            if numbers[a] < numbers[a+1]:
                numbers[a+1] = numbers[a]
                numbers[a] = temp
    return numbers


def change(lis):
    a = 0
    list = []
    for b in lis:
        x = str(b)
        list.insert(a, x)
        a += 1
    return list


def type(List):
    numbers = []
    b = 0
    for a in List:
        try:
            a = int(a)
            numbers.insert(b, a)
            b += 1
        except ValueError:
            numbers = change(List)
            return numbers
    return numbers


inp = input('Enter List: ')
List = inp.split(',')
numbers = type(List)
print(f'Ascending Order : {ascend(numbers)}')
print(f'Descending Order: {descend(numbers)}')
