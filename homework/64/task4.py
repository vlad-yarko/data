class UserHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def add(self, name, phone):
        index = self.hash(name)
        for i, (n, p) in enumerate(self.table[index]):
            if n == name:
                self.table[index][i] = (name, phone)
                return
        self.table[index].append((name, phone))

    def search(self, name):
        index = self.hash(name)
        for n, p in self.table[index]:
            if n == name:
                return p
        return None

    def delete(self, name):
        index = self.hash(name)
        for i, (n, p) in enumerate(self.table[index]):
            if n == name:
                self.table[index].pop(i)
                return True
        return False

    def list_all(self):
        users = []
        for bucket in self.table:
            for name, phone in bucket:
                users.append((name, phone))
        return users

def main():
    ht = UserHashTable()

    while True:
        print("\n=== User Phone Directory ===")
        print("1. Add user")
        print("2. Search user")
        print("3. Delete user")
        print("4. List all users")
        print("5. Exit")

        choice = input("Select (1-5): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            ht.add(name, phone)
            print(f"Added {name}: {phone}")

        elif choice == '2':
            name = input("Enter name to search: ").strip()
            phone = ht.search(name)
            if phone:
                print(f"{name}: {phone}")
            else:
                print("User not found")

        elif choice == '3':
            name = input("Enter name to delete: ").strip()
            if ht.delete(name):
                print(f"Deleted {name}")
            else:
                print("User not found")

        elif choice == '4':
            users = ht.list_all()
            if users:
                print("\nAll users:")
                for name, phone in sorted(users):
                    print(f"  {name}: {phone}")
            else:
                print("No users")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
