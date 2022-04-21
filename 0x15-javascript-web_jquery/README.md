# JavaScript - Web jQuery
In this project I will be learning how to use jQuery to the following:
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a GET request with JQuery Ajax
- How to make a POST request with JQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events
## Importing JQuery
<head>
	<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

## Tasks:
* **0. No JQuery**
[0-script.js](./0-script.js): Updates the text color of the <header> element to red (#FF0000):
* Use document.querySelector to select the HTML tag
* No using the JQuery API
* **1. With JQuery**
[1-script.js](./1-script.js): Updates the text color of the <header> element to red (#FF0000):
* No Using the document.querySelector to select the HTML tag
* Use the JQuery API
* **2. Click and turn red**
[2-script.js](./2-script.js): Updates the text color of the <header> element to red (#FF0000) when the user clicks the tag **DIV#red\_header**:
* No using the document.querySelector to select the HTML tag
* Use the JQuery API
* **3. Add `.red` class**
[3-script.js](./3-script.js): Adds the class red to the <header> element when the user clicks the tag **DIV#red\_header**:
* No using the document.querySelector to select the HTML tag
* Use the JQuery API
* **4. Toggle classes**
[4-script.js](./4-script.js): Toggles the class of the <header> element when the user clicks the tag **DIV#toggle_header**:
* the <header> element must always have one class: *red* or *green*
* No using the document.querySelector to select the HTML tag
* Use the JQuery API
* **5. List of elements**
[5-script.js](./5-script.js): Adds a <li> element to a list when the user clicks on the tag DIV#add_item:
* The new element must be :<li>Item</li>
* The new element must be added to UL.my_list
* No using the document.querySelector to select the HTML tag
* Use the JQuery API

* **6. Change the text**
[6-script.js](./6-script.js): updates the text of the <header> element to **New Header!!!** when the user clicks on DIV#update_header.

* **7. Star wars character**
[7-script.js](./7-script.js): Fetches the character _name_ from the URL: **https://swapi-api.hbtn.io/api/people/5/?format=json**.

* **8. Star Wars movies**
[8-script.js](./8-script.js): Fetches the _title_ for all movies by using the URL: **https://swapi-api.hbtn.io/api/films/?format=json**.

* **9. Say Hello!**
[9-script.js](./9-script.js):  Fetches from **https://fourtonfish.com/hellosalut/?lang=fr** and displays the value of hello from that fetch in the HTML tag DIV#hello.
* The translation of “hello” must be displayed in the HTML tag DIV#hello
* Don’t use document.querySelector to select the HTML tag
* Use the JQuery API
* The script must work when it is imported from the \<head\> tag

* **10. No jQuery - document loaded!**
[10-script.js](./10-script.js): updates the text color of the <header> element to red (#FF0000):
* Use the document.querySelector to select the HTML tag
* The script must be imported from the \<head\> tag, not at the end of the HTML

* **11. List, add, remove**
[11-script.js](./11-script.js):  adds, removes and clears LI elements from a list when the user clicks:
* The new element must be: <li>Item</li>
* The new element must be added to UL.my_list
* When the user clicks on DIV#add_item: a new element is added to the list
* When the user clicks on DIV#remove_item: the last element is removed from the list
* When the user clicks on DIV#clear_list: all elements of the list are removed
* You can’t use document.querySelector to select the HTML tag
* You must use the JQuery API
* You script must work when it imported from the HEAD tag

* **12. Say Hello to everybody!**
[12-script.js](./12-script.js): fetches and prints how to say “Hello” depending on the language
* use this API service: https://www.fourtonfish.com/hellosalut/hello/
* The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
* The translation must be fetched when the user clicks on INPUT#btn_translate
* The translation of “Hello” must be displayed in the HTML tag DIV#hello
* Use the JQuery API
* The script must work when imported from the \<head\> tag

* **13. And press ENTER**
[13-script.js](./13-script.js): fetches and prints how to say “Hello” depending on the language
* Use this API service: https://www.fourtonfish.com/hellosalut/hello/
* The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
* The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
* The translation of “Hello” must be displayed in the HTML tag DIV#hello
* use the JQuery API
* The script must work when imported from the <head> tag
