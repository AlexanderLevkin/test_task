# test_task project

## Prerequisites
- [Check list for this task](https://docs.google.com/spreadsheets/d/1eZIDDJxqv2zlvOqXj91-A-MvR_4ce08Ym1TJsyxfpI8/edit?usp=sharing)
- [Python 3.8](https://www.python.org/downloads/) or higher installed on your local machine.
- [Git](https://git-scm.com/downloads) installed on your local machine.
- [Allure command-line tool](https://docs.qameta.io/allure/#_installing_a_commandline) installed on your local machine.
- [Poetry package manager](https://python-poetry.org/docs/#installation) installed on your local machine.

## Getting Started

1. Clone this repository to your local machine.

`git clone https://github.com/AlexanderLevkin/test_task`

2. Install the required Python libraries using Poetry.

``` sh
poetry install 
```

``` sh
poetry shell
```

3. Run the tests.

``` sh
pytest -s -v --alluredir=./allure-report
```

4. Open the Allure report in your browser.

``` sh
allure serve ./allure-report
```

## Contributor

- [Levkin.A.A](mailto:levkin.alexan@gmail.com)