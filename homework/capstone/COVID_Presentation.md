# COVID-19 Data Analysis
## Аналіз даних пандемії COVID-19

---

<div align="center">

# 📊 Частина 1: Огляд даних
## Data Overview

</div>

### 📈 Розмір датасету
| Параметр | Значення |
|----------|----------|
| **Записів** | 429,435 |
| **Колонок** | 67 |
| **Країн** | 200+ |
| **Період** | Січ 2020 — Сер 2024 |

### 🌍 Розподіл по континентах
```
Africa          95,419  ████████████████████░░░░░  22.2%
Europe          91,031  ███████████████████░░░░░░░░  21.2%
Asia            84,199  █████████████████░░░░░░░░░░  19.6%
North America   68,638  ██████████████░░░░░░░░░░░░░  16.0%
Oceania         40,183  ████████░░░░░░░░░░░░░░░░░░░   9.4%
South America   23,440  █████░░░░░░░░░░░░░░░░░░░░░░   5.5%
```

---

<div align="center">

# 📈 Частина 2: Динаміка пандемії
## Pandemic Dynamics

</div>

### 🇺🇦 Україна — Динаміка випадків
*Графік: Time series of total_cases та total_deaths*

**Спостереження:**
- Пік хвилі: **Лютий 2022**
- Максимальні нові випадки: **2022-02-06**

### 🇺🇸🇺🇦🇩🇪 Порівняння країн: США, Україна, Німеччина
*Графік: new_cases по датах для трьох країн*

**Результати:**
| Країна | Пік нових випадків | Дата піку |
|--------|-------------------|-----------|
| USA | 4,423,623 | 2022-01-16 |
| UKR | 351,325 | 2022-02-06 |
| DEU | 412,890 | 2022-03-27 |

---

<div align="center">

# 🔧 Частина 3: ETL та Кореляції
## ETL & Correlations

</div>

### 🧹 Обробка даних
```
✅ Пропущені значення: Заповнено 0 для new_cases/new_deaths
✅ Дублікати: Видалено (0 знайдено)
✅ Часові ряди: Відсортовано по location та date
✅ Зростання: Обчислено growth_rate_new_cases та growth_rate_new_deaths
```

### 📊 Кореляційна матриця
*Графік: Heatmap кореляцій*

| Змінні | Коефіцієнт кореляції |
|--------|---------------------|
| new_cases ↔ new_deaths | **0.51** |
| total_cases ↔ population | **0.67** |
| gdp_per_capita ↔ population | **-0.03** |

### 📈 Розподіл total_cases
*Графік: Histogram з 50 bins*

**Характеристики:**
- Середнє: **7,365,292.15**
- Медіана: **63,653.00**
- Макс: **775,866,782.00**

---

<div align="center">

# 💉 Частина 4: Вакцинація
## Vaccination Dynamics

</div>

### 🌍 Динаміка вакцинації: 5 країн
*Графік: Plotly interactive — USA, UKR, DEU, FRA, ITA*

**Спостереження:**
- **USA** — лідер за темпами вакцинації
- **UKR** — повільніший старт, але стабільний ріст
- **DEU, FRA, ITA** — схожі темпи

---

<div align="center">

# 🤖 Частина 5: Моделювання — Класифікація
## Modeling — Classification

</div>

### 🎯 Цільова змінна
```
high_cases = (new_cases > 1000) → 0 або 1
```

### 🔧 Підготовка даних
| Крок | Метод | Результат |
|------|-------|-----------|
| Кодування континентів | One-Hot Encoding | 5 бінарних змінних |
| Кодування iso_code | LabelEncoder | Числові значення |
| Масштабування | StandardScaler | Середнє=0, σ=1 |
| Балансування | SMOTE | 50/50 класи |

### 📊 Результати моделей класифікації

| Модель | Accuracy | Precision | Recall | F1 |
|--------|----------|-----------|--------|-----|
| **Logistic Regression** | 0.34 | 0.11 | **0.81** | 0.19 |
| **Decision Tree** | **0.82** | 0.16 | 0.19 | 0.17 |
| **Random Forest** | **0.84** | 0.11 | 0.10 | 0.11 |
| **KNN** | 0.79 | 0.14 | 0.23 | 0.17 |

**Висновок:** Random Forest — найкраща точність (**0.84**), Logistic Regression — найкраща повнота (**0.81**)

