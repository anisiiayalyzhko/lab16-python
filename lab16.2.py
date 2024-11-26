import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантажуємо необхідні ресурси NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Зберігаємо довільний текст у файл
text = """The left-handed batter has represented his state in national championships, such as Ranji and Mushtaq Ali trophies, and India in the Under-19 internationals.
Delhi Capitals and RR bid for him starting from 3m rupees but RR, where he had trained previously, managed to seal the deal.
Indian cricket was traditionally dominated by urban centres such as Mumbai, Delhi and Bengaluru but IPL has managed to attract a wider pool of cricketers from far-off villages and small towns of India."""
with open('original_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Читаємо текст із файлу
with open('original_text.txt', 'r', encoding='utf-8') as file:
    text_raw = file.read()

# Токенізація по словам
tokens = word_tokenize(text_raw)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.isalpha()]
stemmed_words = [stemmer.stem(word) for word in lemmatized_words]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in stemmed_words if word not in stop_words]

# Видалення пунктуації
# (це вже зроблено під час фільтрації через `.isalpha()`)

# Запис обробленого тексту у файл
processed_text = ' '.join(filtered_words)
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)

# Виводимо результат
print(f"Original Text: {text_raw}")
print(f"Processed Text: {processed_text}")
