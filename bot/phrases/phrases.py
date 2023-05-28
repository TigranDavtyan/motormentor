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

Enjoy using the Motor Mentor Bot! Feel free to ask any questions you may have along the way. Let's begin!'''
    phrases = ['''Բարի գալուստ Motor Mentor Bot: Այս բոտը կանխատեսում է մեքենաների գները՝ հիմնվելով տարբեր հատկանիշների վրա: Անկախ նրանից, թե դուք վաճառում եք, գնում եք կամ հետաքրքրված եք շուկայի միտումների վերլուծությամբ, այս բոտն այստեղ է ձեզ օգնելու համար:

Տրամադրելով ձեր մեքենայի մասին մանրամասներ, ինչպիսիք են ապրանքանիշը, մոդելը, տարին, վազքը և այլն, բոտը կգնահատի ձեր մեքենայի գների միջակայքը: Սա կարող է օգնել ձեզ սահմանել մրցունակ վաճառքի գին, կայացնել տեղեկացված գնման որոշումներ կամ ձեռք բերել պատկերացումներ մեքենաների գների վրա ազդող գործոնների մասին:

Խնդրում ենք նկատի ունենալ, որ ներկայացված կանխատեսումները գնահատումներ են՝ հիմնված առկա տվյալների վրա: Իրական շուկայական գները կարող են տարբեր լինել՝ պայմանավորված այնպիսի գործոններով, ինչպիսիք են գտնվելու վայրը, վիճակը և շուկայական պահանջարկը:

Ազատորեն տվեք ցանկացած հարց: Վայելե՛ք Motor Mentor Bot-ը: Եկեք սկսենք!''', '''Добро пожаловать в бота Motor Mentor! Этот бот прогнозирует цены на автомобили на основе различных характеристик. Если вы продаете, покупаете или интересуетесь анализом рыночных тенденций, этот бот здесь, чтобы помочь вам.

Предоставляя информацию о вашем автомобиле, такую как марка, модель, год выпуска, пробег и т. д., бот оценит диапазон цен на ваш автомобиль. Это может помочь вам установить конкурентоспособную цену продажи, принять обоснованное решение о покупке или получить представление о факторах, влияющих на цену автомобиля.

Обратите внимание, что представленные прогнозы являются оценками, основанными на доступных данных. Фактические рыночные цены могут варьироваться в зависимости от таких факторов, как местоположение, состояние и рыночный спрос.

Наслаждайтесь использованием бота Motor Mentor! Не стесняйтесь задавать любые вопросы, которые могут у вас возникнуть по пути. Давай начнем!''', '''Welcome to the Motor Mentor Bot! This bot predicts car prices based on various features. Whether you're selling, buying, or interested in analyzing market trends, this bot is here to assist you.

By providing details about your car, such as brand, model, year, mileage, and more, the bot will estimate the price range for your vehicle. This can help you set a competitive selling price, make informed buying decisions, or gain insights into the factors that influence car prices.

Please note that the predictions provided are estimates based on available data. Actual market prices may vary due to factors like location, condition, and market demand.

Enjoy using the Motor Mentor Bot! Feel free to ask any questions you may have along the way. Let's begin!''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def help(cid : int, all : bool = False) -> str:
    '''If you are stuck or have any questions you can contact the admin at <a href="https://t.me/propertizeadmin">Propertize Admin</a>․ He will definitely help you🙂'''
    phrases = ['''Եթե անելանելի վիճակում եք կամ հարցեր ունեք, կարող եք կապվել ադմինիստրատորի հետ <a href="https://t.me/propertizeadmin">Propertize Admin</a>։ Նա անպայման կօգնի ձեզ🙂''', '''Если вы застряли или у вас есть какие-либо вопросы, вы можете связаться с администратором по адресу <a href="https://t.me/propertizeadmin">Propertize Admin</a>․ Он обязательно вам поможет🙂''', '''If you are stuck or have any questions you can contact the admin at <a href="https://t.me/propertizeadmin">Propertize Admin</a>․ He will definitely help you🙂''']
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

def main_menu(cid : int, all : bool = False) -> str:
    '''📜 Menu'''
    phrases = ['''📜 Մենյու''', '''📜 Меню''', '''📜 Menu''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def get_car_price(cid : int, all : bool = False) -> str:
    '''Car prices'''
    phrases = ['''Car prices''', '''Car prices''', '''Car prices''']
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

def payment_successfull(cid : int,pay_amount,days, all : bool = False) -> str:
    '''You have paid [pay_amount] dram so your subscription is prolonged for [days] days.'''
    phrases = ['''Դուք վճարել եք [pay_amount] դրամ, ուստի ձեր բաժանորդագրությունը երկարաձգվում է [days] օրով:''', '''Вы заплатили [pay_amount] драм, ваша подписка продлена на [days] дней.''', '''You have paid [pay_amount] dram so your subscription is prolonged for [days] days.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[pay_amount]",str(pay_amount)).replace("[days]",str(days))

def billing_info(cid : int,date,days,pay_amount, all : bool = False) -> str:
    '''Payment date is [date] ([days] days until payment). Payment amount is [pay_amount] dram.'''
    phrases = ['''Վճարման ամսաթիվը [date] է ([days] օր մինչև վճարումը): Վճարման գումարը [pay_amount] դրամ է:''', '''Дата платежа [date] ([days] дней до платежа). Сумма платежа составляет [pay_amount] драм.''', '''Payment date is [date] ([days] days until payment). Payment amount is [pay_amount] dram.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[date]",str(date)).replace("[days]",str(days)).replace("[pay_amount]",str(pay_amount))

def pay_button(cid : int, all : bool = False) -> str:
    '''💵 Pay'''
    phrases = ['''💵 Վճարել''', '''💵 Платить''', '''💵 Pay''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_image_sent(cid : int, all : bool = False) -> str:
    '''Thank you! The admin will review the invoice and will prolong your subscription 🙂'''
    phrases = ['''Շնորհակալություն! Ադմինը կվերանայի հաշիվ-ապրանքագիրը և կերկարաձգի ձեր բաժանորդագրությունը 🙂''', '''Спасибо! Админ рассмотрит счет и продлит подписку 🙂''', '''Thank you! The admin will review the invoice and will prolong your subscription 🙂''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def payment_accepted(cid : int,price, all : bool = False) -> str:
    '''Your payment of [price] dram was successful.'''
    phrases = ['''Ձեր [price] դրամ վճարումը հաջող է եղել''', '''Ваш платеж в размере [price] драма успешно завершен''', '''Your payment of [price] dram was successful.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[price]",str(price))

def subscription_not_enough(cid : int,user_sub,min_sub, all : bool = False) -> str:
    '''Your subscription level ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is [min_sub]'''
    phrases = ['''Ձեր բաժանորդագրության մակարդակը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը [min_sub] է''', '''Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: [min_sub]''', '''Your subscription level ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is [min_sub]''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[user_sub]",str(user_sub)).replace("[min_sub]",str(min_sub))

def subscription_end_close(cid : int,days, all : bool = False) -> str:
    '''⚠️ Warning ⚠️
Your subscrbtion ends in [days] days. Go to "Billing" menu to pay and prolong the subscription.'''
    phrases = ['''⚠️ Զգուշացում ⚠️
Ձեր բաժանորդագրությունն ավարտվում է [days] օրից: Բաժանորդագրությունը վճարելու և երկարացնելու համար գնացեք «Վճարումներ» ընտրացանկը:''', '''⚠️ Внимание ⚠️
Ваша подписка заканчивается через [days] дней. Перейдите в меню «Оплата», чтобы оплатить и продлить подписку.''', '''⚠️ Warning ⚠️
Your subscrbtion ends in [days] days. Go to "Billing" menu to pay and prolong the subscription.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[days]",str(days))

def subscription_end(cid : int,days, all : bool = False) -> str:
    '''❗️ Warning ❗️
Your subscrbtion ended and your account will be deactivated in [days] days. New people cant make an appointment with you. Contact the administrator to activate your account. <a href="https://t.me/pheriadmin">Pheri Admin</a>'''
    phrases = ['''❗️ Զգուշացում ❗️
Ձեր բաժանորդագրությունն ավարտվել է, և ձեր հաշիվը կանջատվի [days] օրվա ընթացքում: Նոր մարդիկ չեն կարող ձեր մոտ գրանցվել: Կապվեք ադմինիստրատորի հետ՝ ձեր հաշիվն ակտիվացնելու համար: <a href="https://t.me/pheriadmin">Pheri Admin</a>''', '''❗️ Предупреждение ❗️
Ваша подписка закончилась, и ваша учетная запись будет деактивирована через [days] дней. Новые люди не могут записаться к вам на прием. Свяжитесь с администратором для активации вашей учетной записи. <a href="https://t.me/pheriadmin">Pheri Admin</a>''', '''❗️ Warning ❗️
Your subscrbtion ended and your account will be deactivated in [days] days. New people cant make an appointment with you. Contact the administrator to activate your account. <a href="https://t.me/pheriadmin">Pheri Admin</a>''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[days]",str(days))

def referral(cid : int, all : bool = False) -> str:
    '''🔗 Referrals'''
    phrases = ['''🔗 Ուղղորդումներ''', '''🔗 Рефералы''', '''🔗 Referrals''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

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

def get_car_price(cid : int, all : bool = False) -> str:
    '''Car prices'''
    phrases = ['''Car prices''', '''Car prices''', '''Car prices''']
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

def calculate_result(cid : int,price,price_dram,price_rub, all : bool = False) -> str:
    '''Car price is:
------- [price] $
------- [price_dram] dram
------- [price_rub] rub

*Dram and ruble prices are calculated using 385 and 79.7 exchange rates.
'''
    phrases = ['''Մեքենայի գինը. 
------- [price] $
------- [price_dram] դրամ
------- [price_rub] ռուբլի

*Դրամի և ռուբլու գները հաշվարկված են 385 և 79,7 փոխարժեքներով:
''', '''Цена автомобиля:
------- [price] $
------- [price_dram] драм
------- [price_rub] руб

*Цены в драмах и рублях рассчитаны по курсам 385 и 79,7.
''', '''Car price is:
------- [price] $
------- [price_dram] dram
------- [price_rub] rub

*Dram and ruble prices are calculated using 385 and 79.7 exchange rates.
''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang].replace("[price]",str(price)).replace("[price_dram]",str(price_dram)).replace("[price_rub]",str(price_rub))

def car_price_info(cid : int, all : bool = False) -> str:
    '''Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car in Armenia, dont base your decisions only on this results when buying or selling.'''
    phrases = ['''Ընտրեք մեքենայի պարամետրերը և սեղմեք հաշվարկել՝ գինը ստանալու համար:
⚠️Արհեստական ինտելեկտը հաշվարկում է այս կոնկրետ մեքենայի ՄԻՋԻՆ ՇՈՒԿԱՅԱԿԱՆ ԱՐԺԵՔԸ հայաստանում, գնելիս կամ վաճառելիս մի հիմնեք ձեր որոշումները միայն այս արդյունքների վրա:''', '''Выберите параметры автомобиля и нажмите рассчитать, чтобы узнать цену․
⚠️ИИ рассчитывает СРЕДНЮЮ РЫНОЧНУЮ СТОИМОСТЬ для данного конкретного автомобиля в Армении, не основывайте свои решения только на этих результатах при покупке или продаже.''', '''Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car in Armenia, dont base your decisions only on this results when buying or selling.''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

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
    '''Please enter the manufacturing year of your car, for example "2018".'''
    phrases = ['''Խնդրում ենք մուտքագրել ձեր մեքենայի արտադրության տարեթիվը, օրինակ՝ «2018»:''', '''Пожалуйста, введите год выпуска вашего автомобиля, например "2018".''', '''Please enter the manufacturing year of your car, for example "2018".''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_mileage(cid : int, all : bool = False) -> str:
    '''Please enter the mileage of your car, for example "68000".'''
    phrases = ['''Խնդրում ենք մուտքագրել ձեր մեքենայի վազքը, օրինակ՝ «68000»:''', '''Пожалуйста, введите пробег вашего автомобиля, например "68000".''', '''Please enter the mileage of your car, for example "68000".''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]

def choose_car_engine_size(cid : int, all : bool = False) -> str:
    '''Please enter the engine size of your car, for example "2.5".'''
    phrases = ['''Խնդրում ենք մուտքագրել ձեր մեքենայի շարժիչի չափը, օրինակ՝ «2.5»:''', '''Пожалуйста, введите объем двигателя вашего автомобиля, например "2,5".''', '''Please enter the engine size of your car, for example "2.5".''']
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
    '''Please enter the wheel size of your car, for example "16".'''
    phrases = ['''Խնդրում ենք մուտքագրել ձեր մեքենայի անիվի չափը, օրինակ՝ «16»:''', '''Пожалуйста, введите размер колес вашего автомобиля, например "16".''', '''Please enter the wheel size of your car, for example "16".''']
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