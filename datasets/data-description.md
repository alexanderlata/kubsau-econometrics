# Описание наборов данных

Файлы в формате CSV: разделитель ячеек — запятая, десятичный разделитель — точка. Переменные вида «=1, если …» — бинарные: 1, если условие выполнено, и 0 в остальных случаях.

## sleep75

Число наблюдений: 706

- age: возраст, лет
- black: =1, если чернокожий
- case: номер наблюдения
- clerical: =1, если офисный служащий
- construc: =1, если работает в строительстве
- educ: число лет образования
- earns74: общий заработок за 1974 год
- gdhlth: =1, если здоровье хорошее или отличное
- inlf: =1, если входит в состав рабочей силы
- leis1: sleep − totwrk
- leis2: slpnaps − totwrk
- leis3: rlxall − totwrk
- smsa: =1, если живёт в крупной городской агломерации (SMSA)
- lhrwage: логарифм почасовой зарплаты
- lothinc: логарифм othinc (прочего дохода), кроме случаев othinc < 0
- male: =1, если мужчина
- marr: =1, если состоит в браке
- prot: =1, если протестант
- rlxall: slpnaps + время на личные занятия
- selfe: =1, если самозанятый
- sleep: ночной сон, минут в неделю
- slpnaps: сон с учётом дневного, минут в неделю
- south: =1, если живёт на Юге
- spsepay: заработок супруга (супруги)
- spwrk75: =1, если супруг (супруга) работает
- totwrk: рабочее время, минут в неделю
- union: =1, если член профсоюза
- worknrm: время на основной работе, минут
- workscnd: время на второй работе, минут
- exper: age − educ − 6
- yngkid: =1, если есть дети младше 3 лет
- yrsmarr: число лет в браке
- hrwage: почасовая зарплата
- agesq: age²

*Источник*: Wooldridge; J. E. Biddle and D. S. Hamermesh (1990), “Sleep and the Allocation of Time,” Journal of Political Economy 98, 922–943.

## Electricity

Число наблюдений: 158

- cost: общие издержки
- q: общий выпуск
- pl: ставка заработной платы
- sl: доля труда в издержках
- pk: индекс цены капитала
- sk: доля капитала в издержках
- pf: цена топлива
- sf: доля топлива в издержках

*Источник*: Christensen, L. and W. H. Greene (1976) “Economies of scale in U.S. electric power generation”, Journal of Political Economy, 84, 655–676.

## Diamond

Число наблюдений: 308

- carat: вес бриллианта, карат
- colour: цвет, категориальная переменная с уровнями D, E, F, G, H, I
- clarity: чистота, категориальная переменная с уровнями IF, VVS1, VVS2, VS1, VS2
- certification: сертифицирующая организация, категориальная переменная с уровнями GIA, IGI, HRD
- price: цена, сингапурских долларов

*Источник*: Chu, Singfat (2001) “Pricing the C’s of Diamond Stones”, Journal of Statistics Education, 9(2).

## Labour (бельгийские фирмы)

Число наблюдений: 569

- capital: основные средства на конец 1995 года, млн евро
- labour: число работников (занятость)
- output: добавленная стоимость, млн евро
- wage: расходы на оплату труда на одного работника, тыс. евро

*Источник*: Verbeek, Marno (2004) A Guide to Modern Econometrics, John Wiley and Sons, chapter 4.

## diamonds (цены более 50 000 бриллиантов круглой огранки)

Число наблюдений: 53940

- price: цена, долларов США (326–18 823)
- carat: вес бриллианта, карат (0.2–5.01)
- cut: качество огранки (Fair, Good, Very Good, Premium, Ideal)
- color: цвет, от D (лучший) до J (худший)
- clarity: чистота бриллианта (I1 (худшая), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (лучшая))
- x: длина, мм (0–10.74)
- y: ширина, мм (0–58.9)
- z: глубина, мм (0–31.8)
- depth: общая глубина в процентах = z / mean(x, y) = 2 · z / (x + y) (43–79)
- table: ширина верхней площадки относительно самого широкого места (43–95)

*Источник*: пакет ggplot2 для R.

## wage1

Число наблюдений: 526, переменных: 24

- wage: средний почасовой заработок
- educ: число лет образования
- exper: потенциальный опыт работы, лет
- tenure: стаж у нынешнего работодателя, лет
- nonwhite: =1, если не белый
- female: =1, если женщина
- married: =1, если состоит в браке
- numdep: число иждивенцев
- smsa: =1, если живёт в крупной городской агломерации (SMSA)
- northcen: =1, если живёт в северо-центральном регионе США
- south: =1, если живёт в южном регионе
- west: =1, если живёт в западном регионе
- construc: =1, если работает в строительстве
- ndurman: =1, если работает в производстве товаров кратковременного пользования
- trcommpu: =1, если работает в транспорте, связи, коммунальных услугах
- trade: =1, если работает в оптовой или розничной торговле
- services: =1, если работает в сфере услуг
- profserv: =1, если работает в сфере профессиональных услуг
- profocc: =1, если занят профессиональной (квалифицированной) деятельностью
- clerocc: =1, если офисный служащий
- servocc: =1, если работник сферы обслуживания
- lwage: log(wage)
- expersq: exper²
- tenursq: tenure²

