# Тест-кейсы для API объявлений

## Позитивные сценарии POST

### TC-P-01: Создание объявления с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, заполненным валидными данными (см. пример) | Статус ответа `200 OK` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" }` |

**Пример валидного тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

## Негативные сценарии POST

### TC-N-01: Создание объявления с невалидным sellerID (строковое значение) с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `sellerID` передан строковым значением, остальные поля заполнены валидными данными (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": "abc",
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-02: Создание объявления с sellerID = -1 с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `sellerID = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": -1,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-03: Создание объявления с sellerID = 0 с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `sellerID = 0`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 0,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-04: Создание объявления с пустым полем name с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `name = ""` (пустая строка), остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-05: Создание объявления с отрицательной ценой с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `price = -500`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": -500,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-06: Создание объявления с ценой в виде строки с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `price` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": "abc",
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-07: Создание объявления с ценой 0 с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `price = 0`, остальные поля валидны (см. пример) | Статус ответа `200 OK` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 0,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-08: Создание объявления с отрицательным значением likes с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.likes = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": -10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-09: Создание объявления с likes в виде строки с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.likes` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": "abc",
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-10: Создание объявления с viewCount в виде строки с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.viewCount` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": "abc",
    "contacts": 10
  }
}
```

---

### TC-N-11: Создание объявления с отрицательным viewCount с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.viewCount = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": -1,
    "contacts": 10
  }
}
```

---

### TC-N-12: Создание объявления с contacts в виде строки с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.contacts` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": "abc"
  }
}
```

---

### TC-N-13: Создание объявления с отрицательным contacts с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.contacts = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": -1
  }
}
```

---

## Проверка обязательности полей

### TC-N-14: Создание объявления без поля sellerID с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `sellerID` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-15: Создание объявления без поля name с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `name` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-16: Создание объявления без поля price с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `price` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-17: Создание объявления без поля statistics с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `statistics` (см. пример) | Статус ответа `200 OK` или `400 Bad Request` (уточнить у аналитика) |
| 4 | Проверить тело ответа | Если `200 OK` — тело ответа соответствует JSON-схеме из TC-P-01. Если `400 Bad Request` — схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  }
}
```

---

### TC-N-18: Создание объявления с пустым JSON с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с пустым телом `{}` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**
```json
{}
```

---

### TC-N-19: Создание объявления с лишним полем с помощью API - `https://qa-internship.avito.com/api/1/item`

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, содержащим дополнительное поле `"extraField": "test"` (см. пример) | Статус ответа `200 OK` или `400 Bad Request` (уточнить у аналитика) |
| 4 | Проверить тело ответа | Если `200 OK` — тело ответа соответствует JSON-схеме из TC-P-01 (лишнее поле не возвращается). Если `400 Bad Request` — схеме ошибки |

**Пример тела запроса:**
```json
{
  "sellerID": 555555,
  "name": "Ноутбук",
  "price": 150000,
  "statistics": {
    "likes": 10,
    "viewCount": 10,
    "contacts": 10
  },
  "extraField": "test"
}
```

---

## Сводная таблица проверок

| № | Проверка | Ожидаемый статус |
|---|----------|------------------|
| TC-P-01 | Валидные данные | 200 OK |
| TC-N-01 | sellerID строка | 400 |
| TC-N-02 | sellerID = -1 | 400 |
| TC-N-03 | sellerID = 0 | 400? (уточнить) |
| TC-N-04 | name пустая строка | 400 |
| TC-N-05 | price отрицательная | 400 |
| TC-N-06 | price строка | 400 |
| TC-N-07 | price = 0 | 400? (уточнить) |
| TC-N-08 | likes отрицательная | 400 |
| TC-N-09 | likes строка | 400 |
| TC-N-10 | viewCount строка | 400 |
| TC-N-11 | viewCount отрицательная | 400 |
| TC-N-12 | contacts строка | 400 |
| TC-N-13 | contacts отрицательная | 400 |
| TC-N-14 | нет sellerID | 400 |
| TC-N-15 | нет name | 400 |
| TC-N-16 | нет price | 400 |
| TC-N-17 | нет statistics | уточнить |
| TC-N-18 | пустой JSON | 400 |
| TC-N-19 | лишнее поле | уточнить |
```
