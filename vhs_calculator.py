import streamlit as st

st.set_page_config(page_title="VHS Калькулятор", page_icon="🐾")

BREED_NORMS = {
    "Собаки": {
        "Аффенпинчер": {"value": 9.0, "deviation": 0.5},
        "Акита": {"range": (9.5, 11.0)},
        "Английский бульдог": {"range": (10.2, 11.8)},
        "Бассет-хаунд": {"range": (10.0, 11.5)},
        "Бедуин": {"value": 10.5, "deviation": 0.7},
        "Бернский зенненхунд": {"range": (10.5, 12.0)},
        "Бигль": {"range": (9.5, 11.0)},
        "Боксёр": {"range": (10.6, 12.0)},
        "Борзая": {"range": (10.5, 12.0)},
        "Бульмастиф": {"range": (10.5, 12.5)},
        "Веймаранер": {"range": (10.0, 11.5)},
        "Вельш-корги": {"range": (9.0, 10.5)},
        "Венгерская выжла": {"value": 10.5, "deviation": 0.5},
        "Далматинец": {"range": (10.0, 11.5)},
        "Доберман": {"range": (10.0, 11.5)},
        "Золотистый ретривер": {"range": (10.0, 11.5)},
        "Ирландский волкодав": {"range": (10.0, 11.8)},
        "Йоркширский терьер": {"range": (8.8, 10.0)},
        "Кавказская овчарка": {"range": (10.5, 12.0)},
        "Кане-корсо": {"range": (10.0, 11.8)},
        "Китайская хохлатая": {"range": (8.5, 10.0)},
        "Кокер-спаниель": {"range": (9.5, 11.0)},
        "Лабрадор ретривер": {"range": (10.1, 11.5)},
        "Лхаса апсо": {"range": (9.5, 11.0)},
        "Майоркская овчарка": {"range": (10.5, 12.0)},
        "Мальтийская болонка": {"range": (8.5, 9.8)},
        "Мопс": {"range": (9.5, 11.0)},
        "Немецкая овчарка": {"range": (9.7, 11.0)},
        "Немецкий дог": {"range": (11.0, 13.0)},
        "Ньюфаундленд": {"range": (10.5, 12.5)},
        "Пекинес": {"range": (9.0, 10.5)},
        "Пудель (той)": {"range": (8.5, 10.0)},
        "Пудель (миниатюрный)": {"range": (9.0, 10.5)},
        "Пудель (стандартный)": {"range": (10.0, 11.5)},
        "Ротвейлер": {"range": (10.0, 11.8)},
        "Салюки": {"range": (9.5, 11.5)},
        "Сенбернар": {"range": (11.0, 13.0)},
        "Сиба-ину": {"range": (9.0, 10.5)},
        "Среднеазиатская овчарка": {"range": (10.5, 12.0)},
        "Той-терьер": {"range": (8.5, 10.0)},
        "Такса": {"value": 8.9, "deviation": 0.4},
        "Французский бульдог": {"range": (9.8, 11.5)},
        "Хаски": {"range": (9.5, 11.0)},
        "Чихуахуа": {"value": 9.2, "deviation": 0.5},
        "Шелти": {"range": (9.0, 10.5)},
        "Ши-тцу": {"range": (9.5, 10.8)},
        "Шпиц (померанский)": {"range": (8.5, 10.0)},
        "Южноафриканский бурбуль": {"range": (10.5, 12.5)},
        "Грейхаунд": {"range": (10.5, 12.0)},
        "Гладкошёрстная такса": {"value": 8.9, "deviation": 0.4},
        "Джек-рассел-терьер": {"range": (8.8, 10.0)},
        "Спаниель": {"range": (9.5, 11.0)},
        "Бульдог": {"range": (10.2, 11.8)},
        "Бордер-колли": {"range": (9.5, 11.0)},
        "Австралийская овчарка": {"range": (9.5, 11.0)},
        "Колли": {"range": (9.5, 11.0)},
        "Румынская миоритическая овчарка": {"value": 10.8, "deviation": 0.7},
    },
    "Кошки": {
        "Британская короткошёрстная": {"range": (6.5, 8.5)},
        "Британская длинношёрстная": {"range": (6.5, 8.5)},
        "Мейн-кун": {"range": (6.5, 8.5)},
        "Рэгдолл": {"range": (6.5, 8.5)},
        "Сфинкс": {"range": (6.5, 8.5)},
        "Шотландская вислоухая": {"range": (6.5, 8.5)},
        "Персидская": {"range": (6.5, 8.5)},
        "Абиссинская": {"range": (6.5, 8.5)},
        "Бенгальская": {"range": (6.5, 8.5)},
        "Сиамская": {"range": (6.5, 8.5)},
        "Ориентальная": {"range": (6.5, 8.5)},
        "Русская голубая": {"range": (6.5, 8.5)},
        "Норвежская лесная": {"range": (6.5, 8.5)},
        "Сибирская": {"range": (6.5, 8.5)},
        "Бурма": {"range": (6.5, 8.5)},
        "Экзотическая короткошёрстная": {"range": (6.5, 8.5)},
        "Домашняя короткошёрстная": {"range": (6.5, 8.5)},
        "Домашняя длинношёрстная": {"range": (6.5, 8.5)},
        "Девон-рекс": {"range": (6.5, 8.5)},
        "Корниш-рекс": {"range": (6.5, 8.5)},
        "Бирманская": {"range": (6.5, 8.5)},
        "Турецкая ангора": {"range": (6.5, 8.5)},
        "Турецкий ван": {"range": (6.5, 8.5)},
        "Американская короткошёрстная": {"range": (6.5, 8.5)},
        "Балийская": {"range": (6.5, 8.5)},
        "Оцикет": {"range": (6.5, 8.5)},
        "Сомалийская": {"range": (6.5, 8.5)},
        "Европейская короткошёрстная": {"range": (6.5, 8.5)},
    },
    "Экзоты": {
        "Кролик (декоративный)": {"range": (1.4, 1.9)},
        "Кролик (карликовый)": {"range": (1.4, 1.9)},
        "Кролик (кролик)": {"range": (1.4, 1.9)},
        "Морская свинка": {"range": (1.6, 2.1)},
        "Хомяк": {"range": (1.0, 1.4)},
        "Хорёк": {"range": (3.5, 5.5)},
        "Шиншилла": {"range": (1.0, 1.4)},
        "Дегу": {"range": (1.0, 1.4)},
        "Крыса": {"range": (1.0, 1.4)},
        "Мышь": {"range": (0.8, 1.1)},
        "Песчанка": {"range": (0.9, 1.2)},
        "Суслик": {"range": (0.9, 1.3)},
        "Беличья обезьяна": {"range": (2.5, 3.5)},
        "Енот-полоскун": {"range": (4.0, 5.5)},
        "Феретта": {"range": (3.5, 5.5)},
        "Скунс": {"range": (3.5, 5.0)},
    }
}

