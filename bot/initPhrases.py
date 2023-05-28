import re

def insertPhrase(name:str, arm:str, rus:str, eng:str):
    global phrasespy

    matches = re.findall(r'(\[.*?\])', eng)
    arguments = ''
    replaces = ''
    for arg in matches:
        argn = arg[1:-1]
        arguments += argn + ','
        replaces += f'.replace("{arg}",str({argn}))'


    phrasespy.write(f"""\n\ndef {name}(cid : int,{arguments} all : bool = False) -> str:
    '''{eng}'''
    phrases = ['''{arm}''', '''{rus}''', '''{eng}''']
    if all:
        return phrases
    if cid > 10:
        lang = db.getUserLang(cid)
    else: 
        lang = cid
    return phrases[lang]{replaces}""")


phrasespy = open("./phrases/phrases.py", "w", encoding="utf-8")
phrasespy.write('''#This is a generated file
from data import DatabaseManager
db = DatabaseManager()

ARM = 0
RUS = 1
ENG = 2''')


insertPhrase('start',
"""Բարի գալուստ Motor Mentor Bot: Այս բոտը կանխատեսում է մեքենաների գները՝ հիմնվելով տարբեր հատկանիշների վրա: Անկախ նրանից, թե դուք վաճառում եք, գնում եք կամ հետաքրքրված եք շուկայի միտումների վերլուծությամբ, այս բոտն այստեղ է ձեզ օգնելու համար:

Տրամադրելով ձեր մեքենայի մասին մանրամասներ, ինչպիսիք են ապրանքանիշը, մոդելը, տարին, վազքը և այլն, բոտը կգնահատի ձեր մեքենայի գների միջակայքը: Սա կարող է օգնել ձեզ սահմանել մրցունակ վաճառքի գին, կայացնել տեղեկացված գնման որոշումներ կամ ձեռք բերել պատկերացումներ մեքենաների գների վրա ազդող գործոնների մասին:

Խնդրում ենք նկատի ունենալ, որ ներկայացված կանխատեսումները գնահատումներ են՝ հիմնված առկա տվյալների վրա: Իրական շուկայական գները կարող են տարբեր լինել՝ պայմանավորված այնպիսի գործոններով, ինչպիսիք են գտնվելու վայրը, վիճակը և շուկայական պահանջարկը:

Ազատորեն տվեք ցանկացած հարց: Վայելե՛ք Motor Mentor Bot-ը: Եկեք սկսենք!""",


"""Добро пожаловать в бота Motor Mentor! Этот бот прогнозирует цены на автомобили на основе различных характеристик. Если вы продаете, покупаете или интересуетесь анализом рыночных тенденций, этот бот здесь, чтобы помочь вам.

Предоставляя информацию о вашем автомобиле, такую как марка, модель, год выпуска, пробег и т. д., бот оценит диапазон цен на ваш автомобиль. Это может помочь вам установить конкурентоспособную цену продажи, принять обоснованное решение о покупке или получить представление о факторах, влияющих на цену автомобиля.

Обратите внимание, что представленные прогнозы являются оценками, основанными на доступных данных. Фактические рыночные цены могут варьироваться в зависимости от таких факторов, как местоположение, состояние и рыночный спрос.

Наслаждайтесь использованием бота Motor Mentor! Не стесняйтесь задавать любые вопросы, которые могут у вас возникнуть по пути. Давай начнем!""",


"""Welcome to the Motor Mentor Bot! This bot predicts car prices based on various features. Whether you're selling, buying, or interested in analyzing market trends, this bot is here to assist you.

By providing details about your car, such as brand, model, year, mileage, and more, the bot will estimate the price range for your vehicle. This can help you set a competitive selling price, make informed buying decisions, or gain insights into the factors that influence car prices.

Please note that the predictions provided are estimates based on available data. Actual market prices may vary due to factors like location, condition, and market demand.

Enjoy using the Motor Mentor Bot! Feel free to ask any questions you may have along the way. Let's begin!""")

#help
insertPhrase('help',
             'Եթե անելանելի վիճակում եք կամ հարցեր ունեք, կարող եք կապվել ադմինիստրատորի հետ <a href="https://t.me/propertizeadmin">Propertize Admin</a>։ Նա անպայման կօգնի ձեզ🙂', 
             'Если вы застряли или у вас есть какие-либо вопросы, вы можете связаться с администратором по адресу <a href="https://t.me/propertizeadmin">Propertize Admin</a>․ Он обязательно вам поможет🙂', 
             'If you are stuck or have any questions you can contact the admin at <a href="https://t.me/propertizeadmin">Propertize Admin</a>․ He will definitely help you🙂')

