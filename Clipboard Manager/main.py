#Program allows you to store multiple text on your clipboard
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

#Save text to a json file
def save_text(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

#load the text from a json file
def load_text(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

def main():
    
    print("Welcome to multi-clipboard manager!")
    data = load_text(SAVED_DATA)

    while True:
        command = input("Enter command (save|load|list|clear|delete|quit): ").lower()
        #Save text from clipboard
        if command == "save":
        
            key = input("Enter a key: ")
            data [key] = clipboard.paste()
            save_text(SAVED_DATA,data)
            print("Text Saved...")

        #Load text from clipboard
        elif command == "load":
        
            key = input("Enter a key: ")
            if key in data:
                clipboard.copy(data[key])
                print("Data copied to clipboard...")
            else:
                print("Key not found")

        #List all the data stored
        elif command == "list":
        
            print(data)
        
        #Clear all the data stored
        elif command == "clear":
        
            data = {}
            save_text(SAVED_DATA,data)
            print("Data cleared...")
        
        #Delete a data entry
        elif command == "delete":
            key = input("Enter a key: ")
            if key in data:
                del data[key]
                save_text(SAVED_DATA,data)
                print("Data deleted...")
            else:
                print("Key not found")

        #Quit the program
        elif command == "quit":
            break

        else:
            print("unknown command")

main()