def main():
    data = "8982374987239873294873294879823749872349872394872398472398472398749876564638238"
    price = data[23:28]
    amount = data[31:33]

    print(price, amount)

    PRICE = slice(23, 28)
    AMOUNT = slice(31, 33)

    price = data[PRICE]
    amount = data[AMOUNT]

    print(price, amount)


if __name__ == '__main__':
    main()