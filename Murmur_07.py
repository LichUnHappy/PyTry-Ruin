# 将常量集中到一个文件
class _const:
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.{}".format(name))
        if not name.isupper():
            raise self.ConstCaseError("const name {} is not all uppercase".format(name))
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()
import Murmur_07 as const
const.A = 1
const.S = 2
const.D = 'hello'
const.F = '$$$!!!#'