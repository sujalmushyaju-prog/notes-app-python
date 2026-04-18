import os

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("✅ Note saved!")

def view_notes():
    if not os.path.exists(FILE_NAME):
        print("No notes yet.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No notes yet.")
    else:
        print("\n📌 Your Notes:")
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line}", end="")

def delete_note():
    if not os.path.exists(FILE_NAME):
        print("No notes to delete.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No notes to delete.")
        return

    view_notes()
    try:
        num = int(input("\nEnter note number to delete: "))
        if 1 <= num <= len(lines):
            lines.pop(num - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(lines)

            print("🗑️ Note deleted!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def edit_note():
    if not os.path.exists(FILE_NAME):
        print("No notes to edit.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No notes to edit.")
        return

    view_notes()
    try:
        num = int(input("\nEnter note number to edit: "))
        if 1 <= num <= len(lines):
            new_note = input("Enter new note: ")
            lines[num - 1] = new_note + "\n"

            with open(FILE_NAME, "w") as file:
                file.writelines(lines)

            print("✏️ Note updated!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def clear_notes():
    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")
        print("All notes cleared!")
    else:
        print("Cancelled.")

# MAIN LOOP
while True:
    print("\n==== Notes App ====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Edit Note")
    print("5. Clear All Notes")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        clear_notes()
    elif choice == "6":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")