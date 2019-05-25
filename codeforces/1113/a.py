def _func(remained_cities, max_tank_value, cur_city_number, cur_tank_value, spend_money):
    # print(f"remained_cities={remained_cities}; max_tank_value={max_tank_value}; cur_city_number={cur_city_number}; cur_tank_value={cur_tank_value}; spend_money={spend_money}")
    if remained_cities == 0:
        return spend_money
    else:
        if remained_cities > cur_tank_value:
            bay_liters = min(remained_cities, max_tank_value) - cur_tank_value
        else:
            bay_liters = 0

        return _func(
            remained_cities=remained_cities - 1,
            max_tank_value=max_tank_value,
            cur_city_number=cur_city_number + 1,
            cur_tank_value=cur_tank_value + bay_liters - 1,
            spend_money=spend_money + bay_liters * cur_city_number
        )


def func(n, v):
    return _func(
        remained_cities=n-1,
        max_tank_value=v,
        cur_city_number=1,
        cur_tank_value=0,
        spend_money=0
    )


print(f"{func(4, 2)} 4")
print(f"{func(7, 6)} 6")
print(f"{func(6, 3)} 8")

# input_str = input().split(' ')
# n, v = map(lambda _: int(_), input_str)
# print(func(n, v))
