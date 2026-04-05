import requests
import pytest
import time

BASE_URL = "https://qa-internship.avito.com"


class TestAvitoAPI:

    # Проверка всех обязательных полей
    def validate_full_item_response(self, data, expected_seller_id, expected_name, expected_price, expected_stats):
        assert "id" in data, "Отсутствует поле id"
        assert "sellerId" in data, "Отсутствует поле sellerId"
        assert "name" in data, "Отсутствует поле name"
        assert "price" in data, "Отсутствует поле price"
        assert "statistics" in data, "Отсутствует поле statistics"
        assert "createdAt" in data, "Отсутствует поле createdAt"


        assert isinstance(data["id"], str), "id должен быть строкой"
        assert len(data["id"]) > 0, "id не может быть пустым"

        assert data["sellerId"] == expected_seller_id, f"sellerId должен быть {expected_seller_id}"
        assert isinstance(data["sellerId"], int), "sellerId должен быть целым числом"

        assert data["name"] == expected_name, f"name должен быть '{expected_name}'"
        assert isinstance(data["name"], str), "name должен быть строкой"

        assert data["price"] == expected_price, f"price должен быть {expected_price}"
        assert isinstance(data["price"], int), "price должен быть целым числом"


        assert "likes" in data["statistics"], "Отсутствует поле statistics.likes"
        assert "viewCount" in data["statistics"], "Отсутствует поле statistics.viewCount"
        assert "contacts" in data["statistics"], "Отсутствует поле statistics.contacts"

        assert data["statistics"]["likes"] == expected_stats["likes"]
        assert isinstance(data["statistics"]["likes"], int)

        assert data["statistics"]["viewCount"] == expected_stats["viewCount"]
        assert isinstance(data["statistics"]["viewCount"], int)

        assert data["statistics"]["contacts"] == expected_stats["contacts"]
        assert isinstance(data["statistics"]["contacts"], int)


        assert isinstance(data["createdAt"], str), "createdAt должен быть строкой"
        assert len(data["createdAt"]) > 0, "createdAt не может быть пустым"

        return True

    # POST /api/1/item - Создание объявления

    # TC-POST-01: Создание объявления с валидными данными
    def test_tc_post_01_create_item_success(self):
        payload = {
            "sellerID": 555555,
            "name": "Ноутбук",
            "price": 150000,
            "statistics": {"likes": 10, "viewCount": 10, "contacts": 10}
        }

        response = requests.post(f"{BASE_URL}/api/1/item", json=payload)

        assert response.status_code == 200
        data = response.json()

        self.validate_full_item_response(
            data,
            expected_seller_id=555555,
            expected_name="Ноутбук",
            expected_price=150000,
            expected_stats={"likes": 10, "viewCount": 10, "contacts": 10}
        )

    # TC-POST-08: цена = 0 -> 200 OK
    def test_tc_post_08_create_item_price_zero(self):

        payload = {
            "sellerID": 555555,
            "name": "Бесплатно",
            "price": 0,
            "statistics": {"likes": 10, "viewCount": 10, "contacts": 10}
        }

        response = requests.post(f"{BASE_URL}/api/1/item", json=payload)

        assert response.status_code == 200
        data = response.json()

        self.validate_full_item_response(
            data,
            expected_seller_id=555555,
            expected_name="Бесплатно",
            expected_price=0,
            expected_stats={"likes": 5, "viewCount": 5, "contacts": 5}
        )

    # GET /api/1/item/{id} - Получение объявления по ID

    # TC-GET-ITEM-01: Получение существующего объявления по ID
    def test_tc_get_item_01_get_existing_item(self):
        create_payload = {
            "sellerID": 555555,
            "name": "Телефон",
            "price": 50000,
            "statistics": {"likes": 5, "viewCount": 20, "contacts": 3}
        }
        create_response = requests.post(f"{BASE_URL}/api/1/item", json=create_payload)
        assert create_response.status_code == 200
        created_item = create_response.json()
        item_id = created_item["id"]

        response = requests.get(f"{BASE_URL}/api/1/item/{item_id}")

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data, list), "Ответ должен быть массивом"
        assert len(data) == 1, "Массив должен содержать 1 элемент"

        item = data[0]
        assert item["id"] == item_id, f"id должен быть {item_id}"
        assert item["sellerId"] == create_payload["sellerID"]
        assert item["name"] == create_payload["name"]
        assert item["price"] == create_payload["price"]
        assert item["statistics"]["likes"] == create_payload["statistics"]["likes"]
        assert item["statistics"]["viewCount"] == create_payload["statistics"]["viewCount"]
        assert item["statistics"]["contacts"] == create_payload["statistics"]["contacts"]
        assert "createdAt" in item
        assert isinstance(item["createdAt"], str)
        item2 = data[1]
        assert item2["id"] == item_id, f"id должен быть {item_id}"
        assert item2["sellerId"] == create_payload["sellerID"]
        assert item2["name"] == create_payload["name"]
        assert item2["price"] == create_payload["price"]
        assert item2["statistics"]["likes"] == create_payload["statistics"]["likes"]
        assert item2["statistics"]["viewCount"] == create_payload["statistics"]["viewCount"]
        assert item2["statistics"]["contacts"] == create_payload["statistics"]["contacts"]
        assert "createdAt" in item2
        assert isinstance(item2["createdAt"], str)

    # GET /api/1/statistic/{id} - Получение статистики

    # TC-GET-STAT-01: Получение статистики существующего объявления
    def test_tc_get_stat_01_get_statistics_existing_item(self):
        create_payload = {
            "sellerID": 555555,
            "name": "Статистика",
            "price": 1000,
            "statistics": {"likes": 10, "viewCount": 10, "contacts": 10}
        }
        create_response = requests.post(f"{BASE_URL}/api/1/item", json=create_payload)
        assert create_response.status_code == 200
        item_id = create_response.json()["id"]

        response = requests.get(f"{BASE_URL}/api/1/statistic/{item_id}")

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data, list), "Ответ должен быть массивом"
        assert len(data) > 0, "Массив не должен быть пустым"

        stats = data[0]
        assert "likes" in stats, "Отсутствует поле likes"
        assert "viewCount" in stats, "Отсутствует поле viewCount"
        assert "contacts" in stats, "Отсутствует поле contacts"

        assert isinstance(stats["likes"], int), "likes должен быть целым числом"
        assert isinstance(stats["viewCount"], int), "viewCount должен быть целым числом"
        assert isinstance(stats["contacts"], int), "contacts должен быть целым числом"

        assert stats["likes"] == 10, "likes не совпадает с отправленным"
        assert stats["viewCount"] == 10, "viewCount не совпадает с отправленным"
        assert stats["contacts"] == 10, "contacts не совпадает с отправленным"

        stats1 = data[1]
        assert "likes" in stats1, "Отсутствует поле likes"
        assert "viewCount" in stats1, "Отсутствует поле viewCount"
        assert "contacts" in stats1, "Отсутствует поле contacts"

        assert isinstance(stats1["likes"], int), "likes должен быть целым числом"
        assert isinstance(stats1["viewCount"], int), "viewCount должен быть целым числом"
        assert isinstance(stats1["contacts"], int), "contacts должен быть целым числом"

        assert stats1["likes"] == 10, "likes не совпадает с отправленным"
        assert stats1["viewCount"] == 10, "viewCount не совпадает с отправленным"
        assert stats1["contacts"] == 10, "contacts не совпадает с отправленным"

    # GET /api/1/{sellerID}/item - Получение объявлений по sellerID

    # TC-GET-SELLER-01: Получение объявлений существующего продавца
    def test_tc_get_seller_01_get_items_existing_seller(self):
        seller_id = 777777

        items_created = []
        for i in range(2):
            payload = {
                "sellerID": seller_id,
                "name": f"Товар {i + 1}",
                "price": 1000 * (i + 1),
                "statistics": {"likes": i, "viewCount": i * 10, "contacts": i}
            }
            response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
            assert response.status_code == 200
            items_created.append(response.json())

        response = requests.get(f"{BASE_URL}/api/1/{seller_id}/item")

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data, list), "Ответ должен быть массивом"
        assert len(data) >= 2, "Должно быть минимум 2 объявления"

        for item in data:
            assert "id" in item
            assert "sellerId" in item
            assert "name" in item
            assert "price" in item
            assert "statistics" in item
            assert "createdAt" in item
            assert "likes" in item["statistics"]
            assert "viewCount" in item["statistics"]
            assert "contacts" in item["statistics"]
            assert item["sellerId"] == seller_id, f"sellerId должен быть {seller_id}"

    # Идемпотентность

    # TC-IDEMP-01: Повторное создание объявления с такими же данными
    def test_tc_idemp_01_duplicate_creation(self):
        payload = {
            "sellerID": 555555,
            "name": "Дубликат",
            "price": 5000,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}
        }

        response1 = requests.post(f"{BASE_URL}/api/1/item", json=payload)
        assert response1.status_code == 200
        item1 = response1.json()

        response2 = requests.post(f"{BASE_URL}/api/1/item", json=payload)
        assert response2.status_code == 200
        item2 = response2.json()

        assert item1["id"] != item2["id"], "ID должны быть разными при повторном создании"

        assert item1["sellerId"] == item2["sellerId"]
        assert item1["name"] == item2["name"]
        assert item1["price"] == item2["price"]
        assert item1["statistics"] == item2["statistics"]

    # Нефункциональные проверки

    # TC-NF-01: Время ответа GET /api/1/item/{id} не превышает 500 мс
    def test_tc_nf_01_get_item_response_time(self):
        payload = {
            "sellerID": 555555,
            "name": "Тест скорости",
            "price": 1000,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}
        }
        create_response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
        item_id = create_response.json()["id"]

        start_time = time.time()
        response = requests.get(f"{BASE_URL}/api/1/item/{item_id}")
        end_time = time.time()

        response_time_ms = (end_time - start_time) * 1000

        assert response.status_code == 200
        assert response_time_ms < 500, f"Время ответа {response_time_ms}ms превышает 500ms"

    # TC-NF-03: Время ответа POST /api/1/item не превышает 1000 мс
    def test_tc_nf_03_post_item_response_time(self):


        payload = {
            "sellerID": 555555,
            "name": "Тест скорости POST",
            "price": 2000,
            "statistics": {"likes": 2, "viewCount": 2, "contacts": 2}
        }

        start_time = time.time()
        response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
        end_time = time.time()

        response_time_ms = (end_time - start_time) * 1000

        assert response.status_code == 200
        assert response_time_ms < 1000, f"Время ответа {response_time_ms}ms превышает 1000ms"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])