## wage2

Число наблюдений: 935, переменных: 17

- wage: месячный заработок
- hours: средняя продолжительность рабочей недели, часов
- IQ: показатель IQ, баллов
- KWW: показатель теста на знание мира труда (knowledge of world work), баллов
- educ: число лет образования
- exper: опыт работы, лет
- tenure: стаж у нынешнего работодателя, лет
- age: возраст, лет
- married: =1, если состоит в браке
- black: =1, если чернокожий
- south: =1, если живёт на Юге
- urban: =1, если живёт в крупной городской агломерации (SMSA)
- sibs: число братьев и сестёр
- brthord: порядок рождения
- meduc: образование матери
- feduc: образование отца
- lwage: натуральный логарифм wage

*Источник*: M. Blackburn and D. Neumark (1992), “Unobserved Ability, Efficiency Wages, and Interindustry Wage Differentials,” Quarterly Journal of Economics 107, 1421–1436.

## Student Performance

Файл `Student_Performance.csv`. Набор данных для изучения факторов, влияющих на успеваемость студентов: 10 000 записей о студентах, в каждой — значения объясняющих переменных и индекс успеваемости.

Объясняющие переменные:

- Hours Studied: общее число часов, потраченных студентом на учёбу
- Previous Scores: баллы, полученные студентом на предыдущих тестах
- Extracurricular Activities: участвует ли студент во внеучебной деятельности (Yes или No)
- Sleep Hours: среднее число часов сна в сутки
- Sample Question Papers Practiced: число решённых студентом вариантов пробных заданий

Целевая переменная:

- Performance Index: показатель общей успеваемости студента, округлён до целого. Принимает значения от 10 до 100; чем больше, тем выше успеваемость

*Источник*: [Kaggle](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression).

Замечание: набор данных синтетический и создан для иллюстрации. Связи между переменными и индексом успеваемости могут не отражать реальные закономерности.

## Mishkin

Месячные наблюдения с февраля 1950 года по декабрь 1990 года

Число наблюдений: 491

Страна: США

- pai1: месячная инфляция (в процентах, в годовом выражении)
- pai3: трёхмесячная инфляция (в процентах, в годовом выражении)
- tb1: ставка по одномесячным казначейским векселям (в процентах, в годовом выражении)
- tb3: ставка по трёхмесячным казначейским векселям (в процентах, в годовом выражении)
- cpi: индекс потребительских цен для городских потребителей, все товары (среднее за 1982–1984 годы принято за 100)

Первый столбец файла (`rownames`) — номер наблюдения.

*Источник*: Mishkin, F. (1992) “Is the Fisher effect for real?”, Journal of Monetary Economics, 30, 195–215.

## Tbrate

Квартальные наблюдения с I квартала 1950 года по IV квартал 1996 года

Число наблюдений: 188

Страна: Канада

- r: ставка по 91-дневным казначейским векселям
- y: логарифм реального ВВП
- pi: инфляция

Первый столбец файла (`rownames`) — номер наблюдения.

## Icecream

Наблюдения за четырёхнедельные периоды с 18 марта 1951 года по 11 июля 1953 года

Число наблюдений: 30

Страна: США

- cons: потребление мороженого на душу населения, пинт
- income: средний доход семьи в неделю, долларов США
- price: цена мороженого за пинту
- temp: средняя температура, градусов Фаренгейта

Первый столбец файла (`rownames`) — номер наблюдения.

*Источник*: Hildreth, C. and J. Lu (1960) Demand relations with autocorrelated disturbances, Technical Bulletin No 2765, Michigan State University.

## Consumption

Квартальные наблюдения с I квартала 1947 года по IV квартал 1996 года

Число наблюдений: 200

Страна: Канада

- yd: располагаемый личный доход, в долларах 1986 года
- ce: личные потребительские расходы, в долларах 1986 года

Первый столбец файла (`rownames`) — номер наблюдения.

*Источник*: Davidson, R. and James G. MacKinnon (2004) Econometric Theory and Methods, New York, Oxford University Press, chapter 1, 3, 4, 6, 9, 10, 14 and 15.

## MoneyUS

Квартальные наблюдения с I квартала 1954 года по IV квартал 1994 года

Число наблюдений: 164

Страна: США

- m: логарифм реальной денежной массы M1
- infl: квартальная инфляция (изменение логарифма цен), % в год
- cpr: ставка по коммерческим бумагам, % в год
- y: логарифм реального ВВП (в млрд долларов 1987 года)
- tbr: ставка по казначейским векселям

