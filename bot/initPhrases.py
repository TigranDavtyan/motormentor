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

Ազատորեն ցանկացած հարց ուղղեք ադմինին: Վայելե՛ք Motor Mentor Bot-ը: Եկեք սկսենք!\n<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>""",


"""Добро пожаловать в бота Motor Mentor! Этот бот прогнозирует цены на автомобили на основе различных характеристик. Если вы продаете, покупаете или интересуетесь анализом рыночных тенденций, этот бот здесь, чтобы помочь вам.

Предоставляя информацию о вашем автомобиле, такую как марка, модель, год выпуска, пробег и т. д., бот оценит диапазон цен на ваш автомобиль. Это может помочь вам установить конкурентоспособную цену продажи, принять обоснованное решение о покупке или получить представление о факторах, влияющих на цену автомобиля.

Обратите внимание, что представленные прогнозы являются оценками, основанными на доступных данных. Фактические рыночные цены могут варьироваться в зависимости от таких факторов, как местоположение, состояние и рыночный спрос.

Наслаждайтесь использованием бота Motor Mentor! Не стесняйтесь задавать любые вопросы администратору. Давай начнем!\n<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>""",


"""Welcome to the Motor Mentor Bot! This bot predicts car prices based on various features. Whether you're selling, buying, or interested in analyzing market trends, this bot is here to assist you.

By providing details about your car, such as brand, model, year, mileage, and more, the bot will estimate the price range for your vehicle. This can help you set a competitive selling price, make informed buying decisions, or gain insights into the factors that influence car prices.

Please note that the predictions provided are estimates based on available data. Actual market prices may vary due to factors like location, condition, and market demand.

Enjoy using the Motor Mentor Bot! Feel free to ask any questions to the admin. Let's begin! \n<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>""")

#help
insertPhrase('help',
             'Եթե անելանելի վիճակում եք կամ հարցեր ունեք, կարող եք կապվել ադմինիստրատորի հետ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>։ Նա անպայման կօգնի ձեզ🙂', 
             'Если вы застряли или у вас есть какие-либо вопросы, вы можете связаться с администратором по адресу <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ Он обязательно вам поможет🙂', 
             'If you are stuck or have any questions you can contact the admin at <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ He will definitely help you🙂')

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
'''Ձեր վճարումը հաջող է եղել🎉 Բաժանորդագրությունն ավարտվում է [sub_end]-ին: Այժմ դուք կարող եք զգալ այս բոտի իրական ուժը💪''',
'''Ваш платеж прошел успешно🎉 Подписка заканчивается в [sub_end]. Теперь вы можете почувствовать настоящую мощь этого бота💪''',
'''Your payment was successfull🎉 Subscription ends at [sub_end]. Now you can feel the real power of this bot💪''')

# insertPhrase('billing_info', 
# 'Վճարման ամսաթիվը [date] է ([days] օր մինչև վճարումը): Վճարման գումարը [pay_amount] դրամ է:',
# 'Дата платежа [date] ([days] дней до платежа). Сумма платежа составляет [pay_amount] драм.',
# "Payment date is [date] ([days] days until payment). Payment amount is [pay_amount] dram.")

# insertPhrase('pay_button', '💵 Վճարել','💵 Платить','💵 Pay')

# insertPhrase('payment_image_sent', 'Շնորհակալություն! Ադմինը կվերանայի հաշիվ-ապրանքագիրը և կերկարաձգի ձեր բաժանորդագրությունը 🙂','Спасибо! Админ рассмотрит счет и продлит подписку 🙂','Thank you! The admin will review the invoice and will prolong your subscription 🙂')

# insertPhrase('payment_accepted', 'Ձեր [price] դրամ վճարումը հաջող է եղել','Ваш платеж в размере [price] драма успешно завершен','Your payment of [price] dram was successful.')

#Subscription
insertPhrase('subscription', '⭐️ Բաժանորդագրություն','⭐️ Подписка','⭐️ Subscription')

