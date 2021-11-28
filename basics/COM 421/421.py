# create class
class repair:
    def __init__(self, customer_name, item_type, description):
        self.customer_name = customer_name
        self.item_type = item_type
        self.description = description

    # create a new list item
    def create(repairs):
        new_repair = repair()
        print("Please enter the customers name")
        new_repair.customer_name = input
        print("Please enter the item type")
        new_repair.item_type = input
        print("Please enter the repair description")
        new_repair.description = input
        repairs.append()
        return repairs

    # function to sort list by customer name
    def sort(list):
        for i in range(len(list)):
            for j in range(len(list) - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]

        return list

    # function to enable user to search all items under a customer name
    def search_by_name(list):
        print("Please enter customer name")
        customer_name = input
        temp_list = []
        for repair in range(list):
            if customer_name == repair.customer_name:
                temp_list.append(repair)
        print("{temp_list}")

    # function to display all of one type of item, sorted by customer name
    def search_by_item(list):
        temp_list = []
        print("Please enter an item type")
        item_type = input
        for repair in range(list):
            if item_type == repair.item_type:
                temp_list.append(repair)
        repair.sort(temp_list)
        print("{temp_list}")

    # function to display whole list, sorted by customer name
    def display_list(list):
        repair.sort(list)
        print({list})

    # function to delete an item once repaired
    def delete(list):
        customer_name = ""
        print("Please enter the customer name")
        customer_name = input
        print("Please enter item type")
        item_type = input
        for repair in list:
            if customer_name == repair.customer_name and item_type == repair.item_type:
                list.remove(repair)


def run():
    repairs = []
    print("Please select a function")
    selection = int(input("1. Repairs menu\n"))
    if selection == 1:
        print("Repairs Menu:1.Create 2.Search by name 3.Search by item 4.Display all 5.Complete Repair")
        sub_selection = input
        if sub_selection == 1:
            repairs = repair.create(repairs)
        elif sub_selection == 2:
            repair.search_by_name(repairs)
        elif sub_selection == 3:
            repair.search_by_item(repairs)
        elif sub_selection == 4:
            repair.display_list(repairs)
        elif sub_selection == 5:
            repair.delete(repairs)
        else:
            print("WHAAAAAAAAAAT")
    else:
        print("Wrong")


run()




