import re

def insertPhrase(name:str, arm:str, rus:str, eng:str, ge:str):
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
    phrases = ['''{arm}''', '''{rus}''', '''{eng}''', '''{ge}''']
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
ENG = 2
GE  = 3''')


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

Enjoy using the Motor Mentor Bot! Feel free to ask any questions to the admin. Let's begin! \n<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>""",

"""კეთილი იყოს თქვენი მობრძანება Motor Mentor Bot-ში! ეს ბოტი პროგნოზირებს მანქანის ფასებს სხვადასხვა მახასიათებლების საფუძველზე. მიუხედავად იმისა, ყიდით, ყიდულობთ ან დაინტერესებული ხართ ბაზრის ტენდენციების ანალიზით, ეს ბოტი აქ არის დაგეხმაროთ.

თქვენი მანქანის შესახებ დეტალების მიწოდებით, როგორიცაა ბრენდი, მოდელი, წელი, გარბენი და სხვა, ბოტი შეაფასებს თქვენი მანქანის ფასის დიაპაზონს. ეს დაგეხმარებათ დააყენოთ კონკურენტული გასაყიდი ფასი, მიიღოთ ინფორმირებული შესყიდვის გადაწყვეტილებები ან მიიღოთ ინფორმაცია იმ ფაქტორებზე, რომლებიც გავლენას ახდენენ მანქანის ფასებზე.

გთხოვთ გაითვალისწინოთ, რომ მოწოდებული პროგნოზები შეფასებებია ხელმისაწვდომი მონაცემების საფუძველზე. ფაქტობრივი საბაზრო ფასები შეიძლება განსხვავდებოდეს ისეთი ფაქტორების გამო, როგორიცაა მდებარეობა, მდგომარეობა და ბაზრის მოთხოვნა.

ისიამოვნეთ Motor Mentor Bot-ის გამოყენებით! თავისუფლად დაუსვით ნებისმიერი შეკითხვა ადმინს. Მოდით დავიწყოთ! \n<a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>""")

#help
insertPhrase('help',
             'Եթե անելանելի վիճակում եք կամ հարցեր ունեք, կարող եք կապվել ադմինիստրատորի հետ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>։ Նա անպայման կօգնի ձեզ🙂', 
             'Если вы застряли или у вас есть какие-либо вопросы, вы можете связаться с администратором по адресу <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ Он обязательно вам поможет🙂', 
             'If you are stuck or have any questions you can contact the admin at <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>․ He will definitely help you🙂',
             'თუ გაჭედილი ხართ ან გაქვთ რაიმე შეკითხვა, შეგიძლიათ დაუკავშირდეთ ადმინისტრატორს მისამართზე <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>. ის აუცილებლად დაგეხმარება 🙂')

#language
insertPhrase('language_change','🇦🇲🇷🇺🇺🇸🇬🇪 Փոխել լեզուն', '🇦🇲🇷🇺🇺🇸🇬🇪 Изменить язык', '🇦🇲🇷🇺🇺🇸🇬🇪 Change language', '🇦🇲🇷🇺🇺🇸🇬🇪 Ენის შეცვლა')
insertPhrase('language_choose','Ընտրեք լեզուն 🇦🇲', 'Выберите язык 🇷🇺', 'Select language 🇺🇸', 'Აირჩიეთ ენა 🇬🇪')
insertPhrase('languages','Հայերեն🇦🇲', 'Русский🇷🇺', 'English🇺🇸', 'Georgian🇬🇪')
insertPhrase('language_set','Ընտրվեց հայերեն լեզուն 🇦🇲','Выбран русский язык 🇷🇺','English is selected 🇺🇸', 'შერჩეულია ქართული 🇬🇪')

insertPhrase('agree','✅ Համաձայն եմ!','✅ Я согласен!','✅ I agree!','✅ Ვეთანხმები!')
insertPhrase('disagree','❌ Համաձայն չեմ','❌ Я не согласен','❌ I disagree','❌ არ ვეთანხმები')
insertPhrase('cancel','🚫 Չեղարկել','🚫 Отменить','🚫 Cancel','🚫 გაუქმება')
insertPhrase('canceled','🚫 Չեղարկված է','🚫 Отменено','🚫 Canceled','🚫 გაუქმდა')
insertPhrase('all_right','✅ Ճիշտ է','✅ Все верно',"✅ That's right","✅ Სწორია")
insertPhrase('back','👈 Վերադառնալ','👈 Назад','👈 Back','👈 უკან')
insertPhrase('skip','👉 Բաց թողնել','👉 Пропустить','👉 Skip', '👉 გამოტოვება')
insertPhrase('confirm','👍 Հաստատել','👍 Подтвердить','👍 Confirm','👍 დაადასტურეთ')
insertPhrase('confirmed','👍 Հաստատված է','👍 Подтверждено','👍 Confirmed','👍 დადასტურდა')
insertPhrase('yes','✅ Այո՛', '✅ Да', '✅ Yes', '✅ დიახ')
insertPhrase('no','❌ Ոչ', '❌ Нет', '❌ No', '❌ არა')
insertPhrase('ok', 'օկ', 'ок', 'ok', 'კარგი')

insertPhrase('wrong_action',
             '❌Սխալ գործողություն❌\n Կրկին կարդացեք հաղորդագրությունը☝️, ստացեք /help ադմինիստրատորից կամ /start արեք և նորից փորձեք:',
             '❌Неверное действие❌\n Прочитайте сообщение еще раз☝️, получите /help от администратора или вернитесь и повторите попытку.',
             '❌Wrong action❌\n Read the message again☝️, get /help from admin or go to /start and try again.',
             '❌არასწორი ქმედება❌\n ხელახლა წაიკითხეთ შეტყობინება☝️, მიიღეთ /დახმარება ადმინისტრატორისგან ან გადადით /start-ზე და სცადეთ ხელახლა.')


insertPhrase('duration','Տևողություն', 'Продолжительность', 'Duration', 'ხანგრძლივობა')
insertPhrase('fee','Վճար', 'Плата', 'Fee', 'საფასური')
insertPhrase('dram','դրամ', 'драм', 'amd', 'ამდ')
insertPhrase('minute','րոպե', 'минут', 'minutes', 'წუთები')

insertPhrase('today','Այսօր', 'Сегодня', 'Today', 'დღეს')
insertPhrase('tomorrow','Վաղը', 'Завтра', 'Tomorrow', 'ხვალ')
insertPhrase('afterTomorrow','Վաղը չէ մյուս օրը', 'Послезавтра', 'The day after tomorrow', 'ზეგ')
insertPhrase('date','Ամսաթիվ', 'Дата', 'Date', 'თარიღი')

insertPhrase('start2', 'Սկիզբ', 'Начало', 'Start', 'დაწყება')
insertPhrase('end', 'Վերջ', 'Конец', 'End', 'Დასასრული')
insertPhrase('day', 'Օր', 'День', 'Day', 'Დღეს')


insertPhrase('january',     'Հունվարի',   'Январь',  'January',  'იანვარი')
insertPhrase('february',    'Փետրվարի',   'Февраль', 'February', 'თებერვალი')
insertPhrase('march',       'Մարտի',      'Март',    'March',    'მარტი')
insertPhrase('april',       'Ապրիլի',     'Апрель',  'April',  'აპრილი')
insertPhrase('may',         'Մայիսի',     'Май',     'May',     'მაისი')
insertPhrase('june',        'Հունիսի',    'Нюнь',    'June',    'ივნისი')
insertPhrase('july',        'Հուլիսի',    'Июль',    'July',    'ივლისი')
insertPhrase('august',      'Օգոստոսի',   'Август',  'August',  'აგვისტო')
insertPhrase('september',   'Սեպտեմբերի', 'Сентябрь','September','სექტემბერი')
insertPhrase('october',     'Հոկտեմբերի', 'Октябрь', 'October', 'ოქტომბერი')
insertPhrase('november',    'Նոյեմբերի',  'Ноябрь',  'November',  'ნოემბერი')
insertPhrase('december',    'Դեկտեմբերի', 'Декабрь', 'December', 'დეკემბერი')

insertPhrase('details','🧾','🧾','🧾','🧾')
insertPhrase('cancel','❌','❌','❌','❌')

insertPhrase('anonymous', 'անհայտ 🤷‍♀️','неизвестный 🤷‍♀️','unknown 🤷‍♀️', 'უცნობი 🤷‍♀️')

insertPhrase('payment_successfull', 
'''Ձեր վճարումը հաջող է եղել🎉 Բաժանորդագրությունն ավարտվում է [sub_end]-ին: Այժմ դուք կարող եք զգալ այս բոտի իրական ուժը💪''',
'''Ваш платеж прошел успешно🎉 Подписка заканчивается в [sub_end]. Теперь вы можете почувствовать настоящую мощь этого бота💪''',
'''Your payment was successfull🎉 Subscription ends at [sub_end]. Now you can feel the real power of this bot💪''',
'''თქვენი გადახდა წარმატებით დასრულდა🎉 გამოწერა სრულდება [sub_end]-ზე. ახლა თქვენ შეგიძლიათ იგრძნოთ ამ ბოტის ნამდვილი ძალა 💪''')

# insertPhrase('billing_info', 
# 'Վճարման ամսաթիվը [date] է ([days] օր մինչև վճարումը): Վճարման գումարը [pay_amount] դրամ է:',
# 'Дата платежа [date] ([days] дней до платежа). Сумма платежа составляет [pay_amount] драм.',
# "Payment date is [date] ([days] days until payment). Payment amount is [pay_amount] dram.")

# insertPhrase('pay_button', '💵 Վճարել','💵 Платить','💵 Pay')

# insertPhrase('payment_image_sent', 'Շնորհակալություն! Ադմինը կվերանայի հաշիվ-ապրանքագիրը և կերկարաձգի ձեր բաժանորդագրությունը 🙂','Спасибо! Админ рассмотрит счет и продлит подписку 🙂','Thank you! The admin will review the invoice and will prolong your subscription 🙂')

# insertPhrase('payment_accepted', 'Ձեր [price] դրամ վճարումը հաջող է եղել','Ваш платеж в размере [price] драма успешно завершен','Your payment of [price] dram was successful.')

#Subscription
insertPhrase('subscription', '⭐️ Բաժանորդագրություն','⭐️ Подписка','⭐️ Subscription','⭐️ გამოწერა')

insertPhrase('sub_free', 'Անվճար','Бесплатный','Free','უფასო')
insertPhrase('sub_premium', 'Պրեմիում','Премиум','Premium','პრემიუმი')
insertPhrase('sub_business', 'Բիզնես','Бизнес','Business','ბიზნესი')

insertPhrase('sub_info_free', 
             'Ձեր բաժանորդագրությունը «Անվճար» է: Եթե ցանկանում եք ունենալ «Պրեմիում» բաժանորդագրություն, դիմեք ադմինիստրատորին: Այն արժե ընդամենը <b>990 դրամ</b>, բայց դուք ստանում եք շատ օգտակար ֆունկցիոնալություն: <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Ваша подписка "Бесплатная". Если вы хотите иметь подписку «Премиум», свяжитесь с администратором. Это стоит всего <b>990 драм</b>, но вы получаете много полезного функционала. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Your subscription is "Free". If you want to have a "Premium" subscription contact the admin. It only costs <b>990 AMD</b> but you get a lot of useful functionality. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'თქვენი გამოწერა არის "უფასო". თუ გსურთ გქონდეთ "Premium" გამოწერა დაუკავშირდით ადმინისტრატორს. ის მხოლოდ <b>990 AMD ღირს</b> მაგრამ თქვენ მიიღებთ უამრავ სასარგებლო ფუნქციას. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>')

insertPhrase('sub_info_premium', 
             'Ձեր բաժանորդագրությունը «Պրեմիում» է: Այն ավարտվում է [sub_end_days] օրից: Եթե ցանկանում եք երկարացնել բաժանորդագրությունը, դիմեք ադմինիստրատորին։ <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Ваша подписка "Премиум". Он заканчивается через [sub_end_days] дней. Если вы хотите продлить подписку, свяжитесь с администратором. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'Your subscription is "Premium". It ends in [sub_end_days] days. If you want to prolonge the subscription contact the admin. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
             'თქვენი გამოწერა არის "Premium". ის მთავრდება [sub_end_days] დღეში. თუ გსურთ გამოწერის გახანგრძლივება, დაუკავშირდით ადმინისტრატორს. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>')


insertPhrase('subscription_not_enough', 
             'Ձեր բաժանորդագրությանը ([user_sub]) բավարար չէ այս գործողության համար: Այս գործողության համար բաժանորդագրության նվազագույն մակարդակը "[min_sub]" է',
             'Уровень вашей подписки ([user_sub]) недостаточен для этого действия. Минимальный уровень подписки для этого действия: "[min_sub]"',
             'Your subscription ([user_sub]) is not sufficient for this action. Minimum subscription level for this action is "[min_sub]"․',
             'თქვენი გამოწერა ([user_sub]) არ არის საკმარისი ამ მოქმედებისთვის. ამ მოქმედებისთვის გამოწერის მინიმალური დონეა „[min_sub]“.')

# insertPhrase('subscription_end_close', 
# '⚠️ Զգուշացում ⚠️\nՁեր բաժանորդագրությունն ավարտվում է [days] օրից: Բաժանորդագրությունը վճարելու և երկարացնելու համար գնացեք «Վճարումներ» ընտրացանկը:',
# '⚠️ Внимание ⚠️\nВаша подписка заканчивается через [days] дней. Перейдите в меню «Оплата», чтобы оплатить и продлить подписку.',
# '⚠️ Warning ⚠️\nYour subscribtion ends in [days] days. Go to "Billing" menu to pay and prolong the subscription.')

insertPhrase('subscription_end', 
'❗️ Զգուշացում ❗️\nՁեր «Պրեմիում» բաժանորդագրությունն ավարտվել է: Կապվեք ադմինիստրատորի հետ՝ այն ակտիվացնելու համար: <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
'❗️ Предупреждение ❗️\nВаша подписка "Премиум" закончилась. Свяжитесь с администратором, чтобы активировать его. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
'❗️ Warning ❗️\nYour "Premium" subscribtion ended. Contact the administrator to activate it. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>',
'❗️ გაფრთხილება ❗️\თქვენი "Premium" გამოწერა დასრულდა. დაუკავშირდით ადმინისტრატორს მის გასააქტიურებლად. <a href="https://t.me/MotorMentorAdmin">Motor Mentor Admin</a>')


#Referrals
insertPhrase('referral', '🔗 Ռեֆերալներ','🔗 Рефералы','🔗 Referrals','🔗 რეფერალები')

insertPhrase('referral_info', 
'''Ուղարկեք այս հղումը ձեր ընկերներին և եթե նրանք օգտվեն այս բոտից, դուք կստանաք բոնուս:
Յուրաքանչյուր [bonus_refs] ուղղորդման համար ձեր Premium բաժանորդագրությունը կերկարաձգվի [bonus_days] օրով:
Ձեր ուղղորդման հղումն է \n<code>[ref_link]</code>''',
'''Отправьте эту ссылку своим друзьям, и если они воспользуются этим ботом, вы получите бонус.
За каждого [bonus_refs] реферала ваша Премиум-подписка будет продлена на [bonus_days] дней.
Ваша реферальная ссылка \n<code>[ref_link]</code>''',
'''Send this link to your friends and if they use this bot you will get a bonus. 
For every [bonus_refs] referrals your Premium subscription will be prolonged for [bonus_days] days.
Your referral link is \n<code>[ref_link]</code>''',
'''გაუგზავნეთ ეს ბმული თქვენს მეგობრებს და თუ ისინი გამოიყენებენ ამ ბოტს, თქვენ მიიღებთ ბონუსს.
ყოველი [bonus_refs] მიმართვისთვის თქვენი Premium გამოწერა გაგრძელდება [bonus_days] დღით.
თქვენი რეფერალური ბმული არის \n<code>[ref_link]</code>''')

insertPhrase('no_referral_bonus', 
'Դուք ունեք [referrals] ուղղորդումներ: Ձեզ անհրաժեշտ են առնվազն [nrefs] ուղղորդումներ՝ բոնուսային [ndays] օրեր ստանալու համար:',
'У вас есть [referrals] рефералов. Вам нужно как минимум [nrefs] рефералов, чтобы получить бонусные [ndays] дней.',
'You have [referrals] referrals. You need at least [nrefs] referrals to get bonus [ndays] days.',
'თქვენ გაქვთ [რეფერალური] მიმართვები. თქვენ გჭირდებათ მინიმუმ [nrefs] მიმართვები, რომ მიიღოთ ბონუს [დღე] დღე.')

insertPhrase('referral_bonus',
'Դուք ունեք [referrals] ուղղորդումներ: Սեղմեք այս կոճակը՝ ձեր [ndays] օրվա բոնուսը ստանալու համար 😀',
'У вас есть [referrals] рефералов. Нажмите эту кнопку, чтобы получить бонус [ndays] дней 😀',
'You have [referrals] referrals. Press this button to get your [ndays] days bonus 😀',
'თქვენ გაქვთ [რეფერალური] მიმართვები. დააჭირეთ ამ ღილაკს, რომ მიიღოთ თქვენი [დღის] დღის ბონუსი 😀')

insertPhrase('get_referral_bonus', '🎉 ՍՏԱՆԱԼ ԲՈՆՈՒՍ!!! 🎉', '🎉 ПОЛУЧИТЕ БОНУС!!! 🎉', '🎉 GET BONUS!!! 🎉', '🎉 მიიღეთ ბონუსი!!! 🎉')

insertPhrase('congratulate_bonus', 
'🎉 Շնորհավորում ենք!!! 🎉\n դուք ստացաք [ndays] օրվա բոնուս:', 
'🎉 Поздравляем!!! 🎉\n Вы получили бонус [ndays] дней.', 
'🎉 Congratulations!!! 🎉\n You got [ndays] days bonus.',
'🎉 გილოცავთ!!! 🎉\და თქვენ მიიღეთ [ndays] დღე ბონუსი.')


insertPhrase('phone_number', 'Հեռախոսահամար','Номер телефона','Phone number', 'Ტელეფონის ნომერი')
insertPhrase('deleted', '❌ Ջնջված է ❌','❌ Удалено ❌','❌ Deleted ❌','❌ წაშლილია ❌')
insertPhrase('delete', '❌ Ջնջել', '❌ Удалить', '❌ Delete', '❌ წაშლა')




#User menu
insertPhrase('menu','📜 Մենյու','📜 Меню','📜 Menu','📜 მენიუ')
insertPhrase('main_menu',
'''📜 Մենյու
⭐️-ով նշված կոճակներն ունեն գործողություններ, որոնք պահանջում են Պրեմիում բաժանորդագրություն:''', 
'''📜 Меню
Кнопки, отмеченные ⭐️, имеют действия, требующие Премиум-подписки.''', 
'''📜 Menu
Buttons marked with ⭐️ have actions which require Premium subscription.''',
'''📜 მენიუ
⭐️-ით მონიშნულ ღილაკებს აქვთ მოქმედებები, რომლებიც საჭიროებს Premium-ის გამოწერას.''')

insertPhrase('get_car_price','🚗 Ձեր մեքենայի արժեքը', '🚗 Цена вашего автомобиля', '🚗 Your car price', '🚗 თქვენი მანქანის ფასი')
insertPhrase('import_from_listam','🧾 Ներմուծել List.am-ից⭐️', '🧾 Импорт из List.am⭐️', '🧾 Import from List.am⭐️', '🧾 იმპორტი List.am-დან⭐️')
insertPhrase('import_from_myautoge','🧾 Ներմուծել MyAuto.ge-ից⭐️', '🧾 Импорт из MyAuto.ge⭐️', '🧾 Import from MyAuto.ge⭐️', '🧾 იმპორტი MyAuto.ge-დან⭐️')
insertPhrase('saved_cars', '📌 Պահպանված մեքենաներ⭐️', '📌 Сохраненные автомобили⭐️', '📌 Saved cars⭐️', '📌 შენახული მანქანები⭐️')
insertPhrase('general_info','ℹ️ Ինֆո', 'ℹ️ Информация', 'ℹ️ Info', 'ℹ️ ინფორმაცია')




insertPhrase('found_saved_car', 
             'Ձեր պահպանված մեքենայի պարամետրերի հիման վրա ես գտա [nCars] մեքենաներ: Այս ցանկը միշտ կարող եք տեսնել «📌 Պահպանված մեքենաներ» բաժնում։\n',
             'По вашим сохраненным параметрам автомобиля я нашел [nCars] автомобилей. Вы всегда можете увидеть этот список в меню "📌 Сохраненные автомобили".\n', 
             'Based on your saved car`s parameters I found [nCars] cars. You can always see this list in the "📌 Saved cars" menu.\n',
             'თქვენი შენახული მანქანის პარამეტრებზე დაყრდნობით ვიპოვე [nCars] მანქანები. ამ სიის ნახვა ყოველთვის შეგიძლიათ მენიუში „📌 შენახული მანქანები“.\n')

insertPhrase('found_cars_so_far', 'Մինչ այժմ գտնվել են [nCars] մեքենաներ:', 'На данный момент найдено [nCars] автомобилей.', 'Found [nCars] cars so far.', 'ნაპოვნია [nCars] მანქანები ჯერჯერობით.')


#Admin
insertPhrase('add_ad', 'Add advertisement', 'Add advertisement', 'Add advertisement', 'Add advertisement')
insertPhrase('visit_website', 'Visit website', 'Visit website', 'Visit website', 'Visit website')

#Import from list am
insertPhrase('list_am_usage', 
             'Ներմուծեք ավտոմեքենայի տվյալները List.am-ից՝ պատճենելով և տեղադրելով մեքենայի էջի url-ը այստեղ, օրինակ՝ «https://www.list.am/item/19911991»', 
             'Импортируйте информацию об автомобиле из List.am, скопировав и вставив URL-адрес страницы автомобиля, например «https://www.list.am/item/19911991».', 
             'Import car detailes from List.am by copy and pasting the car page url here, like "https://www.list.am/item/19911991"',
             'მანქანის დეტალების იმპორტი List.am-დან მანქანის გვერდის url-ის კოპირებით და ჩასმით აქ, როგორიცაა "https://www.list.am/item/19911991"')

insertPhrase('listam_not_possible', 
             'Ես չեմ կարող ներմուծել այս մեքենաների տվյալները, փորձեք մեկ ուրիշը:', 
             'Я не могу импортировать данные этого автомобиля, попробуйте другой.', 
             'I cant import this cars data, try another one.',
             'მე არ შემიძლია ამ მანქანის მონაცემების იმპორტი, სცადე სხვა.')

insertPhrase('search_for_cars', 'Փնտրել նման մեքենաներ', 'Искать такие машины', 'Search for cars like this', 'მოძებნეთ მსგავსი მანქანები')

insertPhrase('listam_what_to_do', 
             'Ի՞նչ եք ուզում անել սրա հետ:',
             'Что вы хотите с этим делать?',
             'What do you want to do with this?',
             'რისი გაკეთება გინდა ამით?')


#Import from myauto ge
insertPhrase('myautoge_usage', 
             'Ներմուծեք ավտոմեքենայի տվյալները MyAuto.ge-ից՝ պատճենելով և տեղադրելով մեքենայի էջի url-ը այստեղ, օրինակ՝ <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>', 
             'Импортируйте информацию об автомобиле из MyAuto.ge, скопировав и вставив URL-адрес страницы автомобиля, например <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>.', 
             'Import car detailes from MyAuto.ge by copy and pasting the car page url here, like <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200-2001-benzinvsprysk-tbilisi?offerType=superVip</code>',
             'მანქანის დეტალების იმპორტი MyAuto.ge-დან მანქანის გვერდის url-ის კოპირებით და ჩასმით აქ, მოიწონეთ <code>https://www.myauto.ge/ru/pr/94171446/prodaetsya-mashini-kupe-mercedes-benz-c-200 -2001-benzinvsprysk-tbilisi?offerType=superVip</code>')

insertPhrase('myautoge_not_possible', 
             'Ես չեմ կարող ներմուծել այս մեքենաների տվյալները, փորձեք մեկ ուրիշը:', 
             'Я не могу импортировать данные этого автомобиля, попробуйте другой.', 
             'I cant import this cars data, try another one.',
             'მე არ შემიძლია ამ მანქანის მონაცემების იმპორტი, სცადე სხვა.')

insertPhrase('myautoge_what_to_do', 
             'Ի՞նչ եք ուզում անել սրա հետ:',
             'Что вы хотите с этим делать?',
             'What do you want to do with this?',
             'რისი გაკეთება გინდა ამით?')


insertPhrase('import_data', 'Ներմուծել ավտոմեքենայի պարամետրերը', 'Импорт параметров автомобиля', 'Import car parameters', 'მანქანის პარამეტრების იმპორტი')
insertPhrase('show_price_updates', 'Ցույց տալ գների թարմացումները⭐️', 'Показать изменения цен⭐️', 'Show price updates⭐️', 'ფასების განახლებების ჩვენება⭐️')
insertPhrase('follow_price_updates', 'Հետևեք ապագա թարմացումներին⭐️', 'Следите за будущими обновлениями⭐️', 'Follow future updates⭐️', 'მიჰყევით მომავალ განახლებებს⭐️')
insertPhrase('no_price_updates', '❌ Գների թարմացումներ չկան:', '❌Нет обновлений цен!', '❌ No price updates!', '❌ ფასის განახლებები არ არის!')
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
✅ Car saved''', 
             '''[car_brand] [model] 
[year]   [engine_size] L
[price] $
✅ მანქანა შენახულია''')