insertPhrase('sub_free', 'Անվճար','Бесплатный','Free')
insertPhrase('sub_premium', 'Պրեմիում','Премиум','Premium')
insertPhrase('sub_business', 'Բիզնես','Бизнес','Business')

insertPhrase('sub_info_free', 
             'Ձեր բաժանորդագրությունը «Անվճար» է: Եթե ցանկանում եք ունենալ «Պրեմիում» բաժանորդագրություն, դիմեք ադմինիստրատորին: Այն արժե ընդամենը <b>990 դրամ</b>, բայց դուք ստանում եք շատ օգտակար ֆունկցիոնալություն: <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Ваша подписка "Бесплатная". Если вы хотите иметь подписку «Премиум», свяжитесь с администратором. Это стоит всего <b>990 драм</b>, но вы получаете много полезного функционала. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Your subscription is "Free". If you want to have a "Premium" subscription contact the admin. It only costs <b>990 AMD</b> but you get a lot of useful functionality. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>')

insertPhrase('sub_info_premium', 
             'Ձեր բաժանորդագրությունը «Պրեմիում» է: Այն ավարտվում է [sub_end_days] օրից: Եթե ցանկանում եք երկարացնել բաժանորդագրությունը, դիմեք ադմինիստրատորին։ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Ваша подписка "Премиум". Он заканчивается через [sub_end_days] дней. Если вы хотите продлить подписку, свяжитесь с администратором. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Your subscription is "Premium". It ends in [sub_end_days] days. If you want to prolonge the subscription contact the admin. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>')


insertPhrase('subscription_not_enough', 
             'Ձեր բաժանորդագրությանը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը "[min_sub]" է',
             'Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: "[min_sub]"',
             'Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․ Contact the admin ')

# insertPhrase('subscription_end_close', 
# '⚠️ Զգուշացում ⚠️\nՁեր բաժանորդագրությունն ավարտվում է [days] օրից: Բաժանորդագրությունը վճարելու և երկարացնելու համար գնացեք «Վճարումներ» ընտրացանկը:',
# '⚠️ Внимание ⚠️\nВаша подписка заканчивается через [days] дней. Перейдите в меню «Оплата», чтобы оплатить и продлить подписку.',
# '⚠️ Warning ⚠️\nYour subscribtion ends in [days] days. Go to "Billing" menu to pay and prolong the subscription.')

insertPhrase('subscription_end', 
'❗️ Զգուշացում ❗️\nՁեր «Պրեմիում» բաժանորդագրությունն ավարտվել է: Կապվեք ադմինիստրատորի հետ՝ այն ակտիվացնելու համար: <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
'❗️ Предупреждение ❗️\nВаша подписка "Премиум" закончилась. Свяжитесь с администратором, чтобы активировать его. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
'❗️ Warning ❗️\nYour "Premium" subscribtion ended. Contact the administrator to activate it. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>')


#Referrals
insertPhrase('referral', '🔗 Ռեֆերալներ','🔗 Рефералы','🔗 Referrals')

insertPhrase('referral_info', 
'''Ուղարկեք այս հղումը ձեր ընկերներին և եթե նրանք օգտվեն այս բոտից, դուք կստանաք բոնուս:
Յուրաքանչյուր [bonus_refs] ուղղորդման համար ձեր Premium բաժանորդագրությունը կերկարաձգվի [bonus_days] օրով:
Ձեր ուղղորդման հղումն է \n<code>[ref_link]</code>''',
'''Отправьте эту ссылку своим друзьям, и если они воспользуются этим ботом, вы получите бонус.
За каждого [bonus_refs] реферала ваша Премиум-подписка будет продлена на [bonus_days] дней.
Ваша реферальная ссылка \n<code>[ref_link]</code>''',
'''Send this link to your friends and if they use this bot you will get a bonus. 
For every [bonus_refs] referrals your Premium subscription will be prolonged for [bonus_days] days.
Your referral link is \n<code>[ref_link]</code>''')

