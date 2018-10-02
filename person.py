import random
# TODO: Import the virus clase
class Virus():
    # virus needs a name, a mortality rate, and a reproduction rate
    def __init__(self, name, mortality_rate, repro_rate):
        self.name = name
        self.mortality_rate = mortality_rate
        self.repro_rate = repro_rate

def test_virus_instantiation():
    # instantiate a virus to the virus class
    virus = Virus("ebola", 0.7, 0.5)
    # make sure the Virus properties pair to that of the instantiation
    assert virus.name == "ebola"
    assert virus.mortality_rate == 0.7
    assert virus.repro_rate == 0.5


class Person(object):
    '''
    Person objects will populate the simulation.

    _____Attributes______:

    _id: Int.  A unique ID assigned to each person.

    is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.

    is_alive: Bool. All person objects begin alive (value set to true).  Changed
        to false if person object dies from an infection.

    infection:  None/Virus object.  Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the person
        is infected with.

    _____Methods_____:

    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.

    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infected to None.
    '''

    def __init__(self, _id, is_vaccinated, infected=None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the correct values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = None
        self.infected = infected
        self.alive = True
        self.infection = None


    def did_survive_infection(self):
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infected = None, return True. 
        random_number = random.uniform(0, 1)
        print(random_number) 
        if self.infected != None:
            if random_number <= self.infected.mortality_rate:
                print("person has died :(")
                self.is_alive = False
                return False
            else:
                print("person is alive YAY!")
                self.is_vaccinated = True
                self.infected = None
                return True

def test_did_survive_infection():
    virus = Virus("ebola", 0.8, 0.5)
    person = Person(301, False, virus)
    assert person.did_survive_infection()

# if __name__ == "__main__":
#     Virus("ebola", 0.8, 0.5)
#     person = Person(123, True)
#     person.did_survive_infection()