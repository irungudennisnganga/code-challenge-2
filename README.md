# code-challenge-2
# Restaurant Review System

This project implements a simple restaurant review system with three main classes: `Customer`, `Restaurant`, and `Review`. The relationships between these classes represent the core functionality of the system.

## Table of Contents
- [Getting Started](#getting-started)
- [Class Descriptions](#class-descriptions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
- Python 3.10

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/irungudennisnganga/code-challenge-2

   ```
2 on the terminal run the following command
  ``````bash 
    pipenv install
  `````` 
3 To enter the virtual environment     
   ``````bash 
    pipenv shell
  ``````  

Certainly! Below is the README content in Markdown format:

markdown

# Restaurant Review System

This project implements a simple restaurant review system with three main classes: `Customer`, `Restaurant`, and `Review`. The relationships between these classes represent the core functionality of the system.

## Table of Contents
- [Getting Started](#getting-started)
- [Class Descriptions](#class-descriptions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/restaurant-review-system.git
   cd restaurant-review-system

    Install dependencies:

    bash

    pip install -r requirements.txt

#  Class Descriptions
## Customer

    1. Represents a customer who can leave reviews.
    ### Properties:
        -given_name: The given name of the customer.
        -family_name: The family name of the customer.
    ### Methods:
        - full_name(): Returns the full name of the customer.
        - all(): Returns all customer instances.
        - num_reviews(): Returns the total number of reviews authored by the customer.
        - find_by_name(name): Class method to find a customer by their full name.
        - find_all_by_given_name(name): Class method to find all customers with a given name.

## Restaurant

    Represents a restaurant that can be reviewed.
    ### Properties:
        - name: The name of the restaurant.
    ### Methods:
        - reviews(): Returns a list of all reviews for the restaurant.
        - customers(): Returns a unique list of all customers who have reviewed the restaurant.
        - average_star_rating(): Returns the average star rating for the restaurant based on its reviews.

## Review

    Represents a review left by a customer for a restaurant.
    ### Properties:
        - customer: The customer who left the review.
        - restaurant: The restaurant being reviewed.
        - rating: The star rating given in the review.
    ### Methods:
        - customer(): Returns the customer object for the review.
        - restaurant(): Returns the restaurant object for the review.
        - all(): Returns all review instances.
##  🚀 About Me
 * I'm a full stack developer
 * find me [here](https://github.com/irungudenninganga)


## License 
MIT License

Copyright (c) 2023 irungudennisnganga

>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.  

        