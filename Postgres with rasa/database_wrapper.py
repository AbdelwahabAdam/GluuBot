
import psycopg2
from psycopg2.extras import RealDictCursor
from coverter import MyConverter


class BotDataBase:
    def __init__(self, **args):
        self.user = args.get('user', 'postgres')
        self.password = args.get('password', 'password')
        self.port = args.get('port', 5432)
        self.dbname = args.get('dbname', 'postgres')
        self.host = args.get('host', 'db')
        self.connection = None
        self.nlu_json = args.get('nlu_json', {"version": "3.1", "nlu": []})
        self.domain_json = args.get('domain_json', {"version": "3.1", "intents": [], "responses": {
        }, "session_config": {"session_expiration_time": 60, "carry_over_slots_to_new_session": True}})
        self.rules_json = args.get(
            'rules_json', {"version": "3.1", "rules": [], })
        self.converter = MyConverter()

    def connect(self):
        pg_conn = psycopg2.connect(user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   port=self.port,
                                   database=self.dbname)

        self.connection = pg_conn

    def get_cursor(self):
        return self.connection.cursor()

    @staticmethod
    def execute_and_fetch(cursor, query, get_bool):
        if get_bool == 0:
            cursor.execute(query)
            res = cursor.fetchall()
            cursor.close()
            return res
        else:
            cursor.execute(query)
            cursor.close()
            return 1

    def get_response(self, query, get_bool=0):
        cursor = self.get_cursor()
        response = self.execute_and_fetch(cursor, query, get_bool)
        self.connection.commit()
        return response

    def get_all(self):
        # return List for each row as a tuble of dict
        query = '''SELECT json_build_object('id',intent.id,'intent_name',intent.intent_name,'intent_examples',intent.intent_examples,'response',intent.response) from intent;'''
        return self.get_response(query)

    def get_rowsCount(self):
        # return int for rows count
        query = '''SELECT COUNT(*) FROM intent;'''
        return self.get_response(query)[0][0]

    def get_certainValue(self, select='*', where='', equal=''):
        # return a certain value, and if empty, it will return all data as tuble.
        if where != '':
            query = (
                f'''SELECT {select} FROM intent WHERE intent.{where}= '{equal}' ''')
            return self.get_response(query)[0][0]
        else:
            query = (f'''SELECT {select} FROM intent ''')
            return self.get_response(query)

    def remove_valueById(self, id):
        query = (f'''DELETE FROM intent  WHERE id = '{id}' ''')
        self.get_response(query)

    def update_value(self, value, new_value, where, where_value):
        query = (
            f'''UPDATE intent SET {value} = '{new_value}' WHERE {where} = {where_value} ''')
        self.get_response(query=query, get_bool=1)

    def add_value(self, id, intent_name, intent_examples, response):
        query = (
            f'''INSERT INTO intent (id, intent_name, intent_examples, response) VALUES({id},'{intent_name}',ARRAY {intent_examples},'{response}');''')
        self.get_response(query=query, get_bool=1)

    def get_nluData(self, directory_data):
        for i in self.get_all():
            temp_dict = {'intent': i[0]['intent_name'],
                         'examples': i[0]['intent_examples']}
            self.nlu_json['nlu'].append(temp_dict)

        # directory_data = 'tempForData'
        # os.makedirs(name=directory_data)

        with open(f"{directory_data}/nlu.yaml", "w") as yaml_out:
            self.converter.get_yaml(json_data=self.nlu_json, yaml_out=yaml_out)

    def get_domainData(self, directory_data):
        intents = []
        respoces = {}
        for i in self.get_all():
            intent_name = i[0]['intent_name']
            intents.append(intent_name)
            respoces['utter_'+intent_name] = [{"text": (i[0]['response'])}]

        self.domain_json['intents'] = intents
        self.domain_json['responses'] = respoces

        # directory_data = 'tempForData'
        # os.makedirs(name=directory_data)

        with open(f"{directory_data}/domain.yaml", "w") as yaml_out:
            self.converter.get_yaml(
                json_data=self.domain_json, yaml_out=yaml_out)

    def get_rulesData(self, directory_data):
        rules = []
        for i in self.get_all():
            steps = []
            intent_name = i[0]['intent_name']
            steps.append({'intent': intent_name})
            steps.append({'action': 'utter_'+intent_name})
            rules.append({"rule": intent_name+'_rule', "steps": steps})

        self.rules_json["rules"] = rules

        # directory_data = 'tempForData'
        # os.makedirs(name=directory_data)

        with open(f"{directory_data}/rules.yaml", "w") as yaml_out:
            self.converter.get_yaml(
                json_data=self.rules_json, yaml_out=yaml_out)


# directory_data = tempfile.mkdtemp()
dbconn = BotDataBase()
dbconn.connect()
print(dbconn.get_all())
# dbconn.get_nluData(directory_data=directory_data)
# dbconn.get_domainData(directory_data=directory_data)
# dbconn.get_rulesData(directory_data=directory_data)

# print(os.listdir(directory_data))
# print(dbconn.get_rowsCount())
# print(dbconn.update_value(value='response',new_value='Bye!',where='id',where_value='1'))
# print(dbconn.get_certainValue(select='response',where='id',equal='1'))
