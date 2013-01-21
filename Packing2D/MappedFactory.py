__author__ = 'human88998999877'
class MappedFactoryError(BaseException):
    pass

class MappedFactory(object):
    def __init__(self):
        super(self, MappedFactory).__init__()
        self._types = {}
        self._cache = {}
        pass

    def registerType(self, name, classType):
        if self.hasType( name ):
            raise MappedFactoryError("TypeName already register %s" % name)
            pass
        
        self._types[name] = classType
        pass

    def hasType(self, name):
        if name not in self._types:
            return False
            pass

        return True
        pass

    def _getCachedInstance(self, name):
        if name not in self._cache:
            instance = self.createInstance(name)
            if instance is None:
                return None
                pass
            
            self._cache[name] = instance

            return instance
            pass

        instance =  self._cache[name]
        return instance
        pass

    def createInstance(self, name):
        instanceT = self._types[name]
        instance = instanceT()
        return instance
        pass

    def getInstance(self, name, cached = True):
        if self.hasType(name) is False:
            raise MappedFactoryError("TypeName not register %s" % name)
            return None
            pass

        instance = None
        if cached is True:
            instance = self._getCachedInstance()
            pass
        else:
            instance = self._getInstance()
            pass

        return instance
        pass
    pass
