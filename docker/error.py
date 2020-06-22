class ManagerException(Exception):
    
    

    
    def __init__(self, code, msg):
        self.msg = msg
        self.code = code


    @staticmethod
    def getError(value,code,msg):
        
        switcher = { 
            1 : '{"code": ' + '400' + ',"msg": ' + msg + '}',
            2 : '{"code": ' + '500' + ',"msg": ' + msg + '}',
        }

        content = switcher.get(value)

        return content