#language
insertPhrase('language_change','🇦🇲🇷🇺🇺🇸 Փոխել լեզուն', '🇦🇲🇷🇺🇺🇸 Изменить язык', '🇦🇲🇷🇺🇺🇸 Change language')
insertPhrase('language_choose','Ընտրեք լեզուն 🇦🇲', 'Выберите язык 🇷🇺', 'Select language 🇺🇸')
insertPhrase('languages','Հայերեն🇦🇲', 'Русский🇷🇺', 'English🇺🇸')
insertPhrase('language_set','Ընտրվեց հայերեն լեզուն 🇦🇲','Выбран русский язык 🇷🇺','English is selected 🇺🇸')

insertPhrase('agree','✅ Համաձայն եմ!','✅ Я согласен!','✅ I agree!')
insertPhrase('disagree','❌ Համաձայն չեմ','❌ Я не согласен','❌ I disagree')
insertPhrase('cancel','🚫 Չեղարկել','🚫 Отменить','🚫 Cancel')
insertPhrase('canceled','🚫 Չեղարկված է','🚫 Отменено','🚫 Canceled')
insertPhrase('all_right','✅ Ճիշտ է','✅ Все верно',"✅ That's right")
insertPhrase('back','👈 Վերադառնալ','👈 Назад','👈 Back')
insertPhrase('skip','👉 Բաց թողնել','👉 Пропустить','👉 Skip')
insertPhrase('confirm','👍 Հաստատել','👍 Подтвердить','👍 Confirm')
insertPhrase('confirmed','👍 Հաստատված է','👍 Подтверждено','👍 Confirmed')
insertPhrase('yes','✅ Այո՛', '✅ Да', '✅ Yes')
insertPhrase('no','❌ Ոչ', '❌ Нет', '❌ No')
insertPhrase('ok', 'օկ','ок','ok')

insertPhrase('wrong_action',
             '❌Սխալ գործողություն❌\n Կրկին կարդացեք հաղորդագրությունը☝️, ստացեք /help ադմինիստրատորից կամ /start արեք և նորից փորձեք:',
             '❌Неверное действие❌\n Прочитайте сообщение еще раз☝️, получите /help от администратора или вернитесь и повторите попытку.',
             '❌Wrong action❌\n Read the message again☝️, get /help from admin or go to /start and try again.')


#User menu
insertPhrase('main_menu','📜 Մենյու', '📜 Меню', '📜 Menu')
insertPhrase('get_car_price','Car prices', 'Car prices', 'Car prices')



insertPhrase('duration','Տևողություն', 'Продолжительность', 'Duration')
insertPhrase('fee','Վճար', 'Плата', 'Fee')
insertPhrase('dram','դրամ', 'драм', 'amd')
insertPhrase('minute','րոպե', 'минут', 'minutes')

insertPhrase('today','Այսօր', 'Сегодня', 'Today')
insertPhrase('tomorrow','Վաղը', 'Завтра', 'Tomorrow')
insertPhrase('afterTomorrow','Վաղը չէ մյուս օրը', 'Послезавтра', 'The day after tomorrow')
insertPhrase('date','Ամսաթիվ', 'Дата', 'Date')

insertPhrase('start2', 'Սկիզբ', 'Начало', 'Start')
insertPhrase('end', 'Վերջ', 'Конец', 'End')
insertPhrase('day', 'Օր', 'День', 'Day')


insertPhrase('january',     'Հունվարի',   'Январь',  'January')
insertPhrase('february',    'Փետրվարի',   'Февраль', 'February')
insertPhrase('march',       'Մարտի',      'Март',    'March')
insertPhrase('april',       'Ապրիլի',     'Апрель',  'April')
insertPhrase('may',         'Մայիսի',     'Май',     'May')
insertPhrase('june',        'Հունիսի',    'Нюнь',    'June')
insertPhrase('july',        'Հուլիսի',    'Июль',    'July')
insertPhrase('august',      'Օգոստոսի',   'Август',  'August')
insertPhrase('september',   'Սեպտեմբերի', 'Сентябрь','September')
insertPhrase('october',     'Հոկտեմբերի', 'Октябрь', 'October')
insertPhrase('november',    'Նոյեմբերի',  'Ноябрь',  'November')
insertPhrase('december',    'Դեկտեմբերի', 'Декабрь', 'December')

