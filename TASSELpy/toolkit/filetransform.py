# Help ur copy and paste process from .java file to .py file

# import plyj.parser
__helper__ = "edit: inputfile and outputfile at the beginning"
__name__ == "Bokan"
import os
import os.path
import sys
import getopt

# parser = plyj.Parser()
# aa = parser.parse_file(file(r'F:\JavaBokan\Tassel\code\src\net\maizegenetics\dna\map\TOPMInterface.java'))

# print aa
JAVA_TYPE_KEY = {'int': "metaInteger",
                 'long': "metaInteger",
                 "short": "metaInteger",
                 'String': "metaString",
                 'boolean': "metaBoolean"}
JAVA_TYPE_OUT_KEY = {'int': 'None',
                     'long': 'None',
                     'String': 'None',
                     'double': 'np.float64',
                     'boolean': 'None',
                     'Byte': 'np.int8',
                     "short": 'np.int16'}

JAVA_IMPORT_STRING = {'int': "from TASSELpy.java.lang.Integer import metaInteger\n",
                      'long': "from TASSELpy.java.lang.Integer import metaInteger\n",
                      "short": "from TASSELpy.java.lang.Integer import metaInteger\n",
                      'String': "from TASSELpy.java.lang.String import metaString\n",
                      'boolean': "from TASSELpy.java.lang.Boolean import metaBoolean\n"}

JAVA_ARR_KEY = {'int[]': 'javaPrimativeArray.get_array_type(\'byte\')',
                'byte[]': 'javaPrimativeArray.get_array_type(\'byte\')',
                'long[]': 'javaPrimativeArray.get_array_type(\'long\')',
                'double[]': 'javaPrimativeArray.make_array_from_obj(\'double\')',
                'String[]': 'javaPrimativeArray.make_array_from_obj(\'string\')',
                'double[][]': 'javaArray.get_array_type(javaPrimativeArray.get_array_type(\'double\'))',
                'long[][]': 'javaArray.get_array_type(javaPrimativeArray.get_array_type(\'long\'))',
                'int[][]': 'javaArray.get_array_type(javaPrimativeArray.get_array_type(\'int\'))',
                'Object[][]': 'javaArray.get_array_type(javaPrimativeArray.get_array_type(\'Object\'))'
                }

JAVA_IMPORT_KEY = {'Phenotype': 'net/maizegenetics/trait/Phenotype',
                   'Tags': 'net/maizegenetics/dna/tag/Tags',
                   'Map': 'java/util/Map',
                   'Chromosome': 'net/maizegenetics/dna/map/Chromosome',
                   'Collection': 'java/util/Collection',
                   'MaxNumAlleles': 'net/maizegenetics/dna/snp/NucleotideAlignmentConstants/NUMBER_NUCLEOTIDE_ALLELES',
                   'ArrayList': 'java/util/ArrayList',
                   'UnmodifiableBitSet': 'net/maizegenetics/util/UnmodifiableBitSet',
                   'BitStorage': 'net/maizegenetics/dna/snp/bit/BitStorage',
                   'FilterGenotypeTable': 'net/maizegenetics/dna/snp/FilterGenotypeTable',
                   'IBSDistanceMatrix': 'net/maizegenetics/analysis/distance/IBSDistanceMatrix',
                   'BitSet': 'net/maizegenetics/util/BitSet',
                   'Set': 'java/util/Set',
                   'ProgressListener': 'net/maizegenetics/util/ProgressListener',
                   'List': 'java/util/List',
                   'TaxaListMatrix': 'net/maizegenetics/taxa/distance/TaxaListMatrix',
                   'AlleleDepth': 'net/maizegenetics/dna/snp/depth/AlleleDepth',
                   'AbstractPhenotype': 'net/maizegenetics/trait/AbstractPhenotype',
                   'Trait': 'net/maizegenetics/trait/Trait',
                   'TOPMInterfacelols': '/net/maizegenetics/dna/map/TOPMInterfacelols',
                   'TaxaListBuilder': 'net/maizegenetics/taxa/TaxaListBuilder',
                   'SimplePhenotype': 'net/maizegenetics/trait/SimplePhenotype',
                   'GenotypeCallTable': 'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable',
                   'LinkageDisequilibrium': 'net/maizegenetics/analysis/popgen/LinkageDisequilibrium',
                   'FisherExact': 'net/maizegenetics/stats/statistics/FisherExact',
                   'ByteGenotypeCallTable': 'net/maizegenetics/dna/dnp/genotypecall/ByteGenotypeCallTable',
                   'TOPMInterface': 'net/maizegenetics/dna/map/TOPMInterface',
                   'Boolean': 'java/lang/Boolean',
                   'AbstractGenotypeCallTable': 'net/maizegenetics/dna/snp/genotypecall/AbstractGenotypeCallTable',
                   'TagsOnGeneticMap': '/net/maizegenetics/dna/map/TagsOnGeneticMap',
                   'WHICH_ALLELE': 'net/maizegenetics/dna/WHICH_ALLELE',
                   'LDResult': 'net/maizegenetics/analysis/popgen/LDResult',
                   'SuperByteMatrixBuilder': 'net/maizegenetics/util/SuperByteMatrixBulider',
                   'TableReport': 'net/maizegenetics/util/TableReport.java',
                   'Byte': 'java/lang/Byte',
                   'Taxon': 'net/maizegenetics/taxa/Taxon',
                   'Object': 'java/lang/Object',
                   'TaxaList': 'net/maizegenetics/taxa/TaxaList',
                   'String': 'java/lang/String',
                   'DoubleMatrix2D': 'cern/colt/matrix/DoubleMatrix2D',
                   'genotypecall': 'net/maizegenetics/dna/snp/genotypecall',
                   'SetMultimap': 'com/google/common/collect/SetMultimap',
                   'SuperByteMatrix': 'net/maizegenetics/util/SuperByteMatrix',
                   'Kinship': 'net/maizegenetics/analysis/distance/Kinship',
                   'OpenBitSet': 'net/maizegenetics/util/OpenBitSet',
                   'Position': 'net/maizegenetics/dna/map/Position',
                   'ImportUtils': 'net/maizegenetics/dna/snp/ImportUtils',
                   'GeneralAnnotation': 'net/maizegenetics/util/GeneralAnnotation',
                   'PositionList': 'net/maizegenetics/dna/map/PositionList',
                   'GenotypeTable': 'net/maizegenetics/dna/snp/GenotypeTable',
                   'SiteScore': 'net/maizegenetics/dna/snp/score/SiteScore',
                   'DistanceMatrix': 'net/maizegenetics/taxa/distance/DistanceMatrix',
                   'CoreGenotypeTable': 'net/maizegenetics/dna/snp/CoreGenotypeTable'}

