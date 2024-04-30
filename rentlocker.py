#Test Case: TestLockerRental
#Purpose: Test if guest can successfully pay for locker rental
#Setup: Specify either True or False for Payment. If true return the locker code with the locker number. If false ask user to enter different payment method and try again.
#Test:
#1. Specify mock locker number, mock code,  and either True or False for payment success.
#2. Call TestLockerRental().
#3. Confirm Locker number and code are returned if Paymentsuccess is True.

import unittest

class LockerRentalSystem:
    def rentlocker(guest, lockernumber, paymentsuccess, code):
        if paymentsuccess == "True":
            print("Locker " + lockernumber + " rented. Code is " + code)
            return "Locker Rented!", True
        else :
            print("Payment unable to be processed. Try again or with another payment method.")
            return "Failed", False
class TestLockerRental(unittest.TestCase):
    def setUp(guest):
        guest.rent_system = LockerRentalSystem()
        guest.lockernumber = "1234"
        guest.paymentsuccess = "True"
        guest.code = "11111"

    def testlockerrent(guest):
        message, status = guest.rent_system.rentlocker(guest.lockernumber,guest.paymentsuccess, guest.code)
        #guest.assertTrue(status)
        guest.assertEqual(message, "Locker Rented!")

    
if __name__ == '__main__':
    unittest.main()