insertPhrase('details','🧾','🧾','🧾')
insertPhrase('cancel','❌','❌','❌')

insertPhrase('anonymous', 'անհայտ 🤷‍♀️','неизвестный 🤷‍♀️','unknown 🤷‍♀️')

insertPhrase('payment_successfull', 
'''Դուք վճարել եք [pay_amount] դրամ, ուստի ձեր բաժանորդագրությունը երկարաձգվում է [days] օրով:''',
'''Вы заплатили [pay_amount] драм, ваша подписка продлена на [days] дней.''',
'''You have paid [pay_amount] dram so your subscription is prolonged for [days] days.''')

insertPhrase('billing_info', 
'Վճարման ամսաթիվը [date] է ([days] օր մինչև վճարումը): Վճարման գումարը [pay_amount] դրամ է:',
'Дата платежа [date] ([days] дней до платежа). Сумма платежа составляет [pay_amount] драм.',
"Payment date is [date] ([days] days until payment). Payment amount is [pay_amount] dram.")

insertPhrase('pay_button', '💵 Վճարել','💵 Платить','💵 Pay')

insertPhrase('payment_image_sent', 'Շնորհակալություն! Ադմինը կվերանայի հաշիվ-ապրանքագիրը և կերկարաձգի ձեր բաժանորդագրությունը 🙂','Спасибо! Админ рассмотрит счет и продлит подписку 🙂','Thank you! The admin will review the invoice and will prolong your subscription 🙂')

insertPhrase('payment_accepted', 'Ձեր [price] դրամ վճարումը հաջող է եղել','Ваш платеж в размере [price] драма успешно завершен','Your payment of [price] dram was successful.')

#Subscription
insertPhrase('subscription_not_enough', 
             'Ձեր բաժանորդագրության մակարդակը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը [min_sub] է',
             'Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: [min_sub]',
             'Your subscription level ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is [min_sub]')

insertPhrase('subscription_end_close', 
'⚠️ Զգուշացում ⚠️\nՁեր բաժանորդագրությունն ավարտվում է [days] օրից: Բաժանորդագրությունը վճարելու և երկարացնելու համար գնացեք «Վճարումներ» ընտրացանկը:',
'⚠️ Внимание ⚠️\nВаша подписка заканчивается через [days] дней. Перейдите в меню «Оплата», чтобы оплатить и продлить подписку.',
'⚠️ Warning ⚠️\nYour subscrbtion ends in [days] days. Go to "Billing" menu to pay and prolong the subscription.')

insertPhrase('subscription_end', 
'❗️ Զգուշացում ❗️\nՁեր բաժանորդագրությունն ավարտվել է, և ձեր հաշիվը կանջատվի [days] օրվա ընթացքում: Նոր մարդիկ չեն կարող ձեր մոտ գրանցվել: Կապվեք ադմինիստրատորի հետ՝ ձեր հաշիվն ակտիվացնելու համար: <a href="https://t.me/pheriadmin">Pheri Admin</a>',
'❗️ Предупреждение ❗️\nВаша подписка закончилась, и ваша учетная запись будет деактивирована через [days] дней. Новые люди не могут записаться к вам на прием. Свяжитесь с администратором для активации вашей учетной записи. <a href="https://t.me/pheriadmin">Pheri Admin</a>',
'❗️ Warning ❗️\nYour subscrbtion ended and your account will be deactivated in [days] days. New people cant make an appointment with you. Contact the administrator to activate your account. <a href="https://t.me/pheriadmin">Pheri Admin</a>')


#Referrals
insertPhrase('referral', '🔗 Ուղղորդումներ','🔗 Рефералы','🔗 Referrals')

insertPhrase('phone_number', 'Հեռախոսահամար','Номер телефона','Phone number')
insertPhrase('deleted', '❌ Ջնջված է ❌','❌ Удалено ❌','❌ Deleted ❌')



#Car prices
insertPhrase('get_car_price', 'Car prices', 'Car prices', 'Car prices')
insertPhrase('year', '[year] թ․', '[year]', '[year]')
insertPhrase('mileage', '[mileage] կմ', '[mileage] km', '[mileage] km')