SYS_KEYWORDS = ["private", "public", "static", "abstract", "final", "synchronized", "enum", "final"]
TITLE_KEYWORDS = ['public', 'interface', 'private', 'extend', "static", "interface", "class"]
DELETE_KEYWORDS = ['public', 'interface', 'private', 'extend', "class", "static"]
TYPE = ['int', ]
KEYWORDS = ('this', 'class', 'void', 'super', 'extends', 'implements', 'enum', 'interface',
            'byte', 'short', 'int', 'long', 'char', 'float', 'double', 'boolean', 'null',
            'true', 'false',
            'final', 'public', 'protected', 'private', 'abstract', 'static', 'strictfp', 'transient', 'volatile',
            'synchronized', 'native',
            'throws', 'default',
            'instanceof',
            'if', 'else', 'while', 'for', 'switch', 'case', 'assert', 'do',
            'break', 'continue', 'return', 'throw', 'try', 'catch', 'finally', 'new',
            'package', 'import'
)
SPACE = "    "
DOUBLE_SPACE = SPACE * 2
TRIPLE_SPACE = SPACE * 3
TRI_QUOTE = "\"\"\""
ENTER = "\n"
TAB = "\t"
key = []


def collect_wait_key(string):
    if string is None:
        pass
    elif string in JAVA_IMPORT_KEY:
        pass
    else:
        global key
        key.append(string)


def get_dir(root_dir):
    name_list = []
    for root, dirs, files in os.walk(r"C:\Users\Administrator\Desktop\FUNCTION"):
        for string in files:
            if string.find(".py") != -1 and string.find(".pyc") == -1:
                if string.find("__init__.py") != -1:
                    pass
                else:
                    name_list.append(os.path.join(root, string))
    for i in name_list:
        print i
    return name_list


def _if_main(string):
    if string.find(SPACE) == 0:
        is_main = False
        string = string[4:]
    elif string[0] == "\t":
        is_main = False
        string = string[1:]
    else:
        is_main = True
    return is_main, string


# helper
# titile processing will return the subject of method
# titile_process

# yield string
# delete redundant space
def _prepare_name_string(string):
    if "{" in string:
        string = string[:string.find("{")]
    if ";" in string:
        string = string[:string.find(";")]
    if string[-1] == '\n':
        string = string[:-1]
    string = _remove_redun_space(string)
    return string, string


def _remove_redun_space(string):
    string = string.split(" ")
    string[:] = [x for x in string if x != ""]
    return " ".join(string)


def _remove_all_space(string):
    if string == "":
        return ""
    elif string[0] == " ":
        return _remove_all_space(string[1:])
    else:
        return string[0] + _remove_all_space(string[1:])


def _remove_sys_char(string):
    string = string.split(" ")
    edit_string = list(string)
    sys_char = []
    for i in string:
        if i in SYS_KEYWORDS:
            sys_char.append(i)
            edit_string.remove(i)
    return _remove_redun_space(" ".join(edit_string)), sys_char


def _title_parser(string):
    in_bra = 0
    word = ""
    add = ("(", "<")
    min = (")", ">")
    word_list = []
    for i in string:
        if i in add:
            if i == "(":
                # something(
                if word != "":
                    word_list.append(word)
                    word = "("
                else:
                    word += i
            else:
                # something<
                word += i
            in_bra += 1
        elif i in min:
            in_bra -= 1
            word += i
            if in_bra == 0:
                word_list.append(word)
                word = ""

        elif i == " ":
            if word != "":
                if word[-1] == ",":
                    word += i
                else:
                    if in_bra == 0:
                        word_list.append(word)
                        word = ""
                    else:
                        word += i if word[-1] != " " else ""
        else:
            word += i
    if word != "":
        word_list.append(word)
    return word_list


    # if found interface
    # return interface name and what it extends


def class_interf_detec(string_list):
    if "class" in string_list or "interface" in string_list:
        output = None
        type_fun = ""
        if "class" in string_list:
            name = string_list[string_list.index("class") + 1]
            type_fun = "class"
        else:
            #print string_list
            name = string_list[string_list.index("interface") + 1]
            assert type_fun == "", "type exists"
            type_fun = "interface"
        input_entry = []
        if "extends" in string_list:
            #print string_list
            #print string_list
            input_entry.append(string_list[string_list.index("extends") + 1])
        if "implements" in string_list:
            input_entry.append(string_list[string_list.index("implements") + 1])

    else:
        type_fun = "normal"
        if len(string_list) != 3:
            if len(string_list) == 2:
                output, name, input_entry = (None,) + tuple(string_list)
            elif len(string_list) == 1:
                output, name, input_entry = (None, string_list[0], [])
            elif len(string_list) > 3:
                output, name, input_entry = (string_list[-3], string_list[-2], string_list[-1])
        else:
            output, name, input_entry = tuple(string_list)
    return output, name, input_entry, type_fun


