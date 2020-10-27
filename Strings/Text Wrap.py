import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

    # # wrap text width
    # wrapper = textwrap.TextWrapper(width = max_width)
    # # cut the text to array[]
    # word_list = wrapper.wrap(text = string)
    # return '\n'.join(word_list)


if __name__ == '__main__':
    string, max_width = input(), int(input()) # => string = input() | max_width = int(input())
    result = wrap(string, max_width)
    print(result)
