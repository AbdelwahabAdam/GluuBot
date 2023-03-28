from database_wrapper import BotDataBase
import sys


class AddData():
    def __init__(self) -> None:
        self.dbconn = BotDataBase()
        self.dbconn.connect()

    def extract_command(self):
        if len(sys.argv) >= 2:
            self.command = sys.argv[1]
            eval('self.'+self.command+'()')
        else:
            self.command = None
            message = '''Please Provide some parametar\nparametar:\nget: to get all data in the DB, ex: python3 db_command.py get\nadd: to add a new values, ex: python3 db_command.py add id intent_name ['intent','example'] responce\nupdate: to update certain value, ex: python3 db_command.py update response Bye! id 1\ngetValue: to get certain value, ex: python3 db_command.py get_Value response id 1\ndelete: to delete a row (on id), ex: python3 db_command.py delete 1\n'''
            print(message.strip())

    def add(self):
        if len(sys.argv) == 6:
            id = sys.argv[2]
            intent_name = sys.argv[3]
            intent_exmaple = sys.argv[4].strip('][').split(', ')
            responce = sys.argv[5]
            self.dbconn.add_value(id, intent_name, intent_exmaple, responce)
            print(
                "Data Added Succesfully, call `get` to fetch all data or `getValue` for certain value")

        else:
            print("Please provide all data.")
            print(
                "example: python3 db_command.py add id intent_name ['intent','example'] responce")

    def get(self):
        print(self.dbconn.get_all())

    def update(self):
        if len(sys.argv) == 6:
            value = sys.argv[2]
            new_value = sys.argv[3]
            where = sys.argv[4]
            where_value = sys.argv[5]
            self.dbconn.update_value(
                value=value, new_value=new_value, where=where, where_value=where_value)
            print(
                "Data Updated Succesfully, call `get` to fetch all data or `getValue` for certain value")
        else:
            print("Please provide all data.")
            print("example: python3 db_command.py update response Bye! id 1")

    def getValue(self):
        if len(sys.argv) == 5:
            select = sys.argv[2]
            where = sys.argv[3]
            equal = sys.argv[4]
            value = self.dbconn.get_certainValue(
                select=select, where=where, equal=equal)
            print(f"The Value for '{select}': {value}")
        else:
            print("Please provide all data.")
            print("example: python3 db_command.py get_Value response id 1")

    def delete(self):
        if len(sys.argv) == 3:
            id = sys.argv[2]
            print(id)
            self.dbconn.remove_valueById(id)
            print(
                "Row has been DELETED Succesfully, call `get` to fetch all data or `getValue` for certain value")

        else:
            print("Please provide all data.")
            print("example: python3 db_command.py delete 1")


if __name__ == '__main__':
    inst = AddData()
    inst.extract_command()
