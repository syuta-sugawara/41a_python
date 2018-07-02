
class Reader:
    def __init__(self):
        import csv
        import re
        pattern = r"\s{2}"
        pattern_last = r'.+(Last).+(Last).'
        pattern_first = r'.+(First).+(First).'
        pattern_row = r'.+(Row).+(Row).'
        pattern_seat = r'.+(Seat).+(Seat).'

        first_temp = []
        for line in csv.reader(open("Airline.xml")):

            obj1 = re.match(pattern_last, str(line))
            obj2 = re.match(pattern_first, str(line))
            obj3 = re.match(pattern_row, str(line))
            obj4 = re.match(pattern_seat, str(line))

            if obj1 or obj2 or obj3 or obj4:
                first_temp.append(line)

        second_temp = []
        for line in range(0, len(first_temp)):
            removed_space = re.sub(r'\s', "", str(first_temp[line]))

            if re.match(pattern_first, removed_space):
                removed_extra = re.sub(r'\[\'<First>|</First>\'\]', "", removed_space)

            if re.match(pattern_last, removed_space):
                removed_extra = re.sub(r'\[\'<Last>|</Last>\'\]', "", removed_space)

            if re.match(pattern_row, removed_space):
                removed_extra = re.sub(r'\[\'<Row>|</Row>\'\]', "", removed_space)

            if re.match(pattern_seat, removed_space):
                removed_extra = re.sub(r'\[\'<Seat>|</Seat>\'\]', "", removed_space)

            second_temp.append(removed_extra)

        group_by = 4
        third = [second_temp[i:i + group_by] for i in range(0, len(second_temp), group_by)]

        self.list = third

    def Output(self):
        for item in range(0, len(self.list)):
            print(self.list[item][0], self.list[item][1], self.list[item][2], self.list[item][3])

    def __len__(self):
        return len(self.list)

    def create_list(self):

        list_of_passengers=[]
        for i in range(0,len(self)):
                list_of_passengers.append([str(self.list[i][0]), str(self.list[i][1]), int(self.list[i][2]), str(self.list[i][3])])
        return list_of_passengers



class Person:
    def __init__(self, give_name, family_name):
        self.first_name = give_name
        self.last_name = family_name

    def __str__(self):
        return "first name is " + self.first_name + " last name is " + self.last_name


class Passenger(Person):
    def __init__(self, give_name, family_name, row_num, seat_num):
        super().__init__(give_name, family_name)

        self.row = row_num
        self.seat = seat_num
        self.rowID = str(row_num) + seat_num

    def __str__(self):
        return str(self.first_name) + ", " + str(self.last_name) + ", " + str(self.row )+ ",  " + str(self.seat )+ ", " + str(self.rowID)

class Seat():
    def __init__(self, passenger):
        self.passenger = passenger

    def Print(self):
        return 'Passenger [ ' + str(self.passenger)+ ' ]'


class Row:
    def __init__(self):
        self.seats = {}

    def insert(self, passenger):
        self.seats[passenger.rowID] = Seat(passenger)

    def Print(self):
        for key, value in self.seats.items():
            print(key,value.Print())



class Section:
    def __init__(self, start, end):
        self.rows = {row: Row() for row in range(start, end + 1)}

    def insert(self, passenger):
        self.rows[passenger.row].insert(passenger)


    def Print(self, Name):

            if (Name == 'First'):
                print('************First Class******************:')
                for key, value in self.rows.items():
                    value.Print()

            elif (Name == 'Business'):
                print('************Business Class****************:')
                for key, value in self.rows.items():
                    value.Print()
            elif (Name == 'Economy'):
                print('*************Economy Class****************:')
                for key, value in self.rows.items():
                    value.Print()


class Jet:
    def __init__(self):
        self.sections = [Section(0, 5), Section(6, 15), Section(15, 36)]

    def insert(self, passenger):
        if 0 <= passenger.row and  passenger.row <= 5:
            self.sections[0].insert(passenger)
        if 6 <= passenger.row and  passenger.row <= 15:
            self.sections[1].insert(passenger)
        if 16 <= passenger.row and passenger.row <= 36:
            self.sections[2].insert(passenger)


    def Print(self):
         self.sections[0].Print('First')
         self.sections[1].Print('Business')
         self.sections[2].Print('Economy')


test_read = Reader()

li=test_read.create_list()

jet = Jet()
for line in range(0,len(li)):
    passenger= Passenger(li[line][0],li[line][1],li[line][2],li[line][3])
    jet.insert(passenger)

jet.Print()








