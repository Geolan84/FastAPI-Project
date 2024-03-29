from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from models import region, specialization, skills

skills_val = [
    {"skill_name": "Python"},
    {"skill_name": "C/C++"},
    {"skill_name": "SAS"},
    {"skill_name": "SQL"},
    {"skill_name": "BPMN"},
    {"skill_name": "UML"},
    {"skill_name": "Archimate"},
    {"skill_name": "Visual Paradigm"},
    {"skill_name": "Golang"},
    {"skill_name": "Java"},
    {"skill_name": "C#"},
    {"skill_name": "Lua"},
    {"skill_name": "Javascript"},
    {"skill_name": "Kotlin"},
    {"skill_name": "Dart"},
    {"skill_name": "Ruby"},
    {"skill_name": "VBA"},
    {"skill_name": "PHP"},
    {"skill_name": "WordPress"},
    {"skill_name": "Flutter"},
    {"skill_name": "Microsoft Office"},
    {"skill_name": "QT"},
    {"skill_name": "PyQT"},
    {"skill_name": "Git"},
    {"skill_name": "Docker"},
    {"skill_name": "Kubernetes"},
    {"skill_name": "Pytest"},
    {"skill_name": "JUnit"},
    {"skill_name": "Spring"},
    {"skill_name": "Netty"},
    {"skill_name": "ASP.NET"},
    {"skill_name": "WPF"},
    {"skill_name": "CI"},
    {"skill_name": "Jira"},
    {"skill_name": "Asana"},
    {"skill_name": "Agile"},
    {"skill_name": "SCRUM"},
    {"skill_name": "Slack"},
    {"skill_name": "CL"},
    {"skill_name": "EPC"},
    {"skill_name": "Clion"},
    {"skill_name": "Pycharm"},
    {"skill_name": "Visual Studio"},
    {"skill_name": "Goland"},
    {"skill_name": "Intelij Idea"},
    {"skill_name": "VS Code"},
    {"skill_name": "Android Studio"},
    {"skill_name": "Swift"},
    {"skill_name": "JavaFX"},
    {"skill_name": "Swing"},
    {"skill_name": "FastAPI"},
    {"skill_name": "Django"}
]

geonames = [
    {"geoname": "Адыгея (Республика Адыгея)"},
    {"geoname": "Алтай (Республика Алтай)"},
    {"geoname": "Алтайский край"},
    {"geoname": "Амурская область"},
    {"geoname": "Архангельская область"},
    {"geoname": "Астраханская область"},
    {"geoname": "Башкортостан (Республика Башкортостан)"},
    {"geoname": "Белгородская область"},
    {"geoname": "Брянская область"},
    {"geoname": "Бурятия (Республика Бурятия)"},
    {"geoname": "Владимирская область"},
    {"geoname": "Волгоградская область"},
    {"geoname": "Вологодская область"},
    {"geoname": "Воронежская область"},
    {"geoname": "Дагестан (Республика Дагестан)"},
    {"geoname": "Донецкая Народная Республика"},
    {"geoname": "Еврейская автономная область"},
    {"geoname": "Забайкальский край"},
    {"geoname": "Запорожская область"},
    {"geoname": "Ивановская область"},
    {"geoname": "Ингушетия (Республика Ингушетия)"},
    {"geoname": "Иркутская область"},
    {"geoname": "Кабардино-Балкария (Кабардино-Балкарская Республика)"},
    {"geoname": "Калининградская область"},
    {"geoname": "Калмыкия (Республика Калмыкия)"},
    {"geoname": "Калужская область"},
    {"geoname": "Камчатский край"},
    {"geoname": "Карачаево-Черкесия (Карачаево-Черкесская Республика)"},
    {"geoname": "Карелия (Республика Карелия)"},
    {"geoname": "Кемеровская область"},
    {"geoname": "Кировская область"},
    {"geoname": "Коми (Республика Коми)"},
    {"geoname": "Костромская область"},
    {"geoname": "Краснодарский край (Кубань)"},
    {"geoname": "Красноярский край"},
    {"geoname": "Крым (Республика Крым)"},
    {"geoname": "Курганская область"},
    {"geoname": "Курская область"},
    {"geoname": "Ленинградская область"},
    {"geoname": "Липецкая область"},
    {"geoname": "Луганская Народная Республика"},
    {"geoname": "Магаданская область"},
    {"geoname": "Марий Эл (Республика Марий Эл)"},
    {"geoname": "Мордовия (Республика Мордовия)"},
    {"geoname": "Москва"},
    {"geoname": "Московская область"},
    {"geoname": "Мурманская область"},
    {"geoname": "Ненецкий автономный округ"},
    {"geoname": "Нижегородская область"},
    {"geoname": "Новгородская область"},
    {"geoname": "Новосибирская область"},
    {"geoname": "Омская область"},
    {"geoname": "Оренбургская область"},
    {"geoname": "Орловская область"},
    {"geoname": "Пензенская область"},
    {"geoname": "Пермский край"},
    {"geoname": "Приморский край"},
    {"geoname": "Псковская область"},
    {"geoname": "Ростовская область"},
    {"geoname": "Рязанская область"},
    {"geoname": "Самарская область"},
    {"geoname": "Санкт-Петербург"},
    {"geoname": "Саратовская область"},
    {"geoname": "Саха (Республика Саха (Якутия))"},
    {"geoname": "Сахалинская область"},
    {"geoname": "Свердловская область"},
    {"geoname": "Севастополь"},
    {"geoname": "Северная Осетия (Республика Северная Осетия — Алания)"},
    {"geoname": "Смоленская область"},
    {"geoname": "Ставропольский край"},
    {"geoname": "Тамбовская область"},
    {"geoname": "Татарстан (Республика Татарстан)"},
    {"geoname": "Тверская область"},
    {"geoname": "Томская область"},
    {"geoname": "Тульская область"},
    {"geoname": "Тыва (Республика Тыва)"},
    {"geoname": "Тюменская область"},
    {"geoname": "Удмуртия (Удмуртская Республика)"},
    {"geoname": "Ульяновская область"},
    {"geoname": "Хабаровский край"},
    {"geoname": "Хакасия (Республика Хакасия)"},
    {"geoname": "Ханты-Мансийский автономный округ — Югра"},
    {"geoname": "Херсонская область"},
    {"geoname": "Челябинская область"},
    {"geoname": "Чечня (Чеченская Республика)"},
    {"geoname": "Чувашия (Чувашская Республика)"},
    {"geoname": "Чукотка (Чукотский автономный округ)"},
    {"geoname": "Ямало-Ненецкий автономный округ"},
    {"geoname": "Ярославская область"}
]

specs = [
    {"spec_name": "QA-инженер"},
    {"spec_name": "Разработчик"},
    {"spec_name": "Архитектор"},
    {"spec_name": "Технический писатель"},
    {"spec_name": "Системный аналитик"},
    {"spec_name": "Бизнес-аналитик"}
]

async def fill_db(session: AsyncSession):
    stmt = insert(skills).values(skills_val)
    await session.execute(stmt)
    stmt = insert(region).values(geonames)
    await session.execute(stmt)
    stmt = insert(specialization).values(specs)
    await session.execute(stmt)
    await session.commit()