Первый столбец файла (`rownames`) — номер наблюдения.

*Источник*: Hoffman, D. L. and R. H. Rasche (1996) “Assessing forecast performance in a cointegrated system”, Journal of Applied Econometrics, 11, 495–517.

## Macrodat

Квартальные наблюдения с I квартала 1959 года по IV квартал 2000 года

Число наблюдений: 168

Страна: США

- lhur: уровень безработицы (среднее за месяцы квартала)
- punew: индекс потребительских цен (среднее за месяцы квартала)
- fyff: ставка по федеральным фондам (последний месяц квартала)
- fygm3: ставка по трёхмесячным казначейским векселям (последний месяц квартала)
- fygt1: ставка по одногодичным казначейским облигациям (последний месяц квартала)
- exruk: курс доллара к фунту стерлингов (последний месяц квартала)
- gdpjp: реальный ВВП Японии

Первый столбец файла (без имени) — номер наблюдения.

*Источник*: Bureau of Labor Statistics, OECD, Federal Reserve.


---

# Dataset descriptions

## sleep75

*number of observations* : 706

- age: in years
- black: =1 if black
- case: identifier
- clerical: =1 if clerical worker
- construc: =1 if construction worker
- educ: years of schooling
- earns74: total earnings, 1974
- gdhlth: =1 if in good or excel. health - inlf: =1 if in labor force
- leis1: sleep - totwrk
- leis2: slpnaps - totwrk
- leis3: rlxall - totwrk
- smsa: =1 if live in smsa
- lhrwage: log hourly wage
- lothinc: log othinc, unless othinc < 0
- male: =1 if male
- marr: =1 if married
- prot: =1 if Protestant
- rlxall: slpnaps + personal activs
- selfe: =1 if self employed
- sleep: mins sleep at night, per wk
- slpnaps: minutes sleep, inc. naps
- south: =1 if live in south
- spsepay: spousal wage income
- spwrk75: =1 if spouse works
- totwrk: mins worked per week
- union: =1 if belong to union
- worknrm: mins work main job
- workscnd: mins work second job
- exper: age - educ - 6
- yngkid: =1 if children < 3 present
- yrsmarr: years married
- hrwage: hourly wage
- agesq: age^2

*Source*: Wooldridge Source: J.E. Biddle and D.S. Hamermesh (1990), “Sleep and the Allocation of Time,” Journal of Political Economy 98, 922-943

## Electricity

*number of observations* : 158

- cost total cost
- q total output
- pl wage rate
- sl cost share for labor
- pk capital price index
- sk cost share for capital
- pf fuel price
- sf cost share for fuel

*Source*: Christensen, L. and W. H. Greene (1976) “Economies of scale in U.S. electric power generation”, Journal of Political Economy, 84, 655-676.

## Diamond

*number of observations* : 308

- carat weight of diamond stones in carat unit
- colour a factor with levels (D,E,F,G,H,I)
- clarity a factor with levels (IF,VVS1,VVS2,VS1,VS2)
- certification certification body, a factor with levels ( GIA, IGI, HRD)
- price price in Singapore $

*Source*: Chu, Singfat (2001) “Pricing the C’s of Diamond Stones”, Journal of Statistics Education, 9(2).

## Labour (Belgian firms)

*number of observations* : 569

- capital total fixed assets, end of 1995 (in 1000000 euro)
- labour number of workers (employment)
- output value added (in 1000000 euro)
- wage wage costs per worker (in 1000 euro)

*Source*: Verbeek, Marno (2004) A Guide to Modern Econometrics, John Wiley and Sons, chapter 4.

## diamonds (Prices of over 50,000 round cut diamonds)

*number of observations* : 53940

- price price in US dollars ($326–$18,823)
- carat weight of the diamond (0.2–5.01)
- cut quality of the cut (Fair, Good, Very Good, Premium, Ideal) 
- color diamond colour, from D (best) to J (worst)
- clarity a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
- x length in mm (0–10.74)
- y width in mm (0–58.9)
- z depth in mm (0–31.8)
- depth total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43–79)
- table width of top of diamond relative to widest point (43–95)

*Source*: пакет ggplot2 для R

## wage1

A dataset with 526 observations on 24 variables

* wage: average hourly earnings
* educ: years of education
* exper: years potential experience
* tenure: years with current employer
* nonwhite: =1 if nonwhite
* female: =1 if female
* married: =1 if married
* numdep: number of dependents
* smsa: =1 if live in SMSA
* northcen: =1 if live in north central U.S
* south: =1 if live in southern region
* west: =1 if live in western region
* construc: =1 if work in construc. indus.
* ndurman: =1 if in nondur. manuf. indus. * trcommpu: =1 if in trans, commun, pub ut * trade: =1 if in wholesale or retail
* services: =1 if in services indus.
* profserv: =1 if in prof. serv. indus.
* profocc: =1 if in profess. occupation
* clerocc: =1 if in clerical occupation
* servocc: =1 if in service occupation
* lwage: log(wage)
* expersq: exper^2
* tenursq: tenure^2

