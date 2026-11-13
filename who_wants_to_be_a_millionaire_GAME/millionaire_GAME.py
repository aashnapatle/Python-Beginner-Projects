questions = [
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["How many colours are there in a rainbow?", "5", "6", "7", "8", 3],
    ["Who is known as the Father of the Nation in India?", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "B. R. Ambedkar", 2],
    ["Which is the largest ocean in the world?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the chemical symbol for gold?", "Ag", "Go", "Au", "Gd", 3],
    ["Who wrote the Indian national anthem?", "Bankim Chandra", "Rabindranath Tagore", "Sarojini Naidu", "Subhas Chandra Bose", 2],
    ["Which data structure follows LIFO?", "Queue", "Stack", "Array", "Linked List", 2],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3],
    ["Who proposed the theory of general relativity?", "Isaac Newton", "Galileo", "Albert Einstein", "Nikola Tesla", 3],
    ["What is the time complexity of binary search?", "O(n)", "O(log n)", "O(n²)", "O(1)", 2]
]
for question in questions:
    print(question[0])
    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])
    answer = int(input("Enter the number of your answer: "))
    if answer == question[5]:
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {question[5]}.\n")