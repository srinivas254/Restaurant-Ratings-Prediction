# Restaurant Ratings Prediction

This project utilizes the Zomato dataset from Kaggle to perform data preprocessing, exploratory data analysis (EDA), and predictive modeling. 
The main objective is to analyze restaurant data and build a predictive model to forecast outcomes based on various features.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Training](#model-training)
- [API Development](#api-development)
- [Front-End Implementation](#front-end-implementation)
- [How to Run the Project](#how-to-run-the-project)
- [License](#license)

## Technologies Used

- **Python Libraries**:
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
- **Flask** for the web server
- **HTML, CSS, and JavaScript** for the front end

## Data Preprocessing

The dataset was cleaned and preprocessed to handle missing values, normalize features, and prepare it for analysis.

## Exploratory Data Analysis

Performed EDA to uncover insights and patterns within the data using visualization libraries such as Matplotlib and Seaborn.

## Model Training

Trained multiple models to predict outcomes using:
- Linear Regression
- Random Forest
- Extra Trees Regressor (chosen for its high accuracy of 93%)

The model was saved using Pickle for later use.

## API Development

Developed a REST API using Flask:
- **GET** method at `/` to check the server status.
- **POST** method at `/predict` to receive input data and return predictions.

## Front-End Implementation

The front end was created using HTML, CSS, and JavaScript, featuring a responsive design to enhance user experience.

## How to Run the Project

1. Clone the repository:
   ```bash
   
   git clone <https://github.com/srinivas254/Restaurant-Ratings-Prediction>

2. Navigate to the project directory:
   ```bash
   
   cd C:\Users\AZhar ALi\Downloads\Restaurant Ratings Prediction

4. Install the required packages:
   ```bash

   pip install -r requirements.txt

6. Run the Flask application:
   ```bash

   python app.py

8. Access the application in your web browser:

   a. For the GET method (to check server status):
   ```bash
        http://127.0.0.1:5000/
    
  b. For the POST method (to make predictions):
  ```bash
      http://127.0.0.1:5000/predict


License

This project is licensed under the MIT License. See the LICENSE file for more details.


### Instructions to Customize

- Replace `<https://github.com/srinivas254/Restaurant-Ratings-Prediction>` with the actual URL of your GitHub repository.
- You may want to add sections for installation instructions, usage examples, or additional details specific to your project.

Feel free to adjust any section to better fit your project! If you need more help, just let me know!
   
