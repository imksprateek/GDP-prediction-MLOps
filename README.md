# 🧠 GDP Prediction Web App

A simple machine learning web app built with Flask to predict GDP based on economic factors like investment, consumption, and exports. The model is trained using `scikit-learn`, serialized with `pickle`, and served via a Flask server with HTML forms for input.

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
├── kubedefs/              # Kubernetes definitions
│   ├── deployment.yaml    # Kubernetes deployment configuration
│   └── service.yaml       # Kubernetes service configuration
└── templates/
    └── form.html          # HTML form for user input
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+ (if running locally)
- Docker (if running in a container)
- Minikube (for local Kubernetes deployment)
- kubectl (for interacting with Kubernetes clusters)

#### Installing Prerequisites

**Docker:**
- Download and install Docker from [Docker's official website](https://www.docker.com/products/docker-desktop/)

**For Windows Users:**
- Install Chocolatey (Windows package manager):
  1. Open PowerShell as Administrator
  2. Run the following command:
     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
     ```
  3. Close and reopen PowerShell

**Minikube:**
```bash
# macOS (using Homebrew)
brew install minikube

# Windows (using Chocolatey)
choco install minikube

# Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

**kubectl:**
```bash
# macOS (using Homebrew)
brew install kubectl

# Windows (using Chocolatey)
choco install kubernetes-cli

# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

---

## 🚀 Running the Application

**Choose ONE of the following three methods to run the application:**

## Method 1: 💻 Run Locally (Python)

Best for development and quick testing.

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

## Method 2: 🐳 Run with Docker

Best for consistent environments and isolated deployment.

1. **Clone the repository**

```bash
git clone https://github.com/imksprateek/GDP-prediction-MLOps
cd GDP-prediction-MLOps
```

2. **Build the Docker image**

```bash
docker build -t gdp-predictor .
```

3. **Run the Docker container**

```bash
docker run -p 5000:5000 gdp-predictor
```

4. **Visit in your browser**

Open: [http://localhost:5000](http://localhost:5000)

**Alternatively, pull from Docker Hub:**

```bash
docker pull imksprateek/gdp-prediction-mlops
docker run -p 5000:5000 imksprateek/gdp-prediction-mlops
```

## Method 3: ☸️ Run on Kubernetes (Local)

Best for production-like environment and scalability testing.

1. **Start Minikube**

```bash
minikube start --cpus=2 --memory=2048
```

2. **Verify Minikube is running properly**

```bash
minikube status
```

All components (host, kubelet, apiserver) should show as "Running".

3. **Apply Kubernetes configurations**

```bash
kubectl apply -f kubedefs/deployment.yaml
kubectl apply -f kubedefs/service.yaml
```

4. **Check if pods are running**

```bash
kubectl get pods
```

Wait until you see the pods in "Running" state.

5. **Access the application**

```bash
minikube service flask-service --url
```

This will return a URL you can open in your web browser. Alternatively, if using Minikube with tunneling:

```bash
minikube tunnel
```

Then access: [http://localhost:30080](http://localhost:30080)

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
- Kubernetes/Minikube

---

## 🧹 Cleanup

### Docker Cleanup

```bash
docker ps -a                  # List running containers
docker rm <container_id>      # Remove container
docker rmi gdp-predictor      # Remove image
```

### Kubernetes Cleanup

```bash
kubectl delete deployment flask-app
kubectl delete service flask-service
minikube stop
# Optional: Delete the minikube VM completely
minikube delete
```

---

## 📬 Acknowledgement

**Task 1** built as a part of the **IEEE Computer Society Bangalore Chapter's Student Internship Program**.  
The task was to containerize a simple Machine Learning model using Docker and test it on a local Kubernetes setup.