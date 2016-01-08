SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

def print_dorky_line():
    """print dorky line as fancy style"""
    print "*" * DORKY_LINE_LENGTH
    return

print_dorky_line()

def print_sales_summary(melon_type, melon_price):
    """given the melon type, counts the amounts that were sold"""
    the_file = open("orders-by-type.txt")
    melon_sold = 0
    #total_sold = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    for line in the_file:
        data = line.split("|")
        if data[1] == melon_type:
            melon_sold += int(data[2])
        #total_sold[melon_type] += melon_count 
    the_file.close()

    """calculates and prints the revenus for each type"""
    #melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    revenue = melon_sold * melon_price
    # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
    print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_sold, melon_type, melon_price, revenue)

print_sales_summary("Musk", 1.15)
print_sales_summary("Hybrid", 1.30)
print_sales_summary("Watermelon", 1.75)
print_sales_summary("Winter", 4.00)

print_dorky_line()
# print "******************************************"

def print_online_vs_phone():
    """separates and compares online sales and phone sales"""
    the_file = open("orders-with-sales.txt")
    sales = [0, 0] 
    #first number is online sales sum, second is phone sales. 

    for line in the_file:
        data = line.split("|")
        if data[2] == "ONLINE":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
    print "Internet sales generated ${:.2f} in revenue.".format(sales[0])

    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

print_online_vs_phone()

print_dorky_line()
# print "******************************************"