def parse_norm(breed_data):
    if "range" in breed_data:
        return breed_data["range"]
    elif "value" in breed_data:
        value = breed_data["value"]
        deviation = breed_data.get("deviation", 0.3)
        return (round(value - deviation, 1), round(value + deviation, 1))

def format_norm(breed_data):
    if "range" in breed_data:
        r = breed_data["range"]
        return f"{r[0]}–{r[1]}"
    elif "value" in breed_data:
        value = breed_data["value"]
        deviation = breed_data.get("deviation", 0.3)
        return f"{value} ± {deviation} ({round(value - deviation, 1)}–{round(value + deviation, 1)})"

def check_status(vhs, norm_range):
    vhs_rounded = round(vhs, 1)
    norm_min, norm_max = norm_range
    if vhs_rounded < norm_min:
        return "Ниже нормы", "🔽"
    elif vhs_rounded > norm_max:
        return "Выше нормы", "🔼"
    else:
        return "В норме", "✅"

st.title("🐾 VHS Калькулятор")
st.markdown("**VHS (Vertebral Heart Score)** — метод оценки размеров сердца у животных по рентгеновским снимкам")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Категория:", options=list(BREED_NORMS.keys()))

breeds = sorted(BREED_NORMS[category].keys())
with col2:
    breed = st.selectbox("Порода/Вид:", options=breeds)

st.markdown("---")
st.markdown("### Параметры измерений")

col3, col4 = st.columns(2)

with col3:
    L = st.number_input("**L** (длинная ось сердца в телах позвонков):", 
                        min_value=0.0, step=0.1, format="%.1f", value=0.0)

with col4:
    S = st.number_input("**S** (короткая ось сердца в телах позвонков):", 
                        min_value=0.0, step=0.1, format="%.1f", value=0.0)

st.markdown("---")

if st.button("Рассчитать VHS", type="primary", use_container_width=True):
    if L == 0 and S == 0:
        st.warning("Введите значения L и S")
    else:
        vhs = round(L + S, 1)
        norm_data = BREED_NORMS[category][breed]
        norm_range = parse_norm(norm_data)
        norm_str = format_norm(norm_data)
        status, icon = check_status(vhs, norm_range)
        
        st.markdown("---")
        st.markdown("### Результат")
        
        col5, col6, col7 = st.columns(3)
        with col5:
            st.metric("**VHS**", f"{vhs}")
        with col6:
            st.metric("**Норма**", norm_str)
        with col7:
            st.metric("**Статус**", f"{icon} {status}")
        
        st.success(f"VHS = **{vhs}**. Норма для **{breed}** составляет **{norm_str}**. Статус: **{status}**")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.85em;">
    <p>Источник: VHS РУ 06.07.25</p>
    <p>Формула: VHS = L + S</p>
</div>
""", unsafe_allow_html=True)
