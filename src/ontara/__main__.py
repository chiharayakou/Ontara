"""Точка входа для запуска Ontara."""

from ontara import __version__

def main() -> None:
    """Вывести приветствие и версию программы"""
    print(f"Ontara {__version__}")
    print("Environment for creating and simulating fictional worlds.")

if __name__ == "__main__":
    main()