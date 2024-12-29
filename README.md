# Grade Prediction using Linear Regression

## 📋 Project Description
This project predicts student grades using a linear regression model based on six parameters derived from a dataset sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). The primary goal is to demonstrate how machine learning can be applied to solve real-world educational challenges by analyzing and predicting outcomes based on meaningful features.

---

## 📂 Project Structure
The repository contains the following files:

- **`Grade_Prediction.py`**: The main Python script that preprocesses the data, trains the linear regression model, evaluates its performance, and visualizes the results.
- **`StudentModel.pkl`**: A saved binary file of the trained linear regression model using `pickle`.
- **`parameters_definition.txt`**: A text file explaining the six parameters used for grade prediction.
- **`README.md`**: Documentation for the project.
- **`student-mat.csv`**: Folder containing the dataset used for training and evaluation.

---

## ⚙️ Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - `pandas`: For data manipulation.
  - `numpy`: For numerical computations.
  - `scikit-learn`: For building and evaluating the linear regression model.
  - `pickle`: For saving and loading the trained model.
  - `matplotlib`: For visualizing data and model predictions.

---

## 🔍 Dataset Information
The dataset was sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) and was trimmed to include only six meaningful parameters. The parameters and their definitions are detailed in `parameters_definition.txt`.

---

## 🚀 How to Run the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/grade-prediction.git
2. **Navigate to the project directory:**:
   ```bash
   cd grade-prediction
3. **Install the required dependencies manually by running:**:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
4. **Run the script:**:
   ```bash
   python grade_prediction.py

---

## 📊 Results
The linear regression model achieves high accuracy in predicting student grades based on the provided dataset. Additionally, the project visualizes:

- Correlations between input features and target grades.
- The predicted vs. actual grades for a better understanding of model performance.

---

## 📌 Acknowledgements
- Dataset: The data used in this project is sourced from the UCI Machine Learning Repository.
- Libraries: Special thanks to the developers of scikit-learn, pandas, numpy, and matplotlib for providing robust tools for data analysis, visualization, and machine - learning.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.
