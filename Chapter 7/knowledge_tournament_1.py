# Knowledge tournament

# for using sys.exit() we need to import sys
# if finishes program after except occurs
import sys


# creating function open_file()
def open_file(file_name, mode):
    """Open the file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("File can't be open", file_name, "Program will be close.\n", e)
        input("\n\nFor closing press enter.")
        sys.exit()
    else:
        return the_file


# creating function next line
def next_line(the_file):
    """Return next row from file."""
    line = the_file.readline()
    # python do not runaround text without \n so we need to replace all / to \n
    line = line.replace("/", "\n")
    return line


# creating function next_block()
def next_block(the_file):
    """Return next block of data from file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation


# creating welcome function
def welcome(title):
    """Welcome player and download it title of episode."""
    print("\t\t Welcome in knowledge tournament!\n")
    print("\t\t", title, "\n")


# creating main function
def main():
    trivia_file = open_file("quiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # take first block from file
    category, question, answers, correct, explanation = next_block(trivia_file)
    # repeat until category will not be empty
    while category:
        # ask question
        print(category)
        print(question)

        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # take the answer from player
        answer = input("What is your answer?: ")

        # check the answer
        if answer == correct:
            print("This is the correct answer!", end=" ")
            score += 1
        else:
            print("This is not the correct answer.", end=" ")
        print(explanation)
        print("Your score:", score, "\n\n")

        # taking another block from file
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()
    print("Your final score is:", score)


main()
input("\n\nFor ending, press enter.")
