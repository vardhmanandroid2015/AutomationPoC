import configparser
import ast
import json

config = configparser.ConfigParser()
config.read('regAutomation.cfg')
print(config.sections())

print(config['CONTRACT']['Field1'][1])
print(ast.literal_eval(config['CONTRACT'].get('Field1'))[0])
print(len(ast.literal_eval(config['CONTRACT'].get('Field1'))))

print(json.loads(config['CONTRACT'].get('Field2')))
print(len(json.loads(config['CONTRACT'].get('Field2'))))
print(json.loads(config['CONTRACT'].get('Field2'))[0])
print(json.loads(config['CONTRACT'].get('Field2'))[1])
print(json.loads(config['CONTRACT'].get('Field2'))[2])
