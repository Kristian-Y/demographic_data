# Demographic Data

### Използвани технологии:

* **Django**
* **Django REST Framework (DRF)** – Позволява бързо изграждане на RESTful API-та.
* **SQLite3** – Лека релационна база данни, подходяща за малки и средни проекти.

### Използвани библиотеки:

* **APScheduler** – Периодично изпълнение на задачи (за актуализиране на данни).
* **Requests** – Изпращане на HTTP заявки към външни API източници.

### Избор на база данни

Използвам **SQLite3**, защото не се очаква да съхранява голям обем от данни. Няма нужда от по-сложна система като PostgreSQL, защото информацията се обновява периодично и няма критични изисквания за производителност или мащабируемост.

### Алгоритми и техники:

* **Извличане на данни от външен REST API** – Данните се обработват и записват в базата данни.

# How to Run the Demographic Data API

## **1. Installation & Setup**

### **1.1 Install Dependencies**

Ensure you have Python installed (preferably Python 3.10 or later). Then, install the required dependencies:

```
pip install django djangorestframework apscheduler requests
```

### **1.2 Create and run a python venv**

```
py -m venv venv
venv/Scripts/activate
```

### **1.3 Apply Migrations**

```
cd backend
python manage.py migrate
```

## **2. Running the Server**

Start the Django development server:

```
python manage.py runserver
```

Access the API at: `http://127.0.0.1:8000/api/`

## **3. Running the Scheduled Task**

The API fetches and updates population data daily using APScheduler.

### **3.1 Manually Trigger the Update**

To manually fetch and update data, run:

```
python manage.py update_population
```

### **3.2 Verify Data in Django Admin**

1. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
2. Log in to the admin panel at: `http://127.0.0.1:8000/admin/`

## **4. API Endpoints**

### **4.1 Get All States' Population Data**

```
GET /api/states/
```

### **4.2 Get Population Data for a Specific State**

```
GET /api/states/filter_by_state/?state_name=California
```

## **5. Stopping the Server**

To stop the server, press **CTRL + C** in the terminal.
