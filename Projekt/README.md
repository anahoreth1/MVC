# System Aukcyjny

## Spis treści

1. Opis projektu
2. Funkcjonalności
3. Technologie
4. Instrukcja uruchomienia lokalnego
5. Uruchomienie backendu przez Docker
6. Link do aplikacji w chmurze
7. Dodatkowe funkcjonalności

## 1. Opis projektu

Projekt przedstawia system aukcyjny oparty na architekturze REST API. Jest to platforma internetowa umożliwiająca użytkownikom rejestrację i zarządzanie własnym kontem, a także tworzenie i publikowanie aukcji przedmiotów przeznaczonych na sprzedaż.

Użytkownicy mogą przeglądać dostępne oferty, wyświetlać szczegóły aukcji oraz składać własne oferty cenowe w ramach licytacji.

Szczegółową dokumentację projektu znajduje się w folderze [docs](https://github.com/anahoreth1/MVC/tree/main/Projekt/docs).

## 2. Funkcjonalności

### Użytkownicy

* `POST /users` – rejestracja użytkownika
* `POST /login` – logowanie użytkownika
* `GET /users` – pobieranie listy użytkowników
* `GET /users/{id}` – pobieranie danych konkretnego użytkownika
* `PUT /users/{id}` – edycja danych użytkownika
* `DELETE /users/{id}` – usuwanie użytkownika

### Aukcje

* `POST /auctions` – tworzenie aukcji
* `GET /auctions` – pobieranie listy aukcji
* `GET /auctions/{id}` – pobieranie szczegółów aukcji
* `PUT /auctions/{id}` – edycja aukcji
* `DELETE /auctions/{id}` – usuwanie aukcji
* `GET /auctions?category=...` – filtrowanie po kategorii
* `GET /auctions?status=...` – filtrowanie po statusie

### Licytacja

* `POST /auctions/{id}/bids` – składanie oferty
* walidacja wysokości oferty (oferta musi być wyższa od aktualnej najwyższej oferty)
* blokada składania ofert po zakończeniu aukcji
* przechowywanie historii ofert dla każdej aukcji

## 3. Technologie

* Backend: Django
* Frontend: React
* Baza danych: SQLite
* Docker: używany do uruchamiania backendu
* Wdrożenie w chmurze:

  * backend: Render
  * frontend: GitHub Pages

## 4. Instrukcja uruchomienia lokalnego

### 4.1. Backend

```bash
cd Projekt/backend/auction_system
# instalacja zależności
pip install -r requirements.txt
# migracje
python manage.py migrate
# uruchomienie
python manage.py runserver
```

Przykład działania backendu po uruchomieniu:

* Otwórz stronę http://127.0.0.1:8000/api/users/
* Do pola **Content** dodaj:

```json
{
  "email": "test@example.com",
  "name": "John Doe",
  "password": "12345678"
}
```

* Naciśnij „POST”.

### 4.2. Frontend

Przed uruchomieniem frontendu lokalnie należy utworzyć plik `.env` w folderze `frontend` na podstawie pliku `.env.example`.

```bash
cd Projekt/frontend
npm install
npm run dev
```

Przykład działania frontendu po uruchomieniu:

* Otwórz stronę http://localhost:5173/MVC
* Sprawdź, czy frontend działa poprawnie.

## 5. Uruchomienie backendu przez Docker

Istnieje możliwość uruchomienia aplikacji w kontenerze Docker:

```bash
cd Projekt/backend/auction_system
docker build -t auction-backend .
docker run -p 8000:8000 auction-backend
```

Przykład działania backendu po uruchomieniu przez Docker:

* Otwórz stronę:
  http://127.0.0.1:8000/api/users/

* Do pola **Content** dodaj:

```json
{
  "email": "test@example.com",
  "name": "John Doe",
  "password": "12345678"
}
```

* Naciśnij „POST”.

## 6. Link do aplikacji w chmurze

GitHub Actions realizuje automatyczne wdrażanie aplikacji (workflow dostępny tutaj: [link](https://github.com/anahoreth1/MVC/blob/main/.github/workflows/deploy.yml)). 

Każdy commit do gałęzi `main` powoduje automatyczną aktualizację backendu i frontendu w chmurze.

* Frontend: https://anahoreth1.github.io/MVC/
* Backend (API): https://mvc-9x30.onrender.com

Przykład działania backendu w chmurze:

* Otwórz stronę https://mvc-9x30.onrender.com/api/users/
* Do pola **Content** dodaj:

```json
{
  "email": "test@example.com",
  "name": "John Doe",
  "password": "12345678"
}
```

* Naciśnij „POST”.

## 7. Dodatkowe funkcjonalności

W projekcie zostały również zrealizowane następujące elementy:

* Testy jednostkowe Django dla modułów auctions i users. Testy są automatycznie uruchamiane przy każdym pushu do GitHuba.

* Walidacja po stronie serwera oraz klienta, np. sprawdzanie wymaganych pól i poprawności formatów danych (np., adres e-mail użytkowników).

* Filtrowanie aukcji według kategorii oraz statusu.

* System logowania użytkowników z wykorzystaniem hasła.

* Automatyczna dokumentacja API wygenerowana przy użyciu drf-spectacular (Swagger UI dostępny pod adresem `/api/docs/`).
