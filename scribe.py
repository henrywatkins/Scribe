import click
import os
from collections import OrderedDict
import yaml
import utils


@click.group(help="A tool to aid scientific writing projects")
@click.help_option("-h", "--help")
@click.version_option("1.0", "-v", "--version", message="%(prog)s v%(version)s")
def main():
    pass


@main.command(help="create a new writing project skeleton file")
@click.help_option("-h", "--help")
@click.argument("file_name")
def create(file_name):
    assert file_name[-4:]==".yml"
    if os.path.isfile(file_name):
        raise ValueError("File with that name already exists")
    else:
        print(utils.PREAMBLE)
        content_dictionary = {}
        for section, questions in utils.MARKDOWN_TEMPLATE.items():
            print("\nSection: {}".format(section))
            print("-------------------------------------------")
            answers = []
            for question in questions:
                answer = utils.multiinput(question)
                answers.extend(answer)
            content_dictionary[section] = answers
        with open(file_name, "w") as file:
            yaml.dump(content_dictionary, file)


@main.command(help="run the the writing process tests")
@click.help_option("-h", "--help")
@click.argument("file_name")
def test(file_name):
    assert file_name[-4:]==".yml"
    with open(file_name, "r") as file:
        file_dictionary = yaml.load(file, Loader=yaml.FullLoader)
    print("================= test session starts ===================")
    test_cases = []
    for section in utils.MARKDOWN_TEMPLATE.keys():
        notes =  file_dictionary[section]
        print("\nSection: {}".format(section))
        print("-------------------------------------------")
        for note in notes:
            print("\n{}".format(note))
            answer = input("Does the paragraph satisfy this note-test? y/[n]: ") or "n"
            if answer == "n":
                test_cases.append("\033[31mF\033[0m")
                print("\033[31m" + "FAILED" + "\033[0m")
            else:
                test_cases.append("\033[32mP\033[0m")
                print("\033[32m" + "PASSED" + "\033[0m")
    test_cases = "".join(test_cases)
    print("\nResults of test session: {}".format(test_cases))


if __name__ == "__main__":
    main()
