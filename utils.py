"""utils.py

Utilities for scribe writing assistant
"""
import yaml
from collections import OrderedDict

MARKDOWN_TEMPLATE = {
    "title": {
        "section_name": "Title ideas",
        "questions": ["What is a possible title of this work?: "],
    },
    "narrative": {
        "section_name": "Narrative",
        "questions": ["How whould you describe the narrative of this work?: "],
    },
    "refs": {
        "section_name": "Key references",
        "questions": [
            "What are the key references of this work? (e.g. Smith et al. 2017): "
        ],
    },
    "journals": {
        "section_name": "Possible journals",
        "questions": ["What possible journals are there for this work?: "],
    },
    "intro": {
        "section_name": "Introduction",
        "questions": [
            "What is the context for this work?: ",
            "Why is it interesting?: ",
        ],
    },
    "background": {
        "section_name": "Previous work",
        "questions": [
            "Where does this work follow from?: ",
            "What does the field need?: ",
        ],
    },
    "methods": {
        "section_name": "Methods",
        "questions": [
            "What are you doing?: ",
            "How does this improve on previous work?: ",
            "What methods are being used?: ",
        ],
    },
    "results": {
        "section_name": "Results",
        "questions": [
            "Describe the data you are using: ",
            "What are your results?: ",
            "What do your results mean in context?: ",
        ],
    },
    "discussion": {
        "section_name": "Conclusions",
        "questions": [
            "What are your conclusions?: ",
            "How has your work fullfilled what the field needs?: ",
        ],
    },
    "abstract": {
        "section_name": "Abstract",
        "questions": ["Write an abstract for your work: "],
    },
}


paper_sections = [
    "title",
    "abstract",
    "intro",
    "background",
    "results",
    "discussion",
    "methods",
]


PREAMBLE = """                SCRIBE
    A small tool to help with scientific
    writing projects. Answer the question
    prompts with short notes that act as
    unit tests. These notes should briefly
    detail the purpose or operation of a
    paragraph or short section. """


def read_content():
    with open("content.yml", "r", encoding="utf-8") as file:
        file_dictionary = yaml.load(file, Loader=yaml.FullLoader)
    return file_dictionary


def save_content(dictionary):
    with open(project_dir / "content.yml", "w", encoding="utf-8") as file:
        yaml.dump(content_dictionary, file)


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
