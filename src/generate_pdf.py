from weasyprint import HTML
from random import shuffle
from itertools import repeat
from questions import questions

style = """<style>
h1, h2 { margin-bottom: 30px; }
.question { display: block; margin-bottom: 20px; }
table { display: block; }
.question--multiple { display: block; margin-bottom: 50px; }
.question__id { display: block; margin-right: 50px; }
.answer__letter { display: block; 
                  margin-left: 35px; 
                  margin-right: 20px;
                  border: 1px solid;
                  padding: 3px;
                 }
</style>
"""


def shuffle_question_and_answers(src):
    shuffle(src)
    for question in src:
        answers = question.get("answers")
        if answers:
            shuffle(answers)


def generate_html(src, title):
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        {style}
    </head>
    <h1>{title}</h1>
    <h2>Class: &nbsp;&nbsp;&nbsp;&nbsp; Date: <br>Full name:</h2>
    <body>
    """

    question_counter = 0

    for question_dict in src:
        question_counter = question_counter + 1
        question = question_dict.get("question")
        question_type = "question--multiple"
        html = (
            html
            + f"""
            <table class={question_type}>
                <thead class="question">
                <tr>
                    <td class="question__id"><strong>{question_counter}</strong></td>
                    <td><strong>{question}</strong></td>
                </tr>
                </thead>
                <tbody>
            """
        )

        answers = question_dict.get("answers")
        letters = ["A", "B", "C", "D"]
        for letter, answer in zip(letters, answers):
            html = (
                html
                + f"""
                    <tr>
                        <td class="answer__letter">{letter}</td>
                        <td>{answer}</td>
                    </tr>
                """
            )
        html = html + f"</tbody></table>"

    html = html + '<p style="break-before: always;"></p></html></body>'
    return html


def main():
    times = int(
        input("Hello teacher! How many random variations do you want to generate?\n")
    )
    title = (
        input('Please provide a title too. Defaults to: "Python quiz"\n')
        or "Python quiz"
    )
    full_html = ""

    for _ in repeat(None, times):
        shuffle_question_and_answers(questions)
        h = generate_html(src=questions, title=title)
        full_html = full_html + h

    filename = title.lower().replace(" ", "_") + ".pdf"
    HTML(string=full_html).write_pdf(target=filename)
    print(f"{filename} created!")


main()
