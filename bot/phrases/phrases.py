#This is a generated file
from data import DatabaseManager
db = DatabaseManager()

ARM = 0
RUS = 1
ENG = 2

def start(cid : int, all : bool = False) -> str:
    '''Welcome to the Motor Mentor Bot! This bot predicts car prices based on various features. Whether you're selling, buying, or interested in analyzing market trends, this bot is here to assist you.

By providing details about your car, such as brand, model, year, mileage, and more, the bot will estimate the price range for your vehicle. This can help you set a competitive selling price, make informed buying decisions, or gain insights into the factors that influence car prices.

Please note that the predictions provided are estimates based on available data. Actual market prices may vary due to factors like location, condition, and market demand.

Enjoy using the Motor Mentor Bot! Feel free to ask any questions to the admin. Let's begin! 
<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>'''
    phrases = ['''Բարի գալուստ Motor Mentor Bot: Այս բոտը կանխատեսում է մեքենաների գները՝ հիմնվելով տարբեր հատկանիշների վրա: Անկախ նրանից, թե դուք վաճառում եք, գնում եք կամ հետաքրքրված եք շուկայի միտումների վերլուծությամբ, այս բոտն այստեղ է ձեզ օգնելու համար:

Տրամադրելով ձեր մեքենայի մասին մանրամասներ, ինչպիսիք են ապրանքանիշը, մոդելը, տարին, վազքը և այլն, բոտը կգնահատի ձեր մեքենայի գների միջակայքը: Սա կարող է օգնել ձեզ սահմանել մրցունակ վաճառքի գին, կայացնել տեղեկացված գնման որոշումներ կամ ձեռք բերել պատկերացումներ մեքենաների գների վրա ազդող գործոնների մասին:

Խնդրում ենք նկատի ունենալ, որ ներկայացված կանխատեսումները գնահատումներ են՝ հիմնված առկա տվյալների վրա: Իրական շուկայական գները կարող են տարբեր լինել՝ պայմանավորված այնպիսի գործոններով, ինչպիսիք են գտնվելու վայրը, վիճակը և շուկայական պահանջարկը:

Ազատորեն ցանկացած հարց ուղղեք ադմինին: Վայելե՛ք Motor Mentor Bot-ը: Եկեք սկսենք!
<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''Добро пожаловать в бота Motor Mentor! Этот бот прогнозирует цены на автомобили на основе различных характеристик. Если вы продаете, покупаете или интересуетесь анализом рыночных тенденций, этот бот здесь, чтобы помочь вам.

Предоставляя информацию о вашем автомобиле, такую как марка, модель, год выпуска, пробег и т. д., бот оценит диапазон цен на ваш автомобиль. Это может помочь вам установить конкурентоспособную цену продажи, принять обоснованное решение о покупке или получить представление о факторах, влияющих на цену автомобиля.

Обратите внимание, что представленные прогнозы являются оценками, основанными на доступных данных. Фактические рыночные цены могут варьироваться в зависимости от таких факторов, как местоположение, состояние и рыночный спрос.

Наслаждайтесь использованием бота Motor Mentor! Не стесняйтесь задавать любые вопросы администратору. Давай начнем!
<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''Welcome to the Motor Mentor Bot! This bot predicts car prices based on various features. Whether you're selling, buying, or interested in analyzing market trends, this bot is here to assist you.

By providing details about your car, such as brand, model, year, mileage, and more, the bot will estimate the price range for your vehicle. This can help you set a competitive selling price, make informed buying decisions, or gain insights into the factors that influence car prices.

Please note that the predictions provided are estimates based on available data. Actual market prices may vary due to factors like location, condition, and market demand.

Enjoy using the Motor Mentor Bot! Feel free to ask any questions to the admin. Let's begin! 
<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def help(cid : int, all : bool = False) -> str:
    '''If you are stuck or have any questions you can contact the admin at <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ He will definitely help you🙂'''
    phrases = ['''Եթե անելանելի վիճակում եք կամ հարցեր ունեք, կարող եք կապվել ադմինիստրատորի հետ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>։ Նա անպայման կօգնի ձեզ🙂''', '''Если вы застряли или у вас есть какие-либо вопросы, вы можете связаться с администратором по адресу <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ Он обязательно вам поможет🙂''', '''If you are stuck or have any questions you can contact the admin at <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ He will definitely help you🙂''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def language_change(cid : int, all : bool = False) -> str:
    '''🇦🇲🇷🇺🇺🇸 Change language'''
    phrases = ['''🇦🇲🇷🇺🇺🇸 Փոխել լեզուն''', '''🇦🇲🇷🇺🇺🇸 Изменить язык''', '''🇦🇲🇷🇺🇺🇸 Change language''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def language_choose(cid : int, all : bool = False) -> str:
    '''Select language 🇺🇸'''
    phrases = ['''Ընտրեք լեզուն 🇦🇲''', '''Выберите язык 🇷🇺''', '''Select language 🇺🇸''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def languages(cid : int, all : bool = False) -> str:
    '''English🇺🇸'''
    phrases = ['''Հայերեն🇦🇲''', '''Русский🇷🇺''', '''English🇺🇸''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def language_set(cid : int, all : bool = False) -> str:
    '''English is selected 🇺🇸'''
    phrases = ['''Ընտրվեց հայերեն լեզուն 🇦🇲''', '''Выбран русский язык 🇷🇺''', '''English is selected 🇺🇸''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def agree(cid : int, all : bool = False) -> str:
    '''✅ I agree!'''
    phrases = ['''✅ Համաձայն եմ!''', '''✅ Я согласен!''', '''✅ I agree!''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def disagree(cid : int, all : bool = False) -> str:
    '''❌ I disagree'''
    phrases = ['''❌ Համաձայն չեմ''', '''❌ Я не согласен''', '''❌ I disagree''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def cancel(cid : int, all : bool = False) -> str:
    '''🚫 Cancel'''
    phrases = ['''🚫 Չեղարկել''', '''🚫 Отменить''', '''🚫 Cancel''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def canceled(cid : int, all : bool = False) -> str:
    '''🚫 Canceled'''
    phrases = ['''🚫 Չեղարկված է''', '''🚫 Отменено''', '''🚫 Canceled''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def all_right(cid : int, all : bool = False) -> str:
    '''✅ That's right'''
    phrases = ['''✅ Ճիշտ է''', '''✅ Все верно''', '''✅ That's right''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def back(cid : int, all : bool = False) -> str:
    '''👈 Back'''
    phrases = ['''👈 Վերադառնալ''', '''👈 Назад''', '''👈 Back''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def skip(cid : int, all : bool = False) -> str:
    '''👉 Skip'''
    phrases = ['''👉 Բաց թողնել''', '''👉 Пропустить''', '''👉 Skip''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def confirm(cid : int, all : bool = False) -> str:
    '''👍 Confirm'''
    phrases = ['''👍 Հաստատել''', '''👍 Подтвердить''', '''👍 Confirm''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def confirmed(cid : int, all : bool = False) -> str:
    '''👍 Confirmed'''
    phrases = ['''👍 Հաստատված է''', '''👍 Подтверждено''', '''👍 Confirmed''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def yes(cid : int, all : bool = False) -> str:
    '''✅ Yes'''
    phrases = ['''✅ Այո՛''', '''✅ Да''', '''✅ Yes''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def no(cid : int, all : bool = False) -> str:
    '''❌ No'''
    phrases = ['''❌ Ոչ''', '''❌ Нет''', '''❌ No''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def ok(cid : int, all : bool = False) -> str:
    '''ok'''
    phrases = ['''օկ''', '''ок''', '''ok''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def wrong_action(cid : int, all : bool = False) -> str:
    '''❌Wrong action❌
 Read the message again☝️, get /help from admin or go to /start and try again.'''
    phrases = ['''❌Սխալ գործողություն❌
 Կրկին կարդացեք հաղորդագրությունը☝️, ստացեք /help ադմինիստրատորից կամ /start արեք և նորից փորձեք:''', '''❌Неверное действие❌
 Прочитайте сообщение еще раз☝️, получите /help от администратора или вернитесь и повторите попытку.''', '''❌Wrong action❌
 Read the message again☝️, get /help from admin or go to /start and try again.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def duration(cid : int, all : bool = False) -> str:
    '''Duration'''
    phrases = ['''Տևողություն''', '''Продолжительность''', '''Duration''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def fee(cid : int, all : bool = False) -> str:
    '''Fee'''
    phrases = ['''Վճար''', '''Плата''', '''Fee''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def dram(cid : int, all : bool = False) -> str:
    '''amd'''
    phrases = ['''դրամ''', '''драм''', '''amd''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def minute(cid : int, all : bool = False) -> str:
    '''minutes'''
    phrases = ['''րոպե''', '''минут''', '''minutes''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def today(cid : int, all : bool = False) -> str:
    '''Today'''
    phrases = ['''Այսօր''', '''Сегодня''', '''Today''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def tomorrow(cid : int, all : bool = False) -> str:
    '''Tomorrow'''
    phrases = ['''Վաղը''', '''Завтра''', '''Tomorrow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def afterTomorrow(cid : int, all : bool = False) -> str:
    '''The day after tomorrow'''
    phrases = ['''Վաղը չէ մյուս օրը''', '''Послезавтра''', '''The day after tomorrow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def date(cid : int, all : bool = False) -> str:
    '''Date'''
    phrases = ['''Ամսաթիվ''', '''Дата''', '''Date''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def start2(cid : int, all : bool = False) -> str:
    '''Start'''
    phrases = ['''Սկիզբ''', '''Начало''', '''Start''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def end(cid : int, all : bool = False) -> str:
    '''End'''
    phrases = ['''Վերջ''', '''Конец''', '''End''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def day(cid : int, all : bool = False) -> str:
    '''Day'''
    phrases = ['''Օր''', '''День''', '''Day''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def january(cid : int, all : bool = False) -> str:
    '''January'''
    phrases = ['''Հունվարի''', '''Январь''', '''January''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def february(cid : int, all : bool = False) -> str:
    '''February'''
    phrases = ['''Փետրվարի''', '''Февраль''', '''February''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def march(cid : int, all : bool = False) -> str:
    '''March'''
    phrases = ['''Մարտի''', '''Март''', '''March''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def april(cid : int, all : bool = False) -> str:
    '''April'''
    phrases = ['''Ապրիլի''', '''Апрель''', '''April''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def may(cid : int, all : bool = False) -> str:
    '''May'''
    phrases = ['''Մայիսի''', '''Май''', '''May''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def june(cid : int, all : bool = False) -> str:
    '''June'''
    phrases = ['''Հունիսի''', '''Нюнь''', '''June''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def july(cid : int, all : bool = False) -> str:
    '''July'''
    phrases = ['''Հուլիսի''', '''Июль''', '''July''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def august(cid : int, all : bool = False) -> str:
    '''August'''
    phrases = ['''Օգոստոսի''', '''Август''', '''August''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def september(cid : int, all : bool = False) -> str:
    '''September'''
    phrases = ['''Սեպտեմբերի''', '''Сентябрь''', '''September''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def october(cid : int, all : bool = False) -> str:
    '''October'''
    phrases = ['''Հոկտեմբերի''', '''Октябрь''', '''October''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def november(cid : int, all : bool = False) -> str:
    '''November'''
    phrases = ['''Նոյեմբերի''', '''Ноябрь''', '''November''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def december(cid : int, all : bool = False) -> str:
    '''December'''
    phrases = ['''Դեկտեմբերի''', '''Декабрь''', '''December''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def details(cid : int, all : bool = False) -> str:
    '''🧾'''
    phrases = ['''🧾''', '''🧾''', '''🧾''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def cancel(cid : int, all : bool = False) -> str:
    '''❌'''
    phrases = ['''❌''', '''❌''', '''❌''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def anonymous(cid : int, all : bool = False) -> str:
    '''unknown 🤷‍♀️'''
    phrases = ['''անհայտ 🤷‍♀️''', '''неизвестный 🤷‍♀️''', '''unknown 🤷‍♀️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_successfull(cid : int,sub_end, all : bool = False) -> str:
    '''Your payment was successfull🎉 Subscription ends at [sub_end]. Now you can feel the real power of this bot💪'''
    phrases = ['''Ձեր վճարումը հաջող է եղել🎉 Բաժանորդագրությունն ավարտվում է [sub_end]-ին: Այժմ դուք կարող եք զգալ այս բոտի իրական ուժը💪''', '''Ваш платеж прошел успешно🎉 Подписка заканчивается в [sub_end]. Теперь вы можете почувствовать настоящую мощь этого бота💪''', '''Your payment was successfull🎉 Subscription ends at [sub_end]. Now you can feel the real power of this bot💪''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[sub_end]",str(sub_end))

def subscription(cid : int, all : bool = False) -> str:
    '''⭐️ Subscription'''
    phrases = ['''⭐️ Բաժանորդագրություն''', '''⭐️ Подписка''', '''⭐️ Subscription''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_free(cid : int, all : bool = False) -> str:
    '''Free'''
    phrases = ['''Անվճար''', '''Бесплатный''', '''Free''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_premium(cid : int, all : bool = False) -> str:
    '''Premium'''
    phrases = ['''Պրեմիում''', '''Премиум''', '''Premium''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_business(cid : int, all : bool = False) -> str:
    '''Business'''
    phrases = ['''Բիզնես''', '''Бизнес''', '''Business''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_info_free(cid : int, all : bool = False) -> str:
    '''Your subscription is "Free". If you want to have a "Premium" subscription contact the admin. It only costs <b>990 AMD</b> but you get a lot of useful functionality. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>'''
    phrases = ['''Ձեր բաժանորդագրությունը «Անվճար» է: Եթե ցանկանում եք ունենալ «Պրեմիում» բաժանորդագրություն, դիմեք ադմինիստրատորին: Այն արժե ընդամենը <b>990 դրամ</b>, բայց դուք ստանում եք շատ օգտակար ֆունկցիոնալություն: <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''Ваша подписка "Бесплатная". Если вы хотите иметь подписку «Премиум», свяжитесь с администратором. Это стоит всего <b>990 драм</b>, но вы получаете много полезного функционала. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''Your subscription is "Free". If you want to have a "Premium" subscription contact the admin. It only costs <b>990 AMD</b> but you get a lot of useful functionality. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sub_info_premium(cid : int,sub_end_days, all : bool = False) -> str:
    '''Your subscription is "Premium". It ends in [sub_end_days] days. If you want to prolonge the subscription contact the admin. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>'''
    phrases = ['''Ձեր բաժանորդագրությունը «Պրեմիում» է: Այն ավարտվում է [sub_end_days] օրից: Եթե ցանկանում եք երկարացնել բաժանորդագրությունը, դիմեք ադմինիստրատորին։ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''Ваша подписка "Премиум". Он заканчивается через [sub_end_days] дней. Если вы хотите продлить подписку, свяжитесь с администратором. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''Your subscription is "Premium". It ends in [sub_end_days] days. If you want to prolonge the subscription contact the admin. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[sub_end_days]",str(sub_end_days))

def subscription_not_enough(cid : int,user_sub,min_sub, all : bool = False) -> str:
    '''Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․ Contact the admin '''
    phrases = ['''Ձեր բաժանորդագրությանը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը "[min_sub]" է''', '''Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: "[min_sub]"''', '''Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․ Contact the admin ''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[user_sub]",str(user_sub)).replace("[min_sub]",str(min_sub))

def subscription_end(cid : int, all : bool = False) -> str:
    '''❗️ Warning ❗️
Your "Premium" subscribtion ended. Contact the administrator to activate it. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>'''
    phrases = ['''❗️ Զգուշացում ❗️
Ձեր «Պրեմիում» բաժանորդագրությունն ավարտվել է: Կապվեք ադմինիստրատորի հետ՝ այն ակտիվացնելու համար: <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''❗️ Предупреждение ❗️
Ваша подписка "Премиум" закончилась. Свяжитесь с администратором, чтобы активировать его. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''', '''❗️ Warning ❗️
Your "Premium" subscribtion ended. Contact the administrator to activate it. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def referral(cid : int, all : bool = False) -> str:
    '''🔗 Referrals'''
    phrases = ['''🔗 Ռեֆերալներ''', '''🔗 Рефералы''', '''🔗 Referrals''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def referral_info(cid : int,bonus_refs,bonus_days,ref_link, all : bool = False) -> str:
    '''Send this link to your friends and if they use this bot you will get a bonus. 
For every [bonus_refs] referrals your Premium subscription will be prolonged for [bonus_days] days.
Your referral link is 
<code>[ref_link]</code>'''
    phrases = ['''Ուղարկեք այս հղումը ձեր ընկերներին և եթե նրանք օգտվեն այս բոտից, դուք կստանաք բոնուս:
Յուրաքանչյուր [bonus_refs] ուղղորդման համար ձեր Premium բաժանորդագրությունը կերկարաձգվի [bonus_days] օրով:
Ձեր ուղղորդման հղումն է 
<code>[ref_link]</code>''', '''Отправьте эту ссылку своим друзьям, и если они воспользуются этим ботом, вы получите бонус.
За каждого [bonus_refs] реферала ваша Премиум-подписка будет продлена на [bonus_days] дней.
Ваша реферальная ссылка 
<code>[ref_link]</code>''', '''Send this link to your friends and if they use this bot you will get a bonus. 
For every [bonus_refs] referrals your Premium subscription will be prolonged for [bonus_days] days.
Your referral link is 
<code>[ref_link]</code>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[bonus_refs]",str(bonus_refs)).replace("[bonus_days]",str(bonus_days)).replace("[ref_link]",str(ref_link))

def no_referral_bonus(cid : int,referrals,nrefs,ndays, all : bool = False) -> str:
    '''You have [referrals] referrals. You need at least [nrefs] referrals to get bonus [ndays] days.'''
    phrases = ['''Դուք ունեք [referrals] ուղղորդումներ: Ձեզ անհրաժեշտ են առնվազն [nrefs] ուղղորդումներ՝ բոնուսային [ndays] օրեր ստանալու համար:''', '''У вас есть [referrals] рефералов. Вам нужно как минимум [nrefs] рефералов, чтобы получить бонусные [ndays] дней.''', '''You have [referrals] referrals. You need at least [nrefs] referrals to get bonus [ndays] days.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[referrals]",str(referrals)).replace("[nrefs]",str(nrefs)).replace("[ndays]",str(ndays))

def referral_bonus(cid : int,referrals,ndays, all : bool = False) -> str:
    '''You have [referrals] referrals. Press this button to get your [ndays] days bonus 😀'''
    phrases = ['''Դուք ունեք [referrals] ուղղորդումներ: Սեղմեք այս կոճակը՝ ձեր [ndays] օրվա բոնուսը ստանալու համար 😀''', '''У вас есть [referrals] рефералов. Нажмите эту кнопку, чтобы получить бонус [ndays] дней 😀''', '''You have [referrals] referrals. Press this button to get your [ndays] days bonus 😀''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[referrals]",str(referrals)).replace("[ndays]",str(ndays))

def get_referral_bonus(cid : int, all : bool = False) -> str:
    '''🎉 GET BONUS!!! 🎉'''
    phrases = ['''🎉 ՍՏԱՆԱԼ ԲՈՆՈՒՍ!!! 🎉''', '''🎉 ПОЛУЧИТЕ БОНУС!!! 🎉''', '''🎉 GET BONUS!!! 🎉''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def congratulate_bonus(cid : int,ndays, all : bool = False) -> str:
    '''🎉 Congratulations!!! 🎉
 You got [ndays] days bonus.'''
    phrases = ['''🎉 Շնորհավորում ենք!!! 🎉
 դուք ստացաք [ndays] օրվա բոնուս:''', '''🎉 Поздравляем!!! 🎉
 Вы получили бонус [ndays] дней.''', '''🎉 Congratulations!!! 🎉
 You got [ndays] days bonus.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[ndays]",str(ndays))

def phone_number(cid : int, all : bool = False) -> str:
    '''Phone number'''
    phrases = ['''Հեռախոսահամար''', '''Номер телефона''', '''Phone number''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def deleted(cid : int, all : bool = False) -> str:
    '''❌ Deleted ❌'''
    phrases = ['''❌ Ջնջված է ❌''', '''❌ Удалено ❌''', '''❌ Deleted ❌''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def delete(cid : int, all : bool = False) -> str:
    '''❌ Delete'''
    phrases = ['''❌ Ջնջել''', '''❌ Удалить''', '''❌ Delete''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def menu(cid : int, all : bool = False) -> str:
    '''📜 Menu'''
    phrases = ['''📜 Մենյու''', '''📜 Меню''', '''📜 Menu''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def main_menu(cid : int, all : bool = False) -> str:
    '''📜 Menu
Buttons marked with ⭐️ have actions which require Premium subscription.'''
    phrases = ['''📜 Մենյու
⭐️-ով նշված կոճակներն ունեն գործողություններ, որոնք պահանջում են Պրեմիում բաժանորդագրություն:''', '''📜 Меню
Кнопки, отмеченные ⭐️, имеют действия, требующие Премиум-подписки.''', '''📜 Menu
Buttons marked with ⭐️ have actions which require Premium subscription.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def get_car_price(cid : int, all : bool = False) -> str:
    '''🚗 Your car price'''
    phrases = ['''🚗 Ձեր մեքենայի արժեքը''', '''🚗 Цена вашего автомобиля''', '''🚗 Your car price''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def import_from_listam(cid : int, all : bool = False) -> str:
    '''🧾 Import from List.am⭐️'''
    phrases = ['''🧾 Ներմուծել List.am-ից⭐️''', '''🧾 Импорт из List.am⭐️''', '''🧾 Import from List.am⭐️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def import_from_myautoge(cid : int, all : bool = False) -> str:
    '''🧾 Import from MyAuto.ge⭐️'''
    phrases = ['''🧾 Ներմուծել MyAuto.ge-ից⭐️''', '''🧾 Импорт из MyAuto.ge⭐️''', '''🧾 Import from MyAuto.ge⭐️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def saved_cars(cid : int, all : bool = False) -> str:
    '''📌 Saved cars⭐️'''
    phrases = ['''📌 Պահպանված մեքենաներ⭐️''', '''📌 Сохраненные автомобили⭐️''', '''📌 Saved cars⭐️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def general_info(cid : int, all : bool = False) -> str:
    '''ℹ️ Info'''
    phrases = ['''ℹ️ Ինֆո''', '''ℹ️ Информация''', '''ℹ️ Info''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def found_saved_car(cid : int,nCars, all : bool = False) -> str:
    '''Based on your saved car`s parameters I found [nCars] cars. You can always see this list in the "📌 Saved cars" menu.
'''
    phrases = ['''Ձեր պահպանված մեքենայի պարամետրերի հիման վրա ես գտա [nCars] մեքենաներ: Այս ցանկը միշտ կարող եք տեսնել «📌 Պահպանված մեքենաներ» բաժնում։
''', '''По вашим сохраненным параметрам автомобиля я нашел [nCars] автомобилей. Вы всегда можете увидеть этот список в меню "📌 Сохраненные автомобили".
''', '''Based on your saved car`s parameters I found [nCars] cars. You can always see this list in the "📌 Saved cars" menu.
''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[nCars]",str(nCars))

def found_cars_so_far(cid : int,nCars, all : bool = False) -> str:
    '''Found [nCars] cars so far.'''
    phrases = ['''Մինչ այժմ գտնվել են [nCars] մեքենաներ:''', '''На данный момент найдено [nCars] автомобилей.''', '''Found [nCars] cars so far.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[nCars]",str(nCars))

def add_ad(cid : int, all : bool = False) -> str:
    '''Add advertisement'''
    phrases = ['''Add advertisement''', '''Add advertisement''', '''Add advertisement''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def visit_website(cid : int, all : bool = False) -> str:
    '''Visit website'''
    phrases = ['''Visit website''', '''Visit website''', '''Visit website''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def list_am_usage(cid : int, all : bool = False) -> str:
    '''Import car detailes from List.am by copy and pasting the car page url here, like "https://www.list.am/item/19911991"'''
    phrases = ['''Ներմուծեք ավտոմեքենայի տվյալները List.am-ից՝ պատճենելով և տեղադրելով մեքենայի էջի url-ը այստեղ, օրինակ՝ «https://www.list.am/item/19911991»''', '''Импортируйте информацию об автомобиле из List.am, скопировав и вставив URL-адрес страницы автомобиля, например «https://www.list.am/item/19911991».''', '''Import car detailes from List.am by copy and pasting the car page url here, like "https://www.list.am/item/19911991"''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def listam_not_possible(cid : int, all : bool = False) -> str:
    '''I cant import this cars data, try another one.'''
    phrases = ['''Ես չեմ կարող ներմուծել այս մեքենաների տվյալները, փորձեք մեկ ուրիշը:''', '''Я не могу импортировать данные этого автомобиля, попробуйте другой.''', '''I cant import this cars data, try another one.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def search_for_cars(cid : int, all : bool = False) -> str:
    '''Search for cars like this'''
    phrases = ['''Փնտրել նման մեքենաներ''', '''Искать такие машины''', '''Search for cars like this''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def listam_what_to_do(cid : int, all : bool = False) -> str:
    '''What do you want to do with this?'''
    phrases = ['''Ի՞նչ եք ուզում անել սրա հետ:''', '''Что вы хотите с этим делать?''', '''What do you want to do with this?''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def myautoge_usage(cid : int, all : bool = False) -> str:
    '''Import car detailes from MyAuto.ge by copy and pasting the car page url here, like <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>'''
    phrases = ['''Ներմուծեք ավտոմեքենայի տվյալները MyAuto.ge-ից՝ պատճենելով և տեղադրելով մեքենայի էջի url-ը այստեղ, օրինակ՝ <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>''', '''Импортируйте информацию об автомобиле из MyAuto.ge, скопировав и вставив URL-адрес страницы автомобиля, например <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>.''', '''Import car detailes from MyAuto.ge by copy and pasting the car page url here, like <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def myautoge_not_possible(cid : int, all : bool = False) -> str:
    '''I cant import this cars data, try another one.'''
    phrases = ['''Ես չեմ կարող ներմուծել այս մեքենաների տվյալները, փորձեք մեկ ուրիշը:''', '''Я не могу импортировать данные этого автомобиля, попробуйте другой.''', '''I cant import this cars data, try another one.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def myautoge_what_to_do(cid : int, all : bool = False) -> str:
    '''What do you want to do with this?'''
    phrases = ['''Ի՞նչ եք ուզում անել սրա հետ:''', '''Что вы хотите с этим делать?''', '''What do you want to do with this?''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def import_data(cid : int, all : bool = False) -> str:
    '''Import car parameters'''
    phrases = ['''Ներմուծել ավտոմեքենայի պարամետրերը''', '''Импорт параметров автомобиля''', '''Import car parameters''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def show_price_updates(cid : int, all : bool = False) -> str:
    '''Show price updates⭐️'''
    phrases = ['''Ցույց տալ գների թարմացումները⭐️''', '''Показать изменения цен⭐️''', '''Show price updates⭐️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def follow_price_updates(cid : int, all : bool = False) -> str:
    '''Follow future updates⭐️'''
    phrases = ['''Հետևեք ապագա թարմացումներին⭐️''', '''Следите за будущими обновлениями⭐️''', '''Follow future updates⭐️''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def no_price_updates(cid : int, all : bool = False) -> str:
    '''❌ No price updates!'''
    phrases = ['''❌ Գների թարմացումներ չկան:''', '''❌Нет обновлений цен!''', '''❌ No price updates!''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def follow_successfull(cid : int,car_brand,model,year,engine_size,price, all : bool = False) -> str:
    '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Car saved'''
    phrases = ['''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Մեքենան պահպանված է''', '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Автомобиль сохранен''', '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Car saved''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[car_brand]",str(car_brand)).replace("[model]",str(model)).replace("[year]",str(year)).replace("[engine_size]",str(engine_size)).replace("[price]",str(price))

def remove_follow(cid : int, all : bool = False) -> str:
    '''❌ Unfollow'''
    phrases = ['''❌ Չհետևել''', '''❌ Отписаться''', '''❌ Unfollow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def notify_price_update(cid : int,car_brand,model,year,engine_size,old_price,new_price,url, all : bool = False) -> str:
    '''[car_brand] [model] 
[year]   [engine_size] L

Old price - [old_price] $
New price - [new_price] $

[url]'''
    phrases = ['''[car_brand] [model] 
[year]   [engine_size] L

Հին արժեք - [old_price] $
Նոր արժեք - [new_price] $

[url]''', '''[car_brand] [model] 
[year]   [engine_size] L

Старая цена - [old_price] $
Новая цена  - [new_price] $

[url]''', '''[car_brand] [model] 
[year]   [engine_size] L

Old price - [old_price] $
New price - [new_price] $

[url]''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[car_brand]",str(car_brand)).replace("[model]",str(model)).replace("[year]",str(year)).replace("[engine_size]",str(engine_size)).replace("[old_price]",str(old_price)).replace("[new_price]",str(new_price)).replace("[url]",str(url))

def add_saved_car(cid : int, all : bool = False) -> str:
    '''➕ Add car'''
    phrases = ['''➕ Ավելացնել մեքենա''', '''➕ Добавить машину''', '''➕ Add car''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def saved_cars_info(cid : int, all : bool = False) -> str:
    '''Here you can add cars and when there is a similar car on the market, bot will notify you.'''
    phrases = ['''Այստեղ դուք կարող եք ավելացնել մեքենաներ, և երբ շուկայում նման մեքենա լինի, բոտը ձեզ կտեղեկացնի:''', '''Здесь вы можете добавлять автомобили и когда на рынке появится похожий автомобиль, бот уведомит вас об этом.''', '''Here you can add cars and when there is a similar car on the market, bot will notify you.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def save_car(cid : int, all : bool = False) -> str:
    '''📌 Save car'''
    phrases = ['''📌 Պահպանել մեքենան''', '''📌 Сохранить машину''', '''📌 Save car''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def car_saved(cid : int, all : bool = False) -> str:
    '''✅ Car saved'''
    phrases = ['''✅ Մեքենան պահպանված է''', '''✅ Автомобиль сохранен''', '''✅ Car saved''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_mileage_start(cid : int, all : bool = False) -> str:
    '''Please choose the minimal mileage of the car.'''
    phrases = ['''Խնդրում ենք ընտրել մեքենայի նվազագույն վազքը:''', '''Пожалуйста, выберите минимальный пробег автомобиля.''', '''Please choose the minimal mileage of the car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_mileage_end(cid : int, all : bool = False) -> str:
    '''Please choose the maximal mileage of the car.'''
    phrases = ['''Խնդրում ենք ընտրել մեքենայի առավելագույն վազքը:''', '''Пожалуйста, выберите максимальный пробег автомобиля.''', '''Please choose the maximal mileage of the car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_price_start(cid : int, all : bool = False) -> str:
    '''Please choose the minimal price of the car.'''
    phrases = ['''Խնդրում ենք ընտրել մեքենայի նվազագույն արժեքը:''', '''Пожалуйста, выберите минимальную цену автомобиля.''', '''Please choose the minimal price of the car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_price_end(cid : int, all : bool = False) -> str:
    '''Please choose the maximal price of the car.'''
    phrases = ['''Խնդրում ենք ընտրել մեքենայի առավելագույն արժեքը:''', '''Пожалуйста, выберите максимальную цену автомобиля.''', '''Please choose the maximal price of the car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def wrong_format(cid : int, all : bool = False) -> str:
    '''❌ Wrong format, try again'''
    phrases = ['''❌ Սխալ ձևաչափ, նորից փորձեք''', '''❌ Неверный формат, попробуйте еще раз''', '''❌ Wrong format, try again''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def year(cid : int,year, all : bool = False) -> str:
    '''[year]'''
    phrases = ['''[year] թ․''', '''[year]''', '''[year]''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[year]",str(year))

def mileage(cid : int,mileage, all : bool = False) -> str:
    '''[mileage] km'''
    phrases = ['''[mileage] կմ''', '''[mileage] km''', '''[mileage] km''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[mileage]",str(mileage))

def engine_size(cid : int,engine_size, all : bool = False) -> str:
    '''[engine_size] L'''
    phrases = ['''[engine_size] L''', '''[engine_size] L''', '''[engine_size] L''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[engine_size]",str(engine_size))

def interior_color(cid : int,interior_color, all : bool = False) -> str:
    '''[interior_color] interior'''
    phrases = ['''[interior_color] ինտերիեր''', '''[interior_color] интерьер''', '''[interior_color] interior''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[interior_color]",str(interior_color))

def interior_material(cid : int,interior_material, all : bool = False) -> str:
    '''[interior_material]'''
    phrases = ['''[interior_material]''', '''[interior_material]''', '''[interior_material]''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[interior_material]",str(interior_material))

def wheel_size(cid : int,wheel_size, all : bool = False) -> str:
    '''R[wheel_size]'''
    phrases = ['''R[wheel_size]''', '''R[wheel_size]''', '''R[wheel_size]''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[wheel_size]",str(wheel_size))

def calculate(cid : int, all : bool = False) -> str:
    '''Calculate'''
    phrases = ['''Հաշվել''', '''Рассчитать''', '''Calculate''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def calculate_by_year(cid : int, all : bool = False) -> str:
    '''📈 Price graph by year'''
    phrases = ['''📈 Գների գրաֆիկը ըստ տարիների''', '''📈 График цен по годам''', '''📈 Price graph by year''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def calculate_by_mileage(cid : int, all : bool = False) -> str:
    '''📉 Price graph by mileage'''
    phrases = ['''📉 Գների գրաֆիկը ըստ վազքի''', '''📉 График цен по пробегу''', '''📉 Price graph by mileage''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def label_price(cid : int, all : bool = False) -> str:
    '''Price'''
    phrases = ['''Գինը''', '''Цена''', '''Price''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def label_year(cid : int, all : bool = False) -> str:
    '''Year'''
    phrases = ['''Տարի''', '''Год''', '''Year''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def label_mileage(cid : int, all : bool = False) -> str:
    '''Mileage'''
    phrases = ['''Վազքը''', '''Пробег''', '''Mileage''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def calculate_result_title(cid : int,url, all : bool = False) -> str:
    '''[url]
💰  PRICE INFO  💰
'''
    phrases = ['''[url]
💰 ԳՆԵՐԻ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ 💰
''', '''[url]
💰ИНФОРМАЦИЯ О ЦЕНАХ 💰
''', '''[url]
💰  PRICE INFO  💰
''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[url]",str(url))

def result_arm(cid : int,l_price, all : bool = False) -> str:
    '''Armenian market : [l_price] $ 💵'''
    phrases = ['''Հայկական շուկա : [l_price] $ 💵''', '''Армянский  рынок : [l_price] $ 💵''', '''Armenian market : [l_price] $ 💵''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[l_price]",str(l_price))

def result_ge(cid : int,g_price, all : bool = False) -> str:
    '''Georgian market : [g_price] $ 💵'''
    phrases = ['''Վրացական շուկա : [g_price] $ 💵''', '''Грузинский рынок : [g_price] $ 💵''', '''Georgian market : [g_price] $ 💵''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[g_price]",str(g_price))

def result_ge_not_available(cid : int, all : bool = False) -> str:
    '''Georgian market : ??? $ 💵
⭐️To know the prices in Georgia sign up for Premium subscription'''
    phrases = ['''Վրացական շուկա : ??? $ 💵
⭐️Վրաստանի գները իմանալու համար գրանցվեք Պրեմիում բաժանորդագրության համար''', '''Грузинский рынок : ??? $ 💵
⭐️Чтобы узнать цены в Грузии, подпишитесь на Премиум подписку''', '''Georgian market : ??? $ 💵
⭐️To know the prices in Georgia sign up for Premium subscription''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def price_result_ask(cid : int, all : bool = False) -> str:
    '''Do you think this car is reasonably priced in Armenian market? You dont have to answer this but it will help build a better AI.'''
    phrases = ['''Ի՞նչ եք կարծում, այս մեքենան խելամի՞տ է գնահատված Հայկական շուկայում: Պարտադիր չէ պատասխանեք այս հարցին, բայց դա կօգնի ավելի խելացի արհեստական ինտելեկտ կառուցել:''', '''Считаете ли вы, что этот автомобиль имеет разумную цену на Армянском рынке?? Вам не обязательно отвечать на этот вопрос, но это поможет создать более умный ИИ.''', '''Do you think this car is reasonably priced in Armenian market? You dont have to answer this but it will help build a better AI.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def calculation_not_possible(cid : int, all : bool = False) -> str:
    '''❌ Price calculation is not possible for this car!'''
    phrases = ['''❌ Այս մեքենայի համար գնի հաշվարկ հնարավոր չէ։''', '''❌ Расчет цены для данного автомобиля невозможен!''', '''❌ Price calculation is not possible for this car!''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def dont_know(cid : int, all : bool = False) -> str:
    '''I don't know'''
    phrases = ['''Չգիտեմ''', '''Я не знаю''', '''I don't know''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def my_price(cid : int, all : bool = False) -> str:
    '''Offer my price'''
    phrases = ['''Առաջարկել իմ գինը''', '''Предложить мою цену''', '''Offer my price''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def my_price_offer(cid : int, all : bool = False) -> str:
    '''What do you think this car costs in dollars? Write your answer like this "18000" '''
    phrases = ['''Ի՞նչ եք կարծում, ինչ արժե այս մեքենան դոլլարով: Գրեք ձեր պատասխանը այսպես «18000»''', '''Как вы думаете, сколько долларов стоит эта машина? Напишите свой ответ так: "18000"''', '''What do you think this car costs in dollars? Write your answer like this "18000" ''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def thanks_for_opinion(cid : int, all : bool = False) -> str:
    '''Thank you for your opinion 👌'''
    phrases = ['''Շնորհակալություն կարծիքի համար 👌''', '''Спасибо за ваше мнение 👌''', '''Thank you for your opinion 👌''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def car_price_info(cid : int,satisfied,notsatisfied,percent, all : bool = False) -> str:
    '''Satisfaction: [satisfied][notsatisfied] [percent]%
Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car in Armenia. Dont base your decisions only on this results when buying or selling.'''
    phrases = ['''Գոհունակություն. [satisfied][notsatisfied] [percent]%
Ընտրեք մեքենայի պարամետրերը և սեղմեք հաշվարկել՝ գինը ստանալու համար:
⚠️Արհեստական ինտելեկտը հաշվարկում է այս կոնկրետ մեքենայի ՄԻՋԻՆ ՇՈՒԿԱՅԱԿԱՆ ԱՐԺԵՔԸ հայաստանում: Գնելիս կամ վաճառելիս մի հիմնեք ձեր որոշումները միայն այս արդյունքների վրա:''', '''Удовлетворенность: [satisfied][notsatisfied] [percent]%
Выберите параметры автомобиля и нажмите рассчитать, чтобы узнать цену․
⚠️ИИ рассчитывает СРЕДНЮЮ РЫНОЧНУЮ СТОИМОСТЬ для данного конкретного автомобиля в Армении․ Не основывайте свои решения только на этих результатах при покупке или продаже.''', '''Satisfaction: [satisfied][notsatisfied] [percent]%
Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car in Armenia. Dont base your decisions only on this results when buying or selling.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[satisfied]",str(satisfied)).replace("[notsatisfied]",str(notsatisfied)).replace("[percent]",str(percent))

def choose_car_brand(cid : int, all : bool = False) -> str:
    '''Please choose the brand of your car. If the brand of your car is not shown below it means there is not enough data and the AI cant make a good prediction.'''
    phrases = ['''Խնդրում եմ ընտրեք ձեր մեքենայի մակնիշը։ Եթե ստորև ներկայացված չէ ձեր մեքենայի մակնիշը, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:''', '''Пожалуйста, выберите марку вашего автомобиля. Если марка вашего автомобиля не указана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.''', '''Please choose the brand of your car. If the brand of your car is not shown below it means there is not enough data and the AI cant make a good prediction.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_model(cid : int, all : bool = False) -> str:
    '''Please choose the model of your car. If the model of your car is not shown below it means there is not enough data and the AI cant make a good prediction.'''
    phrases = ['''Խնդրում եմ ընտրել ձեր մեքենայի մոդելը։ Եթե ձեր մեքենայի մոդելը ներկայացված չէ ստորև, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:''', '''Пожалуйста, выберите модель вашего автомобиля. Если модель вашего автомобиля не показана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.''', '''Please choose the model of your car. If the model of your car is not shown below it means there is not enough data and the AI cant make a good prediction.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_year(cid : int, all : bool = False) -> str:
    '''Please choose the manufacturing year of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի արտադրության տարեթիվը:''', '''Пожалуйста, выберите год выпуска вашего автомобиля.''', '''Please choose the manufacturing year of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_mileage(cid : int, all : bool = False) -> str:
    '''Please choose the mileage of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի վազքը:''', '''Пожалуйста, выберите пробег вашего автомобиля.''', '''Please choose the mileage of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_engine_size(cid : int, all : bool = False) -> str:
    '''Please choose the engine size of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի շարժիչի չափը:''', '''Пожалуйста, выберите объем двигателя вашего автомобиля.''', '''Please choose the engine size of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_exterior_color(cid : int, all : bool = False) -> str:
    '''Please choose the exterior color of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի արտաքին գույնը:''', '''Пожалуйста, выберите цвет кузова вашего автомобиля.''', '''Please choose the exterior color of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_body_type(cid : int, all : bool = False) -> str:
    '''Please choose the body type of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի թափքի տեսակը:''', '''Пожалуйста, выберите тип кузова вашего автомобиля.''', '''Please choose the body type of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_engine_type(cid : int, all : bool = False) -> str:
    '''Please choose the engine type of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի շարժիչի տեսակը:''', '''Пожалуйста, выберите тип двигателя вашего автомобиля.''', '''Please choose the engine type of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_transmission(cid : int, all : bool = False) -> str:
    '''Please choose the transmission type of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի փոխանցման տուփի տեսակը:''', '''Пожалуйста, выберите тип трансмиссии вашего автомобиля.''', '''Please choose the transmission type of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_drive_type(cid : int, all : bool = False) -> str:
    '''Please choose the drive type of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի վարման տեսակը:''', '''Пожалуйста, выберите тип привода вашего автомобиля.''', '''Please choose the drive type of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_condition(cid : int, all : bool = False) -> str:
    '''Please choose the condition of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի վիճակը։''', '''Пожалуйста, выберите состояние вашего автомобиля.''', '''Please choose the condition of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_gas_equipment(cid : int, all : bool = False) -> str:
    '''Please specify if your car has gas equipment.'''
    phrases = ['''Խնդրում ենք նշել, թե արդյոք ձեր մեքենան ունի գազի սարքավորումներ:''', '''Пожалуйста, уточните, есть ли в вашем автомобиле газовое оборудование.''', '''Please specify if your car has gas equipment.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_steering_wheel(cid : int, all : bool = False) -> str:
    '''Please choose the steering wheel position of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի ղեկի դիրքը:''', '''Пожалуйста, выберите положение рулевого колеса вашего автомобиля.''', '''Please choose the steering wheel position of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_headlights(cid : int, all : bool = False) -> str:
    '''Please specify the type of headlights in your car.'''
    phrases = ['''Խնդրում եմ նշեք ձեր մեքենայի լուսարձակների տեսակը:''', '''Пожалуйста, укажите тип фар в вашем автомобиле.''', '''Please specify the type of headlights in your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_interior_color(cid : int, all : bool = False) -> str:
    '''Please choose the interior color of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի սրահի գույնը:''', '''Пожалуйста, выберите цвет салона вашего автомобиля.''', '''Please choose the interior color of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_interior_material(cid : int, all : bool = False) -> str:
    '''Please choose the interior material of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի սրահի նյութը:''', '''Пожалуйста, выберите материал салона вашего автомобиля.''', '''Please choose the interior material of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_sunroof(cid : int, all : bool = False) -> str:
    '''Please specify if your car has a sunroof.'''
    phrases = ['''Խնդրում ենք նշել, թե արդյոք ձեր մեքենան ունի լուսային տանիք:''', '''Пожалуйста, укажите, есть ли в вашем автомобиле люк на крыше.''', '''Please specify if your car has a sunroof.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_wheel_size(cid : int, all : bool = False) -> str:
    '''Please choose the wheel size of your car.'''
    phrases = ['''Խնդրում ենք ընտրել ձեր մեքենայի անիվի չափը:''', '''Пожалуйста, выберите размер колес вашего автомобиля.''', '''Please choose the wheel size of your car.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def best_offers(cid : int, all : bool = False) -> str:
    '''Best offers'''
    phrases = ['''Լավագույն առաջարկներ''', '''Лучшие предложения''', '''Best offers''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_marz(cid : int, all : bool = False) -> str:
    '''Choose region'''
    phrases = ['''Ընտրեք տարածաշրջան''', '''Выберите регион''', '''Choose region''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_YEREVAN(cid : int, all : bool = False) -> str:
    '''Yerevan'''
    phrases = ['''Երևան''', '''Ереван''', '''Yerevan''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_ARMAVIR(cid : int, all : bool = False) -> str:
    '''Armavir'''
    phrases = ['''Արմավիր''', '''Армавир''', '''Armavir''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_ARARAT(cid : int, all : bool = False) -> str:
    '''Ararat'''
    phrases = ['''Արարատ''', '''Арарат''', '''Ararat''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_KOTAYK(cid : int, all : bool = False) -> str:
    '''Kotayk'''
    phrases = ['''Կոտայք''', '''Котайк''', '''Kotayk''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_SHIRAK(cid : int, all : bool = False) -> str:
    '''Shirak'''
    phrases = ['''Շիրակ''', '''Ширак''', '''Shirak''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_LORRI(cid : int, all : bool = False) -> str:
    '''Lorri'''
    phrases = ['''Լոռի''', '''Лори''', '''Lorri''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_GEGHARKUNIK(cid : int, all : bool = False) -> str:
    '''Gegharkunik'''
    phrases = ['''Գեղարքունիք''', '''Гегаркуник''', '''Gegharkunik''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_SYUNIK(cid : int, all : bool = False) -> str:
    '''Syunik'''
    phrases = ['''Սյունիք''', '''Сюник''', '''Syunik''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_ARAGATSOTN(cid : int, all : bool = False) -> str:
    '''Aragatsotn'''
    phrases = ['''Արագածոտն''', '''Арагацотн''', '''Aragatsotn''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_TAVUSH(cid : int, all : bool = False) -> str:
    '''Tavush'''
    phrases = ['''Տավուշ''', '''Тавуш''', '''Tavush''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_VAYOTS_DZOR(cid : int, all : bool = False) -> str:
    '''Vayots Dzor'''
    phrases = ['''Վայոց ձոր''', '''Вайоц Дзор''', '''Vayots Dzor''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def marz_ARTSAKH(cid : int, all : bool = False) -> str:
    '''Artsakh'''
    phrases = ['''Արցախ''', '''Арцах''', '''Artsakh''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def sedan(cid : int, all : bool = False) -> str:
    '''Sedan'''
    phrases = ['''Սեդան''', '''Седан''', '''Sedan''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def hatchback(cid : int, all : bool = False) -> str:
    '''Hatchback'''
    phrases = ['''Հետչբեք''', '''Хэтчбек''', '''Hatchback''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def wagon(cid : int, all : bool = False) -> str:
    '''Wagon'''
    phrases = ['''Ունիվերսալ''', '''Универсал''', '''Wagon''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def coupe(cid : int, all : bool = False) -> str:
    '''Coupe'''
    phrases = ['''Կուպե''', '''Купе''', '''Coupe''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def crossover(cid : int, all : bool = False) -> str:
    '''SUV / Crossover'''
    phrases = ['''Ամենագնաց / Քրոսսովեր''', '''Внедорожник / Кроссовер''', '''SUV / Crossover''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def minivan(cid : int, all : bool = False) -> str:
    '''Minivan'''
    phrases = ['''Մինիվեն''', '''Минивэн''', '''Minivan''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def pickup(cid : int, all : bool = False) -> str:
    '''Pickup'''
    phrases = ['''Փիքափ''', '''Пикап''', '''Pickup''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def minibus(cid : int, all : bool = False) -> str:
    '''Minibus'''
    phrases = ['''Միկրոավտոբուս''', '''Микроавтобус''', '''Minibus''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def van(cid : int, all : bool = False) -> str:
    '''Van'''
    phrases = ['''Ֆուրգոն''', '''Фургон''', '''Van''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def convertible(cid : int, all : bool = False) -> str:
    '''Convertible'''
    phrases = ['''Կաբրիոլետ''', '''Кабриолет''', '''Convertible''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def limo(cid : int, all : bool = False) -> str:
    '''Limo'''
    phrases = ['''Լիմուզին''', '''Лимузин''', '''Limo''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def roadster(cid : int, all : bool = False) -> str:
    '''Roadster'''
    phrases = ['''Ռոդսթեր''', '''Родстер''', '''Roadster''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def liftback(cid : int, all : bool = False) -> str:
    '''Liftback'''
    phrases = ['''Լիֆտբեկ''', '''Лифтбек''', '''Liftback''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def fastback(cid : int, all : bool = False) -> str:
    '''Fastback'''
    phrases = ['''Ֆաստբեկ''', '''Фастбек''', '''Fastback''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def compact_mpv(cid : int, all : bool = False) -> str:
    '''Compact MPV'''
    phrases = ['''Կոմպակտվեն''', '''Компактвэн''', '''Compact MPV''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def gasoline(cid : int, all : bool = False) -> str:
    '''Gasoline'''
    phrases = ['''Բենզին''', '''Бензин''', '''Gasoline''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def diesel(cid : int, all : bool = False) -> str:
    '''Diesel'''
    phrases = ['''Դիզել''', '''Дизель''', '''Diesel''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def hybrid(cid : int, all : bool = False) -> str:
    '''Hybrid'''
    phrases = ['''Հիբրիդ''', '''Гибрид''', '''Hybrid''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def electric(cid : int, all : bool = False) -> str:
    '''Electric'''
    phrases = ['''էլեկտրական''', '''Электро''', '''Electric''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def hydrogen(cid : int, all : bool = False) -> str:
    '''Hydrogen'''
    phrases = ['''Ջրածնային''', '''Водородный''', '''Hydrogen''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def manual(cid : int, all : bool = False) -> str:
    '''Manual'''
    phrases = ['''Մեխանիկական''', '''Механическая''', '''Manual''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def automatic(cid : int, all : bool = False) -> str:
    '''Automatic'''
    phrases = ['''Ավտոմատ''', '''Автоматическая''', '''Automatic''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def front_wheel_drive(cid : int, all : bool = False) -> str:
    '''Front Wheel Drive'''
    phrases = ['''Առջևի քարշակ''', '''Передний привод''', '''Front Wheel Drive''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def rear_wheel_drive(cid : int, all : bool = False) -> str:
    '''Rear Wheel Drive'''
    phrases = ['''Ետևի քարշակ''', '''Задний привод''', '''Rear Wheel Drive''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def all_wheel_drive(cid : int, all : bool = False) -> str:
    '''All Wheel Drive'''
    phrases = ['''Լիաքարշակ''', '''Полный привод''', '''All Wheel Drive''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def car_is_not_damaged(cid : int, all : bool = False) -> str:
    '''Car is not damaged'''
    phrases = ['''Չվթարված''', '''Не битое''', '''Car is not damaged''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def car_is_damaged(cid : int, all : bool = False) -> str:
    '''Car is damaged'''
    phrases = ['''Վթարված''', '''Битое''', '''Car is damaged''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def gas_no(cid : int, all : bool = False) -> str:
    '''Gas not Installed'''
    phrases = ['''Գազ չտեղադրված''', '''Газ не установлен''', '''Gas not Installed''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def gas_installed(cid : int, all : bool = False) -> str:
    '''Gas installed'''
    phrases = ['''Գազ տեղադրված''', '''Газ установлен''', '''Gas installed''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def left_steering(cid : int, all : bool = False) -> str:
    '''Left hand drive'''
    phrases = ['''Ղեկը ձախ''', '''Левый руль''', '''Left hand drive''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def right_steering(cid : int, all : bool = False) -> str:
    '''Right hand drive'''
    phrases = ['''Ղեկը աջ''', '''Правый руль''', '''Right hand drive''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_white(cid : int, all : bool = False) -> str:
    '''White'''
    phrases = ['''Սպիտակ''', '''Белый''', '''White''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_silver(cid : int, all : bool = False) -> str:
    '''Silver'''
    phrases = ['''Արծաթագույն''', '''Серебряный''', '''Silver''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_gray(cid : int, all : bool = False) -> str:
    '''Gray'''
    phrases = ['''Մոխրագույն''', '''Серый''', '''Gray''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_black(cid : int, all : bool = False) -> str:
    '''Black'''
    phrases = ['''Սև''', '''Чёрный''', '''Black''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_brown(cid : int, all : bool = False) -> str:
    '''Brown'''
    phrases = ['''Շագանակագույն''', '''Коричневый''', '''Brown''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_gold(cid : int, all : bool = False) -> str:
    '''Gold'''
    phrases = ['''Ոսկեգույն''', '''Золотой''', '''Gold''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_beige(cid : int, all : bool = False) -> str:
    '''Beige'''
    phrases = ['''Բեժ''', '''Бежевый''', '''Beige''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_red(cid : int, all : bool = False) -> str:
    '''Red'''
    phrases = ['''Կարմիր''', '''Красный''', '''Red''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_blue(cid : int, all : bool = False) -> str:
    '''Blue'''
    phrases = ['''Կապույտ''', '''Синий''', '''Blue''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_orange(cid : int, all : bool = False) -> str:
    '''Orange'''
    phrases = ['''Նարնջագույն''', '''Оранжевый''', '''Orange''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_yellow(cid : int, all : bool = False) -> str:
    '''Yellow'''
    phrases = ['''Դեղին''', '''Жёлтый''', '''Yellow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_green(cid : int, all : bool = False) -> str:
    '''Green'''
    phrases = ['''Կանաչ''', '''Зелёный''', '''Green''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_cyan(cid : int, all : bool = False) -> str:
    '''Cyan'''
    phrases = ['''Երկնագույն''', '''Голубой''', '''Cyan''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_maroon(cid : int, all : bool = False) -> str:
    '''Maroon'''
    phrases = ['''Բորդո''', '''Бордовый''', '''Maroon''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_pink(cid : int, all : bool = False) -> str:
    '''Pink'''
    phrases = ['''Վարդագույն''', '''Розовый''', '''Pink''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def exterior_purple(cid : int, all : bool = False) -> str:
    '''Purple'''
    phrases = ['''Մանուշակագույն''', '''Фиолетовый''', '''Purple''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_white(cid : int, all : bool = False) -> str:
    '''White'''
    phrases = ['''Սպիտակ''', '''Белый''', '''White''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_gray(cid : int, all : bool = False) -> str:
    '''Gray'''
    phrases = ['''Մոխրագույն''', '''Серый''', '''Gray''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_black(cid : int, all : bool = False) -> str:
    '''Black'''
    phrases = ['''Սև''', '''Чёрный''', '''Black''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_brown(cid : int, all : bool = False) -> str:
    '''Brown'''
    phrases = ['''Շագանակագույն''', '''Коричневый''', '''Brown''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_beige(cid : int, all : bool = False) -> str:
    '''Beige'''
    phrases = ['''Բեժ''', '''Бежевый''', '''Beige''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_red(cid : int, all : bool = False) -> str:
    '''Red'''
    phrases = ['''Կարմիր''', '''Красный''', '''Red''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_blue(cid : int, all : bool = False) -> str:
    '''Blue'''
    phrases = ['''Կապույտ''', '''Синий''', '''Blue''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_other(cid : int, all : bool = False) -> str:
    '''Other'''
    phrases = ['''Այլ''', '''Другой''', '''Other''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_gold(cid : int, all : bool = False) -> str:
    '''Gold'''
    phrases = ['''Ոսկեգույն''', '''Золотой''', '''Gold''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_maroon(cid : int, all : bool = False) -> str:
    '''Maroon'''
    phrases = ['''Բորդո''', '''Бордовый''', '''Maroon''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_orange(cid : int, all : bool = False) -> str:
    '''Orange'''
    phrases = ['''Նարնջագույն''', '''Оранжевый''', '''Orange''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def interior_yellow(cid : int, all : bool = False) -> str:
    '''Yellow'''
    phrases = ['''Դեղին''', '''Жёлтый''', '''Yellow''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def no_sunroof(cid : int, all : bool = False) -> str:
    '''No sunroof'''
    phrases = ['''Լյուկ չկա''', '''Люка нет''', '''No sunroof''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def regular_sunroof_sunroof(cid : int, all : bool = False) -> str:
    '''Regular sunroof'''
    phrases = ['''Սովորական լյուկ''', '''Обычный люк''', '''Regular sunroof''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def panoramic_sunroof_sunroof(cid : int, all : bool = False) -> str:
    '''Panoramic sunroof'''
    phrases = ['''Պանորամային լյուկ''', '''Панорамный люк''', '''Panoramic sunroof''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def led_headlights(cid : int, all : bool = False) -> str:
    '''Led headlights'''
    phrases = ['''Լեդ լուսարձակներ''', '''Светодиодные фары''', '''Led headlights''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def halogen_headlights(cid : int, all : bool = False) -> str:
    '''Halogen headlights'''
    phrases = ['''Հալոգեն լուսարձակներկ''', '''Галогенные фары''', '''Halogen headlights''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def хenon_headlights(cid : int, all : bool = False) -> str:
    '''Xenon headlights'''
    phrases = ['''Քսենոնային լուսարձակներ''', '''Ксеноновые фары''', '''Xenon headlights''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def leather(cid : int, all : bool = False) -> str:
    '''Material leather'''
    phrases = ['''Մատերիալ կաշի''', '''Материал кожа''', '''Material leather''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def textile(cid : int, all : bool = False) -> str:
    '''Material textile'''
    phrases = ['''Մատերիալ կտոր''', '''Материал текстиль''', '''Material textile''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def other(cid : int, all : bool = False) -> str:
    '''Material other'''
    phrases = ['''Մատերիալ այլ''', '''Материал другой''', '''Material other''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def alcantara(cid : int, all : bool = False) -> str:
    '''Material alcantara'''
    phrases = ['''Մատերիալ ալկանտարա''', '''Материал алькантара''', '''Material alcantara''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def velour(cid : int, all : bool = False) -> str:
    '''Material velour'''
    phrases = ['''Մատերիալ թավիշ''', '''Материал велюр''', '''Material velour''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def leatherette(cid : int, all : bool = False) -> str:
    '''Material leatherette'''
    phrases = ['''Մատերիալ դերմանտին''', '''Материал искусственная кожа''', '''Material leatherette''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]