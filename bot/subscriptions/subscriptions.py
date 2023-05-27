class USER_SUB_TYPE:
    level_names = {0:'free', 1:'basic', 2:'expert', 3:'business'}
    
    @staticmethod
    def get(level: int):
        return USER_SUB_TYPE.level_names[level]

    FREE = 0
    BASIC = 1
    EXPERT = 2
    BUSINESS = 3