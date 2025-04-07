# 🧠 GDP Prediction Web App

A simple machine learning web app built with Flask to predict GDP based on economic factors like investment, consumption, and exports. The model is trained using `scikit-learn`, serialized with `pickle`, and served via a Flask server with HTML forms for input. The app runs seamlessly in a Docker container.

---

## 📁 Project Structure

```
gdp-predictor/
│
├── app.py                 # Flask server
├── train_model.py         # Trains and saves the GDP prediction model
├── gdp_model.pkl          # Pickled ML model (generated after training)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker setup
└── templates/
    └── form.html          # HTML form for user input
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+ (if running locally)
- Docker (if running in a container)

---

## 💻 Running the App Locally (Without Docker)

1. **Clone the repository**

```bash
git clone https://github.com/imksprateek/GDP-prediction-MLOps

cd GDP-prediction-MLOps
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Train the model**

```bash
python train_model.py
```

4. **Start the Flask server**

```bash
python app.py
```

5. **Visit in your browser**

Open: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Running the App with Docker

1. **Build the Docker image**

```bash
docker build -t gdp-predictor .
```

2. **Run the Docker container**

```bash
docker run -p 5000:5000 gdp-predictor
```

3. **Visit in your browser**

Open: [http://localhost:5000](http://localhost:5000)

---

## ⚙️ API Details

### Endpoint: `/predict`  
**Method:** POST  
**Consumes:** `application/x-www-form-urlencoded` (via HTML form)  
**Returns:** JSON

### Example Response
```json
{
  "predicted_gdp": 870.0
}
```

---

## 📦 Technologies Used

- Python
- Flask
- scikit-learn
- Numpy, Pandas
- Pickle
- HTML (Jinja Templates)
- Docker

---

## 🧹 Cleanup

To remove Docker containers/images:

```bash
docker ps -a                  # List running containers
docker rm <container_id>      # Remove container
docker rmi gdp-predictor      # Remove image
```

---


## 📬 Acknowledgement

**Task 1** built as a part of the **IEEE Computer Society Bangalore Chapter's Student Internship Program**.  
The task was to containerize a simple Machine Learning model using Docker and test it on a local Kubernetes setup.