# use recursion to solve?

def _input_parser(string, input_list=None):
    if not input_list: input_list = []
    # print type(string)
    if string == "()":
        return []
    elif type(string) == list:
        for i in string:
            input_list = _input_parser(i, input_list)
        return input_list
    elif type(string) == str:
        if string[0] == "(":
            assert string[-1] == ")"
            string = string[1:-1]
        # print string
        in_bra = 0
        word = ""
        i_pre = ''
        for i in string:
            if i_pre == '':
                i_pre = i
                continue
            i_next = i
            i = i_pre
            if i == "<":
                # something<
                assert word != ""
                word += i
                in_bra += 1
            elif i == ">":
                in_bra -= 1
                word += i
                if in_bra == 0:
                    if i_next == ' ':
                        pass
                    else:
                        input_list.append(word)
                        word = ""
            elif i == ",":
                if in_bra == 0 and word != "":
                    input_list.append(word)
                    word = ""
            elif i == " ":
                if word != "":
                    word += i
            else:
                word += i
            i_pre = i_next
        i = i_pre
        if i == "<":
                # something<
                assert word != ""
                word += i
                in_bra += 1
        elif i == ">":
                in_bra -= 1
                word += i
                if in_bra == 0:
                    input_list.append(word)
                    word = ""
        elif i == ",":
                if in_bra == 0 and word != "":
                    input_list.append(word)
                    word = ""
        elif i == " ":
                if word != "":
                    word += i
        else:
                word += i
        if word != "":
            input_list.append(word)
        return input_list

def input_parser(string):
    return _input_parser(string)

def title_processing(string, main_name):
    # print "start processing "

    is_main, string = _if_main(string)

    # yield string
    # delete redundant space
    name_string, string = _prepare_name_string(string)

    # yield string

    string, sys_char = _remove_sys_char(string)
    # print string
    string_list = _title_parser(string)
    return_type, name, input_list, type_fun = class_interf_detec(string_list)
    if not is_main and type_fun == 'normal' and name == main_name:
        type_fun = 'constructor'
    if 'enum' in sys_char:
        type_fun = 'enum'
    # print input_list
    if input_list:
        input_list = _input_parser(input_list)
    input_arg = []
    for i in input_list:
        input_arg.append(_input_list_parser(i))

    args = (name_string, name, return_type, input_arg, is_main, type_fun, sys_char)
    print args
    # yield str(java_function(*args))
    if type_fun in ['class', ' interface'] or is_main:
        return MainFunction(*args)
    elif name == main_name:
        assert type_fun == 'constructor'
        return ConFunction(*args)
    elif type_fun == 'normal':
        return SubFunction(*args)
    elif type_fun == 'enum':
        return EnumFunction(*args)

    #string likes: int, index
    #          or: List<Taxa>
def _input_list_parser(string):
    #print "list_parser", type(string), string
    global import_prepare_list, java_imports_list

    try:
        a = import_prepare_list
        b = java_imports_list
    except:
        import_prepare_list = []
        java_imports_list = []


    if string.find('<') == -1:
        aa = string.split(" ")
        import_prepare_list.append(aa[0])
        java_imports_list.append(aa[0])
        return aa
    else:
        assert string.find(">") != -1, "format error: " + string
        if string.find(">") == len(string) -1:
            return [string, ""]
        string1 = string[:string.find(">") + 1]
        string2 = string[string.find(">") + 2:]
        import_prepare_list.append(string1)
        java_imports_list.append(string1)
        return [string1, string2]


def function_management(string, functin_list):
    a = title_processing(string)
    exist = False
    try:
        for fun in functin_list:
            if not exist and a.name == fun.name:
                fun.add_fun(a)
            elif exist and a.name == fun.name:
                raise TypeError
    except TypeError:
        print "function_list build error"


class JavaFunction():
    def __init__(self, name_string, name, return_type, input_list, ismain, type_fun, sys_char):
        assert type(name_string) == str, name_string
        assert type(return_type) == str or return_type is None, return_type
        assert type(name) == str, name
        assert type(input_list) == list, "Wrong type of inputlist"
        assert type(ismain) == bool
        assert type_fun in ['interface', 'class', 'normal', 'constructor','enum'], "error in type_fun"
        if type_fun in ['class', 'interface']:
            assert return_type is None, "format error " + name_string
        else:
            assert type_fun in ["constructor", "enum"] if return_type is None else "normal",  (type_fun,name_string)
        # test whether is constructure
        self.sys_char = sys_char
        self.type_fun = type_fun
        self.return_type = return_type
        self.input_list = input_list
        self.namestring = name_string
        self.name = name
        self.ismain = ismain
        self.before = ""
        self.inside = ""
        self.appendix = ''
        self.implement = ''

    def implement_output(self):
        pass

    def implement_input(self, string):
        assert type(string) == str
        self.implement = string

    def __str__(self):
        return self.namestring

    def overload(self):
        pass

    def overload_output(self):
        pass

    def imple_ouput(self):
        pass


