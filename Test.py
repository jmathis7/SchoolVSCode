import unittest
import time

class LockerRentalSystem:
    def __init__(self, lockernumber, accesscode):
        self.lockernumber = lockernumber
        self.accesscode = accesscode
        self.failed_attempts = 0

    def unlocklocker(self, entered_code):
        if entered_code == self.accesscode:
            print("Locker Successfully Unlocked!")
            return True
        else:
            self.failed_attempts += 1
            print("Code is invalid. Please try again.")
            if self.failed_attempts >= 3:
                print("Failed to unlock the locker after 3 attempts. Please contact support for assistance. System will be locked for 5 seconds.")
                time.sleep(5)
                return False
            return False

    def process_payment(self, payment_data):
        if payment_data.isdigit() and len(payment_data) == 8:
            print("Payment processed successfully.")
            return True
        else:
            print("Credit card data is invalid. Please try again.")
            return False

    def apply_coupon(self, coupon_code):
        if coupon_code == "valid":
            print("Coupon code applied successfully.")
            return True
        else:
            print("Coupon code is invalid.")
            return False

    def release_locker(self):
        release_success = True  # Assume release is successful
        if release_success:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            print("Locker released successfully at {}.".format(timestamp))
            return True
        else:
            # Retry releasing locker for several hours
            for _ in range(3):  # Retry for 3 hours
                time.sleep(3600)  # Sleep for 1 hour
                release_success = True  # Assuming release succeeded after retry
                if release_success:
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                    print("Locker released successfully at {}.".format(timestamp))
                    return True
            print("Failed to release locker. Please contact support for assistance.")
            return False

# Example usage:
if __name__ == '__main__':
    lockernumber = input("Enter locker number: ")
    accesscode = input("Enter access code: ")
    rent_system = LockerRentalSystem(lockernumber, accesscode)

        # Applying coupon
    coupon_code = input("Enter coupon code (valid/invalid): ")
    rent_system.apply_coupon(coupon_code)
    
    # Processing payment loop
    while True:
        payment_data = input("Enter credit card data (8 digits): ")
        if rent_system.process_payment(payment_data):
            break  # Break the loop if the credit card data is valid

    # Unlocking locker loop
    while True:
        entered_code = input("Enter code to unlock locker: ")
        if rent_system.unlocklocker(entered_code):
            break  # Break the loop if the code is correct
    
    # Releasing locker
    rent_system.release_locker()