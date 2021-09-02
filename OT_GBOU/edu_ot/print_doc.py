import win32api
import win32print

def print_doc(filepath, filename):
    f = '"' + filepath + filename + '"'
    win32api.ShellExecute(0, "printto", f, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)