insertPhrase('engine_size', '[engine_size] L', '[engine_size] L', '[engine_size] L')
insertPhrase('interior_color', '[interior_color] ինտերիեր', '[interior_color] интерьер', '[interior_color] interior')
insertPhrase('interior_material', '[interior_material]', '[interior_material]', '[interior_material]')
insertPhrase('wheel_size', 'R[wheel_size]', 'R[wheel_size]', 'R[wheel_size]')


insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')
insertPhrase('calculate_result', 
'''Մեքենայի գինը. 
------- [price] $
------- [price_dram] դրամ
------- [price_rub] ռուբլի

*Դրամի և ռուբլու գները հաշվարկված են 385 և 79,7 փոխարժեքներով:
Ի՞նչ եք կարծում, այս մեքենան խելամի՞տ է գնահատված: Պարտադիր չէ պատասխանեք այս հարցին, բայց դա կօգնի ավելի խելացի արհեստական ինտելեկտ կառուցել:
''', 
'''Цена автомобиля:
------- [price] $
------- [price_dram] драм
------- [price_rub] руб

*Цены в драмах и рублях рассчитаны по курсам 385 и 79,7.
Считаете ли вы, что этот автомобиль имеет разумную цену? Вам не обязательно отвечать на этот вопрос, но это поможет создать более умный ИИ.
''',

'''Car price is:
------- [price] $ 💵
------- [price_dram] dram
------- [price_rub] rub

*Dram and ruble prices are calculated using 385 and 79.7 exchange rates.
Do you think this car is reasonably priced? You dont have to answer this but it will help build a better AI.
''')

insertPhrase('dont_know','Չգիտեմ','Я не знаю',"I don't know")
insertPhrase('my_price','Առաջարկել իմ գինը','Предложи мою цену','Offer my price')
insertPhrase('my_price_offer',
             'Ի՞նչ եք կարծում, ինչ արժե այս մեքենան: Գրեք ձեր պատասխանը այսպես «18000»',
             'Как вы думаете, сколько стоит эта машина? Напишите свой ответ так: "18000"',
             'What do you think this car costs? Write your answer like this "18000" ')

insertPhrase('thanks_for_opinion', 'Շնորհակալություն կարծիքի համար 👌', 'Спасибо за ваше мнение 👌', "Thank you for your opinion 👌")


insertPhrase('car_price_info', 
'''Ընտրեք մեքենայի պարամետրերը և սեղմեք հաշվարկել՝ գինը ստանալու համար:
⚠️Արհեստական ինտելեկտը հաշվարկում է այս կոնկրետ մեքենայի ՄԻՋԻՆ ՇՈՒԿԱՅԱԿԱՆ ԱՐԺԵՔԸ հայաստանում, գնելիս կամ վաճառելիս մի հիմնեք ձեր որոշումները միայն այս արդյունքների վրա:''',
'''Выберите параметры автомобиля и нажмите рассчитать, чтобы узнать цену․
⚠️ИИ рассчитывает СРЕДНЮЮ РЫНОЧНУЮ СТОИМОСТЬ для данного конкретного автомобиля в Армении, не основывайте свои решения только на этих результатах при покупке или продаже.''',
'''Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car in Armenia, dont base your decisions only on this results when buying or selling.''')



insertPhrase('choose_car_brand',             
    'Խնդրում եմ ընտրեք ձեր մեքենայի մակնիշը։ Եթե ստորև ներկայացված չէ ձեր մեքենայի մակնիշը, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:',
    'Пожалуйста, выберите марку вашего автомобиля. Если марка вашего автомобиля не указана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.',
    'Please choose the brand of your car. If the brand of your car is not shown below it means there is not enough data and the AI cant make a good prediction.')

insertPhrase('choose_car_model',             
    'Խնդրում եմ ընտրել ձեր մեքենայի մոդելը։ Եթե ձեր մեքենայի մոդելը ներկայացված չէ ստորև, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:',  
    'Пожалуйста, выберите модель вашего автомобиля. Если модель вашего автомобиля не показана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.',
    'Please choose the model of your car. If the model of your car is not shown below it means there is not enough data and the AI cant make a good prediction.')

insertPhrase('choose_car_year',
    '⚠️Խնդրում ենք մուտքագրել ձեր մեքենայի արտադրության տարեթիվը, օրինակ՝ «2018»:',
    '⚠️Пожалуйста, введите год выпуска вашего автомобиля, например "2018".',
    '⚠️Please enter the manufacturing year of your car, for example "2018".')
