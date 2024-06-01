from django.shortcuts import render
from decouple import config
from langchain_openai import OpenAI,ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

# Create your views here.

def chatbot(request):
    if request.method=="POST":
        inputdata=request.POST['inputField']

        SECRET_KEY = config('OPENAI_API_KEY')
        print(SECRET_KEY)

        chat = ChatOpenAI(openai_api_key=SECRET_KEY)
        msg = inputdata
        message = [
            SystemMessage(content="""You are helpful assistant,you get user input,user ask you
            for the food recceipies,your work is to give step by step recipie to user ,
            give answer in bullet format and new line.do not answer other question ,answer 
            only food receipies ,give output in form like- 
            
            Ingredients:
            Salt and pepper to taste
            Instructions:
            Prepare the Ingredients:
            
            Sprinkle a pinch of salt and pepper over the tomato slices to enhance the flavor.
            Assemble the Sandwich:
            
            Carefully place the other slice of bread (with cheese and mayonnaise side facing down) on top of the stacked ingredients to complete the sandwich.
            Optional: Cut the Sandwich:
            
            If you prefer, you can cut the sandwich in half diagonally or into quarters to make it easier to handle and eat.
            Serve and Enjoy:
            
            Serve the sandwich immediately with your favorite sides, such as chips, pickles, or a side salad.
            Additional Tips:
            Toasting: If you like a toasted sandwich, you can toast the bread slices in a toaster before adding the ingredients, or use a sandwich press to toast the assembled sandwich.
            Variations: Feel free to add other ingredients such as avocado, bacon, pickles, or different types of cheese and meats according to your preference."""),
            HumanMessage(content=msg)
        ]

        resp = chat.invoke(message)
        print(inputdata)
    return render(request,'home.html',{"resp":resp.content})
