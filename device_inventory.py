
class Inventory:

#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#    
    def main_inventory(self):
        while True:
            print("\n")
            self.print_inventory_ui("Device Inventory")
            print("\n")
            print("Please enter option: ", end=" ")
            user_input = input().strip()
            #Home
            if user_input == "0":
                break
            #Add
            elif user_input == "1":
                self.add_inventory()
            #Read
            elif user_input == "2":
                self.read_inventory()

            elif user_input == "3":
                self.update_inventory()

            elif user_input == "4":
                self.delete_inventory()
                
            else:
                print("###___Not a valid option___###")

#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def add_inventory(self):
        self.print_inventory_ui("_Add Device_")
        file = open("Device-Inventory/Inventory.txt", "a")
        while True:
            #User entries for device
            print("\n")
            print("Please enter a device name: ", end=" ")
            device_name = input()
            print("Please enter a device model: ", end=" ")
            device_model = input()
            print("Please enter a description: ", end=" ")
            device_description = input()
            print("Please enter an owner: ", end=" ")
            device_owner = input()
            
            print("\n")
            print("Add? Y = Yes, N = No, Q = Quit:")
            user_input = input().strip()
            if user_input == 'y' or user_input == 'Y':
                file.write("\n")
                file.write(f"Device Name: {device_name}\n")
                file.write(f"Device Model: {device_model}\n")
                file.write(f"Device Description: {device_description}\n")
                file.write(f"Device Owner: {device_owner}\n")
                file.write("#" + "="*85 + "#")
                break
            
            elif user_input == 'n' or user_input == 'N':
                continue
            
            elif user_input == 'q' or user_input == 'Q':
                break

            else:
                print("Incorrect entry, try again.")
                continue
    
#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def read_inventory(self):
        while True:
            self.print_inventory_ui("_Read Device_")
            print("\n")
            print("Please enter option: ", end="")
            user_input = input().strip()
            #Home
            if user_input == "0":
                break
            #Search Inventory
            elif user_input == "1":
                self.search_inventory()
            #Print all
            elif user_input == "2":
                file = open("Device-Inventory/Inventory.txt", "r")
                for line in file:
                    print(line, end="")
                
                print("\n")
                file.close()

#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def update_inventory(self):
        while True:
            print("\n")
            self.print_inventory_ui("_Search Device_")
            file = open("Device-Inventory/Inventory.txt", "r")
            file_lines = file.readlines()
            file.close()
            print("\n")
            print("Please enter an option to search for the device you would like to UPDATE: ", end="")
            user_input = input().strip()
            #Home
            if user_input == "0":
                break
            #Device Name
            elif user_input == "1":
                print("\n")
                print("Please enter the name of the device: ", end="")
                search_input = input()
                updated_lines = self.update_algorithm("Device Name:", search_input, file_lines)
            #Device Model 
            elif user_input == "2":
                print("\n")
                print("Please enter the device model: ", end="")
                search_input = input()
                updated_lines = self.update_algorithm("Device Model:", search_input, file_lines)
            #Device Owner
            elif user_input == "3":
                print("\n")
                print("Please enter the owner of the device: ", end="")
                search_input = input()
                updated_lines = self.update_algorithm("Device Owner:", search_input, file_lines)

            if updated_lines == 1:
                continue

            else:
                file_write = open("Device-Inventory/Inventory.txt", "w")
                file_write.writelines(updated_lines)
                file_write.close()

#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def update_algorithm(self, search_parameter, searching_for, file_lines):
        in_section = False #Determines if it is in the section
        eof = True #Determines if it has found the device or not. Automatically end-of-file will be reached unless the file is found
        current_section = [] #Used to store current sections during iteration
        updated_lines = []#Used to store the whole files updated lines
        for current_line in file_lines:
            current_section.append(current_line)
            current_stripped_line = current_line.strip()
            #if the parameter is found
            if search_parameter in current_line:
                #if the name of the device is found
                if searching_for in current_line:
                    in_section = True
                    eof = False
                    continue

            #the end of the correct section
            elif (current_stripped_line.endswith('#') and '=' in current_stripped_line): 
                #if its the section of the device
                if in_section == True: 
                    print("\n###___Device Found___###")
                    for lines in current_section:
                        print(lines, end="")
                    
                    print("\nPlease enter information to update: ")
                    new_name = input("Device Name: ")
                    new_model = input("Device Model: ")
                    new_description = input("Device Description: ")
                    new_owner = input("Device Owner: ")

                    while True:
                        print("\nAre you sure you this is what you want to update it with? Y= yes, N=no: ")
                        abort = input().strip()
                        if abort == 'N' or abort == 'n':
                            return 1
                        
                        elif abort == 'Y' or abort == 'y':
                            break

                        else:
                            print("\nNot an option. Please try again.")

                    updated_section = [
                        f"Device Name: {new_name}\n",
                        f"Device Model: {new_model}\n",
                        f"Device Description: {new_description}\n",
                        f"Device Owner: {new_owner}\n",
                        current_stripped_line + '\n'
                    ]

                    updated_lines.extend(updated_section)
                    in_section = False
                    
                else:
                    updated_lines.extend(current_section)
                    current_section.clear()

        if eof == True:
            print("\n")
            print("###___File Not Found___###")

        return updated_lines

