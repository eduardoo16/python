import report_generator

from person import Person

class PandemicControl(object):
    def __init__(self, city):
        self.__city = city
        self.__people = []

    @property
    def city(self):
        return self.__city

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, new_value):
        self.__people = new_value

    def print_report(self):
        print(f"----------------------For the City: [{self.__city}]----------------------")
        sick_number = report_generator.get_historical_sicks(people)
        recovered = report_generator.get_recover(people)
        men_sick = report_generator.get_men()
        women_sick = report_generator.get_women()
        kid_sick = report_generator.get_kid()
        young_sick = report_generator.get_young()
        adult_sick = report_generator.get_adult()



        print(f"The number of persons that are sick is [{sick_number}]")
        print(f"The number of persons that are recovered from the sickness is [{recovered}]")
        print(f"The number of persons that are Male is [{men_sick}]")
        print(f"The number of persons that are Female is [{women_sick}]")
        print(f"The number of persons that are Kid's is [{kid_sick}]")
        print(f"The number of persons that are young's is [{young_sick}]")
        print(f"The number of persons that are adult's is [{adult_sick}]")

        print("******************************************************************")

        person1.is_sick = False
        person3.is_sick = False
        person4.is_sick = False
        person5.is_sick = False

        sick_number = report_generator.get_historical_sicks(people)
        recovered = report_generator.get_recover(people)
        men_sick = report_generator.get_men()
        women_sick = report_generator.get_women()
        kid_sick = report_generator.get_kid()
        young_sick = report_generator.get_young()
        adult_sick = report_generator.get_adult()

        men_recovered = report_generator.get_men_recovered()
        women_recovered = report_generator.get_women_recovered()
        kid_recovered = report_generator.get_kid_recovered()
        young_recovered = report_generator.get_young_recovered()
        adult_recovered = report_generator.get_adult_recovered()

        print(f"The number of persons that are sick is [{sick_number}]")
        print(f"The number of persons that are recovered from the sickness is [{recovered}]")
        print(f"The number of persons that are Male is [{men_sick}]")
        print(f"The number of persons that are Female is [{women_sick}]")
        print(f"The number of persons that are Kid's is [{kid_sick}]")
        print(f"The number of persons that are young's is [{young_sick}]")
        print(f"The number of persons that are adult's is [{adult_sick}]")

        print(f"The number of persons that are Male and recovered is [{men_recovered}]")
        print(f"The number of persons that are Female and recovered is [{women_recovered}]")
        print(f"The number of persons that are Kid's and recovered is [{kid_recovered}]")
        print(f"The number of persons that are young's and recovered is [{young_recovered}]")
        print(f"The number of persons that are adult's and recovered is [{adult_recovered}]")
        print(self.__people)


person1 = Person("name1", "last_name1", 14, "Male", 123)
person2 = Person("name2", "last_name2", 30, "Female", 154)
person3 = Person("name3", "last_name3", 30, "Male", 125)
person4 = Person("name4", "last_name4", 18, "Male", 126)
person5 = Person("name5", "last_name5", 21, "Female", 127)
person6 = Person("name6", "last_name6", 68, "Male", 128)
person7 = Person("name7", "last_name7", 78, "Female", 129)
person8 = Person("name8", "last_name8", 58, "Male", 120)

person1.is_sick = True
person2.is_sick = True
person3.is_sick = True
person4.is_sick = True
person5.is_sick = True
person6.is_sick = True
person7.is_sick = True

people = [person1, person2, person3, person4, person5, person6, person7, person8]

p = PandemicControl("Cbba")
p.people = people
p.print_report()