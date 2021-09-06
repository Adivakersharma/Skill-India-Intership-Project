# importing json package
import json
import os


def line():
    print("~"*50)


while(1):
    os.system("cls")  # To clear previos outptut
    os.system("color 09")  # changes color of output window
    line()
    print("\tINVENTORY MANAGEMENT SYSTEM")
    line()
    print("\t\tMENU")
    print("\n\t1.View available Products")
    print("\t2.Update Existing/New Products")
    print("\t3.Puchase any Products")
    print("\t4.View Sales of the Products")
    print("\t5.Exit")
    choice = int(input("\n\tEnter Your Choice : "))

    # To Exit
    if(choice == 5):
        print("\n\tStore Exited !!")
        break

    # For See the Product
    os.system("cls")
    if(choice == 1):
        file = open("record.json", 'r')
        data = file.read()
        record = json.loads(data)
        print("\t\t\t\tPRODUCT LIST")
        print("\n\t\t%-15s %-20s %-15s %-10s" %
              ("Product Id:", "Product Name:", "Price:", "Quantity:"))
        for i in record.keys():
            print("\t\t%-15s %-20s %-15f %-10d" %
                  (i, record[i]['name'], record[i]['price'], record[i]['amount']))
        file.close()

    elif(choice == 2):
        file = open("record.json", 'r')
        data = file.read()
        file.close()
        record = json.loads(data)
        id = input("\t\tEnter product id : ")
        name = input("\t\tEnter name : ")
        pricing = float(input("\t\tEnter price : "))
        product_amt = int(input("\t\tEnter quantity : "))
        record[id] = {'name': name,
                      'price': pricing, 'amount': product_amt}
        all_data = json.dumps(record)
        file = open("record.json", 'w')
        file.write(all_data)
        file.close()

    elif(choice == 3):
        file = open("record.json", 'r')
        data = file.read()
        file.close()
        record = json.loads(data)
        new_id = input("\t\tEnter the product_Id: ")
        new_quantity = int(input("\t\tEnter the quantity: "))
        # For validating the number of product is more or not
        if(record[new_id]['amount'] >= new_quantity):
            print("\n\t\t|Product: ", record[new_id]['name'])
            print("\t\t|Price: ", record[new_id]['price'])
            print("\t\t|Billing Amount: ",
                  record[new_id]['price'] * new_quantity)
            print("\t\t\t|Please Visit Again (*_*) ")
            record[new_id]['amount'] = record[new_id]['amount'] - new_quantity

            file = open("record.json", 'w')
            all_data = json.dumps(record)
            file.write(all_data)
            file.close()

            # Opening sales.json data in read mode
            sales_file = open("sales.json", 'r')
            sales_data = sales_file.read()
            sales_file.close()
            record = json.loads(sales_data)
            record[len(record)+1] = {'name': record[new_id]['name'],
                                     'price': record[new_id]['price'], 'amount': new_quantity}
            # Opening sales.json file in writing mode to update the sales product
            sales_file = open("sales.json", 'w')
            all_data_sales = json.dumps(record)
            sales_file.write(all_data_sales)
            sales_file.close()
        else:
            print("\n\t\t Sorry!! We have only " +
                  str(record[new_id]['amount'])+" Product!!")

    # To see the sale.json data
    elif(choice == 4):
        sales_file = open("sales.json", 'r')
        sales_data = sales_file.read()
        record = json.loads(sales_data)
        print("\t\t\tSOLD PRODUCT LIST")
        print("\n\t\t%-15s %-20s %-15s %-10s" %
              ("Product Id:", "Product Name:", "Price:", "Quantity:"))
        for i in record.keys():
            print("\t\t%-15s %-20s %-15f %-10d" %
                  (i, record[i]['name'], record[i]['price'], record[i]['amount']))
        sales_file.close()

    # Invalid Choice
    else:
        print("Invalid Choice!!")

    var = input("\n\t\tPress 0 to return to menu : ")