insertPhrase('choose_car_mileage',
    '⚠️Խնդրում ենք մուտքագրել ձեր մեքենայի վազքը, օրինակ՝ «68000»:',
    '⚠️Пожалуйста, введите пробег вашего автомобиля, например "68000".',
    '⚠️Please enter the mileage of your car, for example "68000".')
insertPhrase('choose_car_engine_size',       
    '⚠️Խնդրում ենք մուտքագրել ձեր մեքենայի շարժիչի չափը, օրինակ՝ «2.5»:',
    '⚠️Пожалуйста, введите объем двигателя вашего автомобиля, например "2,5".',
    '⚠️Please enter the engine size of your car, for example "2.5".')
insertPhrase('choose_car_exterior_color',
    'Խնդրում ենք ընտրել ձեր մեքենայի արտաքին գույնը:',
    'Пожалуйста, выберите цвет кузова вашего автомобиля.',
    'Please choose the exterior color of your car.')
insertPhrase('choose_car_body_type',
    'Խնդրում ենք ընտրել ձեր մեքենայի թափքի տեսակը:',
    'Пожалуйста, выберите тип кузова вашего автомобиля.',
    'Please choose the body type of your car.')
insertPhrase('choose_car_engine_type',
    'Խնդրում ենք ընտրել ձեր մեքենայի շարժիչի տեսակը:',
    'Пожалуйста, выберите тип двигателя вашего автомобиля.',
    'Please choose the engine type of your car.')
insertPhrase('choose_car_transmission',
    'Խնդրում ենք ընտրել ձեր մեքենայի փոխանցման տուփի տեսակը:',
    'Пожалуйста, выберите тип трансмиссии вашего автомобиля.',
    'Please choose the transmission type of your car.')
insertPhrase('choose_car_drive_type',
    'Խնդրում ենք ընտրել ձեր մեքենայի վարման տեսակը:',
    'Пожалуйста, выберите тип привода вашего автомобиля.',
    'Please choose the drive type of your car.')
insertPhrase('choose_car_condition',
    'Խնդրում ենք ընտրել ձեր մեքենայի վիճակը։',
    'Пожалуйста, выберите состояние вашего автомобиля.',
    'Please choose the condition of your car.')
insertPhrase('choose_car_gas_equipment',
    'Խնդրում ենք նշել, թե արդյոք ձեր մեքենան ունի գազի սարքավորումներ:',
    'Пожалуйста, уточните, есть ли в вашем автомобиле газовое оборудование.',
    'Please specify if your car has gas equipment.')
insertPhrase('choose_car_steering_wheel', 
    'Խնդրում ենք ընտրել ձեր մեքենայի ղեկի դիրքը:',
    'Пожалуйста, выберите положение рулевого колеса вашего автомобиля.',
    'Please choose the steering wheel position of your car.')
insertPhrase('choose_car_headlights',
    'Խնդրում եմ նշեք ձեր մեքենայի լուսարձակների տեսակը:',
    'Пожалуйста, укажите тип фар в вашем автомобиле.',
    'Please specify the type of headlights in your car.')
insertPhrase('choose_car_interior_color',
    'Խնդրում ենք ընտրել ձեր մեքենայի սրահի գույնը:',
    'Пожалуйста, выберите цвет салона вашего автомобиля.',
    'Please choose the interior color of your car.')
insertPhrase('choose_car_interior_material',
    'Խնդրում ենք ընտրել ձեր մեքենայի սրահի նյութը:',
    'Пожалуйста, выберите материал салона вашего автомобиля.',
    'Please choose the interior material of your car.')
insertPhrase('choose_car_sunroof',
    'Խնդրում ենք նշել, թե արդյոք ձեր մեքենան ունի լուսային տանիք:',
    'Пожалуйста, укажите, есть ли в вашем автомобиле люк на крыше.',
    'Please specify if your car has a sunroof.')
insertPhrase('choose_car_wheel_size',
    '⚠️Խնդրում ենք մուտքագրել ձեր մեքենայի անիվի չափը, օրինակ՝ «16»:',
    '⚠️Пожалуйста, введите размер колес вашего автомобиля, например "16".',
    '⚠️Please enter the wheel size of your car, for example "16".')



insertPhrase('best_offers', 'Լավագույն առաջարկներ', 'Лучшие предложения', 'Best offers')


