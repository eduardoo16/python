from datetime import datetime
import time


from parking import Parking
from registry import Registry

company_name = "-Edu's Parking-"
print("========================================")
print("Welcome to {}, register a car.".format(company_name))
print("========================================")
license_plate = input("[+] Enter license plate of car: ")
print("License plate registered: {}".format(license_plate))


parking = Parking(company_name, 10)
registry1 = Registry(datetime.now(), license_plate)
parking.add_registry(registry1)
time.sleep(1)


license_plate = input("[+] Enter license plate of car: ")
print("License plate registered: {}".format(license_plate))
registry2=Registry(datetime.now(), license_plate)
parking.add_registry(registry2)
time.sleep(5)
registry2.out_time()
registry1.out_time()

parking.generate_receive()

