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
    MENU = State(1000)
    ADD_AD = State(1010, 1012)
    AD_HANDLE = State(1012)

    SHOW_ADS = State(1030)
    DELETE_AD = State(1032)
    DISABLE_AD = State(1034)
    ACTIVATE_AD = State(1036)

    UPDATE_DATA = State(1040)

    BROADCAST = State(1050, 1052)
    BROADCAST_HANDLE = State(1052, 1054)
    BROADCAST_CONFIRM = State(1054)

    ACTIVATE_PREMIUM = State(1060, 1062)
    ACTIVATE_PREMIUM_HANDLE = State(1062)

class USER:
    MAIN_MENU = State(10)
    LINK_CLICK = State(20)
    INFO_PAGE = State(30)
    REMOVE_FOLLOW = State(40)
    
    class IMPORT_LISTAM:
        INFO = State(400, 402)
        HANDLE_URL = State(402)
        SHOW_UPDATES = State(404, min_subscription=USER_SUB_TYPE.PREMIUM)
        FOLLOW_UPDATES = State(406, min_subscription=USER_SUB_TYPE.PREMIUM)

    class IMPORT_MYAUTOGE:
        INFO = State(420, 422)
        HANDLE_URL = State(422)
        SHOW_UPDATES = State(424, min_subscription=USER_SUB_TYPE.PREMIUM)
        FOLLOW_UPDATES = State(426, min_subscription=USER_SUB_TYPE.PREMIUM)

    class REFERRAL:
        INFO = State(700)
        GET_BOUNS = State(710)
        
    class SAVED:
        INFO = State(500)
        ADD = State(502)
        DELETE = State(504)

        class CAR:
            BRAND = State(510)
            MODEL = State(520)
            YEAR = State(530,532)
            YEAR_HANDLE = State(532)

            MILEAGE_START = State(540)
            MILEAGE_END = State(544)

            EXTERIOR_COLOR = State(550)
            BODY_TYPE = State(560)
            ENGINE_TYPE = State(570)
            ENGINE_SIZE = State(580, 582)
            ENGINE_SIZE_HANDLE = State(582)

            TRANSMISSION = State(590)
            DRIVE_TYPE = State(600)
            # CONDITION = State(610)
            GAS_EQUIPMENT = State(620)
            STEERING_WHEEL = State(630)

            PRICE_START = State(640)
            PRICE_END = State(644)

            SAVE = State(660, min_subscription=USER_SUB_TYPE.PREMIUM)

    class CAR_PRICE:
        INFO = State(100)
        BRAND = State(110)
        MODEL = State(120)
        YEAR = State(130,132)
        YEAR_HANDLE = State(132)

        MILEAGE = State(140, 142)
        MILEAGE_HANDLE = State(142)

        EXTERIOR_COLOR = State(150)
        BODY_TYPE = State(160)
        ENGINE_TYPE = State(170)
        ENGINE_SIZE = State(180, 182)
        ENGINE_SIZE_HANDLE = State(182)

        TRANSMISSION = State(190)
        DRIVE_TYPE = State(200)
        GAS_EQUIPMENT = State(220)
        STEERING_WHEEL = State(230)
        INTERIOR_COLOR = State(250)
        INTERIOR_MATERIAL = State(260)

        CALCULATE_PRICE = State(290)
        CALCULATE_GOOD = State(292)
        CALCULATE_DONT_KNOW = State(294)
        CALCULATE_OFFER_PRICE = State(296, 298)
        CALCULATE_OFFER_PRICE_HANDLE = State(298)
        
        CALCULATE_PRICE_BY_YEAR = State(300)
        CALCULATE_PRICE_BY_MILEAGE = State(310)

    class SUBSCRIPTION:
        INFO = State(900)
