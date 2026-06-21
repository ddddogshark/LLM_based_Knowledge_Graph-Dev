# Contributing

Thank you for your interest in contributing to the LLM-based Knowledge Graph Builder!

## Getting Started

1. Fork the repository and clone your fork.
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
3. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

- **Code style**: Run `ruff check src/` before submitting.
- **Type hints**: Use type annotations on all public functions.
- **Logging**: Use `src.config.get_logger(__name__)` in all modules; avoid `print()` in library code.
- **Tests**: Add or update tests for new functionality. Run `pytest tests/` to verify.

## Pull Request Process

1. Ensure tests pass and your code follows the project conventions.
2. Update documentation if your changes affect public APIs.
3. Describe what your PR does and why in the description.

## Reporting Issues

When filing an issue, please include:
- Python version (`python --version`)
- Steps to reproduce
- Expected vs actual behavior
- Relevant error messages or logs
