from flask import Flask
from flask import render_template
app = Flask(__name__)

experimentsInfo = {
    "pharaoh":{
        "title":"Фараоновы змеи",
        "text":"<h3>Фараоновыми змеями называют целый ряд реакций, которые сопровождаются образованием пористого продукта из небольшого объема реагирующих веществ. Эти реакции сопровождаются бурным выделением газа. В итоге выглядит реакция так, будто из смесиреагентов выползает большая змея и ползет по столу, как настоящая.</h3><h5>Термическое разложение роданида ртути идёт по уравнению: 2 Hg(SCN)2 = 2 HgS + CS2 + C3N4 CS2 + 3O2 = CO2 + 2SO2 При нагревании роданида ртути образуются черная соль - сульфид ртути, нитрид углерода желтого цвета и дисульфид углерода CS2.Последний на воздухе воспламеняется и сгорает, образуя диоксид углерода CO2 и диоксид серы SO2.</h5>",
    },
    "hydrolysis":{
        "title": "Обратимый гидролиз солей",
        "text": "<h3>Гидролиз – взаимодействие веществ с водой. Гидролизу подвергаются разные классы неорганических и органических веществ:соли, бинарные соединения, углеводы, жиры, белки, эфиры и другие вещества.Гидролиз солей происходит, когда ионы соли способны образовывать с Н+ и ОН— ионами воды малодиссоциированные электролиты. <h3><h5>1.Гидролиз по Аниону.<h5><p>Соли, образованные слабым основанием и сильной кислотой, гидролизуются по аниону. Примеры таких солей: CH3COONa, Na2CO3, Na2S, KCN.Реакция гидролиза: CH3COONa + HOH ↔ CH3COOH + NaOHТаким образом, при гидролизе таких солей в растворе образуется небольшой избыток гидроксид-ионов OH—. Водородный показатель такого раствора рН>7.Гидролиз солей многоосновных кислот (H2CO3, H3PO4 и т.п.) протекает ступенчато, с образованием кислых солей.<p><h5>2.Гидролиз по Катиону<h5><p>Соли, образованные слабым основанием и сильной кислотой, гидролизуются по катиону.Пример такой соли: NH4Cl, FeCl3, Al2(SO4)3 Уравнение гидролиза: NH4+ + HOH ↔ NH3·H2O + H+ При этом катион слабого основания притягивает гидроксид-ионы из воды, а  в растворе возникает избыток ионов Н+. Водородный показатель такого раствора рН<7.Соли, образованные многокислотными основаниями, гидролизуются ступенчато, образуя катионы основных солей.<p><h5>3.Гидролиз по катиону и аниону<h5><p>Соли, образованные слабым основанием и слабой кислотой, гидролизуются и по катиону и по аниону.Примеры таких солей:  CH3COONH4, (NH4)2CO3, HCOONH4,Уравнение гидролиза: CH3COO— + NH4+ + HOH ↔ CH3COOH +  NH3·H2OВ этом случае реакция раствора зависит от соотношения констант диссоциации образующихся кислот и оснований.<p>",
    },
    "electrolysis":{
        "title": "Электролиз растворов",
        "text": "<h3> Различают электролиз раствора или расплава химического вещества.В растворе присутствует дополнительное химическое вещество — вода, которая может принимать участие в окислительно-восстановительных реакциях.<h3><h5>1. Если металл в соли — активный<h5><p>1. Если металл в соли — активный (до Al3+ включительно в ряду напряжений),то вместо металла на катоде восстанавливается (разряжается) водород, т.к. потенциал водорода намного больше.Протекает процесс восстановления молекулярного водорода из воды, при этом образуются ионы OH—, среда возле катода — щелочная:2H2O +2ē → H2 + 2OH—<p><h5>2. Если металл в соли –  средней активности<h5><p>2. Если металл в соли –  средней активности (между Al3+ и Н+), то на катоде восстанавливается (разряжается) и металл,и водород, так как потенциал таких металлов сравним с потенциалом водорода:Men+ + nē → Me0  ;  2H+2O +2ē → H20 + 2OH—<p><h5>3. Если металл в соли — неактивный<h5><p>3. Если металл в соли — неактивный (после водорода в ряду стандартных электрохимических металлов),то ион такого металла является более сильным окислителем, чем ион водорода, и на катоде восстанавливается только металл:Men+ + nē → Me0<p>",
    },
    "silvermirror":{
        "title": "Реакция серебряного зеркала",
        "text": "<h3>Реакция серебряного зеркала является качественной реакцией на альдегиды,это реакция восстановления серебра из раствора аммиачного комплекса серебра [Ag(NH3)2]OH.Альдегиды лекго окисляются под действием мягких оксилителей, в том числе и под действием данного комплекса.К тому же реакция может быть очень интересна и для обычных показательных опытов.В результате опыта в колбе (пробирке) образуется тонки красивый зеркальный налет серебра.<h3><h5>В пробирку нальем немного водного раствора аммиака. Добавим немного нитрата серебра. Это необходимо для получения аммиачного комплекса серебра.Уравнение данной  реакции:2AgNO3 + 2NH3 + H2O = Аg2O↓ + 2NH4NO3и далееАg2O + 4NH3 + H2O = 2[Ag(NH3)2]OHК полученному раствору добавим несколько капель формальдегида, и немного нагреем пробирку. Через некоторое время на стенках пробирки начнет появляться осадок серебра.Уравнение реакции:  2[Ag(NH3)2]OH + НСОН = 2Ag↓ + HCOONH4 + 3NH3 + H2OВ результате опыт имеем  колбу с тонкой пленкой из чистого серебра:<h5>",
    },
    "nitricacid":{
        "title": "Получение азотной кислоты (теория)",
        "text": "<h3>Азотная кислота – бесцветная гигроскопичная жидкость, c резким запахом, «дымит» на воздухе, неограниченно растворимая в воде.tкип. = 83ºC..  При хранении на свету разлагается на оксид азота (IV), кислород и воду, приобретая желтоватый  цвет:4HNO3 = 4NO2 + 2H2O + O2.Азотная кислота ядовита.<h3><h5>1.Контактное окисление аммиака до оксида азота (II) с PT. кат:4NH3+5O2=4NO+6H2O<h5><h5>2.Окисление оксида азота (II) в оксид азота (IV):2NO+O2=2NO2<h5><h5>3.Адсорбция (поглощение) оксида азота (IV) водой при избытке кислорода:4NO2+2H2O+O2=4HNO3Получили аотную кислоту (HNO3)<h5><h5>Лабораторный метод получения:KNO3+H2SO4(конц)=KHSO4+HNO3Получили азотную кислоту<h5>",
    }
}

aboutInfo = {
    "project":{
        "title": "Про ExperimentBox",
        "text": "<h3>Проект ExprerimentBox создан для привлечения интересов детей и взрослых путем 'красивой' подачи информации</h3><h5>Наш сайт предостовляет пользователю текстровую информации, фото и видеоматериалы про эксперементы</h5>",
    },
    "solving":{
        "title": "Решение",
        "text": "<h3>На данный момент создан сайт воплощающий наши желания в реальность</h3><h5>В планах на будещее: создание мобильного приложения на Android и IOS, и модернизация сайта</h5>",
    },
    "members":{
        "title": "Участники",
        "text": "<h3>Все участники ученики 7 класса</h3><h5>Лызинцев Женя - фронтэнд, Проскуряков Дима - бэкэндер</h5>",
    }
}

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()