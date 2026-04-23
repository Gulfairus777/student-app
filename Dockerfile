# Python базалық образ
FROM python:3.10

# Жұмыс папка
WORKDIR /app

# Файлдарды көшіру
COPY . .

# Кітапханаларды орнату
RUN pip install -r requirements.txt

# Тесттерді іске қосу
CMD ["pytest"]