FROM python:3.12-slim

WORKDIR /app

# Installeer requirements in de /app map of de standaard installatielocatie
# We vertrouwen erop dat deze installatie werkt en dat de bind mount de code overschrijft
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# De code wordt hier gekopieerd, maar zal overschreven worden door de bind mount
COPY . .

# Verwijder de CMD hier
