"""utils.py

Utilities for scribe writing assistant
"""

MARKDOWN_TEMPLATE = {
    "Title ideas": ["What is a possible title of this work?: "],
    "Narrative": ["How whould you describe the narrative of this work?: "],
    "Key references": [
        "What are the key references of this work? (e.g. Smith et al. 2017): "
    ],
    "Possible journals": ["What possible journals are there for this work?: "],
    "Introduction": [
        "What is the context for this work?: ",
        "Why is it interesting?: ",
    ],
    "Previous work": [
        "Where does this work follow from?: ",
        "What does the field need?: ",
    ],
    "Methods": [
        "What are you doing?: ",
        "How does this improve on previous work?: ",
        "What methods are being used?: ",
    ],
    "Experiments & results": [
        "Describe the data you are using: ",
        "What are your results?: ",
        "What do your results mean in context?: ",
    ],
    "Conclusions": [
        "What are your conclusions?: ",
        "How has your work fullfilled what the field needs?: ",
    ],
    "Abstract": ["Write an abstract for your work: "],
}

PREAMBLE = """                SCRIBE
    A small tool to help with scientific
    writing projects. Answer the question
    prompts with short notes that act as
    unit tests. These notes should briefly
    detail the purpose or operation of a
    paragraph or short section. """


def multiinput(question):
    """For a given question, allow the user to answer multiple times"""
    answer = input(question)
    new_lines = [answer]
    while True:
        new_line = input()
        if new_line:
            new_lines.append(new_line)
        else:
            break
    return new_lines
