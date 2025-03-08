This api branch:

future documentation:

# API Документація

## Огляд
Ця документація містить деталі про API-ендпоінти для реєстрації користувачів, управління талантами, створення проектів і роботи з контрактами. Ендпоінти розроблені для системи маркетплейсу, де користувачі можуть реєструватися, додавати свої таланти, створювати проекти та пов'язувати таланти з проектами через контракти.

---

## Ендпоінти

### 1. Реєстрація користувача
**Ендпоінт:** `/register/`

**Метод:** `POST`

**Опис:** Реєструє нового користувача зі встановленням значення `is_seller` за замовчуванням як `False`.

#### Формат запиту:
```json
{
    "username": "string",
    "password": "string",
    "first_name": "string",
    "last_name": "string",
    "age": "integer",
    "phone_number": "integer"
}
```

#### Формат відповіді:
**201 Created**
```json
{
    "username": "string",
    "first_name": "string",
    "last_name": "string",
    "age": "integer",
    "phone_number": "integer"
}
```
**400 Bad Request** (у разі помилки валідації)
```json
{
    "error": "string"
}
```

---

### 2. Деталі користувача
**Ендпоінт:** `/me/`

**Метод:** `GET`

**Опис:** Повертає інформацію про автентифікованого користувача, включаючи статус `is_seller`.

**Аутентифікація:** Обов'язкова (Token або Session).

#### Формат відповіді:
**200 OK**
```json
{
    "id": "integer",
    "username": "string",
    "first_name": "string",
    "last_name": "string",
    "age": "integer",
    "phone_number": "integer",
    "is_seller": "boolean"
}
```

---

### 3. Додавання таланту
**Ендпоінт:** `/add_talent/`

**Метод:** `POST`

**Опис:** Додає талант для автентифікованого користувача. Автоматично оновлює статус користувача `is_seller` на `True`.

#### Формат запиту:
```json
{
    "user": "integer",
    "position": "string",
    "description": "string",
    "location": "string",
    "talent_dsc": "integer"
}
```

#### Формат відповіді:
**201 Created**
```json
{
    "id": "integer",
    "user": "integer",
    "position": "string",
    "description": "string",
    "location": "string",
    "talent_dsc": "integer"
}
```
**400 Bad Request** (у разі помилки валідації)
```json
{
    "error": "string"
}
```

---

### 4. Отримання талантів за Talent DSC ID
**Ендпоінт:** `/talent/<int:talent_dsc_id>/`

**Метод:** `GET`

**Опис:** Повертає всі таланти, пов'язані з конкретним `talent_dsc` ID.

#### Формат відповіді:
**200 OK**
```json
[
    {
        "id": "integer",
        "user": "integer",
        "position": "string",
        "description": "string",
        "location": "string",
        "talent_dsc": "integer"
    }
]
```
**404 Not Found** (якщо таланти не знайдені)
```json
{
    "error": "No talents found"
}
```

---

### 5. Створення проекту
**Ендпоінт:** `/create_project/`

**Метод:** `POST`

**Опис:** Створює проект для автентифікованого користувача.

#### Формат запиту:
```json
{
    "title": "string",
    "description": "string",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "status": "boolean",
    "user_id": "integer",
    "location": "string"
}
```

#### Формат відповіді:
**201 Created**
```json
{
    "id": "integer",
    "title": "string",
    "description": "string",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "status": "boolean",
    "user_id": "integer",
    "location": "string",
    "created_at": "YYYY-MM-DDTHH:MM:SS"
}
```
**400 Bad Request** (у разі помилки валідації)
```json
{
    "error": "string"
}
```

---

### 6. Створення контракту
**Ендпоінт:** `/create_contract/`

**Метод:** `POST`

**Опис:** Пов'язує талант і проект через контракт із зазначенням ціни.

#### Формат запиту:
```json
{
    "user_id": "integer",
    "talent_id": "integer",
    "project_id": "integer",
    "price": "decimal"
}
```

#### Формат відповіді:
**201 Created**
```json
{
    "id": "integer",
    "user_id": "integer",
    "talent_id": "integer",
    "project_id": "integer",
    "price": "decimal"
}
```
**400 Bad Request** (у разі помилки валідації)
```json
{
    "error": "string"
}
```

---

### 7. Отримання контракту
**Ендпоінт:** `/contract/<int:contract_id>/`

**Метод:** `GET`

**Опис:** Повертає деталі конкретного контракту.

#### Формат відповіді:
**200 OK**
```json
{
    "id": "integer",
    "user_id": "integer",
    "talent_id": "integer",
    "project_id": "integer",
    "price": "decimal"
}
```
**404 Not Found**
```json
{
    "error": "Contract not found"
}
```

---

### 8. Отримання проекту
**Ендпоінт:** `/project/<int:project_id>/`

**Метод:** `GET`

**Опис:** Повертає деталі конкретного проекту.

#### Формат відповіді:
**200 OK**
```json
{
    "id": "integer",
    "title": "string",
    "description": "string",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "status": "boolean",
    "user_id": "integer",
    "location": "string",
    "created_at": "YYYY-MM-DDTHH:MM:SS"
}
```
**404 Not Found**
```json
{
    "error": "Project not found"
}
```

Тепер можна відправити **POST-запит** на /login/ з JSON:

```
{
  "email": "user@example.com",
  "password": "password123"
}
```
У відповідь отримаєш:

```
{
  "token": "c6b3f5c... (токен користувача)"
}
Цей токен можна використовувати для автентифікації в API.
```
---

## Примітки
1. **Аутентифікація:** Використовуйте токен або сесію для захищених ендпоінтів (наприклад, `/me/`, `/add_talent/`).
2. **Валідація:** Переконайтеся, що всі обов'язкові поля надані в запитах; у разі помилки повертається `400 Bad Request` із повідомленням про помилку.
3. **Формат дат:** Використовуйте формат ISO 8601 (`YYYY-MM-DD`) для всіх полів дати.