insertPhrase('no_referral_bonus', 
'Դուք ունեք [referrals] ուղղորդումներ: Ձեզ անհրաժեշտ են առնվազն [nrefs] ուղղորդումներ՝ բոնուսային [ndays] օրեր ստանալու համար:',
'У вас есть [referrals] рефералов. Вам нужно как минимум [nrefs] рефералов, чтобы получить бонусные [ndays] дней.',
'You have [referrals] referrals. You need at least [nrefs] referrals to get bonus [ndays] days.')

insertPhrase('referral_bonus',
'Դուք ունեք [referrals] ուղղորդումներ: Սեղմեք այս կոճակը՝ ձեր [ndays] օրվա բոնուսը ստանալու համար 😀',
'У вас есть [referrals] рефералов. Нажмите эту кнопку, чтобы получить бонус [ndays] дней 😀',
'You have [referrals] referrals. Press this button to get your [ndays] days bonus 😀')

insertPhrase('get_referral_bonus', '🎉 ՍՏԱՆԱԼ ԲՈՆՈՒՍ!!! 🎉', '🎉 ПОЛУЧИТЕ БОНУС!!! 🎉', '🎉 GET BONUS!!! 🎉')

insertPhrase('congratulate_bonus', 
'🎉 Շնորհավորում ենք!!! 🎉\n դուք ստացաք [ndays] օրվա բոնուս:', 
'🎉 Поздравляем!!! 🎉\n Вы получили бонус [ndays] дней.', 
'🎉 Congratulations!!! 🎉\n You got [ndays] days bonus.')


insertPhrase('phone_number', 'Հեռախոսահամար','Номер телефона','Phone number')
insertPhrase('deleted', '❌ Ջնջված է ❌','❌ Удалено ❌','❌ Deleted ❌')
insertPhrase('delete', '❌ Ջնջել', '❌ Удалить', '❌ Delete')









#User menu
insertPhrase('menu','📜 Մենյու','📜 Меню','📜 Menu')
insertPhrase('main_menu',
'''📜 Մենյու
⭐️-ով նշված կոճակներն ունեն գործողություններ, որոնք պահանջում են Պրեմիում բաժանորդագրություն:''', 
'''📜 Меню
Кнопки, отмеченные ⭐️, имеют действия, требующие Премиум-подписки.''', 
'''📜 Menu
Buttons marked with ⭐️ have actions which require Premium subscription.''')
insertPhrase('get_car_price','🚗 Ձեր մեքենայի արժեքը', '🚗 Цена вашего автомобиля', '🚗 Your car price')
insertPhrase('import_from_listam','🧾 Ներմուծել List.am-ից⭐️', '🧾 Импорт из List.am⭐️', '🧾 Import from List.am⭐️')
insertPhrase('import_from_myautoge','🧾 Ներմուծել MyAuto.ge-ից⭐️', '🧾 Импорт из MyAuto.ge⭐️', '🧾 Import from MyAuto.ge⭐️')
insertPhrase('saved_cars', '📌 Պահպանված մեքենաներ⭐️', '📌 Сохраненные автомобили⭐️', '📌 Saved cars⭐️')
insertPhrase('general_info','ℹ️ Ինֆո', 'ℹ️ Информация', 'ℹ️ Info')






insertPhrase('found_saved_car', 
             'Ձեր պահպանված մեքենայի պարամետրերի հիման վրա ես գտա [nCars] մեքենաներ: Այս ցանկը միշտ կարող եք տեսնել «📌 Պահպանված մեքենաներ» բաժնում։\n',
             'По вашим сохраненным параметрам автомобиля я нашел [nCars] автомобилей. Вы всегда можете увидеть этот список в меню "📌 Сохраненные автомобили".\n', 
             'Based on your saved car`s parameters I found [nCars] cars. You can always see this list in the "📌 Saved cars" menu.\n')
insertPhrase('found_cars_so_far', 'Մինչ այժմ գտնվել են [nCars] մեքենաներ:', 'На данный момент найдено [nCars] автомобилей.', 'Found [nCars] cars so far.')
# insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')
# insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')
# insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')
# insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')

