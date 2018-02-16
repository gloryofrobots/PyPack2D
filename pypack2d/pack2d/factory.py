class FactoryError(BaseException):
    pass


class Factory(object):
    def __init__(self):
        super(Factory, self).__init__()
        self._types = {}

    def register(self, name, class_type):
        if self.has_type(name):
            raise FactoryError("TypeName already register %s" % name)

        self._types[name] = class_type

    def has_type(self, name):
        if name not in self._types:
            return False

        return True

    def __create_instance(self, name):
        ctor = self._types[name]
        instance = ctor()
        return instance

    def create_instance(self, name):
        if self.has_type(name) is False:
            raise FactoryError("TypeName not register %s" % name)

        instance = self.__create_instance(name)
        return instance