class MainFunction(JavaFunction):
    def __init__(self, *args):
        JavaFunction.__init__(self, *args)
        self.fun = []
        #self.add_fun()

    def overload(self):
        # print self.type_fun
        global import_prepare_list, java_imports_list
        if self.type_fun not in ['normal', 'constructor']:
            return ""
        else:
            inp_tp_list = []
            inp_nm_list = []
            if self.input_list:
                for i in self.input_list:
                    if i[0] in JAVA_TYPE_KEY:
                        import_prepare_list.append(i[0])
                        t1 = "\'" + i[0] + "\'"
                        n1 = JAVA_TYPE_KEY[i[0]]
                    elif i[0] in JAVA_IMPORT_KEY:
                        t1 = "java_imports[\'" + i[0] + "\']"
                        import_prepare_list.append(i[0])
                        java_imports_list.append(i[0])
                        n1 = 'object'
                    elif i[0] in JAVA_ARR_KEY:
                        import_prepare_list.append(i[0])
                        t1 = "\'" + i[0] + "\'"
                        n1 = JAVA_ARR_KEY[i[0]]
                    else:
                        t1 = "\'Please Check\'"
                        n1 = "\'Please Check\'"
                    inp_tp_list.append(t1)
                    inp_nm_list.append(n1)
            if self.return_type == 'void'or self.return_type is None:
                out_tp = '\'void\''
                output_string = "(make_sig([" + ",".join(inp_tp_list) + "]," + out_tp + "),(" + \
                                ",".join(inp_nm_list) + "))"

            else:
                if self.return_type in JAVA_TYPE_OUT_KEY:
                    out_tp = '\'' + self.return_type + '\''
                    out_nm = JAVA_TYPE_OUT_KEY[self.return_type]
                elif self.return_type in JAVA_IMPORT_KEY:
                    out_tp = "java_imports[\'" + self.return_type + "\']"
                    out_nm = "\'Please Check\'"
                elif self.return_type in JAVA_ARR_KEY:
                    out_tp = '\'' + self.return_type + '\''
                    tip = JAVA_ARR_KEY[self.return_type]
                    out_nm = "lambda x: " + tip[:tip.find(")")] + ", x" + tip[tip.find(")"):]
                    #print out_nm
                    #a = raw_input("aa")
                else:
                    out_tp = '\'' + self.return_type + '\''
                    out_nm = "\'Please Check\'"
                output_string = "(make_sig([" + ",".join(inp_tp_list) + "]," + out_tp + "),(" + \
                                ",".join(inp_nm_list) + ")," + out_nm + ")"
        return output_string

    def overload_output(self):
        return SPACE + "_java_name = java_imports[\'" + self.name + "\']\n"

    def add_fun(self, obj=None):
        if obj is None:
            assert self.fun == [], "only first time can addfun have no param"

    def check_exists(self, fun_list):
        self.overload()

    def name_output(self):
        pass

    def infun_imple_putput(self):
        pass

    def format_output(self):
        assert type(self.input_list) == list
        #print 'name', self.name
        #print self.input_list
        ol = []
        for i in self.input_list:
            ol.append(' '.join(i))
        otstring = 'class ' + self.name + "(" + ", ".join(ol) + "):\n"
        return otstring


class SubFunction(MainFunction):
    def __init__(self, *args):
        MainFunction.__init__(self, *args)
        assert self.type_fun == 'normal' or "constructor", "subfunction should be normal or constructor" + str(self)

    def add_fun(self, obj=None):
        if obj is None:
            assert self.fun == [], "only first time can addfun have no param"

    # check_return the function(s) sharing the same name
    # and new combined fun itself
    def check_exists(self, fun_list):
        ex = 0
        for i in fun_list:
            if self.name == i.name:
                ex += 1
        assert ex >= 1, "fun not exists in fun_ist??! :<"
        self._combination(fun_list)
        return self

    def _combination(self, sm_list):
        self.name_string_list = []
        self.overload_list = []
        self.implement_list = []
        self.return_type_list = []
        self.input_list_list_bef_fun_output = []
        self.input_list_list_in_fun_output = []
        for i in sm_list:
            self.name_string_list.append(i.namestring)
            self.overload_list.append(i.overload())
            self.implement_list.append(i.implement_ouput())
            self.return_type_list.append(i.return_type)
            self.input_list_list_bef_fun_output.append(i.input_list_output_bef_fun())
            self.input_list_list_in_fun_output.append(i.input_list_output_in_fun())
        #for i in sm_list:
        #    if isinstance(i, ConFunction):
        #        print i.overload(), i.type_fun, "\nhaha"

    def implement_ouput(self):
        #print self.implement
        otstring = SPACE + ("\n" + SPACE + "#").join(self.implement.split("\n"))
        return otstring

    def overload_output(self):
        if 'static' in self.sys_char:
            output_string_title = SPACE + "@javaStaticOverload(\'" + self.name + "\'"
        else:
            output_string_title = SPACE + "@javaOverload(\'" + self.name + "\'"
        assert type(self.overload_list) == list
        output_list_iter = list(self.overload_list)
        for i in output_list_iter:
            # print i
            if i == '':
                #print self.overload_list
                #print "haha"
                self.overload_list.remove('')
                #print self.overload_list

        output_list = [output_string_title]
        output_list.extend(self.overload_list)
        return (",\n" + DOUBLE_SPACE).join(output_list) + ")"

    def input_list_output_bef_fun(self):
        if not self.input_list:
            return ""
        else:
            sl = []
            for i in self.input_list:
                sl.append(": ".join(i))
            for i in range(len(sl)):
                sl[i] = "\n" + SPACE + "#@param" + sl[i]
            return "".join(sl)

    def input_list_output_in_fun(self):
        if not self.input_list:
            return ""
        else:
            sl = []
            for i in self.input_list:
                sl.append(" -- ".join(i))
            return ("\n" + DOUBLE_SPACE).join(sl)

    def input_list_output_bef_fun_output(self):
        if self.input_list_list_bef_fun_output[0] is None:
            return None
        else:
            a = len(self.input_list_list_bef_fun_output[0])
            string = self.input_list_list_bef_fun_output[0]
            for i in self.input_list_list_bef_fun_output:
                assert type(i) == str
                if len(i) > a:
                    string = i
        return string

    def return_type_list_output(self):
        if self.return_type_list[0] is None:
            return None
        else:
            a = len(self.return_type_list[0])
            string = self.return_type_list[0]
            for i in self.return_type_list:
                assert type(i) == str
                if len(i) > a:
                    string = i
        return string

    def title_fun_output(self):
        return SPACE + "def " + self.name + "(self, *args):" + ENTER

    def format_output(self):
        bef_fun = self.implement_ouput() + \
                  SPACE + self.input_list_output_bef_fun_output() + ENTER
        bef_fun += SPACE + "#@Return" + self.return_type_list_output() + ENTER if self.return_type_list_output() != 'void' and self.return_type_list_output() is not None else ''
        bef_fun += self.overload_output() + ENTER
        title_fun = self.title_fun_output()

        if len(self.name_string_list) == 1:
            imple_fun = DOUBLE_SPACE + TRI_QUOTE + (SPACE).join(
                self.implement_ouput().split("#")) + "\n"
            imple_fun += DOUBLE_SPACE + "Signature:" + ENTER + ENTER + DOUBLE_SPACE + self.namestring + ENTER
            imple_fun += ENTER + DOUBLE_SPACE + "Arguments: " + ENTER + ENTER +\
                         DOUBLE_SPACE + self.input_list_output_in_fun() + ENTER \
                if self.input_list_output_in_fun() != '' else ''
            imple_fun += ENTER + DOUBLE_SPACE + "Return:" + ENTER + ENTER +\
                         DOUBLE_SPACE + self.return_type + ENTER \
                if self.return_type != 'void' and self.return_type is not None else ''
            imple_fun += DOUBLE_SPACE + TRI_QUOTE + ENTER + DOUBLE_SPACE + "pass" + ENTER + ENTER + ENTER

        else:
            imple_fun = DOUBLE_SPACE + TRI_QUOTE
            length = len(self.implement_list)
            for a in range(length):
                imple_fun += ENTER + DOUBLE_SPACE + self.name_string_list[a] + \
                             (DOUBLE_SPACE).join(self.implement_list[a].split("#"))
            imple_fun += ENTER + DOUBLE_SPACE + "Signature:" + ENTER
            for a in self.name_string_list:
                imple_fun += TRIPLE_SPACE + a + ENTER
            imple_fun += ENTER + DOUBLE_SPACE + "Arguments: " + ENTER + ENTER
            for a in range(length):
                imple_fun += DOUBLE_SPACE + self.name_string_list[a]
                ii = (DOUBLE_SPACE).join(self.input_list_list_bef_fun_output[a].split("#@param"))
                imple_fun += TRIPLE_SPACE + " --".join(ii.split(":")) + ENTER
            imple_fun += ENTER + DOUBLE_SPACE + "Return: " + ENTER + ENTER
            for a in range(length):
                if self.return_type_list[a] is None:
                    continue
                imple_fun += DOUBLE_SPACE + self.name_string_list[a] + ENTER
                imple_fun += TRIPLE_SPACE + self.return_type_list[a] + ENTER + ENTER
            imple_fun += DOUBLE_SPACE + TRI_QUOTE + ENTER + DOUBLE_SPACE + "pass" + ENTER + ENTER
        return bef_fun, title_fun, imple_fun, self.appendix


