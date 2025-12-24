# Pomoplug - A Plug-in Pomodoro Tool for All Your Planning Tools

## Overview

Pomoplug is a versatile Pomodoro timer tool designed to integrate seamlessly with your favorite planning and productivity tools. Built with Django and powered by UV for dependency management, Pomoplug helps you stay focused and productive by breaking your work into manageable intervals.

## Features

- **Pomodoro Timer**: Customizable work and break intervals.
- **Integration-Friendly**: Designed to plug into your existing planning tools.
- **User-Friendly Interface**: Simple and intuitive UI for maximum productivity.
- **Django-Powered**: Robust backend with Django 6.0 and SQLite database.

## Execution Guide

### Prerequisites

- Python 3.13+
- UV (for dependency management)
- Django 6.0

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/pomoplug.git
   cd pomoplug
   ```

2. **Install Dependencies**:
   ```bash
   uv sync
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

### Commands

- **Run Server**: `python manage.py runserver`
- **Run Tests**: `python manage.py test`
- **Run Single Test**: `python manage.py test timer.tests.TestClassName.test_method_name`
- **Create Migrations**: `python manage.py makemigrations`
- **Apply Migrations**: `python manage.py migrate`
- **Create Superuser**: `python manage.py createsuperuser`

## Contributing Guidelines

### Code Style Guidelines

- **Python Version**: 3.13+ (uses UV for dependency management)
- **Framework**: Django 6.0 with SQLite database
- **Imports**: Use absolute imports, standard library first, then third-party, then local
- **Naming**: PascalCase for classes, snake_case for functions/variables
- **Models**: Use UUIDField for primary keys, include `__str__` method
- **Properties**: Use `@property` decorator for computed fields
- **Time Handling**: Use `datetime.now()` and timezone-aware datetime
- **Database**: Custom apps defined in `CUSTOM_APPS` list in settings
- **Project Structure**: Main app in `tomacheck/`, `manage.py` in `tomacheck/tomacheck/`

### How to Contribute

1. **Fork the Repository**:
   Fork the repository to your GitHub account.

2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**:
   - Follow the code style guidelines.
   - Write tests for your changes.
   - Ensure all tests pass.

4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your commit message here"
   ```

5. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   Open a pull request to the main repository with a clear description of your changes.

### Reporting Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. Provide as much detail as possible, including steps to reproduce the issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact the project maintainers at [matheuslemosf@protonmail.com](mailto:matheuslemosf@protonmail.com).
