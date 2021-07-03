"""
    domonic.utils
    ====================================
    snippets etc
"""
import typing
import random
from re import sub
from itertools import chain, islice
from collections import Counter


class Utils(object):
    """ utils """

    @staticmethod
    def case_camel(s: str):
        """ case_camel('camel-case') > 'camelCase' """
        s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
        return s[0].lower() + s[1:]

    @staticmethod
    def case_snake(s: str):
        """
        snake('camelCase') # 'camel_case'
        """
        return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            s.replace('-', ' '))).split()).lower()

    @staticmethod
    def case_kebab(s: str):
        """
        kebab('camelCase') # 'camel-case'
        """
        return '-'.join(
            sub(r"(\s|_|-)+", " ",
            sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
            lambda mo: ' ' + mo.group(0).lower(), s)).split())

    @staticmethod
    def squash(the_list: list):
        """[turns a 2d array into a flat one]

        Args:
            the_list ([type]): [a 2d array]

        Returns:
            [type]: [a flattened 1d array]
        """
        return [inner for outer in the_list for inner in outer]

    @staticmethod
    def chunk(list: list, size: int):
        """ chunk a list into batches """
        return [list[i:i + size] for i in range(0, len(list), size)]

    @staticmethod
    def dictify(arr: str):
        """[turns a list into a dictionary where the list items are the keys]

        Args:
            arr ([type]): [list to change]

        Returns:
            [type]: [a new dict where the list items are now the keys]
        """
        return dict().fromkeys(arr, 0)

    @staticmethod
    def is_empty(some_str):
        return (not some_str.strip())

    @staticmethod
    def unique(some_arr):
        """[removes duplicates from a list]

        Args:
            some_arr ([type]): [list containing duplicates]

        Returns:
            [type]: [a list containing no duplicates]
        """
        return list(set(some_arr))

    @staticmethod
    def chunks(iterable, size, format=iter):
        """ Iterate over any iterable (list, set, file, stream, strings, whatever), of ANY size """
        it = iter(iterable)
        while True:
            yield format(chain((it.next(),), islice(it, size - 1)))
    # >>> l = ["a", "b", "c", "d", "e", "f", "g"]
    # >>> for chunk in chunks(l, 3, tuple):
    # ...         print chunk

    @staticmethod
    def clean(lst):
        """[removes falsy values (False, None, 0 and “”) from a list ]

        Args:
            lst ([type]): [lst to operate on]

        Returns:
            [type]: [a new list with falsy values removed]
        """
        return list(filter(None, lst))

    @staticmethod
    def get_vowels(string: str):
        """[get a list of vowels from the word]

        Args:
            string ([type]): [the word to check]

        Returns:
            [type]: [a list of vowels]
        """
        return [each for each in string if each in 'aeiou']

    @staticmethod
    def untitle(string: str):
        """[the opposite of title]

        Args:
            str ([type]): [the string to change]

        Returns:
            [type]: [a string with the first character set to lowercase]
        """
        return string[:1].lower() + string[1:]

    @staticmethod
    def merge_dictionaries(a, b):
        """[merges 2 dicts]

        Args:
            a ([type]): [dict a]
            b ([type]): [dict b]

        Returns:
            [type]: [a new dict]
        """
        return {**a, **b}

    @staticmethod
    def to_dictionary(keys, values):
        """[take a list of keys and values and returns a dict]

        Args:
            keys ([type]): [a list of keys]
            values ([type]): [a list of value]

        Returns:
            [type]: [a dictionary]
        """
        return dict(zip(keys, values))

    @staticmethod
    def most_frequent(list):
        return max(set(list), key=list.count)

    @staticmethod
    def anagram(first, second):
        return Counter(first) == Counter(second)

    @staticmethod
    def frequency(data):
        """[check the frequency of elements in the data]

        Args:
            data ([type]): [the data to check]

        Returns:
            [type]: [a list of elements and their frequency]
        """
        freq = {}
        for elem in data:
            if elem in freq:
                freq[elem] += 1
            else:
                freq[elem] = 1
        return freq

    @staticmethod
    def init_assets(dir: str = 'assets'):
        """[creates an assets directory with nested js/css/img dirs]

        Args:
            dir (str, optional): [default directory name]. Defaults to 'assets'.
        """
        from domonic.terminal import mkdir, touch
        mkdir(f"{dir}")
        mkdir(f"{dir}/js")
        mkdir(f"{dir}/css")
        mkdir(f"{dir}/img")
        touch(f"{dir}/js/master.js")
        touch(f"{dir}/css/style.css")
        return

    @staticmethod
    def url2file(url: str):
        """[gen a safe filename from a url. by replacing '/' for '_' and ':' for '__' ]

        Args:
            url ([type]): [the url to turn into a filename]

        Returns:
            [type]: [description]
        """
        import urllib
        url = "_".join(url.split("/"))
        url = "__".join(url.split(":"))
        filename = urllib.parse.quote_plus(url, '')
        return filename

    @staticmethod
    def permutations(word: str):
        """[provides all the possible permutations of a given word]

        Args:
            word ([type]): [the word to get permutations for]

        Returns:
            [type]: [description]
        """
        from itertools import permutations
        return [''.join(perm) for perm in list(permutations(word))]

    @staticmethod
    def random_color(self):
        ''' TODO - remove in 0.3 as we have color class. '''
        r = lambda: random.randint(0, 255)
        return str('#%02X%02X%02X' % (r(), r(), r()))

    @staticmethod
    def escape(s: str):
        """[escape a string]

        Args:
            s ([type]): [the string to escape]

        Returns:
            [type]: [description]
        """
        chars = {
            "&": "&amp;",
            '"': "&quot;",
            "'": "&apos;",
            ">": "&gt;",
            "<": "&lt;"
        }
        return "".join(chars.get(c, c) for c in s)

    @staticmethod
    def unescape(s: str):
        """[unescape a string]

        Args:
            s ([type]): [the string to unescape]

        Returns:
            [type]: [description]
        """
        s = s.replace("&lt;", "<")
        s = s.replace("&gt;", ">")
        s = s.replace("&quot;", '"')
        s = s.replace("&apos;", "'")
        s = s.replace("&amp;", "&")
        return s

    @staticmethod
    def replace_between(content: str, match: str, replacement: str, start: int=0, end: int=0):
        """[replace some text but only between certain indexes]

        Args:
            content (str): [the content whos text you will be replacing]
            match (str): [the string to find]
            replacement (str): [the string to replace it with]
            start (int, optional): [start index]. Defaults to 0.
            end (int, optional): [end index]. Defaults to 0.

        Returns:
            [type]: [description]
        """
        front = content[0:start]
        mid = content[start:end]
        end = content[end:len(content)]
        mid = mid.replace(match, replacement)
        return front + mid + end

    @staticmethod
    def truncate(text='', length=0):
        """[truncates a string and appends 3 dots]

        Args:
            text (str, optional): [the text to truncate]. Defaults to ''.
            length (int, optional): [the max length]. Defaults to 0.

        Returns:
            [type]: [description]
        """
        if len(text) > length:
            return text[0:length] + "..."
        else:
            return text + "..."

    # def any_iter(arr):
    #     ''' given a list. returns random until expired '''
    #     random.shuffle(arr)
    #     return (x for x in arr)

    # @staticmethod
    # def unless(value, condition):
        # return value if condition else not value
        # if any(pred(x.item) for x in sequence):

    # TODO -
    # def beautfiy(): # make nice
    # def uglify(): # make not nice
    # def simplify(sentence): # reduce a sentence to its meaning. remove uneeded words.
    # def factualise():  # returns json document of modelled info from general text
