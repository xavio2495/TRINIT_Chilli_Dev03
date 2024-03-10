<p align="center">
  <img width="650" height="600" src="design/euclid logo.png">
</p>

<h1 style="text-align: center;font-family:Times;font-size:45px;color:gold">EUCLID</h1>
This application allows educators and instructors to create customized question papers by curating questions from user submissions and generating papers based on difficulty levels. 

### Features

* **User-Submitted Questions:** Users can contribute questions to a central database, allowing for a diverse range of content.
* **Difficulty Levels:**  Specify the desired difficulty level (easy, medium, hard) for each question.
* **Paper Generation:** Generate question papers with questions selected based on difficulty and user-defined criteria (number of questions, topics covered).
* **(Optional) Question Ranking:** Implement a system (voting, scoring) for users to rank the quality of submitted questions (future development).

### App Demo
Google Drive Link: [EUCLID APP DEMO](https://tinyurl.com/euclid-app)

### Design & Frontend
![main page](<design/index page.png>)
![upload page](<design/upload page.png>)
![explore page](<design/explore page.png>)

### Installation

**Prerequisites:**

* Python 3 [https://www.python.org/downloads/](https://www.python.org/downloads/)

**Steps:**

1. Clone this repository:

```bash
git clone https://github.com/xavio2945/TRINIT_Chilli_Dev03.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python test_generator.py
```

### Usage

1. **Start the application:** Follow the installation steps to run the application.
<br>**Warning**: The application is split into different parts, where each .py file performs a specific task.*
2. **PDF and Image converter:** In order to convert the user's PDF or Image, the application uses Meta Nougat, a  (Neural Optical Understanding for Academic Documents), a Visual Transformer model that performs an Optical Character Recognition (OCR) task for processing scientific documents into a markup language. Run `ocr_converter.py` *(Needs a GPU to run)* to execute it.
3. **Question Submission:** Users are allowed to upload files to main database and define what subject and chapter it comes under. the In order to subumit questions to the local csv file, run the `qb_input.py` file.
4. **Paper Generation:** Based on the defined criteria, the application generates a question paper selecting questions from the database. The paper will be exported as a file (PDF). To use this function run the `test_generator.py` file.


### Contribution

We welcome contributions to this project! Feel free to:

* Submit bug reports or feature requests through GitHub issues.
* Fork the repository, make your changes, and create a pull request for review.
* Improve the documentation or add new features based on your needs.

### License

This project is licensed under the MIT License (see LICENSE file for details).