#Admin
insertPhrase('add_ad', 'Add advertisement', 'Add advertisement', 'Add advertisement')
insertPhrase('visit_website', 'Visit website', 'Visit website', 'Visit website')

#Import from list am
insertPhrase('list_am_usage', 
             'Ներմուծեք ավտոմեքենայի տվյալները List.am-ից՝ պատճենելով և տեղադրելով մեքենայի էջի url-ը այստեղ, օրինակ՝ «https://www.list.am/item/19911991»', 
             'Импортируйте информацию об автомобиле из List.am, скопировав и вставив URL-адрес страницы автомобиля, например «https://www.list.am/item/19911991».', 
             'Import car detailes from List.am by copy and pasting the car page url here, like "https://www.list.am/item/19911991"')

insertPhrase('listam_not_possible', 
             'Ես չեմ կարող ներմուծել այս մեքենաների տվյալները, փորձեք մեկ ուրիշը:', 
             'Я не могу импортировать данные этого автомобиля, попробуйте другой.', 
             'I cant import this cars data, try another one.')

insertPhrase('search_for_cars', 'Փնտրել նման մեքենաներ', 'Искать такие машины', 'Search for cars like this')

insertPhrase('listam_what_to_do', 
             'Ի՞նչ եք ուզում անել սրա հետ:',
             'Что вы хотите с этим делать?',
             'What do you want to do with this?')


#Import from myauto ge
insertPhrase('myautoge_usage', 
             'Ներմուծեք ավտոմեքենայի տվյալները MyAuto.ge-ից՝ պատճենելով և տեղադրելով մեքենայի էջի url-ը այստեղ, օրինակ՝ <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>', 
             'Импортируйте информацию об автомобиле из MyAuto.ge, скопировав и вставив URL-адрес страницы автомобиля, например <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>.', 
             'Import car detailes from MyAuto.ge by copy and pasting the car page url here, like <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>')

insertPhrase('myautoge_not_possible', 
             'Ես չեմ կարող ներմուծել այս մեքենաների տվյալները, փորձեք մեկ ուրիշը:', 
             'Я не могу импортировать данные этого автомобиля, попробуйте другой.', 
             'I cant import this cars data, try another one.')

insertPhrase('myautoge_what_to_do', 
             'Ի՞նչ եք ուզում անել սրա հետ:',
             'Что вы хотите с этим делать?',
             'What do you want to do with this?')


insertPhrase('import_data', 'Ներմուծել ավտոմեքենայի պարամետրերը', 'Импорт параметров автомобиля', 'Import car parameters')
insertPhrase('show_price_updates', 'Ցույց տալ գների թարմացումները⭐️', 'Показать изменения цен⭐️', 'Show price updates⭐️')
insertPhrase('follow_price_updates', 'Հետևեք ապագա թարմացումներին⭐️', 'Следите за будущими обновлениями⭐️', 'Follow future updates⭐️')
insertPhrase('no_price_updates', '❌ Գների թարմացումներ չկան:', '❌Нет обновлений цен!', '❌ No price updates!')
insertPhrase('follow_successfull', 
             '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Մեքենան պահպանված է''', 
             '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Автомобиль сохранен''', 
             '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ Car saved''')

insertPhrase('remove_follow', '❌ Չհետևել', '❌ Отписаться', '❌ Unfollow')

insertPhrase('notify_price_update', 
             '''[car_brand] [model] 
[year]   [engine_size] L

Հին արժեք - [old_price] $
Նոր արժեք - [new_price] $

[url]''', 

             '''[car_brand] [model] 
[year]   [engine_size] L

Старая цена - [old_price] $
Новая цена  - [new_price] $

[url]''', 

             '''[car_brand] [model] 
[year]   [engine_size] L

Old price - [old_price] $
New price - [new_price] $

[url]''')