class ConFunction(SubFunction):
    def __init__(self, *args):
        SubFunction.__init__(self, *args)

    def overload_output(self):
        output_string_title = SPACE + "@javaConstructorOverload(java_imports[\'" + self.name + "\']"
        assert type(self.overload_list) == list
        output_list_iter = list(self.overload_list)
        #print self.overload_list
        for i in output_list_iter:
            # print i
            if i == '':
                #print self.overload_list
                #print "haha"
                self.overload_list.remove('')
                #print self.overload_list

        output_list = [output_string_title]
        output_list.extend(self.overload_list)
        return (",\n" + DOUBLE_SPACE).join(output_list) + ")"

    def title_fun_output(self):
        return SPACE + "def __init__(self, *args):" + ENTER

class EnumFunction(SubFunction):
    def __init__(self, *args):
        SubFunction.__init__(self, *args)

    def format_output(self):
        return ENTER+ SPACE + "#Need more edit" + \
               ENTER + SPACE + self.name + "java_enum(java_imports[\'main_name\']+\'$"+self.name + '\')'+ ENTER







def file_transform(program_dit, inputroot):
    title_string = []
    for file_name in get_files_indir_java(inputroot):
        # try:
        print "it is: " + file_name
        #for i in get_function_title(file_name):
        #    print i
        title_string.extend(get_function_title(file_name))

        # except Exception:
        # print "here is some error"
        # print file_name
        # sys.exit()
        title_string = list(title_string)

    title_edit_string = []
    for title in title_string:
        title_edit_string.append(str(title_processing(title)))
    title_string = "\n".join(title_string)
    title_edit_string = "\n".join(title_edit_string)
    toolkit_dir = os.path.join(program_dit, "java_title_keyword_kyky.py")
    global key
    print set(key)
    with open(toolkit_dir, "w")as text_file:
        text_file.write(title_string)
        text_file.write("\n\n\n")
        text_file.write(title_edit_string)


def get_function_title(file_name):
    print file_name
    input_line = open(file_name)
    string_list = []
    notfinished = False
    for i in input_line:
        if notfinished:
            if i.find(")") != -1 and i.find(";") == -1:
                notfinished = False
                string_list[-1] += i[:i.find("\n")]
            else:
                string_list[-1] += i[:i.find("\n")]

        else:
            for key in TITLE_KEYWORDS:
                if i.find(key) != -1 and i.find(";") == -1:
                    if i.find("(") != -1:
                        if i.find(")") != -1:
                            string_list.append(i[:i.find("\n")])
                            break
                        else:
                            string_list.append(i[:i.find("\n")])
                            notfinished = True
                            break
                    else:
                        string_list.append(i[:i.find("\n")])
                        break
    return string_list