## wage2

A dataset with 935 observations on 17 variables:

* wage: monthly earnings
* hours: average weekly hours
* IQ: IQ score
* KWW: knowledge of world work score * educ: years of education
* exper: years of work experience
* tenure: years with current employer
* age: age in years
* married: =1 if married
* black: =1 if black
* south: =1 if live in south
* urban: =1 if live in SMSA
* sibs: number of siblings
* brthord: birth order
* meduc: mother’s education
* feduc: father’s education
* lwage: natural log of wage

*Source*: M. Blackburn and D. Neumark (1992), “Unobserved Ability, Efficiency Wages, and Interindustry Wage Differentials,” Quarterly Journal of Economics 107, 1421-1436.

## Student Performance

The Student Performance Dataset is a dataset designed to examine the factors influencing academic student performance. The dataset consists of 10,000 student records, with each record containing information about various predictors and a performance index.

__Variables:__
* __Hours Studied:__ The total number of hours spent studying by each student.
* __Previous Scores:__ The scores obtained by students in previous tests.
* __Extracurricular Activities:__ Whether the student participates in extracurricular activities (Yes or No).
* __Sleep Hours:__ The average number of hours of sleep the student had per day.
* __Sample Question Papers Practiced:__ The number of sample question papers the student practiced.

__Target Variable:__
* __Performance Index:__ A measure of the overall performance of each student. The performance index represents the student's academic performance and has been rounded to the nearest integer. The index ranges from 10 to 100, with higher values indicating better performance.

*Source*: [Kaggle](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression)

__P.S:__ Please note that this dataset is synthetic and created for illustrative purposes. The relationships between the variables and the performance index may not reflect real-world scenarios

## Mishkin

monthly observations from 1950-2 to 1990-12

*number of observations* : 491

*country* : United States

- pai1: one-month inflation rate (in percent, annual rate)
- pai3: three-month inflation rate (in percent, annual rate)
- tb1: one-month T-bill rate (in percent, annual rate)
- tb3: three-month T-bill rate (in percent, annual rate)
- cpi: CPI for urban consumers, all items (the 1982-1984 average is set to 100)

*Source*: Mishkin, F. (1992) “Is the Fisher effect for real ?”, Journal of Monetary Economics, 30, 195-215.

## Tbrate

*quarterly observations* from 1950-1 to 1996-4

*number of observations* : 188

*country* : Canada

- r: the 91-day treasury bill rate
- y: the log of real GDP
- pi: the inflation rate

## Icecream

*four–weekly observations* from 1951–03–18 to 1953–07–11

*number of observations* : 30

*country* : United States

- cons: consumption of ice cream per head (in pints);
- income: average family income per week (in US Dollars);
- price: price of ice cream (per pint);
- temp: average temperature (in Fahrenheit);

*Source*: Hildreth, C. and J. Lu (1960) Demand relations with autocorrelated disturbances, Technical Bulletin No 2765, Michigan State University.

## Consumption

*quarterly observations8 from 1947-1 to 1996-4

*number of observations* : 200

*country* : Canada

- yd: personal disposable income, 1986 dollars
- ce: personal consumption expenditure, 1986 dollars

*Source*: Davidson, R. and James G. MacKinnon (2004) Econometric Theory and Methods, New York, Ox-
ford University Press, chapter 1, 3, 4, 6, 9, 10, 14 and 15.

## MoneyUS

*quarterly observations* from 1954–01 to 1994–12

*number of observations* : 164

*country* : United States

- m: log of real M1 money stock
- infl: quarterly inflation rate (change in log prices), % per year
- cpr: commercial paper rate, % per year
- y: log real GDP (in billions of 1987 dollars)
- tbr: treasury bill rate

*Source*: Hoffman, D.L. and R.H. Rasche (1996) “Assessing forecast performance in a cointegrated system”,
Journal of Applied Econometrics, 11, 495–517.

## Macrodat

*quarterly observations* from 1959-1 to 2000-4

*number of observations* : 168

*country* : United States

- lhur: unemployment rate (average of months in quarter)
- punew: CPI (Average of Months in Quarter)
- fyff: federal funds interest rate (last month in quarter)
- fygm3: 3 month treasury bill interest rate (last month in quarter)
- fygt1: 1 year treasury bond interest rate (last month in quarter)
- exruk: dollar / Pound exchange rate (last month in quarter)
- gdpjp: real GDP for Japan

*Source*: Bureau of Labor Statistics, OECD, Federal Reserve.