insertPhrase('choose_marz',       'Ընտրեք տարածաշրջան', 'Выберите регион', 'Choose region')

insertPhrase('marz_YEREVAN',      'Երևան',          'Ереван',        'Yerevan')
insertPhrase('marz_ARMAVIR',      'Արմավիր',        'Армавир',       'Armavir')
insertPhrase('marz_ARARAT',       'Արարատ',         'Арарат',        'Ararat')
insertPhrase('marz_KOTAYK',       'Կոտայք',         'Котайк',        'Kotayk')
insertPhrase('marz_SHIRAK',       'Շիրակ',          'Ширак',         'Shirak')
insertPhrase('marz_LORRI',        'Լոռի',           'Лори',          'Lorri')
insertPhrase('marz_GEGHARKUNIK',  'Գեղարքունիք',    'Гегаркуник',    'Gegharkunik')
insertPhrase('marz_SYUNIK',       'Սյունիք',        'Сюник',         'Syunik')
insertPhrase('marz_ARAGATSOTN',   'Արագածոտն',      'Арагацотн',     'Aragatsotn')
insertPhrase('marz_TAVUSH',       'Տավուշ',         'Тавуш',         'Tavush')
insertPhrase('marz_VAYOTS_DZOR',  'Վայոց ձոր',      'Вайоц Дзор',    'Vayots Dzor')
insertPhrase('marz_ARTSAKH',      'Արցախ',          'Арцах',         'Artsakh')



#Car properties
insertPhrase("sedan",               "Սեդան"                     ,"Седан"                       ,"Sedan")
insertPhrase("hatchback",           "Հետչբեք"                   ,"Хэтчбек"                     ,"Hatchback")
insertPhrase("wagon",               "Ունիվերսալ"                ,"Универсал"                   ,"Wagon")
insertPhrase("coupe",               "Կուպե"                     ,"Купе"                        ,"Coupe")
insertPhrase("crossover",           "Ամենագնաց / Քրոսսովեր"     ,"Внедорожник / Кроссовер"     ,"SUV / Crossover")
insertPhrase("minivan",             "Մինիվեն"                   ,"Минивэн"                     ,"Minivan")
insertPhrase("pickup",              "Փիքափ"                     ,"Пикап"                       ,"Pickup")
insertPhrase("minibus",             "Միկրոավտոբուս"             ,"Микроавтобус"                ,"Minibus")
insertPhrase("van",                 "Ֆուրգոն"                   ,"Фургон"                      ,"Van")
insertPhrase("convertible",         "Կաբրիոլետ"                 ,"Кабриолет"                   ,"Convertible")
insertPhrase("limo",                "Լիմուզին"                  ,"Лимузин"                     ,"Limo")
insertPhrase("roadster",            "Ռոդսթեր"                   ,"Родстер"                     ,"Roadster")
insertPhrase("liftback",            "Լիֆտբեկ"                   ,"Лифтбек"                     ,"Liftback")
insertPhrase("fastback",            "Ֆաստբեկ"                   ,"Фастбек"                     ,"Fastback")
insertPhrase("compact_mpv",         "Կոմպակտվեն"                ,"Компактвэн"                  ,"Compact MPV")

insertPhrase('gasoline',            "Բենզին",                   "Бензин",                       "Gasoline")
insertPhrase('diesel',              "Դիզել",                    "Дизель",                       "Diesel")
insertPhrase('hybrid',              "Հիբրիդ",                   "Гибрид",                       "Hybrid")
insertPhrase('electric',            "էլեկտրական",               "Электро",                      "Electric")

insertPhrase("manual",              "Մեխանիկական",              "Механическая",                 "Manual")
insertPhrase("automatic",           "Ավտոմատ",                  "Автоматическая",               "Automatic")

insertPhrase("front_wheel_drive",   "Առջևի քարշակ",            "Передний привод",               "Front Wheel Drive")
insertPhrase("rear_wheel_drive",    "Ետևի քարշակ",             "Задний привод",                 "Rear Wheel Drive")
insertPhrase("all_wheel_drive",     "Լիաքարշակ",               "Полный привод",                 "All Wheel Drive")

insertPhrase("car_is_not_damaged",  "Չվթարված",                "Не битое",                      "Car is not damaged")
insertPhrase("car_is_damaged" ,     "Վթարված",                 "Битое",                         "Car is damaged")

