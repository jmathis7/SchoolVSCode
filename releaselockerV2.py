#Test Case: ReleaseLocker
#Purpose: Test if guest can successfully release locker if done using. Locker code will be reset on locker.
#Setup: Specify locker release as true and return success if locker code reset.
#Test:
#1. Specify locker number and current code.
#2. Call TestLockerRelease().
#3. Confirm Locker number and code are a match.
#4. Remove/clear user code from locker.
#5. Notify user of successful clearing of code.

import unittest

class LockerRentalSystem:
    def rentlocker(guest, lockernumber, code, lcode):
        if code == lcode:
            #This is where we would call method to clear existing code on locker
            print("Locker " + lockernumber + " has been released.")
            return "Locker Released!", True
        else :
            print("Code doesn't match. Try again.")
            return "Failed", False

class LockerObject: #Existing code retrieved from locker itself.
    lcode = "11111"

class TestLockerRelease(unittest.TestCase):
    def setUp(guest):
        guest.rent_system = LockerRentalSystem()
        guest.lockernumber = "1234"
        guest.code = "11111"

    def testlockerrent(guest):
        message, status = guest.rent_system.rentlocker(guest.lockernumber, guest.code, LockerObject.lcode)
        #guest.assertTrue(status)
        guest.assertEqual(message, "Locker Released!")

    
if __name__ == '__main__':
    unittest.main()
