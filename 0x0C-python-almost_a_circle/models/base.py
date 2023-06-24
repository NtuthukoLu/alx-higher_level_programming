#!/usr/bin/python3
"""base Module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for Base class"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a
        list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for dic in list_dictionaries:
            if type(dic) is not dict:
                err = "list_dictionaries must be a list of dictionaries"
                raise TypeError(err)
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a
        list of instances to a file
        """
        filename = cls.__name__ + ".json"
        dicList = []
        if list_objs is not None:
            for obj in list_objs:
                dicList.append(obj.to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicList))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of the JSON string representation.
        """
        if json_string is None or (len(json_string) == 0):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already
        set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0, 'a')
        if cls.__name__ == "Square":
            dummy = cls(1, 0, 0, 'b')
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a .json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_string = f.read()
                dicList = []
                for obj in cls.from_json_string(json_string):
                    dicList.append(cls.create(**obj))
        except ValueError:
            dicList = []
        return dicList

    @staticmethod
    def to_csv_lines(list_csv):
        """returns CSV string representation from list of sub class
            objects represented in their csv form
        """
        builder = ""
        for csv in list_csv:
            for i, ele in enumerate(csv):
                builder += str(ele)
                if i != len(csv) - 1:
                    builder += ','
            builder += '\n'
        return builder

    @staticmethod
    def from_csv_lines(list_csv):
        """returns list of CSV instance objects (containing sub class data)
            ->from list of lines of data
        """
        if list_csv is None or len(list_csv) == 0:
            return []

        csv_data = []
        for line in list_csv:
            raw_data = line.strip('\n').split(',')
            csv_data.append([int(ele) for ele in raw_data])
        return csv_data

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects to a file as a JSON string
        """
        new_list = None
        list_obj_copy = list_objs.copy()
        filename = cls.__name__ + ".json"

        super_list = []
        for ele in list_obj_copy:
            if issubclass(type(ele), Base):
                super_list.append(ele.to_dictionary())
        write_str = cls.to_json_string(super_list)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(write_str)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of sub-class objects to their file as csv
        """
        list_obj_copy = list_objs.copy()
        # get_cname_from_sublist also removes non subclass eles, so copy
        filename = cls.__name__ + ".csv"
        super_list = []

        for ele in list_obj_copy:
            if issubclass(type(ele), Base):
                super_list.append(ele.to_csv())
        write_str = cls.to_csv_lines(super_list)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(write_str)

    @classmethod
    def load_from_file_csv(cls):
        """loads a list of objects from their csv file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except ValueError:
            return []

        inst_list = []
        csv_list_list = cls.from_csv_lines(lines)
        for csv_inst in csv_list_list:
            new_obj = cls(1, 1)
            new_obj.update(*csv_inst)
            inst_list.append(new_obj)
        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws the rectangles and squares using turtle GL
        """
        window = turtle.Screen()
        window.bgcolor("green")
        all_eles = list_rectangles.copy()
        all_eles.extend(list_squares)
        turtles = [turtle.Turtle() for ele in all_eles]
        for i, t in enumerate(turtles):
            if i < len(list_rectangles):
                t.color("blue")
                if i > 0:
                    prev_pos = turtles[i - 1].position()
                    prev_x = prev_pos[0] + list_rectangles[i - 1].width
                    pre_y = prev_pos[1]
                    if i % 6 == 0:
                        pre_y = prev_pos[1] + list_rectangles[i - 1].height
                    t.setpos(prev_x, pre_y)
                t.forward(list_rectangles[i].width)
                t.right(90)
                t.forward(list_rectangles[i].height)
                t.right(90)
                t.forward(list_rectangles[i].width)
                t.right(90)
                t.forward(list_rectangles[i].height)
            else:
                t.color("red")
                if i > 0:
                    cur_sq_i = i - len(list_rectangles)
                    prev_pos = turtles[i - 1].position()
                    prev_x = prev_pos[0] + list_squares[cur_sq_i - 1].size
                    prev_y = prev_pos[1]
                    if i % 6 == 0:
                        prev_y = prev_pos[1] + list_squares[cur_sq_i - 1].size
                    t.setpos(prev_x, prev_y)
                for s in range(0, 4):
                    t.forward(list_squares[cur_sq_i].size)
                    t.right(90)
