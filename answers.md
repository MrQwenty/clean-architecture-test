
# ✅ Clean Architecture Task – Answers

## 1. Why can we not easily split this project into two microservices?

Because the original codebase:
- Shares models and logic across features (user/cart/item).
- Lacks clearly separated bounded contexts.
- Has centralized data access (tight SQLAlchemy coupling).
- Uses direct imports without defined service boundaries.

## 2. Why does this project not adhere to Clean Architecture even though we have separate modules for API, repositories, usecases, and model?

- Dependency direction is wrong: use cases depend on infrastructure.
- Models are impure (ORM-based), shared across layers.
- Business logic knows about FastAPI (e.g., HTTP exceptions).
- No use of interfaces/ports between layers.

## 3. What would be your plan to refactor the project to stick to the Clean Architecture?

- Split by **feature**, not by type.
- Use pure entities in `domain/`.
- Declare `Repository` interfaces in domain layer.
- Isolate use cases from infrastructure.
- Implement repositories separately (e.g., `sql_repository`, `memory_repository`).
- Inject dependencies into use cases via interfaces.

## 4. How can you make dependencies between modules more explicit?

- Use Dependency Inversion via interfaces.
- Avoid framework-specific constructs in domain/usecases.
- Leverage constructor/function parameter injection.
- Use static tools (`poetry run graph`, `mypy`) to validate boundaries.

## 🧩 Stretch Goals Completed

| Task                                 | Status |
|--------------------------------------|--------|
| Full Clean Architecture refactor     | ✅     |
| In-memory repositories               | ✅     |
| Test suite for user usecases         | ✅     |
| FastAPI routers for user and item    | ✅     |
| Combined app with main.py            | ✅     |
