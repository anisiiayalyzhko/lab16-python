import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt

# Завантажуємо необхідні ресурси NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Завантажуємо текст із локального файлу
with open('milton-paradise.txt', 'r', encoding='utf-8') as file:
    text_raw = file.read()

# Токенізація тексту
words = nltk.word_tokenize(text_raw)

# Загальна кількість слів у тексті
total_words = len(words)

# Знаходимо 10 найбільш вживаних слів
fdist = FreqDist(words)
most_common_words = fdist.most_common(10)

# Побудова діаграми для найбільш вживаних слів
words_top, counts_top = zip(*most_common_words)

plt.figure(figsize=(10, 6))
plt.bar(words_top, counts_top, color='skyblue')
plt.title('10 Most Frequent Words (Raw Text)', fontsize=14)
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
words_cleaned = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Знаходимо 10 найбільш вживаних слів після очищення
fdist_cleaned = FreqDist(words_cleaned)
most_common_cleaned = fdist_cleaned.most_common(10)

# Побудова діаграми для очищених даних
words_clean_top, counts_clean_top = zip(*most_common_cleaned)

plt.figure(figsize=(10, 6))
plt.bar(words_clean_top, counts_clean_top, color='orange')
plt.title('10 Most Frequent Words (Cleaned Text)', fontsize=14)
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45)
plt.show()

total_words, most_common_words, most_common_cleaned
