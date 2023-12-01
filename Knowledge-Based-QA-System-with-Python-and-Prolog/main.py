from pyswip import Prolog
import time
import json


def prolog_query(query_string):
    prolog = Prolog()
    prolog.consult("knowledge.pl")
    results = []
    for res in prolog.query(query_string):
        results.append(res)

    return results


def ask_question(query_string):
    answers = prolog_query(query_string)
    return answers


def make_json(data):
    json_str = ""
    for c in data:
        if c == "'":
            json_str += '"'
            continue
        json_str += c
    return json_str


def say_answers(prefix, suffix, question_i, answers_i):
    for ansi in answers_i:
        ansi = make_json(str(ansi))
        obj = json.loads(str(ansi))
        print(obj[question_i])
        text = prefix + " " + obj[question_i] + " " + suffix
        print(">>>> ", text)


print(
    "Hi, I'm here to tell you about Taras Shevchenko National University. \
                what do you want to know about Taras Shevchenko National University?"
)
flg = True
while flg:
    # Q/A
    print("\n\n")
    asked_question = str(input("what is in your mind: ")).lower()

    if (
        "name of the university" in asked_question
        or "university name" in asked_question
    ):
        # Q: what is the name of the university?
        question = "UniversityName"
        query = "name(" + question + ")."
        answers = ask_question(query)
        say_answers("The name of the university ", "", question, answers)

    elif (
        "introduction" in asked_question
        or "about ju" in asked_question
        or "about Taras Shevchenko National University" in asked_question
    ):
        # Q: what is Taras Shevchenko National University?
        question = "Introduction"
        query = "introduction('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "history of knu" in asked_question
        or "history of Taras Shevchenko National University" in asked_question
    ):
        # Q: history of Taras Shevchenko National University.
        question = "History"
        query = "history('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers("Brief history: ", "", question, answers)

    elif (
        "location of Taras Shevchenko National University" in asked_question
        or "situated" in asked_question
    ):
        # Q: where is Taras Shevchenko National University?
        question = "Location"
        query = "location('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif "area of Taras Shevchenko National University" in asked_question:
        # Q: where is Taras Shevchenko National University?
        question = "Area"
        query = "area('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "total area of Taras Shevchenko National University is about ", "", question, answers
        )

    elif (
        "current" in asked_question
        or "present" in asked_question
        or "now" in asked_question
    ) and ("vice chancellor" in asked_question or "vc" in asked_question):
        # Q: who is the current vice_chancellor of Taras Shevchenko National University?
        question = "Vice_chancellor"
        query = "vice_chancellor('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "The current vice chancellor of Taras Shevchenko National University is ",
            "",
            question,
            answers,
        )

    elif (
        "number of faculties" in asked_question
        or "how many faculties" in asked_question
        and asked_question.find("faculty of") == -1
    ):
        # Q how many faculties are in Taras Shevchenko National University
        question = "Number_of_faculties"
        query = "number_of_faculties('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "faculties in Taras Shevchenko National University", question, answers
        )

    elif (
        "number of departments" in asked_question
        or "how many departments" in asked_question
    ):
        # Q how many departments are in Taras Shevchenko National University
        question = "Number_of_departments"
        query = "number_of_departments('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "departments in Taras Shevchenko National University", question, answers
        )

    elif (
        "number of institutes" in asked_question
        or "how many institutes" in asked_question
    ):
        # Q how many institutes are in Taras Shevchenko National University
        question = "Number_of_institutes"
        query = "number_of_institutes('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "institutes in Taras Shevchenko National University", question, answers
        )

    elif (
        "names of the faculties" in asked_question
        or "what are the faculties" in asked_question
    ):
        # Q what are the faculties in Taras Shevchenko National University
        question = "Facultiy"
        query = "faculties('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "there are 6 faculties are in Taras Shevchenko National University, they are, ",
            "",
            question,
            answers,
        )

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
    ) and "under the faculty of" in asked_question:
        # Q what are the names departments in faculty of X?
        faculties = ["Faculty of Biology",
                     "Faculty of Chemistry",
                     "Faculty of Economics", 
                     "Faculty of Geography", 
                     "Faculty of History",
                     "Faculty of Cybernetics", 
                     "Faculty of Law",
                     "Faculty of Mechanics and Mathematics",
                     "Faculty of Philology",
                     "Faculty of Philosophy", 
                     "Faculty of Physics",
                     "Faculty of Psychology", 
                     "Faculty of Radiophysics, Electronics and Computer Systems",
                     "Faculty of Social Sciences"
        ]
        id = -1
        for i in range(14):
            if faculties[i] in asked_question:
                id = i
                break
        if id != -1:
            print(faculties[id])
            question = "Departments"
            query = (
                "departments_under_faculty('Taras Shevchenko National University', '"
                + faculties[id]
                + "',"
                + question
                + ")."
            )
            answers = ask_question(query)
            print(">>>>> ", "the departments under " + faculties[id] + " are, ")
            say_answers("", "", question, answers)

        else:
            print(">>>>> ", "sorry, there is no such faculty.")

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
    ):
        # Q what are the departments in Taras Shevchenko National University
        question = "Departments"
        query = "departments('Taras Shevchenko National University', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "there are 96 departments in Taras Shevchenko National University, they are, ",
            "",
            question,
            answers,
        )

    elif (
        "about department of ttp" in asked_question
        or "about ttp" in asked_question
        or "about Department of Theory and Technology of Programming" in asked_question
    ):
        # Q what you know about dept of TTP Taras Shevchenko National University
        question = "Cse"
        query = (
            "about_department_of_department_of_theory_and_technology_of_programming(\
                'Taras Shevchenko National University', "
            + question
            + ")."
        )
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "chairman of department of ttp" in asked_question
        or "chairman of ttp" in asked_question
        or "chairman of Department of Theory and Technology of Programming" in asked_question
        in asked_question
    ):
        # Q who is the chairman of dept of TTP KNU?
        question = "Chairman"
        query = (
            "chairman_of_ttp('Department of Theory and Technology of Programming', "
            + question
            + ")."
        )
        answers = ask_question(query)
        say_answers(
            "",
            "is the chairman of Department of Theory and Technology of Programming",
            question,
            answers,
        )

    elif (
        "who are the developers of this project" in asked_question
        or "who developed" in asked_question
        or "who created" in asked_question
    ):
        # Q who developed this program?
        question = "Developers"
        query = "developers(" + question + ")."
        answers = ask_question(query)
        print(
            ">>>>> "
        )
        say_answers("the developers are", "", question, answers)

    elif "stop" in asked_question or "exit" in asked_question:
        print(">>>>> ", "thank you, hope you have enjoyed the session")
        break

    else:
        if asked_question != "-----------------":
            confirmation = str(
                input(
                    "Sorry, this is out of my knowledge. whould you like to continue? "
                )
            ).lower()
            
            if "no" in confirmation or "nope" in confirmation or "stop" in confirmation:
                print(">>>>> ", "thank you, hope you have enjoyed the session")
                break
            else:
                continue

        time.sleep(2)
