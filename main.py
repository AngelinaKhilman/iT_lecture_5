import csv

def main():
    file = open('prices.csv', 'r')
    reader = csv.reader(file)
    table = list(reader)
    table = table[1:]
    table_col = list(zip(*table))
    for i in range(2):
        table_col[i] = list(map(int, table_col[i]))
    table_col[2] = list(map(float, table_col[2]))
    uitem = len(set(table_col[0]))
    ushop = len(set(table_col[1]))
    #1
    print("Number of unique products: ", uitem)
    print("Number of unique stores: ", ushop)
    #2
    a = max(list((table_col[3].count(x), x) for x in set(table_col[3])))[1]
    print("The user with the most approved prices: ", a)
    #3
    print("The number of products sold in each store: ")
    d = {}
    for j in table:
        if int(j[1]) in d:
            d[int(j[1])].append(int(j[0]))
        else:
            d[int(j[1])] = [int(j[0]),]
    for key, value in d.items():
        d[key] = len(set(value))
        print(key, d[key])
    #4
    d = {}
    print("Average cost of each product: ")
    for j in table:
        if int(j[0]) in d:
            d[int(j[0])].append(float(j[2]))
        else:
            d[int(j[0])] = [float(j[2])]
    for key, value in d.items():
        d[key] = sum(value) / len(value)
        print(key, d[key])
    #5
    print("Store with min price: ", table_col[1][table_col[2].index(min(table_col[2]))], "price: ", min(table_col[2]),
          "Product: ", table_col[0][table_col[2].index(min(table_col[2]))])
    print("Store with max price: ", table_col[1][table_col[2].index(max(table_col[2]))], "price: ", max(table_col[2]),
          "Product: ", table_col[0][table_col[2].index(max(table_col[2]))])


if __name__ == "__main__":
    main()
