import click
import os

import utils


@click.group(help="A tool for helping scientific writing projects")
@click.help_option("-h", "--help")
@click.version_option("1.0", "-v", "--version", message="%(prog)s v%(version)s")
def main():
    pass


@main.command(help="create a new writing project skeleton file")
@click.help_option("-h", "--help")
@click.argument("filename")
def create(filename):
    assert filename[-3:] == ".md"
    if os.path.isfile(filename):
        raise ValueError("File with that name already exists")
    else:
        print(utils.PREAMBLE)
        with open(filename, "w") as file:
            file.write("# Project skeleton\n")
            for section, questions in utils.MARKDOWN_TEMPLATE.items():
                print("\nSection: {}".format(section))
                print("-------------------------------------------")
                file.write("\n## {}\n".format(section))
                for question in questions:
                    answer = utils.multiinput(question)
                    file.write(answer)
            file.close()


@main.command(help="run the the writing process tests")
@click.help_option("-h", "--help")
@click.argument("filename")
def test(filename):
    file_dictionary = utils.read_project_markdown(filename)
    print("================= test session starts ===================")
    for section, notes in file_dictionary.items():
        print("\nSection: {}".format(section))
        print("-------------------------------------------")
        for note in notes:
            print("\n{}".format(note))
            answer = input("Does the paragraph satisfy this note-test? y/[n]: ") or "n"
            if answer == "n":
                print("\033[31m" + "FAILED" + "\033[0m")
            else:
                print("\033[32m" + "PASSED" + "\033[0m")


if __name__ == "__main__":
    main()
