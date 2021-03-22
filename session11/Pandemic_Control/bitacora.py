class Bitacora(object):
    def __init__(self):
        self.__people_sick = []
        self.__people_recovered = []
        self.__people_helthy = []
        self.__registried_people = []

    def add_sick_person(self, person):
        if person.ci not in self.__registried_people:
            self.__people_sick.append(person)
            self.__registried_people.append(person.ci)

    def add_recovered_person(self, person):
        if person.ci not in self.__registried_people:
            self.__people_recovered.append(person)
            self.__registried_people.append(person.ci)

    def add_helthy_person(self, person):
        if person.ci not in self.__registried_people:
            self.__people_helthy.append(person)
            self.__registried_people.append(person.ci)

    def remove_sick_person(self, person):
        self.__people_sick.remove(person)
        self.__registried_people.remove(person.ci)

    @property
    def people_sick(self):
        return self.__people_sick

    @property
    def people_recovered(self):
        return self.__people_recovered

    @property
    def people_helthy(self):
        return self.__people_helthy

    @property
    def people_men(self):
        return self.__people_men