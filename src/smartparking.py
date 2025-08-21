import datetime

# --- Node for the Linked List ---
class CarNode:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.entry_time = datetime.datetime.now()
        self.next = None

# --- Linked List for the Parking Lot ---
class ParkingSpotManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.count = 0

    def park_car(self, license_plate):
        if self.count >= self.capacity:
            print("Sorry, the parking lot is full. No space available.")
            return False
        
        new_car = CarNode(license_plate)
        new_car.next = self.head
        self.head = new_car
        self.count += 1
        print(f"Car with license plate {license_plate} parked successfully.")
        return True

    def unpark_car(self, license_plate):
        current = self.head
        previous = None

        while current:
            if current.license_plate == license_plate:
                # Found the car, remove it
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                
                self.count -= 1
                exit_time = datetime.datetime.now()
                duration = exit_time - current.entry_time
                print(f"Car {license_plate} unparked. Duration: {duration}.")
                # Here you can calculate and display the parking fee
                return True
            
            previous = current
            current = current.next
        
        print(f"Car with license plate {license_plate} not found.")
        return False

    def display_status(self):
        print("\n--- Parking Lot Status ---")
        print(f"Capacity: {self.capacity} | Occupied: {self.count} | Free: {self.capacity - self.count}")
        
        if self.count == 0:
            print("The parking lot is empty.")
            return

        current = self.head
        while current:
            print(f"-> Car: {current.license_plate}, Parked at: {current.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
            current = current.next
        print("--------------------------")

# --- Example Usage ---
if __name__ == "__main__":
    lot = ParkingSpotManager(capacity=3)
    
    lot.park_car("ABC-123")
    lot.park_car("XYZ-789")
    lot.display_status()

    lot.park_car("LMN-456")
    lot.display_status()

    # Try to park in a full lot
    lot.park_car("FULL-001")

    # Unpark a car
    lot.unpark_car("XYZ-789")
    lot.display_status()

    # Park a new car after a slot is freed
    lot.park_car("NEW-CAR")
    lot.display_status()