#Saved cars
insertPhrase('add_saved_car', '➕ Ավելացնել մեքենա', '➕ Добавить машину', '➕ Add car')
insertPhrase('saved_cars_info', 
             'Այստեղ դուք կարող եք ավելացնել մեքենաներ, և երբ շուկայում նման մեքենա լինի, բոտը ձեզ կտեղեկացնի:', 
             'Здесь вы можете добавлять автомобили и когда на рынке появится похожий автомобиль, бот уведомит вас об этом.', 
             'Here you can add cars and when there is a similar car on the market, bot will notify you.')

insertPhrase('save_car', '📌 Պահպանել մեքենան', '📌 Сохранить машину', '📌 Save car')
insertPhrase('car_saved', '✅ Մեքենան պահպանված է', '✅ Автомобиль сохранен', '✅ Car saved')
insertPhrase('choose_car_mileage_start',    
    'Խնդրում ենք ընտրել մեքենայի նվազագույն վազքը:',
    'Пожалуйста, выберите минимальный пробег автомобиля.',
    'Please choose the minimal mileage of the car.')
insertPhrase('choose_car_mileage_end',    
    'Խնդրում ենք ընտրել մեքենայի առավելագույն վազքը:',
    'Пожалуйста, выберите максимальный пробег автомобиля.',
    'Please choose the maximal mileage of the car.')

insertPhrase('choose_car_price_start',    
    'Խնդրում ենք ընտրել մեքենայի նվազագույն արժեքը:',
    'Пожалуйста, выберите минимальную цену автомобиля.',
    'Please choose the minimal price of the car.')
insertPhrase('choose_car_price_end',    
    'Խնդրում ենք ընտրել մեքենայի առավելագույն արժեքը:',
    'Пожалуйста, выберите максимальную цену автомобиля.',
    'Please choose the maximal price of the car.')
# insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')
# insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')



insertPhrase('wrong_format','❌ Սխալ ձևաչափ, նորից փորձեք', '❌ Неверный формат, попробуйте еще раз', '❌ Wrong format, try again')

#Car prices
insertPhrase('year', '[year] թ․', '[year]', '[year]')
insertPhrase('mileage', '[mileage] կմ', '[mileage] km', '[mileage] km')

insertPhrase('engine_size', '[engine_size] L', '[engine_size] L', '[engine_size] L')
insertPhrase('interior_color', '[interior_color] ինտերիեր', '[interior_color] интерьер', '[interior_color] interior')
insertPhrase('interior_material', '[interior_material]', '[interior_material]', '[interior_material]')
insertPhrase('wheel_size', 'R[wheel_size]', 'R[wheel_size]', 'R[wheel_size]')


insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate')
insertPhrase('calculate_by_year', '📈 Գների գրաֆիկը ըստ տարիների', '📈 График цен по годам', '📈 Price graph by year')
insertPhrase('calculate_by_mileage', '📉 Գների գրաֆիկը ըստ վազքի', '📉 График цен по пробегу', '📉 Price graph by mileage')

insertPhrase('label_price','Գինը','Цена','Price')
insertPhrase('label_year','Տարի','Год','Year')
insertPhrase('label_mileage','Վազքը','Пробег','Mileage')


insertPhrase('calculate_result_title', 
'''[url]
💰 ԳՆԵՐԻ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ 💰
''',

'''[url]
💰ИНФОРМАЦИЯ О ЦЕНАХ 💰
''',

'''[url]
💰  PRICE INFO  💰
''')

insertPhrase('result_arm',
             'Հայկական շուկա : [l_price] $ 💵',
             'Армянский рынок : [l_price] $ 💵',
             'Armenian market : [l_price] $ 💵')

insertPhrase('result_ge',
             'Վրացական շուկա : [g_price] $ 💵',
             'Грузинский рынок : [g_price] $ 💵',
             'Georgian market : [g_price] $ 💵')


insertPhrase('income_tax_result_arm',
             'Մաքսային վճար (Հայ.) : [l_price] $ 💵',
             'Таможенный сбор (Арм.) : [l_price] $ 💵',
             'Customs fee (Arm.) : [l_price] $ 💵')

