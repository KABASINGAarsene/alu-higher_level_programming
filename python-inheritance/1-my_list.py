#!/usr/bin/python3
class MyList(list):
    """A class that inherits from list and includes a method to print a sorted list."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)  # Sorts the list without modifying the original
        print(sorted_list)

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
