def format_list(items):
    if len(items) == 0:
        return ""

    if len(items) == 1:
        return items[0]

    if len(items) == 2:
        return f"{items[0]} and {items[1]}"

    last_item = items[-1]
    others = ", ".join(items[:-1])
    return f"{others} and {last_item}"

def how_many():
    num_items = int(input("How many items would you like to enter? "))
    items = []

    for i in range(num_items):
        item = input(f"Enter item {i + 1}: ")
        items.append(item)

    formatted_list = format_list(items)
    print("Formatted list:")
    print(formatted_list)
