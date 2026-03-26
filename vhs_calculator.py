import streamlit as st

st.set_page_config(page_title="VHS Калькулятор", page_icon="🐾")

BREED_NORMS = {
    "Собаки": {
        "Австралийская пастушья собака": [{"value": 10.5, "sd": 0.4}],
        "Американский питбультерьер": [{"value": 10.9, "sd": 0.4}],
        "Американская эскимосская собака": [{"range": (9.5, 11.5)}],
        "Ам.стафф. терьер": [{"value": 10.9, "sd": 0.6}],
        "Беспородные": [{"value": 9.82, "sd": 0.21}, {"value": 9.59, "sd": 0.31}],
        "Бигль": [{"value": 10.3, "sd": 0.4}],
        "Боксёр": [{"value": 11.6, "sd": 0.8}],
        "Бордер-терьер": [{"range": (9.3, 11.6)}],
        "Бостон-терьер": [{"value": 11.7, "sd": 1.4}, {"range": (9.7, 13.0)}],
        "Брюссельский гриффон": [{"range": (9.3, 11.9)}],
        "Бульдог (фр, англ)": [{"value": 12.7, "sd": 1.7}],
        "Грейхаунд": [{"value": 10.5, "sd": 0.1}],
        "Джек-рассел-терьер": [{"range": (9.7, 11.8)}],
        "Доберман": [{"value": 10.0, "sd": 0.6}],
        "Индийский шпиц": [{"value": 10.21, "sd": 0.23}],
        "Йоркширский терьер": [{"value": 9.9, "sd": 0.6}, {"value": 9.7, "sd": 0.5}, {"range": (9.0, 11.4)}],
        "Кавалер кинг чарльз спаниель": [{"value": 10.6, "sd": 0.5}, {"value": 10.08, "sd": 0.56}],
        "Карликовый пинчер": [{"range": (9.6, 12.2)}],
        "Корги": [{"value": 9.36, "sd": 0.27}],
        "Лабрадор ретривер": [{"value": 10.8, "sd": 0.6}, {"value": 10.39, "sd": 0.19}],
        "Лхаса Апсо": [{"value": 9.6, "sd": 0.8}],
        "Мальтезе": [{"value": 9.53, "sd": 0.46}],
        "Миниатюрная австралийская овчарка": [{"range": (9.4, 11.5)}],
        "Мопс": [{"value": 10.7, "sd": 0.9}, {"range": (9.7, 12.0)}],
        "Немецкая овчарка": [{"value": 9.7, "sd": 0.7}, {"value": 9.7, "sd": 0.8}],
        "Норвич-терьер": [{"value": 10.6, "sd": 0.6}],
        "Ротвейлер": [{"value": 9.8, "sd": 0.1}],
        "Такса": [{"value": 9.7, "sd": 0.5}],
        "Тибетский терьер": [{"range": (9.2, 11.4)}],
        "Уиппет (среднее значение)": [{"value": 11.3, "sd": 0.5}],
        "Уиппет (выставочные)": [{"value": 10.8, "sd": 0.6}],
        "Уиппет (беговые)": [{"value": 11.4, "sd": 0.4}],
        "Цвергшнауцер": [{"value": 10.9, "sd": 1.2}],
        "Чихуахуа": [{"value": 10.0, "sd": 0.6}],
        "Ши-тцу": [{"value": 9.5, "sd": 0.6}],
        "Шпиц": [{"value": 10.5, "sd": 0.9}, {"range": (9.5, 12.0)}],
        "Бретонский эпаньоль": [{"value": 10.6, "sd": 0.2}],
    },
    "Кошки": {
        "Кошки (разных возрастов)": [{"value": 7.5, "sd": 0.3}, {"value": 7.65, "sd": 0.54}],
        "Кошки (0.6-6 лет)": [{"value": 7.4, "sd": 0.4}],
        "Кошки (11-17 лет)": [{"value": 7.7, "sd": 0.6}],
        "Мейн-кун": [{"value": 7.61, "sd": 0.34}],
    },
    "Экзоты": {
        "Африканский ёж": [{"value": 8.16, "sd": 0.48}],
        "Кролик (самки до 1.6 кг)": [{"value": 7.75, "sd": 0.46}],
        "Кролик (самки более 1.6 кг)": [{"value": 7.86, "sd": 0.64}],
        "Кролик (самцы до 1.6 кг)": [{"value": 7.37, "sd": 0.2}],
        "Кролик (самцы более 1.6 кг)": [{"value": 8.3, "sd": 0.22}],
        "Кролик (оба пола до 1.6 кг)": [{"value": 7.55, "sd": 0.38}],
        "Кролик (оба пола более 1.6 кг)": [{"value": 7.99, "sd": 0.58}],
        "Кролик (6 мес, правая латеральная)": [{"value": 7.6, "sd": 0.39}],
        "Кролик (6 мес, левая латеральная)": [{"value": 7.94, "sd": 0.54}],
        "Крыса": [{"value": 7.7, "sd": 0.7}],
        "Морская свинка": [{"value": 7.7, "sd": 0.12}],
        "Шиншилла": [{"value": 8.9, "sd": 0.62}],
        "Хорёк (самцы)": [{"value": 5.41, "sd": 0.25}, {"value": 5.52, "sd": 0.28}],
        "Хорёк (самки)": [{"value": 5.27, "sd": 0.23}, {"value": 5.24, "sd": 0.2}],
    }
}

