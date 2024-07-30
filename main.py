from device_inventory import Inventory

####################################################Main#################################################
def main():
    print("\n")
    print_ui("Version")
    while True:
        print("\n")
        print_ui("Home")
        print("\n")
        print("Please enter option: ", end=" ")
        user_input = input().strip()
        #Access the inventory documents
        if user_input == "1":
            inventory_object = Inventory()
            inventory_object.main_inventory()
    
        #elif user_input == "2":
            #section = "_Configuration Files_"
            
        #quit the main program
        elif user_input == "Q" or user_input == "q":
            break

            
#################################################Functions##############################################

#***************************************************************************# 
# Type: Helper Function 
# Function Name: Print UI
# Parameters: setcion_title
# Returns: n/a
#
#***************************************************************************#
def print_ui(section_title):
    try:    
        file = open("UI/UI-Home.txt", 'r')
        in_section = False
        i = 0
        for line in file:
            if section_title in line:
                in_section = True

            if in_section:
                print(line, end="") 

                if line.strip().endswith("#"):
                    i += 1

                if i == 3: 
                    break
        
        file.close()

    except FileNotFoundError:
        print("File not found.")

#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#

if __name__ == "__main__":
    main()
    