insertPhrase('remove_follow', '❌ Չհետևել', '❌ Отписаться', '❌ Unfollow', '❌ გააუქმეთ თვალი')

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

[url]''', 

             '''[car_brand] [model] 
[year]   [engine_size] L

ძველი ფასი - [old_price] $
ახალი ფასი - [new_price] $

[url]''')


#Saved cars
insertPhrase('add_saved_car', '➕ Ավելացնել մեքենա', '➕ Добавить машину', '➕ Add car', '➕ მანქანის დამატება')
insertPhrase('saved_cars_info', 
             'Այստեղ դուք կարող եք ավելացնել մեքենաներ, և երբ շուկայում նման մեքենա լինի, բոտը ձեզ կտեղեկացնի:', 
             'Здесь вы можете добавлять автомобили и когда на рынке появится похожий автомобиль, бот уведомит вас об этом.', 
             'Here you can add cars and when there is a similar car on the market, bot will notify you.',
             'აქ შეგიძლიათ დაამატოთ მანქანები და როდესაც მსგავსი მანქანა იქნება ბაზარზე, ბოტი შეგატყობინებთ.')

insertPhrase('save_car', '📌 Պահպանել մեքենան', '📌 Сохранить машину', '📌 Save car', '📌 მანქანის შენახვა')
insertPhrase('car_saved', '✅ Մեքենան պահպանված է', '✅ Автомобиль сохранен', '✅ Car saved', '✅ მანქანა შენახულია')
insertPhrase('choose_car_mileage_start',    
    'Խնդրում ենք ընտրել մեքենայի նվազագույն վազքը:',
    'Пожалуйста, выберите минимальный пробег автомобиля.',
    'Please choose the minimum mileage of the car.',
    'გთხოვთ, აირჩიოთ მანქანის მინიმალური გარბენი.')
insertPhrase('choose_car_mileage_end',    
    'Խնդրում ենք ընտրել մեքենայի առավելագույն վազքը:',
    'Пожалуйста, выберите максимальный пробег автомобиля.',
    'Please choose the maximum mileage of the car.',
    'გთხოვთ, აირჩიოთ მანქანის მაქსიმალური გარბენი.')

insertPhrase('choose_car_price_start',    
    'Խնդրում ենք ընտրել մեքենայի նվազագույն արժեքը:',
    'Пожалуйста, выберите минимальную цену автомобиля.',
    'Please choose the minimum price of the car.',
    'გთხოვთ აირჩიოთ მანქანის მინიმალური ფასი.')
insertPhrase('choose_car_price_end',    
    'Խնդրում ենք ընտրել մեքենայի առավելագույն արժեքը:',
    'Пожалуйста, выберите максимальную цену автомобиля.',
    'Please choose the maximum price of the car.',
    'გთხოვთ აირჩიოთ მანქანის მაქსიმალური ფასი.')



insertPhrase('wrong_format','❌ Սխալ ձևաչափ, նորից փորձեք', '❌ Неверный формат, попробуйте еще раз', '❌ Wrong format, try again', '❌ არასწორი ფორმატია, სცადეთ ხელახლა')

#Car prices
insertPhrase('year', '[year] թ․', '[year]', '[year]', '[year]')
insertPhrase('mileage', '[mileage] կմ', '[mileage] km', '[mileage] km', '[mileage] km')

insertPhrase('engine_size', '[engine_size] L', '[engine_size] L', '[engine_size] L', '[engine_size] L')
insertPhrase('interior_color', '[interior_color] ինտերիեր', '[interior_color] интерьер', '[interior_color] interior', '[interior_color] ინტერიერი')
insertPhrase('interior_material', '[interior_material]', '[interior_material]', '[interior_material]', '[interior_material]')
insertPhrase('wheel_size', 'R[wheel_size]', 'R[wheel_size]', 'R[wheel_size]', 'R[wheel_size]')


insertPhrase('calculate', 'Հաշվել', 'Рассчитать', 'Calculate', 'გამოთვალეთ')
insertPhrase('calculate_by_year', '📈 Գների գրաֆիկը ըստ տարիների', '📈 График цен по годам', '📈 Price graph by year', '📈 ფასების გრაფიკი წლის მიხედვით')
insertPhrase('calculate_by_mileage', '📉 Գների գրաֆիկը ըստ վազքի', '📉 График цен по пробегу', '📉 Price graph by mileage', '📉 ფასების გრაფიკი გარბენის მიხედვით')

insertPhrase('label_price','Գինը','Цена','Price','ფასი')
insertPhrase('label_year','Տարի','Год','Year','წელიწადი')
insertPhrase('label_mileage','Վազքը','Пробег','Mileage','გარბენი')


insertPhrase('calculate_result_title', 
'''[url]
💰 ԳՆԵՐԻ ՏԵՂԵԿՈՒԹՅՈՒՆՆԵՐ 💰
''',

'''[url]
💰ИНФОРМАЦИЯ О ЦЕНАХ 💰
''',

'''[url]
💰  PRICE INFO  💰
''',

'''[url]
💰  ფასის ინფორმაცია  💰
''')

insertPhrase('result_arm',
             'Հայկական շուկա : [l_price] $ 💵',
             'Армянский рынок : [l_price] $ 💵',
             'Armenian market : [l_price] $ 💵',
             'სომხური ბაზარი : [l_price] $ 💵')

insertPhrase('result_ge',
             'Վրացական շուկա : [g_price] $ 💵',
             'Грузинский рынок : [g_price] $ 💵',
             'Georgian market : [g_price] $ 💵',
             'ქართული ბაზარი : [g_price] $ 💵')


insertPhrase('income_tax_result_arm',
             'Մաքսային վճար (Հայ.) : [l_price] $ 💵',
             'Таможенный сбор (Арм.) : [l_price] $ 💵',
             'Customs fee (Arm.) : [l_price] $ 💵',
             'საბაჟო მოსაკრებელი (Arm.) : [l_price] $ 💵')

insertPhrase('income_tax_result_ge',
             'Մաքսային վճար (Վրաստան) : [l_price] $ 💵',
             'Таможенный сбор (Грузия) : [l_price] $ 💵',
             'Customs fee (Georgia) : [l_price] $ 💵',
             'საბაჟო მოსაკრებელი (Georgia) : [l_price] $ 💵')


insertPhrase('result_ge_not_available',
'''Վրացական շուկա : ??? $ 💵
⭐️Վրաստանի գները իմանալու համար գրանցվեք Պրեմիում բաժանորդագրության համար''',

'''Грузинский рынок : ??? $ 💵
⭐️Чтобы узнать цены в Грузии, подпишитесь на Премиум подписку''',

'''Georgian market : ??? $ 💵
⭐️To know the prices in Georgia sign up for Premium subscription''',

'''ქართული ბაზარი : ??? $ 💵
⭐️საქართველოში ფასების გასაგებად დარეგისტრირდით Premium-ის გამოწერაზე''')


insertPhrase('result_arm_not_available',
'''Հայկական շուկա : ??? $ 💵
⭐️Հայաստանի գները իմանալու համար գրանցվեք Պրեմիում բաժանորդագրության համար''',

'''Армянский  рынок : ??? $ 💵
⭐️Чтобы узнать цены в Армении, подпишитесь на Премиум подписку''',

'''Armenian market : ??? $ 💵
⭐️To know the prices in Armenia sign up for Premium subscription''',

'''სომხური ბაზარი : ??? $ 💵
⭐️სომხეთში ფასების გასაგებად დარეგისტრირდით Premium-ის გამოწერაზე''')


insertPhrase('price_result_ask_arm',
             'Ի՞նչ եք կարծում, այս մեքենան խելամի՞տ է գնահատված Հայկական շուկայում: Պարտադիր չէ պատասխանեք այս հարցին, բայց դա կօգնի ավելի խելացի արհեստական ինտելեկտ կառուցել:',
             'Считаете ли вы, что этот автомобиль имеет разумную цену на Армянском рынке?? Вам не обязательно отвечать на этот вопрос, но это поможет создать более умный ИИ.',
             'Do you think this car is reasonably priced in Armenian market? You dont have to answer this but it will help build a better AI.',
             'როგორ ფიქრობთ, არის თუ არა ეს მანქანა გონივრული ფასი სომხეთის ბაზარზე? თქვენ არ გჭირდებათ ამაზე პასუხის გაცემა, მაგრამ ეს ხელს შეუწყობს უკეთესი AI-ს შექმნას.')

insertPhrase('price_result_ask_ge',
             'Ի՞նչ եք կարծում, այս մեքենան խելամի՞տ է գնահատված Վրացական շուկայում: Պարտադիր չէ պատասխանեք այս հարցին, բայց դա կօգնի ավելի խելացի արհեստական ինտելեկտ կառուցել:',
             'Считаете ли вы, что этот автомобиль имеет разумную цену на Грузинском рынке? Вам не обязательно отвечать на этот вопрос, но это поможет создать более умный ИИ.',
             'Do you think this car is reasonably priced in Georgian market? You dont have to answer this but it will help build a better AI.',
             'როგორ ფიქრობთ, არის თუ არა ამ მანქანის ფასი ქართულ ბაზარზე? თქვენ არ გჭირდებათ ამაზე პასუხის გაცემა, მაგრამ ეს ხელს შეუწყობს უკეთესი AI-ს შექმნას.')


insertPhrase('calculation_not_possible',
             '❌ Այս մեքենայի համար գնի հաշվարկ հնարավոր չէ։',
             '❌ Расчет цены для данного автомобиля невозможен!',
             '❌ Price calculation is not possible for this car!',
             '❌ ამ ავტომობილზე ფასის დათვლა შეუძლებელია!')



insertPhrase('dont_know','Չգիտեմ','Я не знаю',"I don't know","Მე არ ვიცი")
insertPhrase('my_price','Առաջարկել իմ գինը','Предложить мою цену','Offer my price','შემომთავაზეთ ჩემი ფასი')
insertPhrase('my_price_offer',
             'Ի՞նչ եք կարծում, ինչ արժե այս մեքենան դոլլարով: Գրեք ձեր պատասխանը այսպես «18000»',
             'Как вы думаете, сколько долларов стоит эта машина? Напишите свой ответ так: "18000"',
             'What do you think this car costs in dollars? Write your answer like this "18000" ',
             'როგორ ფიქრობთ, რა ღირს ეს მანქანა დოლარებში? დაწერეთ თქვენი პასუხი ასე "18000"')

insertPhrase('thanks_for_opinion', 'Շնորհակալություն կարծիքի համար 👌', 'Спасибо за ваше мнение 👌', "Thank you for your opinion 👌", "გმადლობთ თქვენი აზრისთვის 👌")


insertPhrase('car_price_info', 
'''Գոհունակություն. [satisfied][notsatisfied] [percent]%
Ընտրեք մեքենայի պարամետրերը և սեղմեք հաշվարկել՝ գինը ստանալու համար:
⚠️Արհեստական ինտելեկտը հաշվարկում է այս կոնկրետ մեքենայի ՄԻՋԻՆ ՇՈՒԿԱՅԱԿԱՆ ԱՐԺԵՔԸ: Գնելիս կամ վաճառելիս մի հիմնեք ձեր որոշումները միայն այս արդյունքների վրա:''',
'''Удовлетворенность: [satisfied][notsatisfied] [percent]%
Выберите параметры автомобиля и нажмите рассчитать, чтобы узнать цену․
⚠️ИИ рассчитывает СРЕДНЮЮ РЫНОЧНУЮ СТОИМОСТЬ для данного конкретного автомобиля․ Не основывайте свои решения только на этих результатах при покупке или продаже.''',
'''Satisfaction: [satisfied][notsatisfied] [percent]%
Choose car parameters and press calculate to get the price.
⚠️The AI calculates the AVERAGE MARKET VALUE for this particular car. Dont base your decisions only on this results when buying or selling.''',
'''კმაყოფილება: [satisfied] [notsatisfied] [percent]%
აირჩიეთ მანქანის პარამეტრები და დააჭირეთ გამოთვლას ფასის მისაღებად.
⚠️AI ითვლის საშუალო საბაზრო ღირებულებას ამ კონკრეტული მანქანისთვის. არ დაეყრდნოთ თქვენს გადაწყვეტილებებს მხოლოდ ამ შედეგებზე ყიდვის ან გაყიდვისას.''')



insertPhrase('choose_car_brand',             
    'Խնդրում եմ ընտրեք ձեր մեքենայի մակնիշը։ Եթե ստորև ներկայացված չէ ձեր մեքենայի մակնիշը, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:',
    'Пожалуйста, выберите марку вашего автомобиля. Если марка вашего автомобиля не указана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.',
    'Please choose the brand of your car. If the brand of your car is not shown below it means there is not enough data and the AI cant make a good prediction.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ბრენდი. თუ თქვენი მანქანის ბრენდი არ არის ნაჩვენები ქვემოთ, ეს ნიშნავს, რომ არ არის საკმარისი მონაცემები და AI ვერ გააკეთებს კარგ პროგნოზს.')

insertPhrase('choose_car_model',             
    'Խնդրում եմ ընտրել ձեր մեքենայի մոդելը։ Եթե ձեր մեքենայի մոդելը ներկայացված չէ ստորև, դա նշանակում է, որ բավարար տվյալներ չկան, և AI-ն չի կարող լավ կանխատեսումներ անել:',  
    'Пожалуйста, выберите модель вашего автомобиля. Если модель вашего автомобиля не показана ниже, это означает, что данных недостаточно, и ИИ не может сделать хороший прогноз.',
    'Please choose the model of your car. If the model of your car is not shown below it means there is not enough data and the AI cant make a good prediction.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის მოდელი. თუ თქვენი მანქანის მოდელი არ არის ნაჩვენები ქვემოთ, ეს ნიშნავს, რომ არ არის საკმარისი მონაცემები და AI ვერ გააკეთებს კარგ პროგნოზს.')

insertPhrase('choose_car_year',
    'Խնդրում ենք ընտրել ձեր մեքենայի արտադրության տարեթիվը:',
    'Пожалуйста, выберите год выпуска вашего автомобиля.',
    'Please choose the manufacturing year of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის წარმოების წელი.')
insertPhrase('choose_car_mileage',
    'Խնդրում ենք ընտրել ձեր մեքենայի վազքը:',
    'Пожалуйста, выберите пробег вашего автомобиля.',
    'Please choose the mileage of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის გარბენი.')
insertPhrase('choose_car_engine_size',       
    'Խնդրում ենք ընտրել ձեր մեքենայի շարժիչի չափը:',
    'Пожалуйста, выберите объем двигателя вашего автомобиля.',
    'Please choose the engine size of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ძრავის ზომა.')
insertPhrase('choose_car_exterior_color',
    'Խնդրում ենք ընտրել ձեր մեքենայի արտաքին գույնը:',
    'Пожалуйста, выберите цвет кузова вашего автомобиля.',
    'Please choose the exterior color of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ექსტერიერის ფერი.')
insertPhrase('choose_car_body_type',
    'Խնդրում ենք ընտրել ձեր մեքենայի թափքի տեսակը:',
    'Пожалуйста, выберите тип кузова вашего автомобиля.',
    'Please choose the body type of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ძარის ტიპი.')
insertPhrase('choose_car_engine_type',
    'Խնդրում ենք ընտրել ձեր մեքենայի շարժիչի տեսակը:',
    'Пожалуйста, выберите тип двигателя вашего автомобиля.',
    'Please choose the engine type of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ძრავის ტიპი.')
insertPhrase('choose_car_transmission',
    'Խնդրում ենք ընտրել ձեր մեքենայի փոխանցման տուփի տեսակը:',
    'Пожалуйста, выберите тип трансмиссии вашего автомобиля.',
    'Please choose the transmission type of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის გადაცემის ტიპი.')
insertPhrase('choose_car_drive_type',
    'Խնդրում ենք ընտրել ձեր մեքենայի վարման տեսակը:',
    'Пожалуйста, выберите тип привода вашего автомобиля.',
    'Please choose the drive type of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის დისკის ტიპი.')
insertPhrase('choose_car_condition',
    'Խնդրում ենք ընտրել ձեր մեքենայի վիճակը։',
    'Пожалуйста, выберите состояние вашего автомобиля.',
    'Please choose the condition of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის მდგომარეობა.')
insertPhrase('choose_car_gas_equipment',
    'Խնդրում ենք նշել, թե արդյոք ձեր մեքենան ունի գազի սարքավորումներ:',
    'Пожалуйста, уточните, есть ли в вашем автомобиле газовое оборудование.',
    'Please specify if your car has gas equipment.',
    'გთხოვთ მიუთითოთ აქვს თუ არა თქვენს მანქანას გაზის აღჭურვილობა.')
insertPhrase('choose_car_steering_wheel', 
    'Խնդրում ենք ընտրել ձեր մեքենայի ղեկի դիրքը:',
    'Пожалуйста, выберите положение рулевого колеса вашего автомобиля.',
    'Please choose the steering wheel position of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის საჭის პოზიცია.')
insertPhrase('choose_car_headlights',
    'Խնդրում եմ նշեք ձեր մեքենայի լուսարձակների տեսակը:',
    'Пожалуйста, укажите тип фар в вашем автомобиле.',
    'Please specify the type of headlights in your car.',
    'გთხოვთ, მიუთითოთ თქვენი მანქანის ფარების ტიპი.')
insertPhrase('choose_car_interior_color',
    'Խնդրում ենք ընտրել ձեր մեքենայի սրահի գույնը:',
    'Пожалуйста, выберите цвет салона вашего автомобиля.',
    'Please choose the interior color of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ინტერიერის ფერი.')
insertPhrase('choose_car_interior_material',
    'Խնդրում ենք ընտրել ձեր մեքենայի սրահի նյութը:',
    'Пожалуйста, выберите материал салона вашего автомобиля.',
    'Please choose the interior material of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ინტერიერის მასალა.')
insertPhrase('choose_car_sunroof',
    'Խնդրում ենք նշել, թե արդյոք ձեր մեքենան ունի լուսային տանիք:',
    'Пожалуйста, укажите, есть ли в вашем автомобиле люк на крыше.',
    'Please specify if your car has a sunroof.',
    'გთხოვთ მიუთითოთ აქვს თუ არა თქვენს მანქანას ლუქი.')
insertPhrase('choose_car_wheel_size',
    'Խնդրում ենք ընտրել ձեր մեքենայի անիվի չափը:',
    'Пожалуйста, выберите размер колес вашего автомобиля.',
    'Please choose the wheel size of your car.',
    'გთხოვთ, აირჩიოთ თქვენი მანქანის ბორბლის ზომა.')


insertPhrase('best_offers', 'Լավագույն առաջարկներ', 'Лучшие предложения', 'Best offers', 'საუკეთესო შეთავაზებები')


# insertPhrase('choose_marz',       'Ընտրեք տարածաշրջան', 'Выберите регион', 'Choose region', 'აირჩიეთ რეგიონი')

# insertPhrase('marz_YEREVAN',      'Երևան',          'Ереван',        'Yerevan')
# insertPhrase('marz_ARMAVIR',      'Արմավիր',        'Армавир',       'Armavir')
# insertPhrase('marz_ARARAT',       'Արարատ',         'Арарат',        'Ararat')
# insertPhrase('marz_KOTAYK',       'Կոտայք',         'Котайк',        'Kotayk')
# insertPhrase('marz_SHIRAK',       'Շիրակ',          'Ширак',         'Shirak')
# insertPhrase('marz_LORRI',        'Լոռի',           'Лори',          'Lorri')
# insertPhrase('marz_GEGHARKUNIK',  'Գեղարքունիք',    'Гегаркуник',    'Gegharkunik')
# insertPhrase('marz_SYUNIK',       'Սյունիք',        'Сюник',         'Syunik')
# insertPhrase('marz_ARAGATSOTN',   'Արագածոտն',      'Арагацотн',     'Aragatsotn')
# insertPhrase('marz_TAVUSH',       'Տավուշ',         'Тавуш',         'Tavush')
# insertPhrase('marz_VAYOTS_DZOR',  'Վայոց ձոր',      'Вайоц Дзор',    'Vayots Dzor')
# insertPhrase('marz_ARTSAKH',      'Արցախ',          'Арцах',         'Artsakh')



#Car properties
insertPhrase("sedan",               "Սեդան"                     ,"Седан"                       ,"Sedan",                'სედანი')
insertPhrase("hatchback",           "Հետչբեք"                   ,"Хэтчбек"                     ,"Hatchback",            'ჰეჩბეკი')
insertPhrase("wagon",               "Ունիվերսալ"                ,"Универсал"                   ,"Wagon",                'ვაგონი')
insertPhrase("coupe",               "Կուպե"                     ,"Купе"                        ,"Coupe",                'კუპე')
insertPhrase("crossover",           "Ամենագնաց / Քրոսսովեր"     ,"Внедорожник / Кроссовер"     ,"SUV / Crossover",      'ჯიპი / კროსოვერი')
insertPhrase("minivan",             "Մինիվեն"                   ,"Минивэн"                     ,"Minivan",              'მინივენი')
insertPhrase("pickup",              "Փիքափ"                     ,"Пикап"                       ,"Pickup",               'Აღება')
insertPhrase("minibus",             "Միկրոավտոբուս"             ,"Микроавтобус"                ,"Minibus",              'მიკროავტობუსი')
insertPhrase("van",                 "Ֆուրգոն"                   ,"Фургон"                      ,"Van",                  'ვან')
insertPhrase("convertible",         "Կաբրիոլետ"                 ,"Кабриолет"                   ,"Convertible",          'კონვერტირებადი')
insertPhrase("limo",                "Լիմուզին"                  ,"Лимузин"                     ,"Limo",                 'ლიმუზინი')
insertPhrase("roadster",            "Ռոդսթեր"                   ,"Родстер"                     ,"Roadster",             'როდსტერი')
insertPhrase("liftback",            "Լիֆտբեկ"                   ,"Лифтбек"                     ,"Liftback",             'ლიფტბეკი')
insertPhrase("fastback",            "Ֆաստբեկ"                   ,"Фастбек"                     ,"Fastback",             'ფასტბეკი')
insertPhrase("compact_mpv",         "Կոմպակտվեն"                ,"Компактвэн"                  ,"Compact MPV",          'კომპაქტური MPV')

insertPhrase('gasoline',            "Բենզին",                   "Бензин",                       "Gasoline",     'Ბენზინი')
insertPhrase('diesel',              "Դիզել",                    "Дизель",                       "Diesel",       'დიზელი')
insertPhrase('hybrid',              "Հիբրիդ",                   "Гибрид",                       "Hybrid",       'ჰიბრიდული')
insertPhrase('electric',            "էլեկտրական",               "Электро",                      "Electric",     'ელექტრო')
insertPhrase('hydrogen',            "Ջրածնային",                "Водородный",                   "Hydrogen",     'წყალბადი')


insertPhrase("manual",              "Մեխանիկական",              "Механическая",                 "Manual",       'სახელმძღვანელო')
insertPhrase("automatic",           "Ավտոմատ",                  "Автоматическая",               "Automatic",    'Ავტომატური')

insertPhrase("front_wheel_drive",   "Առջևի քարշակ",            "Передний привод",               "Front Wheel Drive", 'Წინა წამყვანი თვლები')
insertPhrase("rear_wheel_drive",    "Ետևի քարշակ",             "Задний привод",                 "Rear Wheel Drive", 'უკანა წამყვანი')
insertPhrase("all_wheel_drive",     "Լիաքարշակ",               "Полный привод",                 "All Wheel Drive", 'ყველა წამყვანი')

insertPhrase("car_is_not_damaged",  "Չվթարված",                "Не битое",                      "Car is not damaged", 'მანქანა არ არის დაზიანებული')
insertPhrase("car_is_damaged" ,     "Վթարված",                 "Битое",                         "Car is damaged", 'მანქანა დაზიანებულია')

insertPhrase("gas_no",              "Գազ չտեղադրված",          "Газ не установлен",             "Gas not Installed", 'გაზი არ არის დამონტაჟებული')          
insertPhrase("gas_installed",       "Գազ տեղադրված",           "Газ установлен",                "Gas installed", 'გაზი დამონტაჟებულია') 

insertPhrase('left_steering',       "Ղեկը ձախ",                "Левый руль",                    "Left hand drive", 'მარცხენა საჭე')
insertPhrase('right_steering',      "Ղեկը աջ",                 "Правый руль",                   "Right hand drive", 'მარჯვენასაჭიანი')

insertPhrase("exterior_white",               "Սպիտակ",                  "Белый",                         "White", 'თეთრი')
insertPhrase("exterior_silver",              "Արծաթագույն",             "Серебряный",                    "Silver", 'ვერცხლი')
insertPhrase("exterior_gray",                "Մոխրագույն",              "Серый",                         "Gray", 'რუხი')
insertPhrase("exterior_black",               "Սև",                      "Чёрный",                        "Black", 'შავი')
insertPhrase("exterior_brown",               "Շագանակագույն",           "Коричневый",                    "Brown", 'ყავისფერი')
insertPhrase("exterior_gold",                "Ոսկեգույն",               "Золотой",                       "Gold", 'ოქრო')
insertPhrase("exterior_beige",               "Բեժ",                     "Бежевый",                       "Beige", 'კრემისფერი')
insertPhrase("exterior_red",                 "Կարմիր",                  "Красный",                       "Red", 'წითელი')
insertPhrase("exterior_blue",                "Կապույտ",                 "Синий",                         "Blue", 'ლურჯი')
insertPhrase("exterior_orange",              "Նարնջագույն",             "Оранжевый",                     "Orange", 'ნარინჯისფერი')
insertPhrase("exterior_yellow",              "Դեղին",                   "Жёлтый",                        "Yellow", 'ყვითელი')
insertPhrase("exterior_green",               "Կանաչ",                   "Зелёный",                       "Green", 'მწვანე')
insertPhrase("exterior_cyan",                "Երկնագույն",              "Голубой",                       "Cyan", 'ციანი')
insertPhrase("exterior_maroon",              "Բորդո",                   "Бордовый",                      "Maroon", 'მარუნი')
insertPhrase("exterior_pink",                "Վարդագույն",              "Розовый",                       "Pink", 'ვარდისფერი')
insertPhrase("exterior_purple",              "Մանուշակագույն",          "Фиолетовый",                    "Purple", 'მეწამული')

insertPhrase("interior_white",               "Սպիտակ",                  "Белый",                         "White", 'თეთრი')
insertPhrase("interior_gray",                "Մոխրագույն",              "Серый",                         "Gray", 'რუხი')
insertPhrase("interior_black",               "Սև",                      "Чёрный",                        "Black", 'შავი')
insertPhrase("interior_brown",               "Շագանակագույն",           "Коричневый",                    "Brown", 'ყავისფერი')
insertPhrase("interior_beige",               "Բեժ",                     "Бежевый",                       "Beige", 'კრემისფერი')
insertPhrase("interior_red",                 "Կարմիր",                  "Красный",                       "Red", 'წითელი')
insertPhrase("interior_blue",                "Կապույտ",                 "Синий",                         "Blue", 'ლურჯი')
insertPhrase("interior_other",               "Այլ",                     "Другой",                        "Other", 'სხვა')
insertPhrase("interior_gold",                "Ոսկեգույն",               "Золотой",                       "Gold", 'ოქრო')
insertPhrase("interior_maroon",              "Բորդո",                   "Бордовый",                      "Maroon", 'მარუნი')
insertPhrase("interior_orange",              "Նարնջագույն",             "Оранжевый",                     "Orange", 'ნარინჯისფერი')
insertPhrase("interior_yellow",              "Դեղին",                   "Жёлтый",                        "Yellow", 'ყვითელი')

insertPhrase("no_sunroof"       ,           "Լյուկ չկա",               "Люка нет",                      "No sunroof", 'არ არის ლუქი')
insertPhrase("regular_sunroof_sunroof"  ,   "Սովորական լյուկ",         "Обычный люк",                   "Regular sunroof", 'რეგულარული ლუქი')
insertPhrase("panoramic_sunroof_sunroof",   "Պանորամային լյուկ",       "Панорамный люк",                "Panoramic sunroof", 'პანორამული ლუქი')

insertPhrase("led_headlights"       ,       "Լեդ լուսարձակներ",        "Светодиодные фары",       "Led headlights", 'LED ფარები')
insertPhrase("halogen_headlights"   ,       "Հալոգեն լուսարձակներկ",   "Галогенные фары",         "Halogen headlights", 'ჰალოგენური ფარები')          
insertPhrase("\u0445enon_headlights",       "Քսենոնային լուսարձակներ", "Ксеноновые фары",         "Xenon headlights", 'ქსენონის ფარები')                     

insertPhrase("leather",                     'Մատերիալ կաշի',         'Материал кожа',                 'Material leather', 'მასალა ტყავი')
insertPhrase("textile",                     'Մատերիալ կտոր',         'Материал текстиль',             'Material textile', 'მასალა ტექსტილი')
insertPhrase("other",                       'Մատերիալ այլ',          'Материал другой',               'Material other', 'მასალა სხვა')
insertPhrase("alcantara",                   'Մատերիալ ալկանտարա',    'Материал алькантара',           'Material alcantara', 'მასალა ალკანტარა')
insertPhrase("velour",                      'Մատերիալ թավիշ',        'Материал велюр',                'Material velour', 'მატერიალური ხავერდი')
insertPhrase("leatherette",                 'Մատերիալ դերմանտին',    'Материал искусственная кожа',   'Material leatherette', 'მასალა ტყავისფერი')

phrasespy.close()