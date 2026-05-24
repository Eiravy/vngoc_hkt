# Random Forest Prediction Web App

A simple Flask web application for running predictions using a pre-trained **Random Forest model** on uploaded CSV test data.

The application allows users to upload a CSV file, generate predictions using a trained machine learning model, and download/store prediction results.

---

## Features

- Upload a CSV test dataset
- Load a pre-trained Random Forest model (`.pkl`)
- Generate predictions automatically
- Display predictions in a web table
- Label outputs as:
  - **Anomaly** → `1`
  - **Nominal** → `0`
- Save uploaded test data (`X_test.csv`)
- Save prediction results (`predictions.csv`)

---

## Project Structure

```bash
project-folder/
│── app.py
│── random_forest_model.pkl
│── requirements.txt
│── README.md
│── X_test.csv               # generated after upload
│── predictions.csv          # generated after prediction
```

---

## Technologies Used

- Python
- Flask
- Pandas
- Pickle
- Scikit-learn (for the trained Random Forest model)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/random-forest-prediction.git
cd random-forest-prediction
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

Create a `requirements.txt` file containing:

```txt
Flask
pandas
scikit-learn
```

---

## How It Works

1. The application loads a trained Random Forest model from:

```python
random_forest_model.pkl
```

2. The user uploads a **CSV test file** through the web interface.

3. The uploaded file is read using **Pandas**:

```python
pd.read_csv(file)
```

4. Predictions are generated:

```python
clf_rf.predict(X_test)
```

5. Results are shown in the browser and saved to:

```txt
predictions.csv
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application will run on:

```txt
http://localhost:8080
```

or

```txt
http://127.0.0.1:8080
```

---

## Input File Format

Upload a CSV file containing the same feature columns used during model training.

Example:

```csv
feature1,feature2,feature3
0.45,12.3,8
0.91,10.2,4
0.22,15.7,9
```

> **Important:**  
> The uploaded CSV must have the exact same structure and feature order as the training dataset used for the Random Forest model.

---

## Prediction Output

Predictions are displayed in a table with labels:

| Prediction | Label |
|------------|-------|
| 1 | Anomaly |
| 0 | Nominal |

Example output:

```csv
prediction
1
0
1
0
```

Saved as:

```txt
predictions.csv
```

---

## Error Handling

The application includes exception handling to catch errors such as:

- Invalid CSV format
- Missing columns
- Model prediction issues
- Upload problems

Errors are displayed directly in the web interface.

---

## Deployment

The app supports deployment platforms like:

- Render
- Railway
- Heroku
- Docker
- AWS / Azure / GCP

The app automatically uses an environment port:

```python
port = int(os.environ.get("PORT", 8080))
```

---

## Future Improvements

- Download prediction results directly
- Upload trained models dynamically
- Add probability scores
- Better UI styling
- Model performance metrics
- CSV validation before prediction

---

## Author

Vyngoc
---

## License

This project is licensed under the MIT License.
