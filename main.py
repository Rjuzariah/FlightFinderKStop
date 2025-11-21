from utils import find_cheapest_price, load_data


def main():
    data = load_data()

    n = data["n"]
    flights = data["flights"]
    src = data["src"]
    dst = data["dst"]
    k = data["k"]

    result = find_cheapest_price(n, flights, src, dst, k)
    print("Cheapest price:", result)
    return result


if __name__ == "__main__":
    main()
