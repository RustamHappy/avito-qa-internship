# Тест-кейсы для API объявлений

## POST `/api/1/item` - Создание объявления

### TC-POST-01: Создание объявления с валидными данными

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, заполненным валидными данными (см. пример) | Статус ответа `200 OK` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" }` |

**Пример валидного тела запроса:**

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

---

### TC-POST-02: Создание объявления с невалидным sellerID (строковое значение)

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `sellerID` передан строковым значением, остальные поля заполнены валидными данными (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-03: Создание объявления с sellerID = -1

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `sellerID = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-04: Создание объявления с sellerID = 0

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `sellerID = 0`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-05: Создание объявления с пустым полем name

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `name = ""` (пустая строка), остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-06: Создание объявления с отрицательной ценой

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `price = -500`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-07: Создание объявления с ценой в виде строки

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `price` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-08: Создание объявления с ценой 0

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `price = 0`, остальные поля валидны (см. пример) | Статус ответа `200 OK` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-09: Создание объявления с отрицательным значением likes

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.likes = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

    {
      "sellerID": 555555,
      "name": "Ноутбук",
      "price": 150000,
      "statistics": {
        "likes": -1,
        "viewCount": 10,
        "contacts": 10
      }
    }

---

### TC-POST-10: Создание объявления с likes в виде строки

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.likes` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-11: Создание объявления с viewCount в виде строки

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.viewCount` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-12: Создание объявления с отрицательным viewCount

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.viewCount = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-13: Создание объявления с contacts в виде строки

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.contacts` передан строковым значением, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-14: Создание объявления с отрицательным contacts

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где `statistics.contacts = -1`, остальные поля валидны (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

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

---

### TC-POST-15: Создание объявления без поля sellerID

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `sellerID` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

    {
      "name": "Ноутбук",
      "price": 150000,
      "statistics": {
        "likes": 10,
        "viewCount": 10,
        "contacts": 10
      }
    }

---

### TC-POST-16: Создание объявления без поля name

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `name` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

    {
      "sellerID": 555555,
      "price": 150000,
      "statistics": {
        "likes": 10,
        "viewCount": 10,
        "contacts": 10
      }
    }

---

### TC-POST-17: Создание объявления без поля price

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `price` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

    {
      "sellerID": 555555,
      "name": "Ноутбук",
      "statistics": {
        "likes": 10,
        "viewCount": 10,
        "contacts": 10
      }
    }

---

### TC-POST-18: Создание объявления без поля statistics

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, где отсутствует поле `statistics` (см. пример) | Статус ответа `200 OK` или `400 Bad Request` (уточнить у аналитика) |
| 4 | Проверить тело ответа | Если `200 OK` — тело ответа соответствует JSON-схеме из TC-POST-01. Если `400 Bad Request` — схеме ошибки |

**Пример тела запроса:**

    {
      "sellerID": 555555,
      "name": "Ноутбук",
      "price": 150000
    }

---

### TC-POST-19: Создание объявления с пустым JSON

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с пустым телом `{}` (см. пример) | Статус ответа `400 Bad Request` |
| 4 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

**Пример тела запроса:**

    {}

---

### TC-POST-20: Создание объявления с лишним полем

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Content-Type: application/json` | Заголовок установлен |
| 2 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 3 | Отправить POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, содержащим дополнительное поле `"extraField": "test"` (см. пример) | Статус ответа `200 OK` или `400 Bad Request` (уточнить у аналитика) |
| 4 | Проверить тело ответа | Если `200 OK` — тело ответа соответствует JSON-схеме из TC-POST-01 (лишнее поле не возвращается). Если `400 Bad Request` — схеме ошибки |

**Пример тела запроса:**

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

---

## GET `/api/1/item/{id}` - Получение объявления по ID

### TC-GET-ITEM-01: Получение существующего объявления по ID

**Предусловие:** Создано объявление через POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, заполненным валидными данными

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/item/{id}`, где `{id}` — идентификатор созданного в предусловии объявления | Статус ответа `200 OK` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `[ { "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" }, { "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" } ]` |

**Пример валидного тела запроса (для создания объявления):**

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

---

### TC-GET-ITEM-02: Получение объявления с невалидным ID (строковое значение)

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/item/abc` | Статус ответа `400 Bad Request` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

---

### TC-GET-ITEM-03: Получение объявления с невалидным ID (спецсимволы)

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/item/!@#$%` | Статус ответа `400 Bad Request` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

---

### TC-GET-ITEM-04: Получение несуществующего объявления

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/item/00000000-0000-0000-0000-000000000000` | Статус ответа `404 Not Found` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": "laborum", "status": "cillum enim eiusmod" }` |

---

### TC-GET-ITEM-05: Получение объявления с пустым ID

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/item/` | Статус ответа `404 Not Found` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": "laborum", "status": "cillum enim eiusmod" }` |

---

## GET `/api/1/statistic/{id}` - Получение статистики по ID

### TC-GET-STAT-01: Получение статистики существующего объявления

**Предусловие:** Создано объявление через POST запрос на `https://qa-internship.avito.com/api/1/item` с телом, заполненным валидными данными

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/statistic/{id}`, где `{id}` — идентификатор созданного в предусловии объявления | Статус ответа `200 OK` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `[ { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" } ]` |

**Пример валидного тела запроса (для создания объявления):**

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

---

### TC-GET-STAT-02: Получение статистики с невалидным ID (строковое значение)

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/statistic/abc` | Статус ответа `400 Bad Request` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

---

### TC-GET-STAT-03: Получение статистики несуществующего объявления

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/statistic/00000000-0000-0000-0000-000000000000` | Статус ответа `404 Not Found` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": "laborum", "status": "cillum enim eiusmod" }` |

---

### TC-GET-STAT-04: Получение статистики с пустым ID

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/statistic/` | Статус ответа `404 Not Found` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": "laborum", "status": "cillum enim eiusmod" }` |

---

## GET `/api/1/{sellerID}/item` - Получение объявлений по sellerID

### TC-GET-SELLER-01: Получение объявлений существующего продавца

**Предусловие:** Создано два объявления через POST запрос на `https://qa-internship.avito.com/api/1/item` с одинаковым `sellerID` и телом, заполненным валидными данными

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/555555/item` | Статус ответа `200 OK` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `[ { "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" }, { "id": "<string>", "sellerId": "<integer>", "name": "<string>", "price": "<integer>", "statistics": { "likes": "<integer>", "viewCount": "<integer>", "contacts": "<integer>" }, "createdAt": "<string>" } ]` |
| 4 | Проверить, что оба созданных объявления присутствуют в ответе | В ответе найдены оба идентификатора из предусловия |

**Пример валидного тела запроса (для создания объявления):**

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

---

### TC-GET-SELLER-02: Получение объявлений продавца без объявлений

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/1534425463526443753/item` | Статус ответа `200 OK` |
| 3 | Проверить тело ответа | Тело ответа — пустой массив `[]` |

---

### TC-GET-SELLER-03: Получение объявлений с невалидным sellerID (строковое значение)

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/abc/item` | Статус ответа `400 Bad Request` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

---

### TC-GET-SELLER-04: Получение объявлений с sellerID = -1

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/-1/item` | Статус ответа `400 Bad Request` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }` |

---

### TC-GET-SELLER-05: Получение объявлений с sellerID = 0

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/0/item` | Статус ответа `400 Bad Request` (или `200 OK` — уточнить у аналитика) |
| 3 | Проверить тело ответа | Если `400` — тело ответа соответствует JSON-схеме: `{ "result": { "messages": { "culpa_b92": "<string>", "enim_24f": "<string>", "mollit_aa": "<string>" }, "message": "<string>" }, "status": "<string>" }`. Если `200` — пустой массив `[]` |

---

### TC-GET-SELLER-06: Получение объявлений с несуществующим sellerID

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1/999999999/item` | Статус ответа `200 OK` (пустой массив) или `404 Not Found` (уточнить у аналитика — баг в документации) |
| 3 | Проверить тело ответа | Если `200 OK` — пустой массив `[]`. Если `404` — JSON-схема: `{ "result": "laborum", "status": "cillum enim eiusmod" }` |

---

### TC-GET-SELLER-07: Получение объявлений с пустым sellerID

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Установить заголовок `Accept: application/json` | Заголовок установлен |
| 2 | Отправить GET запрос на `https://qa-internship.avito.com/api/1//item` | Статус ответа `404 Not Found` |
| 3 | Проверить тело ответа | Тело ответа соответствует JSON-схеме: `{ "result": "laborum", "status": "cillum enim eiusmod" }` |
