# AGENTS.md

## Commands
- **Run server**: `cd tomacheck && python manage.py runserver`
- **Run tests**: `cd tomacheck && python manage.py test`
- **Run single test**: `cd tomacheck && python manage.py test timer.tests.TestClassName.test_method_name`
- **Create migrations**: `cd tomacheck && python manage.py makemigrations`
- **Apply migrations**: `cd tomacheck && python manage.py migrate`
- **Create superuser**: `cd tomacheck && python manage.py createsuperuser`

## Code Style Guidelines
- **Python version**: 3.13+ (uses uv for dependency management)
- **Framework**: Django 6.0 with SQLite database
- **Imports**: Use absolute imports, standard library first, then third-party, then local
- **Naming**: PascalCase for classes, snake_case for functions/variables
- **Models**: Use UUIDField for primary keys, include __str__ method
- **Properties**: Use @property decorator for computed fields
- **Time handling**: Use datetime.now() and timezone-aware datetime
- **Database**: Custom apps defined in CUSTOM_APPS list in settings
- **Project structure**: Main app in tomacheck/, manage.py in tomacheck/tomacheck/