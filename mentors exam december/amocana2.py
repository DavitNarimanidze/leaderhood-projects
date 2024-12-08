# Count the Number of Unique Words in a Text

def unique_words(st):
    # პუნქტუაცია ესეიგი ვიღებთ ზედმეტ სიმბოლოებს ხარვეზები რომ არ იყოს 
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    clean = ""
    for i in st:
        clean += i # პუნქტუაციის გარეშეა მხოლოდ ასოები და ციფრები 
    clean = clean.lower() # ყველა ასო დავწერე lower ში casesensitive გამო 
    word = clean.split() # სტრინგი იყოფა სიტყვებად სადაც სიტყვები ცარიელი ადგილით გამოყოფილია 

    unique = set(word) # set გამოვიყენე რადგან განმეორებად სიტყვებს ავტომატურად ამოიღებს 

    return len(unique) # ბრუნდება უნიკალური სიტყვების რაოდენობა 

print(unique_words("The quick brown fox jumps over the lazy dog"))
print(unique_words("Hello hello world!"))
print(unique_words(""))
print(unique_words("Python is fun. Python is cool."))
print(unique_words("One word"))
