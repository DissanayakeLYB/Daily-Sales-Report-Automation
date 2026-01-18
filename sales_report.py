entries = []

with open("./sales.txt", "rt") as filename:
    for line in filename:
        new_line = line[:-1] # to remove escape character
        new_line = new_line.split(",")
        entries.append(new_line)


# structure -> item, no. sold, revenue from that item
item_summary = dict()

for entry in entries:
    item = entry[0]
    number_sold = int(entry[1])
    item_price = float(entry[2])
    revenue = number_sold*item_price

    if ( item not in item_summary.keys() ):
        item_summary[item] = [number_sold, revenue]
    else:
        number_sold += item_summary[item][0] 
        revenue = number_sold*item_price
        item_summary[item] = [number_sold, revenue]

max_sold_item = ""
max_number_items_sold = 0
total_revenue = 0

for (key, value) in item_summary.items():
    item_name = key
    number_sold = value[0]
    item_revenue = value[1]

    if number_sold > max_number_items_sold:
        max_sold_item = item_name
        max_number_items_sold = number_sold

    # calculate total revenue
    total_revenue += item_revenue


output_line_1 = "Total Revenue: " + str(total_revenue) + "\n\n"

output_line_3 = "\nBest Selling Item by quantity: " + str(max_sold_item) + " (" + str(max_number_items_sold) + " units sold)\n\n"

with open("./daily_report.txt", "wt") as output_file:
    output_file.write(output_line_1)
    output_file.write("Item Summary:\n")
    for (key, value) in item_summary.items():
        output_file.write(f"{key} -> Quantity Sold: {value[0]} | Revenue: {value[0]*value[1]}\n")
    output_file.write(output_line_3)

print(output_line_1)
for (key, value) in item_summary.items():
        print(f"{key} -> Quantity Sold: {value[0]} | Revenue: {value[0]*value[1]}\n")
print(output_line_3)

# add the output details to the daily_report.txt