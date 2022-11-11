import datetime
import logging


class Employees:
    """Class to contain the properties of Employees

    Parameters
    ----------
    name : str
        employee name
    last_name : str
        employee last name
    birth_date : str
        employee birthdate
    nro_dni : str
        employee dni

    Attributes
    ----------
    name : str
        employee name
    last_name : str
        employee last name
    birth_date : obj
        employee birthdate
    nro_dni : str
        employee dni

    """
    def __init__(self, name: str, last_name: str, birth_date: str, nro_dni: str):

        self.name = name
        self.last_name = last_name
        try:
            self.birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
        except ValueError:
            logging.error("date format error", exc_info=True)
        self.nro_dni = nro_dni

    def calculate_age(self):
        """Obtain the employee age

        Returns
        -------
        age_person : int
            returns the age of the employee
        """

        age_person = datetime.date.today().year - self.birth_date.year

        return f"my age is {age_person}"

    def presentation(self):
        """Returns the presentation of the employee

        Returns
        -------
        presentation_string : str
            returns the employee fullname, birthdate and dni
        """
        presentation_string = f"Hola soy {self.name} {self.last_name}. Nací el {self.birth_date} y mi dni es: {self.nro_dni}"
        return presentation_string


juan = Employees("juan", "pepito", "2000-8-25", "12345678")

if __name__ == '__main__':
    print(juan.calculate_age())
    print(juan.presentation())
