# MoneyManager

Simple CLI-based app to manage your expenses and income.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Install](#install)
- [Usage](#usage)
- [With uv](#with-uv)
    - [Usage](#usage-1)
    - [Testing](#testing)
- [Features](#features)
- [Contributors](#contributors)
- [License](#license)

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.12 or later
- [Git](https://git-scm.com/downloads)
- Optional: [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

## Install

1. Clone this repository from GitHub

    ```sh
    git clone https://github.com/FAZuH/MoneyManager.git
    ```

2. Download application dependencies

    ```sh
    cd MoneyManager  # Change working directory into where you installed MoneyManagerr

    python -m venv .venv

    # On Windows
    .\venv\Scripts\activate.bat

    # On Unix or MacOS
    source .venv/bin/activate

    pip install .
    ```

## Usage

1. Activate python virtual environment

   - On Windows:

   ```sh
   .venv\Scripts\activate.bat
   ```

   - On Unix or MacOS:

   ```sh
   source .venv/bin/activate
   ```

2. Run the application

    ```sh
    python -m moneymanager
    ```

## With uv

### Usage

1. Open a terminal in the project root directory
2. Run `uv run moneymanager`

### Testing

1. Open a terminal in the project root directory
2. Run `uv run pytest`

## Features

## Contributors

![Contributors](https://contrib.rocks/image?repo=FAZuH/MoneyManager)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

