# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('bilmiyom.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
f = open('bilmiyom.txt', 'w', encoding='utf-8')
text = 'Yeni Yazı'
f.write(text)
f.close()

# with open('images/cat.jpg', 'rb') as f:
#         picture = discord.File(f)