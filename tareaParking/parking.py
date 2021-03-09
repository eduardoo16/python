import registry
from datetime import datetime

class Parking:
    def __init__(self,company_name, price_by_hour):
        self.company_name = company_name
        self.price_by_hour = price_by_hour
        self.__registries = []

    def add_registry(self, registry):
        self.__registries.append(registry)

    def generate_receive(self):
        for r in self.__registries:
            self.print_receive(r)

    def print_receive(self, registry):
        print("==================================")
        print("========={}==========".format(self.company_name))
        print("        CHECK FOR PARKING")
        print("           {}".format(datetime.now().strftime("%b %d %Y")))
        print("==================================")
        print("         CAR:  {}".format(registry.license_plate))
        print("FROM:  {}".format(registry.enter_time.strftime("%b %d %Y %H:%M:%S")))
        print("TO:    {}".format(registry.out_time.strftime("%b %d %Y %H:%M:%S")))
        print("          Paid  : {}.00".format(registry.payment(10)))
        print("==================================")
        print("    THANK YOU AND LUCKY ROAD..!!")
        print("==================================")