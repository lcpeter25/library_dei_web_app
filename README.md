# library_dei_web_app

Library DEI Web Application

Diversity Dashboard

Description
The purpose of this web application is to provide a database with the data from the Seabury Academic Library's diversity, equity, and inclusion audit. This application organizes, stores, and makes searchable the DEI data for users of the library. In addition, the application allows future employees of the library to input more DEI data into the database through the admin panel.

Data
The original data which with the database was built were created by Kaitlin Roberts and Laura Petersen, 2022 summer interns of the library. For each book, these data included: title, author (name, race, gender, and additional identities), characters (race and additional identities), and genre. Only books from the young adult ficiton section of the library were recorded at this time.

Technologies
Python
Django
SQLite3

How to Use the Diversity Dashboard
Admin
Adding a Book:

Use the frontend/user side to search for the author to see if the author is in the database already.
If the author exists, skip to step 5.
If the author does not exist yet, click the add button with the green plus next to “Authors”
Use the text fields, menus, and check boxes to add the requested information (up until the Books options). If an option isn’t available (e.g. the author’s race isn’t listed), you can add the option by clicking the green plus.
Next to the “Books” options, click the green plus to add a new book.
A new window will appear to enter the details of the book.
Use the text fields, menus, and check boxes to add the requested information (up until the Characters options). TITLES should be written in all caps. If an option isn’t available (e.g. the book’s genre isn’t listed), you can add the option by clicking the green plus.
Next to the “Characters” options, click the green plus to add a new character set.
A new window will appear to enter information about the main characters in that book. Make sure you enter the title the same as you did on the book window, in ALL CAPS. ENTER ZERO (0) when appropriate, do not leave these fields blank (Notes may be left blank).
Hit Save on the Characters window and Book window. Use the green plus to add additional books to the author if necessary. When done, click Save in the Author window as well.
Go back to the main admin page.
Click the Add button next to “Char gender conns” which stands for Character-Gender Connections.
For each gender of main characters present in the book, add the quantity, gender, and connect this to the character set you just created. The character set will be named “From TITLE” and, if you just created it, will be at the very bottom of the list.
Example workflow for a book with 2 male and 1 other gender characters. Click Add button next to “Char gender conns” Under Quantity, select 2 Under Gender, select “male” Under Character set, scroll all the way to the bottom and select “From CURRENT BOOK” Click Save and add another Under Quantity, select 1 Under Gender, select “other” Under Character set, scroll all the way to the bottom and select “From CURRENT BOOK” Click Save

Click the Add button next to “Char race conns” which stands for Character-Race Connections.
For each race of main characters present in the book, add the quantity, race, and connect this to the character set you just created. The character set will be named “From TITLE” and, if you just created it, will be at the very bottom of the list. (If the character’s race is unknown, indicate this using the ‘unknown’ option. You may add additional races using the small green plus.) Workflow is similar to adding the genders of characters.
You’ve added a new book! Check that it appears in the frontend/user side database.
Editing and deleting should be pretty straightforward with the Django admin panel. However, you must delete Authors, Books, and Characters independently.

Users

Pages: Home

Displays the number of total authors, total book, and the percent of authors who have a marginalized identity.
Displays a selection of 15 authors and 15 books with options for more information and to see all authors or books
Authors

Displays all authors with some information about each
Provides the ability to search for authors by name or identities
“More Information” buttons take the user to an Author Information page
Author Information

Provides information about the selected author, including number of books
Displays table of the author’s books with selected information
Allows user to search for a specific type of book within the author’s books
Books

Displays all books with some information about each
Provides the ability to search for books by title or attributes
“More Information” buttons take the user to an Book Information page
Book Information

Displays information on the book, character(s) within that book, and the author(s) of the book
Suggestions for the Future

Add in character genders
Add search-by-characters functionality
