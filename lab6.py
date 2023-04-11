def get_text_info(filepath):
    word_freq = {}  
    with open(filepath, 'r') as file:
        text = file.read().lower()  
        words = text.split()  
        for word in words:
            word = ''.join(char for char in word if char.isalpha())  
            if word in word_freq:
                word_freq[word] += 1  
            else:
                word_freq[word] = 1  
    for word, freq in word_freq.items():
        print(f"{word} - {freq}")
        get_text_info("article.txt")
        
 ###################################################################

import csv
import requests
import os

def download_csv(urlpath):
    
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source_data")
    
    
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
   
    
    filename = os.path.join(source_dir, "username.csv")
    
    
    response = requests.get(urlpath)
    with open(filename, 'wb') as file:
        file.write(response.content)
    
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        
        
        rows = rows[:-1]
    
    
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)
    
    print("Completed!")
