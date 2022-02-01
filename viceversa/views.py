from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	amount_words_in_text = len(user_text.split(' '))
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'amountwords':amount_words_in_text})