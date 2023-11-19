# Introduction to Unit Testing

In this repository, I introduce myself to unit testing using Pytest. Test Driven Development is useful because:

1. It helps us fix bugs before they are even detected.
2. It serves as documentation.

To get started:

1. Clone this repository.
2. Navigate to the cloned repository and run `pipenv install && pipenv shell` to set up your virtual environment and install the project's dependencies.
3. To run the migrations, navigate to the `server` directory and run `flask db upgrade`, followed by `python seed.py`
4. To begin running the tests, run `pytest -x`

## Technologies Used

* Python v 3.9.12

Author: Joel Nyongesa