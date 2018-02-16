class FactoryError(BaseException):
    pass


class Factory(object):
    def __init__(self):
        super(Factory, self).__init__()
        self._types = {}
        pass

    def register(self, name, class_type):
        if self.has_type(name):
            raise FactoryError("TypeName already register %s" % name)
            pass

        self._types[name] = class_type
        pass

    def has_type(self, name):
        if name not in self._types:
            return False
            pass

        return True
        pass

    def __create_instance(self, name):
        ctor = self._types[name]
        instance = ctor()
        return instance
        pass

    def create_instance(self, name):
        if self.has_type(name) is False:
            raise FactoryError("TypeName not register %s" % name)

        instance = self.__create_instance(name)
        return instance
        pass

    pass