insertPhrase('income_tax_result_ge',
             'Մաքսային վճար (Վրաստան) : [l_price] $ 💵',
             'Таможенный сбор (Грузия) : [l_price] $ 💵',
             'Customs fee (Georgia) : [l_price] $ 💵')


insertPhrase('result_ge_not_available',
'''Վրացական շուկա : ??? $ 💵
⭐️Վրաստանի գները իմանալու համար գրանցվեք Պրեմիում բաժանորդագրության համար''',

'''Грузинский рынок : ??? $ 💵
⭐️Чтобы узнать цены в Грузии, подпишитесь на Премиум подписку''',

'''Georgian market : ??? $ 💵
⭐️To know the prices in Georgia sign up for Premium subscription''')


insertPhrase('result_arm_not_available',
'''Հայկական շուկա : ??? $ 💵
⭐️Հայաստանի գները իմանալու համար գրանցվեք Պրեմիում բաժանորդագրության համար''',

'''Армянский  рынок : ??? $ 💵
⭐️Чтобы узнать цены в Армении, подпишитесь на Премиум подписку''',

'''Armenian market : ??? $ 💵
⭐️To know the prices in Armenia sign up for Premium subscription''')


insertPhrase('price_result_ask_arm',
             'Ի՞նչ եք կարծում, այս մեքենան խելամի՞տ է գնահատված Հայկական շուկայում: Պարտադիր չէ պատասխանեք այս հարցին, բայց դա կօգնի ավելի խելացի արհեստական ինտելեկտ կառուցել:',
             'Считаете ли вы, что этот автомобиль имеет разумную цену на Армянском рынке?? Вам не обязательно отвечать на этот вопрос, но это поможет создать более умный ИИ.',
             'Do you think this car is reasonably priced in Armenian market? You dont have to answer this but it will help build a better AI.')

insertPhrase('price_result_ask_ge',
             'Ի՞նչ եք կարծում, այս մեքենան խելամի՞տ է գնահատված Վրացական շուկայում: Պարտադիր չէ պատասխանեք այս հարցին, բայց դա կօգնի ավելի խելացի արհեստական ինտելեկտ կառուցել:',
             'Считаете ли вы, что этот автомобиль имеет разумную цену на Грузинском рынке? Вам не обязательно отвечать на этот вопрос, но это поможет создать более умный ИИ.',
             'Do you think this car is reasonably priced in Georgian market? You dont have to answer this but it will help build a better AI.')


insertPhrase('calculation_not_possible','❌ Այս մեքենայի համար գնի հաշվարկ հնարավոր չէ։','❌ Расчет цены для данного автомобиля невозможен!','❌ Price calculation is not possible for this car!')



insertPhrase('dont_know','Չգիտեմ','Я не знаю',"I don't know")
insertPhrase('my_price','Առաջարկել իմ գինը','Предложить мою цену','Offer my price')
insertPhrase('my_price_offer',
             'Ի՞նչ եք կարծում, ինչ արժե այս մեքենան դոլլարով: Գրեք ձեր պատասխանը այսպես «18000»',
             'Как вы думаете, сколько долларов стоит эта машина? Напишите свой ответ так: "18000"',
             'What do you think this car costs in dollars? Write your answer like this "18000" ')

insertPhrase('thanks_for_opinion', 'Շնորհակալություն կարծիքի համար 👌', 'Спасибо за ваше мнение 👌', "Thank you for your opinion 👌")


insertPhrase('car_price_info', 
'''Գոհունակություն. [satisfied][notsatisfied] [percent]%
Ընտրեք մեքենայի պարամետրերը և սեղմեք հաշվարկել՝ գինը ստանալու համար:
⚠️Արհեստական ինտելեկտը հաշվարկում է այս կոնկրետ մեքենայի ՄԻՋԻՆ ՇՈՒԿԱՅԱԿԱՆ ԱՐԺԵՔԸ շուկայում: Գնելիս կամ վաճառելիս մի հիմնեք ձեր որոշումները միայն այս արդյունքների վրա:''',
'''Удовлетворенность: [satisfied][notsatisfied] [percent]%
Выберите параметры автомобиля и нажмите рассчитать, чтобы узнать цену․
⚠️ИИ рассчитывает СРЕДНЮЮ РЫНОЧНУЮ СТОИМОСТЬ для данного конкретного автомобиля на рынке․ Не основывайте свои решения только на этих результатах при покупке или продаже.''',
'''Satisfaction: [satisfied][notsatisfied] [percent]%
Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car in the market. Dont base your decisions only on this results when buying or selling.''')



