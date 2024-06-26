import sys
import typing
sys.dont_write_bytecode = True

class TxtUtils(object):
    def read(self, file:typing.TextIO):
        file = open(file, "r")
        data = file.readlines()
        file.close()
        return data

    def write(self, data:str, file:typing.TextIO):
        file = open(file, "a")
        file.write(f'{data}\n')
        file.close()

    def clear(self, file:typing.TextIO):
        file = open(file, "w")
        file.write('')
        file.close()