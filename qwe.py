print("🤖🤖😁Welcome To My Questions")
print("Answers the questions by typing a,b,c or d\n")
score=0
questions = [
    {
        "questions":"1.What is Ai?",
        "a":"Artifical intellengence",
        "b":"All India",
        "c":"American Internet",
        "d":"African Impala",
        "answer":"a"
    },
    {
        "questions":"2. Who is the CEO of ST Software Solutions ,Tirupur?",
        "a":"Elon musk",
        "b":"Ratan TATA",
        "c":"Dharun",
        "d":"Dharmaraj Kumar",
        "answer":"c"
    },
    {
      "questions":"3. What do you call a potato that talks too much?",
      "a":"Chat-potato",
      "b":"Hot potato",
      "c":"Cold fries",
      "d":"Spicy chips",
      "answer":"a"
    },
    {
      "questions":"4. What is the favourite sport of ghosts?",
      "a":"Cricket",
      "b":"Badminton",
      "c":"Boo-ling",
      "d":"Football",
      "answer":"c"
    },
    {
      "questions":"5. Why did the tomato turn red?",
      "a":"It saw ketchup",
      "b":"It was shy",
      "c":"It was angry",
      "d":"It ran a marathon",
      "answer":"a"
    },
    {
      "questions":"6. What is a computer’s favourite snack?",
      "a":"Chips",
      "b":"Cookies",
      "c":"Hard disk",
      "d":"RAM biryani",
      "answer":"a"
    },
    {
      "questions":"7. Which bird loves shopping?",
      "a":"Crow",
      "b":"Peacock",
      "c":"Penguin",
      "d":"Duck (because it always has a bill!)",
      "answer":"d"
    },
    {
      "questions":"8. What will happen if you eat a clock?",
      "a":"You become fast",
      "b":"You become slow",
      "c":"It will take time",
      "d":"Nothing happens",
      "answer":"c"
    },
    {
      "questions":"9. What is the favourite subject of a music-loving student?",
      "a":"Maths",
      "b":"Science",
      "c":"History",
      "d":"Note-book",
      "answer":"d"
    },
    {
      "questions":"10. Which day of the week is the strongest?",
      "a":"Monday",
      "b":"Tuesday",
      "c":"Saturday",
      "d":"Sunday (because the rest are weak!)",
      "answer":"d"
    }
]
for q in questions:
    print(q["questions"])
    print("a)", q["a"])
    print("b)", q["b"])
    print("c)", q["c"])
    print("d)", q["d"])

    user_ans = input("Your answer: ").lower()

    if user_ans == q["answer"]:
        print("💯☑️__CORRECT__✅✔️\n")
        score += 1
    else:
        print("❌Wrong! Correct answer is:", q["answer"], "\n")

print("🤖Your Final Score:",score, "/", len(questions)) 