#***************************************************************************# 
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def delete_inventory(self):
        while True:
            print("\n")
            self.print_inventory_ui("_Search Device_")
            file = open("Device-Inventory/Inventory.txt", "r")
            file_lines = file.readlines()
            file.close()
            print("\n")
            print("Please enter an option to search for the device you would like to DELETE: ", end="")
            user_input = input().strip()
            #Home
            if user_input == "0":
                break
            #Device Name
            elif user_input == "1":
                print("\n")
                print("Please enter the name of the device: ", end="")
                search_input = input()
                updated_lines = self.delete_algorithm("Device Name:", search_input, file_lines)
            #Device Model 
            elif user_input == "2":
                print("\n")
                print("Please enter the device model: ", end="")
                search_input = input()
                updated_lines = self.delete_algorithm("Device Model:", search_input, file_lines)
            #Device Owner
            elif user_input == "3":
                print("\n")
                print("Please enter the owner of the device: ", end="")
                search_input = input()
                updated_lines = self.delete_algorithm("Device Owner:", search_input, file_lines)
            
            if updated_lines == 1:
                continue

            else:
                file_write = open("Device-Inventory/Inventory.txt", "w")
                file_write.writelines(updated_lines)
                file_write.close()

#***************************************************************************#
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def delete_algorithm(self, search_parameter, searching_for, file_lines):
        in_section = False #Determines if it is in the section
        eof = True #Determines if it has found the device or not. Automatically end-of-file will be reached unless the file is found
        current_section = [] #Used to store current sections during iteration
        updated_lines = []#Used to store the whole files updated lines
        for current_line in file_lines:
            current_section.append(current_line)
            current_stripped_line = current_line.strip()
            #if the parameter is found
            if search_parameter in current_line:
                #if the name of the device is found
                if searching_for in current_line:
                    in_section = True
                    eof = False
                    continue

            #the end of the correct section
            elif (current_stripped_line.endswith('#') and '=' in current_stripped_line): 
                #if its the section of the device
                if in_section == True: 
                    print("\n###___Device Found___###")
                    for lines in current_section:
                        print(lines, end="")

                    while True:
                        print("\nAre you sure you this is the device you want to DELETE? Y= yes, N=no: ")
                        abort = input().strip()
                        if abort == 'N' or abort == 'n':
                            return 1

                        elif abort == 'Y' or abort == 'y':
                            break
                        else:
                            print("\nNot an option. Please try again.")

                    in_section = False
                    
                else:
                    updated_lines.extend(current_section)
                    current_section.clear()

        if eof == True:
            print("\n")
            print("###___File Not Found___###")

        return updated_lines
        
#***************************************************************************#
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def search_inventory(self):
        print("\n")
        self.print_inventory_ui("_Search Device_")
        while True:
            file = open("Device-Inventory/Inventory.txt", "r")
            print("\n")
            print("Please enter an option to search by: ", end="")
            user_input = input().strip()
            #Home
            if user_input == "0":
                break

            elif user_input == "1":
                print("\n")
                print("Please enter the name of the device: ", end="")
                search_input = input()
                self.search_algorithm("Device Name:", search_input, file)
            
            elif user_input == "2":
                print("\n")
                print("Please enter the device model: ", end="")
                search_input = input()
                self.search_algorithm("Device Model:", search_input, file)

            elif user_input == "3":
                print("\n")
                print("Please enter the owner of the device: ", end="")
                search_input = input()
                self.search_algorithm("Device Owner:", search_input, file)
                
            file.close()

#***************************************************************************#
# Type: 
# Function Name:
# Parameters:
# Returns:
#
#***************************************************************************#
    def search_algorithm(self, search_parameter, searching_for, file):
        in_section = False #Determines if it is in the section
        eof = True #Determines if it has found the device or not. Automatically end-of-file will be reached unless the file is found
        current_section = [] #Used to store the whole section. Only recorded if the device is found
        for current_line in file:
            current_section.append(current_line)
            current_stripped_line = current_line.strip()
            #if the parameter is found
            if search_parameter in current_line:
                #if the name of the device is found
                if searching_for in current_line:
                    in_section = True
                    eof = False
                    continue

            #the end of the correct section
            elif (current_stripped_line.endswith('#') and '=' in current_stripped_line): 
                #if its the section of the device
                if in_section == True: 
                    print("\n")
                    print("###___Device Found___###")
                    for lines in current_section:
                        print(lines, end="")
                    
                    in_section = False
                    current_section.clear()
                    break
                    
                else:
                    current_section.clear()

        if eof == True:
            print("\n")
            print("###___File Not Found___###")

#***************************************************************************# 
# Type: Helper Function 
# Function Name: Print UI
# Parameters: setcion_title
# Returns: n/a
#
#***************************************************************************#
    def print_inventory_ui(self, section_title):
        try:    
            file = open("UI/UI-Inventory.txt", 'r')
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