def get_files_indir_java(address):
    # import sys
    # C:\Users\bb576\Documents\NetBeansProjects\code\src\net\maizegenetics\dna
    # sys.path.append(r'C:\Users\bb576\Dropbox\TASSELpy')
    # from toolkit.filetransform import get_files_indir_java
    name_list = []
    for root, dirs, files in os.walk(address):
        for string in files:
            # print files
            if string[-5:] == ".java":
                name_list.append(os.path.join(root, string))
    for i in name_list:
        print i
    return name_list


def _java_import_combo(name, index):
    return "\'" + name + "\':\'" + index + "\'"


    # @param import_list
    # @param import_java_list
    # @param java_function list
    # @param import_list
    #


def _initiate(inputfile, outputroot):
    print '\n\nstart init'
    import_list = "from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaStaticOverload\n" + \
                  "from utils.helper import make_sig\nimport numpy as np\n"
    sub_output = get_output_filename(inputfile)

    # net\maizegenetics\dna\Chromosome.java
    input_string_list = list(os.path.split(sub_output))
    # yield input_string_list
    # ('net\\maizegenetics\\dna', 'Chromosome.java')

    # get main_name of this .java file from name list
    main_name = input_string_list[-1].split('.')[0]
    # yield type(main_name)

    # get target file name in list
    input_string_list[-1] = main_name + '.py'
    # yield input_string_list
    # ['net\\maizegenetics\\dna', 'Chromosome.py']

    # get whole dir of target file
    outputfile = os.path.join(outputroot, *input_string_list)
    if not os.path.exists(os.path.split(outputfile)[0]):
        os.mkdir(os.path.split(outputfile)[0], 0754)
    #yield outputfile
    #C:\Users\bb576\Dropbox\TASSElpy\net\maizegenetics\dna\Chromosome.py

    input_string_list[-1] = main_name
    index = java_import_polish(_java_import_combo(main_name, os.path.join(*input_string_list)))
    #yield index
    #'Chromosome': 'net/maizegenetics/dna/Chromosome'
    #java_imports = {'Chromosome': 'net/maizegenetics/dna/Chromosome',} <-- here should add something
    import_java_list = ['java_imports = {' + index]
    print "\nEnd init\n"
    print 'Fun name is: ', main_name
    print 'Output addrs is: ', outputfile, "\n\n"
    return main_name, import_java_list, import_list, outputfile


def get_function_title_line(i, notfinished, string):
    if notfinished:
        if i.find(")") != -1 and i.find(";") == -1:
            notfinished = False
            string += i[:i.find("\n")]
        else:
            string += i[:i.find("\n")]
    else:
        for key in TITLE_KEYWORDS:
            if i.find(key) != -1 and i.find(";") == -1:
                if i.find("(") != -1:
                    if i.find(")") != -1:
                        string = i[:i.find("\n")]
                        break
                    else:
                        string = i[:i.find("\n")]
                        notfinished = True
                        break
                else:
                    string = i[:i.find("\n")]
                    break
    return notfinished, string


def into_doc_pro(i, main_fun, in_fun, in_doc):
    assert not in_doc
    ram = []
    if i == "/*\n" or i == "/**\n":
        if not main_fun:
            ram.append(TRI_QUOTE + ENTER)
        elif in_fun:
            ram.append(DOUBLE_SPACE + TRI_QUOTE)
    else:
        readline = i[i.find('/*') + 2:]
        if not main_fun:
            if readline[0] == "*":
                readline = readline[1:]
            ram.append("\"\"\"" + readline)
        else:
            if readline[0] == "*":
                readline = readline[1:]
            ram.append(readline)
    return ram


def in_doc_pro(i, main_fun, in_fun):
    if not i[i.find("*") + 1] == "\n":
        readline = i.split("* ")
        #print (readline)
        if not main_fun:
            readline = readline[-1]
        elif in_fun:
            readline = DOUBLE_SPACE + readline[-1]
        else:
            readline = readline[-1]
    else:
        readline = ''
    return readline