def parse_norm_item(item):
    if "range" in item:
        return item["range"]
    elif "value" in item:
        value = item["value"]
        sd = item.get("sd", 0.3)
        return (round(value - sd, 1), round(value + sd, 1))

def format_norm_item(item):
    if "range" in item:
        r = item["range"]
        return f"{r[0]}–{r[1]}"
    elif "value" in item:
        value = item["value"]
        sd = item.get("sd", 0.3)
        return f"{value} ± {sd}"

def check_status(vhs, norm_range):
    vhs_rounded = round(vhs, 1)
    norm_min, norm_max = norm_range
    if vhs_rounded < norm_min:
        return "Ниже нормы", "🔽"
    elif vhs_rounded > norm_max:
        return "Выше нормы", "🔼"
    else:
        return "В норме", "✅"

def check_status_all(vhs, norm_items):
    statuses = []
    for item in norm_items:
        norm_range = parse_norm_item(item)
        status, icon = check_status(vhs, norm_range)
        norm_str = format_norm_item(item)
        statuses.append((norm_str, status, icon, norm_range))
    return statuses

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
        norm_items = BREED_NORMS[category][breed]
        results = check_status_all(vhs, norm_items)
        
        st.markdown("---")
        st.markdown("### Результат")
        
        st.metric("**VHS**", f"{vhs}")
        
        if len(results) == 1:
            norm_str, status, icon, norm_range = results[0]
            st.success(f"VHS = **{vhs}**. Норма для **{breed}** составляет **{norm_str}**. Статус: **{icon} {status}**")
        else:
            st.markdown(f"**Норма для {breed}:**")
            for i, (norm_str, status, icon, norm_range) in enumerate(results, 1):
                st.write(f"{i}. {norm_str} — {icon} {status}")
            
            overall_statuses = [r[1] for r in results]
            if "Выше нормы" in overall_statuses:
                final_status = "Выше нормы"
                final_icon = "🔼"
            elif "Ниже нормы" in overall_statuses:
                final_status = "Ниже нормы"
                final_icon = "🔽"
            else:
                final_status = "В норме"
                final_icon = "✅"
            
            st.success(f"VHS = **{vhs}**. Статус: **{final_icon} {final_status}**")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.85em;">
    <p>Источник: VHS РУ 06.07.25</p>
    <p>Формула: VHS = L + S</p>
</div>
""", unsafe_allow_html=True)
