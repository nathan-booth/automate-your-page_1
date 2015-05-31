# html generator

def generate_html_frame(section_title, section_text):
    '''
    str, str -> str

    Input title and text strings, then output HTML code framework as strings.

    '''

    html_text_1 = '''
    <div class="section">
        <div class="section-title">
            ''' + section_title
    html_text_2 = '''
        </div>
        <div class="section-text">
            ''' + section_text
    html_text_3 = '''
        </div>
    </div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(section):
    start_location = section.find("TITLE:")
    end_location = section.find('DESCRIPTION:')
    return section[start_location + 7 : end_location - 1]


def get_description(section):
    start_location = section.find('DESCRIPTION:')
    return section[start_location + 13 : ]

def get_section_by_number(text, section_number):
    '''
    str, int -> str

    Pass str text and int section_number to return the section title and description as a str.

    '''

    counter = 0
    while counter < section_number:
        counter += 1
        next_section_start = text.find('TITLE:')
        next_section_end = text.find('TITLE:', next_section_start + 1)
        section = text[next_section_start : next_section_end]
        text = text[next_section_end : ]
    return section

def generate_all_html(text):
    '''
    str -> str

    Input a formatted str and return a complete body of HTML code.

    '''
    section_number = 1
    section = get_section_by_number(text, section_number)
    all_html = ""
    while section != "":
        title = get_title(section)
        description = get_description(section)
        section_html = generate_html_frame(title, description)
        all_html += section_html
        section_number += 1
        section = get_section_by_number(text, section_number)
    return all_html

# v.1 of make_HTML
# def make_HTML(section):
#     for item in section:
#         section_title = section[0]
#         section_text = section[1]
#     return generate_html_frame(section_title, section_text)

def make_HTML(section_list):
    '''
    list -> str

    Input a list of lists with section titles and associated text. Return a formatted str
    of HTML.

    '''

    html_text = ""
    for section in section_list:
        section_title = section[0]
        section_text = section[1]
        html_text += generate_html_frame(section_title, section_text)
    return html_text

programming_topics = [['Computers and Programming', '''A computer is a machine that can
execute a program. A program describes a sequence of steps for the computer to execute.
Programs are written in a programming language, which is a constructed language for 
writing computer programs. Python is a programming language. Python uses an interpreter,
which allows programmers to use this high-level language to write in a way that more 
closely resembles human written language.
An expression is something that has a value. Expressions use combinations of data types,
operators, variables, and other expressions. Basic data types include integers (int),
floating-point numbers (float), strings (str), Boolean values (Bool), and lists (list).
Operators include arithmetic (addition, subtraction, multiplication, exponentiation,
division, modulo) and logical (and, or, not, equal to, less than, greater than, etc.)
operators. A variable stores a value on the computer. Assignment refers to
associating some value to a variable. Beware the dangers of aliasing, when a value
is referenced in multiple locations, because changing a value in one location
changes it for every case associated with that location.'''], ['Strings and Lists',
'''Strings are immutable. Lists are mutable and structured, which generally makes them
more powerful than strings. Both data types are indexed similarly.'''], ['Strings and Lists',
'''Strings are immutable. Lists are mutable and structured, which generally makes 
them more powerful than strings. Both data types are indexed similarly.'''], ['Functions',
'''A function is like a sub-program that executes a specific task within a larger
program. Judicious use reduces the amount of code a programmer must write and allows
a program to be built as a series of sub-programs that can be built, tested,
and re-used. This simplifies the task of writing complex programs. Functions take
some input(s) or parameter(s) and return some output(s).'''], ['Control Flow',
'''Control flow refers to specifying the order that tasks are executed. Some tasks
need to be repeated until some endpoint is reached or condition is met; for and
while are used, respectively, sometimes in conjunction with break. Some tasks
only take place if a certain condition is met; these are conditional statements
like if, then, else. If a condition is met, then the code in the block will be
executed.'''], ['Debugging', '''Examine error messages. Work from example code
and understand the desired inputs and outputs. Test examples. Check intermediate
results with the prodigious use of print statements. Record and compare previous
versions and results.
To help minimize the debugging process, break down problems into simple pieces
that can be tested individually and fit together.''']]

print make_HTML(programming_topics)