def file_transform1(inputfile, outputroot):
    if not os.path.isfile(inputfile): raise Exception("input file is not file in transform", inputfile)
    # input file
    global import_prepare_list, java_imports_list
    import_prepare_list = []
    java_imports_list = []
    main_name, import_java_list, import_list, outputfile = _initiate(inputfile, outputroot)

    input_line = open(inputfile)
    # first get import list
    # get sub dir of this file
    ram = []
    in_doc = False
    in_fun = False
    main_fun = False
    not_fun_ram = ''
    fun_name_notfinish = False
    title = ''
    in_fun_ram = ''
    java_function_list = []
    hit = False
    with open(outputfile, 'w')as text_file:
        for i in input_line:
            #print i
            if i.find("//") != -1:
                pass
            elif i.find('/*') != -1:
                #print "path 1"
                if in_doc: raise Exception("Error happens in path1", inputfile, i)
                ram = into_doc_pro(i, main_fun, in_fun, in_doc)
                in_doc = True
                if i.find('*/') != -1:
                    i = ram[0]
                    in_doc = False
                    readline = i[:i.find('*/')]
                    if not main_fun:
                        readline += "\"\"\"\n"
                        text_file.write(readline)
                        #else:
                        #    not_fun_ram = DOUBLE_SPACE.join(ram)
            elif i.find('*/') != -1:
                if not in_doc: raise Exception("Error happens in path2", inputfile, i)
                if not main_fun:
                    ram.append("\"\"\"\n")
                else:
                    not_fun_ram = DOUBLE_SPACE.join(ram)
                #print "path 2"
                #print ram
                ram = []
                in_doc = False
            elif i.find('*') != -1 and in_doc:
                ram.append(in_doc_pro(i, main_fun, in_fun))
            elif not in_doc:
                #print "path not indoc"
                if fun_name_notfinish:
                    if i.find(")") != -1 and i.find(";") == -1:
                        fun_name_notfinish = False
                        name_string += i[:i.find("\n")]
                    else:
                        name_string += i[:i.find("\n")]
                else:
                    for key in TITLE_KEYWORDS:
                        if i.find(key) != -1 and i.find("new") == -1 and i.find("throw") == -1:
                            if i.find(";") != -1:
                                if i.find("(") == -1 or i.find(")") == -1:
                                    break
                            #print i
                            hit = True
                            if i.find("(") != -1:
                                if i.find(")") != -1:
                                    name_string = i[:i.find("\n")]
                                    break
                                else:
                                    name_string = i[:i.find("\n")]
                                    fun_name_notfinish = True
                                    break
                            else:
                                name_string = i[:i.find("\n")]
                                break
                if hit and not fun_name_notfinish:
                    fun = title_processing(i, main_name)
                    java_function_list.append(fun)
                    #pr int i[:4], "i[:4]"
                    if not fun.ismain and main_fun:
                        #print "this is sub class"
                        in_fun = True
                        #print "path3"
                        #print string
                        #print "not_fun_ram\n", not_fun_ram
                        k = not_fun_ram.split("@")
                        not_fun_ram = ''
                        #print k
                        if i_previous.find("    @Override") != -1:
                            fun.implement_input('#@Override')
                        else:
                            fun.implement_input(_remove_redun_space(k[0]))
                        #print "implement", fun.implement
                        #print "end"
                        in_fun = False
                    else:
                        if main_fun: raise Exception("error in path 4", i + str(main_fun))
                        main_fun = True
                        #print "path4"
                if not hit and main_fun:
                    pass
                    #print "path5"
                    #java_function_list[-1].appendix += i
                elif not fun_name_notfinish:
                    hit = False
            i_previous = i

        java_function_list = _fun_group(java_function_list)
        import_prepare_list = list(set(list(import_prepare_list)))
        java_imports_list = list(set(list(java_imports_list)))
        java_import_string_list = []
        for i in import_prepare_list:
            if i in JAVA_TYPE_KEY:
                java_import_string_list.append(JAVA_IMPORT_STRING[i])
            elif i in JAVA_IMPORT_KEY:
                java_import_string_list.append(_package_import_key_modifier(i, JAVA_IMPORT_KEY[i]))
            elif i in JAVA_ARR_KEY:
                java_import_string_list.append(
                    "from TASSELpy.utils.primativeArray import javaPrimativeArray\nfrom TASSELpy.javaObj import javaArray")
        for i in java_imports_list:
            if i in JAVA_IMPORT_KEY:
                import_java_list.append(_java_imports_list_modifier(i, JAVA_IMPORT_KEY[i]))

        text_file.write(import_list)
        text_file.write('\n'.join(java_import_string_list) + ENTER)
        text_file.write((",\n" + DOUBLE_SPACE).join(import_java_list) + "}" + ENTER)

        for fun in java_function_list:
            try:
                print str(fun)
                for i in fun.format_output():
                    text_file.write(i)
            except:
                print str(fun), " has some error"


def _java_imports_list_modifier(i, string):
    assert type(string) == str
    return "\'" + i + "\': \'" + string + "\'"


def _package_import_key_modifier(i, string):
    assert type(string) == str
    k = ".".join(string.split("/"))
    return "from TASSELpy." + k + " import " + i


def _fun_group(java_function_list):
    assert java_function_list[0].ismain
    main = java_function_list[0]
    java_function_list.remove(java_function_list[0])
    fun_grp_list = []
    matched = False
    con_exists = False
    for i in java_function_list:
        if isinstance(i, ConFunction):
            con_exists = True
        if not fun_grp_list:
            fun_grp_list.append([i])
            matched = True
        for liter in fun_grp_list:
            if not matched and i.name == liter[0].name:
                liter.append(i)
                matched = True
        if matched:
            matched = False
        else:
            fun_grp_list.append([i])
    fun_grp_list.insert(0, [main])
    if not con_exists:
        fun_grp_list.insert(1,[ConFunction(main.namestring, main.name, main.return_type,
                                          main.input_list, False, 'constructor', main.sys_char)])
    cb_fun_list = []
    for flist in fun_grp_list:
        flist[0].check_exists(flist)
        cb_fun_list.append(flist[0])
    return cb_fun_list


# def address_prepare():


def check_files_exist(file_list):
    """
    param
    list
    of
    string

    """
    assert type(file_list) is list and file_list != [] and type(file_list[0]) is str, \
        ("error in file_list, which should be a list of string", file_list)

    for file_name in file_list:
        assert os.path.isfile(file_name), (file_name, "file not exists")


def check_dirs_exist(file_list):
    """
    param
    list
    of
    string

    """
    assert type(file_list) is list and file_list != [] and type(file_list[0]) is str, \
        ("error in file_list, which should be a list of string", file_list)

    for file_name in file_list:
        assert os.path.isdir(file_name), (file_name, "file not exists")


def get_files_indir_py(address):
    name_list = []
    for root, dirs, files in os.walk(address):
        for string in files:
            # print files
            if string.find(".py") != -1 and string.find(".pyc") == -1:
                if string.find("__init__.py") != -1:
                    pass
                else:
                    name_list.append(os.path.join(root, string))
    for i in name_list:
        print i
    return name_list


def get_files_indir(address):
    """
    return
    list -- the files' name list"""
    name_list = []
    for root, dirs, files in os.walk(address):
        for string in files:
            name_list.append(os.path.join(root, string))
    #for i in name_list:
    #    print i
    return name_list


def get_output_filenames(address_list):
    dir_list = []
    for i in address_list:
        dir_list.append(get_output_filename(i))
    return dir_list


