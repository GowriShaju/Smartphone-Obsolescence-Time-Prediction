# Smartphone Obsolescence Time Prediction uisng Machine Learning

This project is a **machine learning system** designed to predict the **obsolescence category of smartphones** based on hardware specifications, software support, and pricing features.

The system is integrated with an **interactive Gradio web interface**, allowing users to input smartphone details and receive real-time predictions.

---

## Project Overview

Smartphones gradually become obsolete due to outdated hardware, reduced software support, and evolving technology standards.  
This project aims to classify smartphones into different **obsolescence categories** using machine learning models.

---

## Obsolescence Categories

The model predicts one of the following categories:

- **Best** – Long lifespan with strong performance and future support  
- **Good** – Good performance with moderate support  
- **Below Average** – Limited lifespan and support  
- **Worst** – Likely to become obsolete soon  

---

## Machine Learning Models Used

The following models were implemented and evaluated:

- Multiple Linear Regression
- Support Vector Machine (SVM) Classifier & Regressor
- Decision Tree Classifier & Regressor
- Random Forest Classifier & Regressor
- K-Nearest Neighbors (KNN)

The **best-performing model was selected and saved** for deployment.

---

## Features Used

The model is trained on multiple smartphone attributes:

- Processor Speed (GHz)
- RAM (GB)
- Storage (GB)
- Battery Capacity (mAh)
- Display Technology
- Connectivity
- Camera Score
- Update Support Years
- Security Updates Per Year
- Brand Score
- Release Year
- Initial Price (USD)
- Customer Rating

---

## Gradio Interface

An interactive **Gradio web application** is built to make predictions easy and user-friendly.

- Accepts real-time user input  
- Processes input using trained ML model  
- Displays predicted obsolescence category instantly  

---

## Project Structure

SMARTPHONE_OBSOLESCENCE

App  
 └── app.py                # Gradio application  

Dataset  
 └── smartphone_obsolescence.csv  

Model  
 ├── best_model_SVM.pkl    # Trained model

Notebooks  
 ├── Data preprocessing and training notebook 
  ── Classification Models notebook
  ── Regression Models notebook

Report  


---

## Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Gradio  
- Matplotlib  
- Seaborn  
- Joblib  

---

## How to Run the Project

1. Clone the repository

git clone https://github.com/GowriShaju/Smartphone-Obsolescence-Time-Prediction.git

cd smartphone-obsolescence-prediction

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python App/app.py

4. Open in browser

http://127.0.0.1:7860

---

## Future Improvements

- Deploy the application online for public access  
- Enhance feature engineering  
- Add deep learning models  
- Expand dataset with real-world data  

---

## Author

Gowri Shaju

Machine Learning project focused on classification models and interactive deployment using Gradio.
