# add_book.py
import mysql.connector  # Make sure to import mysql.connector

from test_connection import create_connection  # Import the connection function

def add_book_to_db(title, author, year_published, genre, available_copies):
    connection = create_connection()  # Call the function to get the connection
    if connection:
        try:
            cursor = connection.cursor()  # Create the cursor here

            # Insert new book
            insert_query = """
            INSERT INTO books (title, author, year_published, genre, available_copies)
            VALUES (%s, %s, %s, %s, %s)
            """
            book_data = (title, author, year_published, genre, available_copies)
            cursor.execute(insert_query, book_data)

            connection.commit()
            print("Book added successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection

if __name__ == "__main__":
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year_published = int(input("Enter the year of publication: "))
    genre = input("Enter the genre: ")
    available_copies = int(input("Enter the number of available copies: "))

    add_book_to_db(title, author, year_published, genre, available_copies)
