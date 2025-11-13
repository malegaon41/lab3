def fractional_knapsack():
    # Safe input function for float
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

    # Safe input function for integer
    def get_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ Invalid input. Please enter an integer.")

    print("=== Fractional Knapsack Problem ===\n")

    # Step 1: Input
    n = get_int("Enter the number of items: ")
    items = []

    print("Enter the weight and profit for each item:")
    for i in range(n):
        weight = get_float(f"Weight of item {i+1}: ")
        profit = get_float(f"Profit of item {i+1}: ")
        if weight == 0:
            print("❌ Weight cannot be zero. Skipping this item.")
            continue
        density = profit / weight
        items.append({
            'item': i + 1,
            'profit': profit,
            'weight': weight,
            'density': density
        })

    capacity = get_float("\nEnter the capacity of the knapsack: ")

    if capacity <= 0:
        print("❌ Knapsack capacity must be greater than 0.")
        return

    # Step 2: Show profit densities
    print("\nStep 1: Calculate profit density (profit / weight) for each item:")
    for item in items:
        print(f"Item {item['item']}: Profit = {item['profit']}, "
              f"Weight = {item['weight']}, Density = {item['density']:.2f}")

    # Step 3: Sort by profit density
    items.sort(key=lambda x: x['density'], reverse=True)

    print("\nStep 2: Sort items by profit density (descending):")
    for item in items:
        print(f"Item {item['item']} - Profit: {item['profit']}, Weight: {item['weight']}, Density: {item['density']:.2f}")

    # Step 4: Greedy selection
    total_profit = 0
    remaining_capacity = capacity

    print("\nStep 3: Select items to maximize profit:")
    for item in items:
        if remaining_capacity == 0:
            break

        if item['weight'] <= remaining_capacity:
            # Take full item
            print(f"✔ Taking FULL Item {item['item']} (Weight: {item['weight']}, Profit: {item['profit']})")
            total_profit += item['profit']
            remaining_capacity -= item['weight']
        else:
            # Take partial item
            fraction = remaining_capacity / item['weight']
            taken_profit = item['profit'] * fraction
            print(f"✔ Taking {fraction:.2f} of Item {item['item']} "
                  f"(Weight taken: {remaining_capacity:.2f}, Profit gained: {taken_profit:.2f})")
            total_profit += taken_profit
            remaining_capacity = 0

        print(f"  ➤ Remaining Capacity: {remaining_capacity:.2f}")

    # Final result
    print("\n✅ Final Result:")
    print(f"Total Profit: {total_profit:.2f}")
    print(f"Remaining Capacity: {remaining_capacity:.2f}")


# Run the program
fractional_knapsack()
