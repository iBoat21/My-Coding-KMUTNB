class MyBag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"[Bag] Added: {item}")

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"[Bag] Removed: {item}")
        else:
            print(f"[Bag] Error: '{item}' not found in bag.")

    def show(self):
        item_str = [str(x) for x in self.items]
        print(f"[Bag Contents ({len(self.items)} items)]: " + ", ".join(item_str))


class MyQueue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"[Queue] Enqueued: {item}")

    def remove(self):
        if len(self.items) > 0:
            removed_item = self.items.pop(0)
            print(f"[Queue] Dequeued (Front): {removed_item}")
            return removed_item
        else:
            print("[Queue] Error: Queue is empty.")
            return None

    def show(self):
        item_str = [str(x) for x in self.items]
        print(f"[Queue Front -> Rear]: " + " -> ".join(item_str))


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Student({self.name}, {self.score})"

if __name__ == "__main__":
    print("=== 1. Testing myBag with Integers ===")
    bag = MyBag()
    bag.add(10)
    bag.add(20)
    bag.add(10)
    bag.show()
    bag.remove(20)
    bag.show()

    print("\n=== 2. Testing myQueue with Any Objects ===")
    queue = MyQueue()
    s1 = Student("Somchai", 85)
    s2 = Student("Wichai", 92)
    s3 = Student("Anong", 78)

    queue.add(s1)
    queue.add(s2)
    queue.add(s3)
    queue.show()

    queue.remove()
    queue.show()