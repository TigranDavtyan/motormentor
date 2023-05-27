from subscriptions.subscriptions import USER_SUB_TYPE

class State:
    states = {}
    @staticmethod
    def get(state):
        if type(state) is int:
            return State.states.get(state)
        return State.states.get(state.ID)
    
    def __hash__(self) -> int:
        return self.ID.__hash__()
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) == int:
            return self.ID == __value
        elif type(__value) == State:
            return self.ID == __value.ID
        else:
            raise ValueError('Value type must be State or int.')
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    
    def __init__(self, id, next = -1, min_subscription = USER_SUB_TYPE.FREE):
        self.ID = id
        self.NEXT = next
        self.ACTION = None
        self.min_subscription = min_subscription
        State.states[self.ID] = self

    async def __call__(self, *kwarg, **args):
        return await self.ACTION(*kwarg, **args)

    def __str__(self):
        return str(self.ID)

    def setAction(self, action):
        self.ACTION = action

class GENERAL:
    NOT_AVAILABLE = State(-2)
    ERROR = State(-1)
    START = State(0)

    class LANGUAGE:
        CHOOSE = State(2, 4)
        FINISH = State(4)

class ADMIN:
    pass

class USER:
    MAIN_MENU = State(10)
    class CAR_PRICE:
        INFO = State(100)#
        BRAND = State(110)#
        MODEL = State(120)#
        YEAR = State(130,132)#
        YEAR_HANDLE = State(132)#

        MILEAGE = State(140, 142)#
        MILEAGE_HANDLE = State(142)#

        EXTERIOR_COLOR = State(150)#
        BODY_TYPE = State(160)#
        ENGINE_TYPE = State(170)#
        ENGINE_SIZE = State(180, 182)#
        ENGINE_SIZE_HANDLE = State(182)#

        TRANSMISSION = State(190)#
        DRIVE_TYPE = State(200)#
        CONDITION = State(210)#
        GAS_EQUIPMENT = State(220)#
        STEERING_WHEEL = State(230)#
        HEADLIGHTS = State(240)#
        INTERIOR_COLOR = State(250)#
        INTERIOR_MATERIAL = State(260)#
        SUNROOF = State(270)
        WHEEL_SIZE = State(280, 282)#
        WHEEL_SIZE_HANDLE = State(282)#

        CALCULATE_PRICE = State(290)
    class SUBSCRIPTION:
        INFO = State(900)
        pass
