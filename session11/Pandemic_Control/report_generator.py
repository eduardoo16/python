from bitacora import Bitacora

bitacora = Bitacora()

def get_historical_sicks(people):
    result = 0
    for person in people:
        if person.is_sick:
            bitacora.add_sick_person(person)
            result += 1
    return result

def get_recover(people):
    result = 0
    for person in people:
        if not person.is_sick and person in bitacora.people_sick:
            bitacora.remove_sick_person(person)
            bitacora.add_recovered_person(person)
            result += 1
    return result

def get_men():
    result = 0
    for person in bitacora.people_sick:
        if person.gender == "Male":
            result += 1
    return result

def get_women():
    result = 0
    for person in bitacora.people_sick:
        if person.gender == "Female":
            result += 1
    return result

def get_kid():
    result = 0
    for person in bitacora.people_sick:
        if person.age < 15:
          result += 1
    return result

def get_young():
    result = 0
    for person in bitacora.people_sick:
        if person.age > 14 and person.age < 60:
            result += 1
    return result

def get_adult():
    result = 0
    for person in bitacora.people_sick:
        if person.age > 60:
            result += 1
    return result

def get_men_recovered():
    result = 0
    for person in bitacora.people_recovered:
        if person.gender == "Male":
            result += 1
    return result

def get_women_recovered():
    result = 0
    for person in bitacora.people_recovered:
        if person.gender == "Female":
            result += 1
    return result

def get_kid_recovered():
    result = 0
    for person in bitacora.people_recovered:
        if person.age < 15:
          result += 1
    return result

def get_young_recovered():
    result = 0
    for person in bitacora.people_recovered:
        if person.age > 14 and person.age < 60:
            result += 1
    return result

def get_adult_recovered():
    result = 0
    for person in bitacora.people_recovered:
        if person.age > 60:
            result += 1
    return result


# def get_sick():
#     result = 0
#     for person in people:
#         if person.is_sick:
#             bitacora.add_sick_person(person)
#             result += 1
#     return result
