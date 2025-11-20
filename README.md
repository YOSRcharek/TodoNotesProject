# Django Todo + Notes API (DRF + JWT)

Une API REST construite avec **Django** et **Django REST Framework**, composée de deux applications interconnectées :

- **Todolist** : gestion des tâches
- **Notes** : prise de notes liées à plusieurs todos

L’API utilise **JWT (SimpleJWT)** pour l’authentification et inclut l’interface **Django Admin**.  
Base de données utilisée : **SQLite**.

---

## 🚀 Installation & Exécution

### 1. Cloner le projet
```bash
   git clone https://github.com/YOSRcharek/TodoNotesProject
   cd TodoNotesProject
```
### 2. Créer un environnement virtuel et l'activer
   ```bash
   py -m venv venv
   source venv/bin/activate
   ```
### 3. Installer les dépendances
   ```bash
   pip install -r requirements.txt
   ```
### 4. Appliquer les migrations
   ```bash
   python manage.py migrate
   ```
### 5. Créer un superutilisateur (pour accéder à l'admin)
   ```bash
   python manage.py createsuperuser
   ```
### 6. Lancer le serveur
   ```bash
   python manage.py runserver
   ```
### 7. Endpoints utiles
   - Admin: `http://127.0.0.1:8000/admin/`
   - API root: `http://127.0.0.1:8000/api/`
   - Todos: `http://127.0.0.1:8000/api/todos/`
   - Notes: `http://127.0.0.1:8000/api/notes/`
   - JWT obtain: `POST http://127.0.0.1:8000/api/auth/login/` (username/password)

## Utilisation rapide (Postman)
- Obtenir token:
  ```bash
   POST http://127.0.0.1:8000/api/auth/login/ 
     "Content-Type: application/json" \
    -d '{"username":"admin", "password":"admin"}'
  ```
  Réponse: `{ "access": "...", "refresh": "..." }`

- Appeler API avec token:
  ```bash
  "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/todos/
  ```

## Notes d'architecture (résumé)
- `Todo` a une `ForeignKey` vers `Note` (`on_delete=SET_NULL`)
- `Note` expose ses `todos` via le reverse relation `todos` (serializers)
- Authentification JWT + Session supportée (settings)
- Pattern: `ViewSet` + `DefaultRouter` pour garder l'API simple et RESTful

