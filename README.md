Student Success Analytics & AI Prediction System

A beginner-friendly Python + Pandas + Data Visualization + Machine Learning + AI/GenAI project for a 45-day project-based internship.


Project idea

The system analyzes student academic/study data, creates visual reports, applies several machine-learning algorithms, groups students with K-Means clustering, demonstrates an ANN-style model, and provides a small Streamlit dashboard.


Main question


Which academic and study-related factors are associated with student performance, and can we predict a student's score or pass/fail status from those factors?



Lessons covered


Python fundamentals: variables, data types, operators, conditions, loops, functions, lists, tuples, sets and dictionaries

Pandas: CSV read/write, summaries, filtering and feature preparation

Visualization: line chart, bar chart, histogram, scatter plot and correlation view

Machine Learning: Linear Regression, Logistic Regression, KNN, Decision Tree, Random Forest and K-Means

AI: AI vs ML vs Deep Learning, regression, classification and ANN basics

GenAI: zero-shot, few-shot and structured prompt engineering

Project workflow, documentation and GitHub development history


Dataset

data/students.csv is a synthetic educational dataset created for learning. It does not represent real students.


Column	Meaning
attendance_pct	Attendance percentage
study_hours	Average study hours per day
assignments_completed	Completed assignments
internal_marks	Internal assessment marks
sleep_hours	Average sleep hours
extracurricular_hours	Extracurricular hours per day
previous_gpa	Previous GPA
internet_access	Yes/No
final_score	Final score
pass_fail	Pass/Fail label
performance_level	Low/Medium/High

Folder structure

student-success-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── students.csv
├── src/
│   ├── data_loader.py
│   ├── eda.py
│   ├── visualize.py
│   ├── train_models.py
│   ├── predict.py
│   ├── clustering.py
│   ├── ann_model.py
│   └── genai_prompts.py
├── models/
├── reports/figures/
├── notebooks/
└── docs/
    └── project_report.md

Setup in VS Code

1. Create a virtual environment

Windows:


python -m venv .venv
.venv\Scripts\activate

PowerShell alternative:


Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate

2. Install packages

pip install -r requirements.txt

3. Run the data analysis

python -m src.data_loader
python -m src.eda

4. Create charts

python -m src.visualize

Charts are saved in reports/figures/.


5. Train the ML models

python -m src.train_models
python -m src.clustering
python -m src.ann_model

6. Test a prediction

python -m src.predict

7. Start the dashboard

streamlit run app.py

Model evaluation


Linear Regression: MAE, RMSE and R²

Classification: accuracy, classification report and confusion matrix

K-Means: silhouette score

ANN/MLP: accuracy and classification report


Always report the metrics produced by your own run rather than inventing or copying numbers.


GenAI component

src/genai_prompts.py demonstrates zero-shot, few-shot and structured prompts without requiring an API key. It can be extended later with an LLM API.


45-day GitHub streak plan

Make one meaningful commit each day and push it after testing. Do not use fake or empty commits merely to change the contribution graph.


Day	Task	Commit
1	Initialize repository + README	docs: initialize project
2	Add requirements + gitignore	chore: add project setup
3	Add synthetic dataset	data: add student dataset
4	Load CSV with Pandas	feat: add data loader
5	Inspect columns and types	feat: add dataset inspection
6	Data-quality checks	feat: add data quality checks
7	Filtering and sorting	feat: add pandas filtering
8	Summary statistics	feat: add data summary
9	Line chart	viz: add line chart
10	Bar chart	viz: add bar chart
11	Histogram	viz: add histogram
12	Scatter plot	viz: add scatter plot
13	Study-hours analysis	analysis: study hours analysis
14	Attendance analysis	analysis: attendance analysis
15	Feature preparation	ml: prepare features
16	Train/test split	ml: add train test split
17	Linear Regression	ml: add linear regression
18	Regression metrics	ml: add regression metrics
19	Save regression model	ml: save regression model
20	Logistic Regression	ml: add logistic regression
21	Evaluate logistic model	ml: evaluate pass fail model
22	KNN	ml: add knn classifier
23	Decision Tree	ml: add decision tree
24	Random Forest	ml: add random forest
25	Classification comparison	ml: add model comparison
26	Prediction script	feat: add student prediction
27	Confusion matrix	viz: add confusion matrix
28	K-Means clustering	ml: add kmeans clustering
29	Cluster analysis	analysis: add cluster summary
30	ANN/MLP classifier	ai: add neural network model
31	Evaluate ANN	ai: evaluate neural network
32	Explain AI/ML/DL	docs: explain ai ml dl
33	GenAI prompt templates	genai: add prompt templates
34	Zero-shot prompts	genai: add zero shot prompts
35	Few-shot prompts	genai: add few shot prompts
36	AI ethics	docs: add ai ethics
37	Streamlit dashboard	feat: add dashboard
38	Dataset preview	feat: add dashboard data view
39	Dashboard charts	feat: add dashboard charts
40	Prediction form	feat: add dashboard prediction
41	Cluster view	feat: add cluster dashboard
42	Improve README	docs: improve readme
43	Add project report	docs: add project report
44	Test and clean	chore: clean and test project
45	Final screenshots + docs	docs: finalize project

Final presentation


Problem statement

Objectives

Dataset and features

Pandas preprocessing

EDA and visualizations

ML algorithms

Evaluation metrics

K-Means clustering

ANN basics

GenAI prompt engineering

Streamlit dashboard

Limitations and future scope

GitHub repository and 45-day development history


Limitations


The dataset is synthetic.

Correlation does not prove causation.

Predictions are for demonstration/learning.

It should not be used for high-stakes decisions about real students.


Future scope


Use a properly collected real-world dataset with consent.

Add stronger validation and hyperparameter tuning.

Add explainable AI.

Add authentication and role-based access.

Deploy the dashboard.

Add an optional LLM API integration with privacy controls
