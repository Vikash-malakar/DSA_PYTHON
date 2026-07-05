
def num_water_bottles(num_bottles, num_exchange):
    total = num_bottles
    empty = num_bottles

    while empty >= num_exchange:
        new_bottles = empty // num_exchange
        total += new_bottles
        empty = empty % num_exchange + new_bottles

    return total


# Example usage
if __name__ == "__main__":
    num_bottles = int(input("Enter number of full bottles: "))
    num_exchange = int(input("Enter number of empty bottles needed to exchange: "))
    
    result = num_water_bottles(num_bottles, num_exchange)
    print(f"Total bottles you can drink: {result}")