### 🎯 Відбір ознак (SelectKBest, k=10)

**Топ-10 ознак:**
1. `iso_code`
2. `total_cases`
3. `total_deaths`
4. `total_vaccinations`
5. `population`
6. `continent_Asia`
7. `continent_Europe`
8. `continent_North America`
9. `continent_Oceania`
10. `continent_South America`

**Покращення:** Random Forest з відібраними ознаками — **Accuracy: 0.85** (+0.02)

---

<div align="center">

# 📉 Частина 6: Моделювання — Регресія
## Modeling — Regression

</div>

### 🎯 Цільова змінна
```
y = new_cases (прогноз кількості нових випадків)
```

### 📊 Результати регресійних моделей

| Модель | MSE | R² | RMSE | MAE |
|--------|-----|-----|------|-----|
| **Lasso Regression** | 9.13×10⁹ | **0.01** | 95,541.25 | 19,303.44 |
| **Ridge Regression** | 9.13×10⁹ | **0.01** | 95,541.60 | 19,305.65 |
| **Linear Regression** | 9.13×10⁹ | **0.01** | 95,542.03 | 19,307.64 |
| **Polynomial (deg=2)** | 1.26×10¹¹ | **0.06** | 355,501.88 | 18,850.35 |

**Висновок:** Всі моделі показують низьку прогнозну здатність (R² ≈ 0.01). Поліноміальна регресія — найвищий R² (**0.06**), але висока похибка.

---

<div align="center">

# 🔍 Частина 7: Оцінка та Оптимізація
## Evaluation & Optimization

</div>

### 📊 Матриці плутанини
*Графіки: Confusion matrices для всіх 4 моделей*

### 🔢 Cross-Validation (5-fold)

| Модель | Mean F1 | Std |
|--------|---------|-----|
| Logistic Regression | 0.19 | 0.03 |
| Decision Tree | 0.18 | 0.02 |
| Random Forest | 0.11 | 0.01 |
| KNN | 0.17 | 0.02 |

### ⚙️ Hyperparameter Tuning (GridSearchCV)

**Random Forest оптимальні параметри:**
```python
{
    'max_depth': 10,
    'min_samples_split': 5,
    'n_estimators': 200
}
```

**Результат після оптимізації:**
- F1: **0.17**
- Точність моделі залишається стабільною

### 🚀 Gradient Boosting Classifier

| Метрика | Значення |
|---------|----------|
| Accuracy | **0.47** |
| F1 | **0.23** |

---

<div align="center">

# 📝 Частина 8: Висновки
## Conclusions

</div>

### ✅ Key Findings

| № | Висновок | Доказ |
|---|----------|-------|
| 1 | **Random Forest** — найкраща модель класифікації | Accuracy = **0.85** |
| 2 | **Feature Selection** покращує результати | +0.02 до accuracy |
| 3 | **Регресія** — низька прогнозна здатність | R² ≈ **0.01** |
| 4 | **Класифікація** ефективніша за регресію | F1 = 0.18 vs R² = 0.01 |
| 5 | **Logistic Regression** — найкраща повнота | Recall = **0.81** |

### 💡 Рекомендації

1. **Додати часові ознаки** (seasonality, trends)
2. **Включити соціальні індикатори** (stringency index)
3. **Застосувати складніші моделі** (XGBoost, Neural Networks)
4. **Аналіз викидів** для покращення регресії

---

<div align="center">

# Дякую за увагу!
## Questions?

📧 Contact: [email]
📁 GitHub: [repository]

</div>

---

## 📎 Додатки

### A. Метрики якості моделей

**Classification:**
- **Accuracy** = (TP + TN) / Total
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **F1** = 2 × (Precision × Recall) / (Precision + Recall)

**Regression:**
- **MSE** = Mean Squared Error
- **R²** = Коефіцієнт детермінації
- **RMSE** = Root Mean Squared Error
- **MAE** = Mean Absolute Error

### B. Використані бібліотеки
```
pandas, numpy, matplotlib, seaborn
scikit-learn, imbalanced-learn, plotly
```

### C. Структура проєкту
```
covid_project/
├── covid_data.csv              # Вихідні дані
├── cleaned_covid_data.csv     # Очищені дані
├── covid_project.ipynb        # Основний ноутбук
├── 39_7.MD                    # Аналітичний звіт
└── COVID_Presentation.md      # Ця презентація
```