insertPhrase('choose_car_brand',             
    'Խնդրում եմ ընտրեք ձեր մեքենայի մակնիշը։ Եթե ստորև ներկայացված չէ ձեր մեքենայի մակնիշը, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:',
    'Пожалуйста, выберите марку вашего автомобиля. Если марка вашего автомобиля не указана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.',
    'Please choose the brand of your car. If the brand of your car is not shown below it means there is not enough data and the AI cant make a good prediction.')

insertPhrase('choose_car_model',             
    'Խնդրում եմ ընտրել ձեր մեքենայի մոդելը։ Եթե ձեր մեքենայի մոդելը ներկայացված չէ ստորև, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:',  
    'Пожалуйста, выберите модель вашего автомобиля. Если модель вашего автомобиля не показана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.',
    'Please choose the model of your car. If the model of your car is not shown below it means there is not enough data and the AI cant make a good prediction.')

insertPhrase('choose_car_year',
    'Խնդրում ենք ընտրել ձեր մեքենայի արտադրության տարեթիվը:',
    'Пожалуйста, выберите год выпуска вашего автомобиля.',
    'Please choose the manufacturing year of your car.')
insertPhrase('choose_car_mileage',
    'Խնդրում ենք ընտրել ձեր մեքենայի վազքը:',
    'Пожалуйста, выберите пробег вашего автомобиля.',
    'Please choose the mileage of your car.')
insertPhrase('choose_car_engine_size',       
    'Խնդրում ենք ընտրել ձեր մեքենայի շարժիչի չափը:',
    'Пожалуйста, выберите объем двигателя вашего автомобиля.',
    'Please choose the engine size of your car.')
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
    'Խնդրում ենք ընտրել ձեր մեքենայի անիվի չափը:',
    'Пожалуйста, выберите размер колес вашего автомобиля.',
    'Please choose the wheel size of your car.')


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
insertPhrase('hydrogen',            "Ջրածնային",                "Водородный",                   "Hydrogen")


insertPhrase("manual",              "Մեխանիկական",              "Механическая",                 "Manual")
insertPhrase("automatic",           "Ավտոմատ",                  "Автоматическая",               "Automatic")

insertPhrase("front_wheel_drive",   "Առջևի քարշակ",            "Передний привод",               "Front Wheel Drive")
insertPhrase("rear_wheel_drive",    "Ետևի քարշակ",             "Задний привод",                 "Rear Wheel Drive")
insertPhrase("all_wheel_drive",     "Լիաքարշակ",               "Полный привод",                 "All Wheel Drive")

insertPhrase("car_is_not_damaged",  "Չվթարված",                "Не битое",                      "Car is not damaged")
insertPhrase("car_is_damaged" ,     "Վթարված",                 "Битое",                         "Car is damaged")

insertPhrase("gas_no",              "Գազ չտեղադրված",          "Газ не установлен",             "Gas not Installed")          
insertPhrase("gas_installed",       "Գազ տեղադրված",           "Газ установлен",                "Gas installed") 

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
insertPhrase("interior_gold",                "Ոսկեգույն",               "Золотой",                       "Gold")
insertPhrase("interior_maroon",              "Բորդո",                   "Бордовый",                      "Maroon")
insertPhrase("interior_orange",              "Նարնջագույն",             "Оранжевый",                     "Orange")      
insertPhrase("interior_yellow",              "Դեղին",                   "Жёлтый",                        "Yellow")    

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