def get_output_filename(address):
    assert type(address) is str, "Type error"
    address_file_name = []
    new_split = os.path.split(address)
    #print new_split
    address_file_name.append(new_split[1])
    old_address = new_split[0]
    while address_file_name[0] != "net":
        #print address_file_name[0]
        new_split = os.path.split(old_address)
        address_file_name.insert(0, new_split[1])
        old_address = new_split[0]
    return os.path.join(*address_file_name)


def junction(input, output):
    try:
        if type(input) is list:
            for name_iter in input:
                file_transform(name_iter, output)
        else:
            if type(input) is str:
                file_transform(input, output)
            else:
                raise TypeError
    except TypeError:
        print "input error"


def get_java_keyword(program_dir, inputroot):
    keywords = []

    for file_name in get_files_indir_py(inputroot):
        try:
            print "it is: " + file_name
            keywords.extend(get_java_imports(file_name))

        except Exception:
            # print "here is some error"
            # print file_name
            # sys.exit()
            keywords = list(set(keywords))
    keywords = (",\n" + SPACE).join(keywords)
    toolkit_dir = os.path.join(program_dir, "java_imports_keyword.py")
    with open(toolkit_dir, "w")as text_file:
        text_file.write("JAVA_IMPORT_KEY = {")
        text_file.write(keywords)
        text_file.write("}")


def get_java_imports(file_name):
    file_string = open(file_name)
    in_string = False
    for i in file_string:

        if in_string:
            if i.find("}") == -1:
                java_imports.append(i[i.find("\'"):i.find("\n")])
            else:
                java_imports.append(i[i.find("\'"):i.find("}")])
                break
        if not in_string and i.find("java_imports") != -1 and i.find("{") != -1:
            in_string = True
            i = i[i.find("{") + 1:i.find("\n")]
            if i.find("}") != -1:
                i = i[:i.find("}")]
                in_string = False
            java_imports = [i]
    print "java_imports"
    print java_imports
    for order in range(len(java_imports)):
        java_imports[order] = java_import_polish(java_imports[order])
    for string_query in java_imports:
        print string_query
    return java_imports

    # for different format in java_import


def java_import_polish(dict_query):
    assert type(dict_query) is str, "not string"
    # print "dict_query in import_polish: ", dict_query
    dict_query = str(dict_query.replace(",", ""))
    dict_query = str(dict_query.replace(" ", ""))
    assert dict_query.find(":") != -1, "Wrong query, no : exists : " + dict_query
    split_dict_query = dict_query.split(":")
    assert len(split_dict_query) == 2
    # print split_dict_query
    if "/" in split_dict_query[1]:
        split_dict_query[1] = "/".join(split_dict_query[1].split("/"))
        # print split_dict_query
    else:
        if "." in split_dict_query[1]:
            split_dict_query[1] = "/".join(split_dict_query[1].split("."))
        else:
            assert "\\" in split_dict_query[1], dict_query
            split_dict_query[1] = "/".join(split_dict_query[1].split("\\"))
    print ": ".join(split_dict_query)
    return ": ".join(split_dict_query)
    # output is like this 'FisherExact': 'net/maizegenetics/stats/statistics/FisherExact'


if __name__ == '__main__':
    # filetransform -i address1 -o -address2, if not exists, raise errors
    input_address = ""
    output_root = ""
    input_java = ""
    program_dir = os.path.split(sys.argv[0])[0]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:j:t:", ["input=", "output=", "--javaimport", "--gettitle"])
        for o, a in opts:
            if o in ("-i", "--input"):
                input_address = a
                if os.path.isfile(input_address):
                    print "input is file: " + input_address
                    name = input_address
                else:
                    if os.path.isdir(input_address):
                        print "input is a dir: " + input_address
                        name = get_files_indir(input_address)
                    else:
                        raise Exception("input:", input_address)
            if o in ("-o", "--output"):
                output_root = a
                if os.path.isdir(output_root):
                    if os.path.exists(os.path.join(output_root, "net")):
                        output = output_root
                        print "The output addres is: " + output_root
                    else:
                        raise Exception("no net/maizegenetics:", output_root)
                else:
                    raise Exception("output:", output_root)
            if o in ("-j", "--javaimport"):
                # should have net and maizegenetics
                input_java = a
                case = "j"
                raise AssertionError

            if o in ("-t", "--gettitle"):
                # should have net and maizegenetics
                input_java = a
                case = "t"
                raise AssertionError

    except AssertionError:
        if case == "j":
            get_java_keyword(program_dir, input_java)
            os._exit(0)
        if case == "t":
            file_transform(program_dir, input_java)
            os._exit(0)
    except Exception as inst:
        x = inst.args[0]
        y = inst.args[1]
        print x, y, "not such directory found"

    if type(name) == str:
        file_transform1(name, output_root)





            # junction(name, output_address)
            # get_files_indir(address)
            # get_file(address)

            # args = sys.argv
            # C:\Python27\Lib\site-packages\TASSELpy\net\maizegenetics
    # input file exist?
    # output file exist?
    # if not exist: create one
    #
    """
    if len(args) == 1:
        input_address = raw_input("Please enter the file's input directory: \n")
        output_address = raw_input("Please enter the file's input directory: \n")
    else:
        input_address = address_prepare(args[1])
        output_address = address_prepare(args[2])

        #inputfile = r"F:\JavaBokan\Tassel\code\src\net\maizegenetics\dna\map\TagsOnGeneticMap.java"
        #process(inputfile)

        #parser = plyj.Parser()
        #aa = parser.parse_file(file(r'F:\JavaBokan\Tassel\code\src\net\maizegenetics\dna\map\TOPMInterface.java'))
        #tree = parser.parse_string('class Foo { }')

        #aa = str(aa)
        #print aa"""