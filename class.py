class Smartphone:
    # Constructor to initialize the Smartphone object
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
    
    # Method to simulate making a call
    def make_call(self, number):
        print(f"Calling {number}...📞")
    
    # Method to send a text message
    def send_text(self, number, message):
        print(f"Sending text to {number}: {message} 📱")
    
    # Method to check battery status
    def check_battery(self):
        print(f"Battery at {self.battery_percentage}% 🔋")
    
    # Method to charge the phone (increases battery percentage)
    def charge(self, charge_amount):
        self.battery_percentage += charge_amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"Charging... Battery is now {self.battery_percentage}%.")

# Subclass demonstrating inheritance and encapsulation
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, camera_megapixels):
        # Call the constructor of the parent class (Smartphone)
        super().__init__(brand, model, battery_percentage)
        self.__camera_megapixels = camera_megapixels  # Private attribute

    # Public method to access the camera megapixels
    def get_camera_info(self):
        return f"{self.model} has a {self.__camera_megapixels}MP camera."

    # Overridden method to simulate making a call with a special feature
    def make_call(self, number):
        print(f"{self.model} calling {number}... 📱 (with enhanced voice clarity!)")
        
    # Method to take a photo (using the camera)
    def take_photo(self):
        print(f"Taking a photo with {self.__camera_megapixels}MP camera... 📸")

# Example usage of the classes
iphone = Smartphone("Apple", "iPhone 13", 80)
iphone.make_call("123-456-7890")
iphone.send_text("123-456-7890", "Hello there!")
iphone.check_battery()

samsung_camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 50, 108)
samsung_camera_phone.make_call("987-654-3210")
samsung_camera_phone.take_photo()
samsung_camera_phone.check_battery()
print(samsung_camera_phone.get_camera_info())
