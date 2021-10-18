"""scribe.py

scribe writing assistant cli script.
contains cli command inplementations.
"""
import os

import click
import yaml
from scribe import utils


@click.group()
@click.version_option("1.0", "-v", "--version", message="%(prog)s v%(version)s")
def cli():
    """A tool to aid scientific writing projects"""


@cli.command()
@click.argument("file_name")
def create(file_name):
    """Create a new writing project skeleton file"""
    assert file_name[-4:] == ".yml"
    if not os.path.isfile(file_name):
        print(utils.PREAMBLE)
        content_dictionary = {}
        for section, questions in utils.MARKDOWN_TEMPLATE.items():
            print(f"\nSection: {section}")
            print("-------------------------------------------")
            answers = []
            for question in questions:
                answer = utils.multiinput(question)
                answers.extend(answer)
            content_dictionary[section] = answers
        with open(file_name, "w", encoding="utf-8") as file:
            yaml.dump(content_dictionary, file)
    else:
        raise ValueError("File with that name already exists")


@cli.command()
@click.argument("file_name")
def test(file_name):
    """Run the the writing process tests"""
    assert file_name[-4:] == ".yml"
    with open(file_name, "r", encoding="utf-8") as file:
        file_dictionary = yaml.load(file, Loader=yaml.FullLoader)
    print("================= test session starts ===================")
    test_cases = []
    for section in utils.MARKDOWN_TEMPLATE:
        notes = file_dictionary[section]
        print(f"\nSection: {section}")
        print("-------------------------------------------")
        for note in notes:
            print(f"\n{note}")
            answer = input("Does the paragraph satisfy this note-test? y/[n]: ") or "n"
            if answer == "n":
                test_cases.append("\033[31mF\033[0m")
                print("\033[31m" + "FAILED" + "\033[0m")
            else:
                test_cases.append("\033[32mP\033[0m")
                print("\033[32m" + "PASSED" + "\033[0m")
    test_cases = "".join(test_cases)
    print(f"\nResults of test session: {test_cases}")
