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
    "Conclusions": ["What are your conclusions?: "],
    "Abstract": ["Write an abstract for your work: "],
}

PREAMBLE = """                SCRIBE
    A small tool to help with scientific
    writing projects. Answer the question
    prompts with short notes that act as
    unit tests. These notes should breifly
    detail the purpose or operation of a
    paragraph or short section. """


def multiinput(question):
    answer = input(question)
    new_lines = [answer]
    while True:
        new_line = input()
        if new_line:
            new_lines.append(new_line)
        else:
            break
    answer = "\n".join(new_lines)
    return answer


def read_project_markdown(filename):
    assert filename[-3:] == ".md"
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    lines_no_empty = [line for line in lines if line]
    section_indices = []
    last_index = len(lines_no_empty)
    keys = list(MARKDOWN_TEMPLATE.keys())
    keys.reverse()
    for key in keys:
        section_index = lines_no_empty.index("## {}".format(key))
        section_indices.append((section_index, last_index))
        last_index = section_index
    section_indices.reverse()
    output_dict = {
        key: [lines_no_empty[k] for k in range(i + 1, j)]
        for key, (i, j) in zip(MARKDOWN_TEMPLATE.keys(), section_indices)
    }
    return output_dict
