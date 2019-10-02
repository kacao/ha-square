class Test(object):

    def __init__(self):
        self.test = "!"
        self.__dict__[''] = ''

test = Test()
print(test.test)
