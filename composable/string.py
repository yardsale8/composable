from .pipeable import pipeable
import re


@pipeable
def split(sep, s):
    ''' splits s into a list of substrings based on sep. analogous to s.split(sep)
    
    args:
        sep: a string used to determine the splitting locations.
        s: the string being splits

    return:
        a list of strings, resulting from splitting s at each instance of sep.
        note that sep is removed in the process.
    '''
    return s.split(sep)


def split_re(pat):
    ''' creates a pipeable function that will split a string using a regular expression based on pat.
    
    args:
        pat: a regular expression pattern used to split strings.

    return:
        a list of strings, resulting from splitting s at each instance of sep.
        note that sep is removed in the process.

    notes:
        Call: 
            To provide efficient computation, split_re returns a pipeable function.
            To perform a regular call: split_re(pat)(s) 
            Use regular syntax for piping: or s >> split_re(pat)

        Partial application: 
            Is curried and can be combined with curried functions (i.e. map)
            Example: list_of_str >> composable.strict.map(split_re("(,|\t)"))
    '''
    r = re.compile(pat)
    return pipeable(lambda s: r.split(s))

