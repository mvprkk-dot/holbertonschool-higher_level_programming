def write_file(filename="", text=""):
    """Fayla mətn yazır və yazılan simvolların sayını qaytarır"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)  # len() funksiyasını buradan sil
