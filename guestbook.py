import sys
import json
import os


GUESTBOOK_FILE = "guestbook.json"


def load_guestbook():
    if not os.path.exists(GUESTBOOK_FILE):
        return []
    with open(GUESTBOOK_FILE, "r") as file:
        return json.load(file)


def save_guestbook(guestbook):
    with open(GUESTBOOK_FILE, "w") as file:
        json.dump(guestbook, file)


def new_entry(note):
    guestbook = load_guestbook()
    guestbook.append(note)
    save_guestbook(guestbook)


def list_entries():
    guestbook = load_guestbook()
    for i, note in enumerate(guestbook, 1):
        print(f"{i}. {note}")


def edit_entry(index, note):
    guestbook = load_guestbook()
    if index > 0 and index <= len(guestbook):
        guestbook[-index] = note
        save_guestbook(guestbook)


def delete_entry(index):
    guestbook = load_guestbook()
    if index > 0 and index <= len(guestbook):
        del guestbook[-index]
        save_guestbook(guestbook)


def export_guestbook():
    guestbook = load_guestbook()
    print(json.dumps(guestbook, indent=4))


def main():
    if len(sys.argv) < 2:
        print("Usage: guestbook.py [command] [arguments]")
        return

    command = sys.argv[1]
    if command == "new":
        if len(sys.argv) < 3:
            print("Usage: guestbook.py new [note]")
        else:
            note = " ".join(sys.argv[2:])
            new_entry(note)
            print("New note added to the guestbook.")
    elif command == "list":
        list_entries()
    elif command == "edit":
        if len(sys.argv) < 4:
            print("Usage: guestbook.py edit [index] [note]")
        else:
            try:
                index = int(sys.argv[2])
                note = " ".join(sys.argv[3:])
                edit_entry(index, note)
                print(f"Note at index {index} updated.")
            except ValueError:
                print("Invalid index. Please provide a valid integer.")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: guestbook.py delete [index]")
        else:
            try:
                index = int(sys.argv[2])
                delete_entry(index)
                print(f"Note at index {index} deleted.")
            except ValueError:
                print("Invalid index. Please provide a valid integer.")
    elif command == "export":
        export_guestbook()
    else:
        print("Invalid command. Available commands: new, list, edit, delete, export")


if __name__ == "__main__":
    main()
