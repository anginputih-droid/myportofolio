# Portofolio PBD

**Name: Angin Putih Ranulaksmi Tsurayya Hapsoro
NPM: 2506557936
Class: KKI**


## Setup Instructions
1. Clone the repository:
git clone https://github.com/anginputih-droid/myportofolio.git

2. Navigate to the project directory:
cd myportofolio

3. Create a virtual environment:
python -m venv env

4. Activate the virtual environment:
env\Scripts\activate

5. Install dependencies:
pip install -r requirements.txt

6. Run the server:
python manage.py runserver

7. Access the local host:
http://127.0.0.1:3000/


## Weekly Progress
### Week 1: Static Web with HTML5 and CSS3
- Setting up the base Django project and framework following the tutorial.
- Built the fundamental HTML5 structure, utilizing semantic tags like '<section>' and '<article>'.
- Implemented custom CSS3 styling, including Flexbox and CSS Grid, to ensure the page is fully responsive for both desktop and mobile.
- Added hover animation and dropdown.
- Added other datas for my personal info.

### Week 2: Implementing Model-View-Template (MVT) in Django


### Week 3: Form & Data Delivery
- Refactored all my HTML files to inherit from the `base.html` skeleton template for shared elements like the navbar.
- Built a Django `ModelForm` to easily add and update my portfolio.
- Implemented a secure delete function protected by a confirmation modal.
- Create a JSON endpoint to serve serialized my data instead of rendering raw HTML.

### Assignment 1
**1. Usage of semantic HTML5 element**
Yes, I used semantic HTML5 tags such as <header>, <main>, <section>, <article>, and <footer> to give my static web page a clear structure. It helped me seperate the distinct areas in my portofolio (profile and technical skills) rather than depending solely on generic <div> wrappers for everything. Using <article> tags for individual items keeps each piece of content organized on its own, making the code much easier to read and update. Plus, these tags make the code cleaner and help screen readers and search engines understand the page better.

**2. Layout challenges in setting up CSS Responsive**


### Assignment 2
**1. Explain what happens when a user opens the new portofolio page, starting from the request received by the project until the data appears in the browser:**
When a user requests the new portofolio page, like the projects URL, their browser sends a HTTP request to the server. The project's `urls.py` receives it and redirects it to the app's `urls.py`, which finds the exact URL match and routes the request to a specific view.

The view acts as the central control hub. To gather any necessary background data, like options for a dropdown menu, it asks the model, which is the interface for the database.

The view then passes this data and an empty portfolio form to the template. The template acts as an HTML blueprint, visually structuring the raw data into a complete web page. Finally, the view wraps this finished HTML into an HTTP response and sends it back to the user's browser, where the page is displayed.

**2. Why should the data for the new portfolio section be stored in a model instead of being written directly in the template?**
It really all comes down to keeping the application dynamic by separating the raw content from the presentation layer. If I were to hardcode everything directly into the HTML template, adding a new project means opening the code editor, copying a block of markup, risking a missing closing tag that breaks the visual layout, and pushing a whole new Git commit. By storing data in a database model instead, the HTML acts as a dumb, reusable skeleton, which makes maintenance completely effortless. Down the line, I can just log into a backend admin panel and fill out a form to update the database directly, and the live site updates automatically without anyone ever needing to rewrite or redeploy the raw code.

**3. What is the difference between makemigrations and migrate in Django?**
- The makemigrations command inspects any changes made to my Django models and generates a migration file, which acts as a blueprint or a set of instructions for updating the database schema. In contrast, the migrate command takes those generated instructions and executes the necessary SQL commands to physically apply the structural changes to my database.

- For example, if you add a new status field to an existing Project model, you must first run makemigrations to create the instructions for the new column, and then run migrate to actually insert that column into the database table.


**AI Usage Disclosure:** I used Gemini to help me understand, check if what I am doing is right or not, and check if there is any error.

- Prompt Strategy: I asked Gemini to kinda tell me what to do on the assignment at first, even though i know i just need to follow the tutorial 2 but change a few small things to fit the new section I'm adding. I still asked to make sure i wasn't wrong. I also ask AI to check if my code is right and doesn't have any errors a few times.

- AI Chat Log: https://share.gemini.google/jkWGEbCDJspv


### Assignment 3
**1. Explain why we use Django’s ModelForm instead of creating HTML forms manually. Additionally, explain why we are required to add `{% csrf_token %}` to these forms!**
Using Django's `ModelForm` saves us a lot of time because it builds the form fields directly from the database models we already set up. Instead of typing out all the standard HTML code and checking for errors ourselves, Django handles the heavy lifting in the background. We have to add `{% csrf_token %}` to protect against CSRF (Cross-Site Request Forgery) attacks. Think of this token as a secret password, it proves that the form being submitted is actually coming from our own website, keeping out hackers who might try to send fake, harmful requests.

**2. In Tutorial 03, we discussed JSON and XML data formats. Why is JSON preferred in modern web application development compared to XML?**
JSON is usually preferred because it's smaller in file size and much easier to read. XML uses bulky opening and closing tags for every single piece of information, which makes it cluttered. JSON just pairs a name with a value (for example: "name": "Ranu"). This setup matches exactly how JavaScript handles data. Since modern websites rely heavily on JavaScript for what the user sees, JSON is much faster and simpler for the browser to process.

**3. Explain the flow that occurs when you use a view function to return your portfolio data in JSON format. Why do we need to perform the serialization process on Django models before returning the data?**
When a user's browser asks for the JSON data, the view function receives that request and asks the database for the right information (like all my projects). However, the database gives us Python objects, and we can't send complex Python code directly over the internet. That's where "serialization" comes in, it translates those Python objects into a simple, standard text format (JSON) that can travel safely across the web. Once translated, the view packages this text up and sends it back to the browser, which can easily understand and display it.

**AI Usage Disclosure:** I barely used AI for this assignment, because I'm starting to understand the Django MVT flow.

- **Prompt Strategy:** I only used AI to help me if I have an error and I don't know how to fix it.
- **Limitations & Manual Fixes:** I manually handled writing the `ModelForm`, creating the CRUD views, implementing the JSON, and refactoring all of my HTML files to extend the `base.html` skeleton.
- **AI Chat Log:** https://share.gemini.google/9VCgGlcNE5OM