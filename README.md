
# 🧱 Clean Architecture Shop Backend

This repository contains a refactored backend system for a simple shop, implemented according to the **Clean Architecture** principles.

---

## 📦 Modules

### `be_task_ca/user_clean`
- `domain`: Pure business entities (`User`, `CartItem`) and interfaces.
- `usecases`: Business logic like `create_user`, `add_item_to_cart`, `list_cart_items`.
- `infrastructure`: In-memory repository implementations.
- `interface`: FastAPI route definitions.

### `be_task_ca/item_clean`
- `domain`: Entity `Item` and its repository interface.
- `usecases`: Logic to `get_item_by_id`, `list_all_items`.
- `infrastructure`: In-memory item repository.
- `interface`: FastAPI routes for product data.

---

## 🚀 How to Run

1. Install dependencies:

```bash
poetry install
```

2. Launch FastAPI:

```bash
poetry run uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests

```bash
pytest tests/user/test_usecases.py
```

Tests cover:
- User creation
- Cart item handling

---

## ✅ Features

- Pure Python domain logic (no framework dependencies)
- Use cases decoupled from delivery and infrastructure
- In-memory repositories for fast testing and prototyping
- Easily extendable to support SQL or external APIs
