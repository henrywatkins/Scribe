"""scribe.py

scribe writing assistant cli script.
contains cli command inplementations.
"""
import os
from pathlib import Path
from collections import OrderedDict

import click
import yaml
from utils import *


@click.group()
@click.version_option("1.0", "-v", "--version", message="%(prog)s v%(version)s")
def cli():
    """A tool to aid scientific writing projects"""


@cli.command()
@click.argument("name")
def create(name):
    """Create a new writing project"""
    cwd = Path.cwd()
    project_dir = cwd / name
    if not project_dir.exists():
        project_dir.mkdir()
        (project_dir / "images").mkdir()
        print(PREAMBLE)
        content_dictionary = {}
        for section, data in MARKDOWN_TEMPLATE.items():
            section_name = data["section_name"]
            print(f"\nSection: {section_name}")
            print("-------------------------------------------")
            answers = []
            for question in data["questions"]:
                answer = multiinput(question)
                answers.extend(answer)
            content_dictionary[section] = {
                "section_name": section_name,
                "replies": answers,
                "content": [],
            }
        with open(project_dir / "content.yml", "w", encoding="utf-8") as file:
            yaml.dump(content_dictionary, file)
        print(f"Created project {name}")
    else:
        raise ValueError("Project with that name already exists")


@cli.command()
@click.argument("name")
def test(name):
    """Run the the writing process tests"""
    with open(file_name, "r", encoding="utf-8") as file:
        file_dictionary = yaml.load(file, Loader=yaml.FullLoader)
    print("================= test session starts ===================")
    test_cases = []
    for section in MARKDOWN_TEMPLATE:
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


@cli.command()
@click.argument("section")
def show(section):
    """Print a section to stdout

    Avaliable sections:

    - title
    - narrative
    - refs
    - journals
    - intro
    - background
    - methods
    - results
    - discussion
    - abstract
    """
    content = read_content()
    if section == "all":
        for s in content.values():
            print(s["section_name"] + "\n")
            for r in s["replies"]:
                print(r)
            for c in s["content"]:
                print(c)
    elif section == "paper":
        for n, s in content.items():
            if n in paper_sections:
                print(s["section_name"] + "\n")
                for c in s["content"]:
                    print(c)
    elif section in paper_sections:
        s = content[section]
        print(s["section_name"] + "\n")
        for r in s["replies"]:
            print(r)
        for c in s["content"]:
            print(c)
    else:
        raise ValueError("Section not recognised")


@cli.command()
@click.argument("section")
def expand(section):
    """Expand each section into full paragraphs

    Available sections:

    - intro
    - background
    - methods
    - results
    - discussion
    """
    content = read_content()
    avalable_sections = ["intro", "background", "methods", "results", "discussion"]
    if section in avalable_sections:
        pass

    else:
        raise ValueError("Section not recognised")


if __name__ == "__main__":
    cli()