insertPhrase("gas_no",              "Գազ չտեղադրված",          "Газ не установлен",             "Gas not Installed")          
insertPhrase("gas_installed"   ,    "Գազ տեղադրված",           "Газ установлен",                "Gas installed") 

insertPhrase('left_steering',       "Ղեկը ձախ",                "Левый руль",                    "Left hand drive")
insertPhrase('right_steering',      "Ղեկը աջ",                 "Правый руль",                   "Right hand drive")

insertPhrase("exterior_white",               "Սպիտակ",                  "Белый",                         "White")       
insertPhrase("exterior_silver",              "Արծաթագույն",             "Серебряный",                    "Silver")                   
insertPhrase("exterior_gray",                "Մոխրագույն",              "Серый",                         "Gray")           
insertPhrase("exterior_black",               "Սև",                      "Чёрный",                        "Black")       
insertPhrase("exterior_brown",               "Շագանակագույն",           "Коричневый",                    "Brown")                       
insertPhrase("exterior_gold",                "Ոսկեգույն",               "Золотой",                       "Gold")               
insertPhrase("exterior_beige",               "Բեժ",                     "Бежевый",                       "Beige")           
insertPhrase("exterior_red",                 "Կարմիր",                  "Красный",                       "Red")           
insertPhrase("exterior_blue",                "Կապույտ",                 "Синий",                         "Blue")       
insertPhrase("exterior_orange",              "Նարնջագույն",             "Оранжевый",                     "Orange")               
insertPhrase("exterior_yellow",              "Դեղին",                   "Жёлтый",                        "Yellow")           
insertPhrase("exterior_green",               "Կանաչ",                   "Зелёный",                       "Green")           
insertPhrase("exterior_cyan",                "Երկնագույն",              "Голубой",                       "Cyan")               
insertPhrase("exterior_maroon",              "Բորդո",                   "Бордовый",                      "Maroon")           
insertPhrase("exterior_pink",                "Վարդագույն",              "Розовый",                       "Pink")               
insertPhrase("exterior_purple",              "Մանուշակագույն",          "Фиолетовый",                    "Purple")             

insertPhrase("interior_white",               "Սպիտակ",                  "Белый",                         "White")       
insertPhrase("interior_gray",                "Մոխրագույն",              "Серый",                         "Gray")           
insertPhrase("interior_black",               "Սև",                      "Чёрный",                        "Black")       
insertPhrase("interior_brown",               "Շագանակագույն",           "Коричневый",                    "Brown")                       
insertPhrase("interior_beige",               "Բեժ",                     "Бежевый",                       "Beige")           
insertPhrase("interior_red",                 "Կարմիր",                  "Красный",                       "Red")           
insertPhrase("interior_blue",                "Կապույտ",                 "Синий",                         "Blue")       
insertPhrase("interior_other",               "Այլ",                     "Другой",                        "Other")       


insertPhrase("no_sunroof"       ,           "Լյուկ չկա",               "Люка нет",                      "No sunroof")
insertPhrase("regular_sunroof_sunroof"  ,   "Սովորական լյուկ",         "Обычный люк",                   "Regular sunroof")          
insertPhrase("panoramic_sunroof_sunroof",   "Պանորամային լյուկ",       "Панорамный люк",                "Panoramic sunroof")                     

insertPhrase("led_headlights"       ,       "Լեդ լուսարձակներ",        "Светодиодные фары",       "Led headlights")
insertPhrase("halogen_headlights"   ,       "Հալոգեն լուսարձակներկ",   "Галогенные фары",         "Halogen headlights")          
insertPhrase("\u0445enon_headlights",       "Քսենոնային լուսարձակներ", "Ксеноновые фары",         "Xenon headlights")                     

insertPhrase("leather",                     'Մատերիալ կաշի',         'Материал кожа',                 'Material leather')
insertPhrase("textile",                     'Մատերիալ կտոր',         'Материал текстиль',             'Material textile')
insertPhrase("other",                       'Մատերիալ այլ',          'Материал другой',               'Material other')
insertPhrase("alcantara",                   'Մատերիալ ալկանտարա',    'Материал алькантара',           'Material alcantara')
insertPhrase("velour",                      'Մատերիալ թավիշ',        'Материал велюр',                'Material velour')
insertPhrase("leatherette",                 'Մատերիալ դերմանտին',    'Материал искусственная кожа',   'Material leatherette')


phrasespy.close()