from controllers.AddController import Addcontroller

def add_customer_view():
    while True:
        name = input("Enter the name of product: ")
        description = input('Enter description: ')
        barcode = int(input("Enter barcode: "))
        controller = Addcontroller()
        print(controller.add(name, description, barcode))
        answer = input('Do you want to add on more? yes/no: ')
        if answer == 'yes' or answer == 'y':
            continue
        else:
            break

def get_customers_view():
    controller = Addcontroller()
    print(controller.get_products())

def main():
    answer = int(input("1)Get all customers\n2)Add customers\nChoose 1/2: "))
    if answer == 2:
        add_customer_view()
    elif answer == 1:
        get_customers_view()
    else:
        print("Error")

if __name__ == "__main__":
    main()