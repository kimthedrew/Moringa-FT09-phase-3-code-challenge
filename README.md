
# Magazine Management System

## Overview

The Magazine Management System is a simple Python application designed to manage a database of authors, magazines, and articles. It allows you to:

Create and manage authors.

Create and manage magazines.

Create and manage articles linked to specific authors and magazines.

This project uses SQLite3 for database management and follows an Object-Oriented Programming (OOP) approach for organizing the models.


## Usage

Running the Application

Run the main application script:

```python app.py```

The application will prompt you to input details for creating an author, magazine, and article. It will save the data into the database and display all entries.


## Features

### Models

Author

Represents an author with attributes like id and name.

Magazine

Represents a magazine with attributes like id, name, and category.

Article

Represents an article with attributes like id, title, content, author_id, and magazine_id.

Database

SQLite3 database with the following tables:

authors

magazines

articles

Connection handled through database/connection.py.

Testing

Unit tests are implemented in tests/test_models.py to verify model behaviors.

How It Works

Creating Entries

The app.py script collects user input and inserts it into the respective database tables.

Object-Relational Mapping

Models like Article, Author, and Magazine map Python objects to database records.

Data Validation

Model attributes are validated using custom setters (e.g., ensuring category is a non-empty string).

Testing

Test cases validate object initialization and behavior.

Example Workflow

Input the following when prompted by the application:
```
Author's name: John Doe

Magazine name: Tech Today

Magazine category: Technology
```
Article title: The Rise of AI

Article content: AI is transforming industries worldwide.

The application will:

Save the data to the SQLite database.

Display all authors, magazines, and articles.

Contributing


License

This project is licensed under the MIT License.

