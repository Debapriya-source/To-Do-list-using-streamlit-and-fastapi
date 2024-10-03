## Create a virtual environment (optional)

```bash
pip install virtualenv
python -m venv ./venv
```

## Activate the virtual env (optional)

For linux or mac

```bash
./venv/Scripts/activate
```

For windows powershell

```bash
./venv/Scripts/Activate.ps1
```

## Install the requirements

```bash
pip install -r requirements.txt
```

## Run the backend

```bash
cd backend
uvicorn app:app --reload
```

## Run the frontend

```bash
cd frontend
streamlit run app.py
```
