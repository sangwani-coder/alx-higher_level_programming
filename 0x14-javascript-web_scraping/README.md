# JavaScript - Web scraping
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.

In this project I was involved in practicing file I/O on Node.js and using the NPM request
framework to interact with the [Star Wars](https://swapi.co/),
[JSONplaceholder](https://jsonplaceholder.typicode.com), and

## Tasks :

* **0. Readme**
  * [0-readme.js](./0-readme.js): JavaScript script that reads and prints the
  contents of a file.
  * Usage: `./0-readme.js <file path>`.

* **1. Write me**
  * [1-writeme.js](./1-writeme.js): JavaScript script that writes a string to a
  file.
  * Usage: `./1-writeme.js <file path> <string to write>`.

* **2. Status code**
  * [2-statuscode.js](./2-statuscode.js): JavaScript script that displays the
  stauts code of a `GET` request using the `request` framework.
  * Usage: `./2-statuscode.js <URL to GET>`.
  * Output: `code: <status code>`.

* **3. Star wars movie title**
  * [3-starwars_title.js](./3-starwars_title.js): JavaScript script that uses the
  Star Wars API to print the title of the Star Wars movie with a given integer episode
  number.
  * Usage: `./3-starwars_title.js <3-starwars_title.js>`.

* **4. Star wars Wedge Antilles**
  * [4-starwars_count.js](./4-starwars_count.js): JavaScript script that uses the
  Star Wars API to print the number of movies featuring the character "Wedge Antilles".
  * Usage: `./4-starwars_count.js http://swapi.co/api/films/`.

* **5. Loripsum**
  * [5-request_store.js](./5-request_store.js): JavaScript script that stores the
  contents of a webpage in a file.
  * Usage: `./5-request_store.js <URL to get> <file path to store content in>`.

* **6. How many completed?**
  * [6-completed_tasks.js](./6-completed_tasks.js): JavaScript script that uses the
  JSONPlaceholder API to compute the number of tasks completed per user ID.
  * Usage: `./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`.

* **7. Who was playing in this movie?**
  * [100-starwars_characters.js](./100-starwars_characters.js): JavaScript script
  that uses the Star Wars API to print all characters featured in a given movie.
  * Usage: `./100-starwars_characters.js <movie ID>`.

* **8. Right order**
  * [101-starwars_characters.js](./101-starwars_characters.js): JavaScript script
  that uses the Star Wars API to print all characters featured in a given movie in
  the same order as they are listed in the `characters` list of the `/films/` response.
  * Usage: `./101-starwars_characters.js <movie ID>`.
