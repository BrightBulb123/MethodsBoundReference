import re
from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ["VCAALexer"]


class VCAALexer(RegexLexer):
    name = "VCAA_Pseudocode"
    aliases = ["vcaa"]
    filenames = ["*.vcaa"]

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    tokens = {
        "root": [
            (r"\s+", Whitespace),
            (r"Import", Keyword.Namespace, "import"),
            (r"Define", Keyword.Declaration, "function"),
            (r"If|Else|Then|For|From|To|Step|Do|EndFor|While|EndWhile|Return", Keyword),
            (r"Empty|True|False", Keyword.Constant),
            (
                r"Int|Float|String|Boolean|Function|Namespace",
                Keyword.Type,
            ),
            (r"Print|Exit", Name.Builtin),
            (r"Not|Xor|And|Or", Operator.Word),
            (r"[+\-*/^×÷=:!←><]", Operator),
            (r"\.{3}", Punctuation),
            (r"[[\](),]", Punctuation),
            (r"#.*?$", Comment.Single),
            (r'"(\\.|[^"])*"', String.Double),
            (r"'(\\.|[^'])*'", String.Single),
            (r"%", String.Escape),
            (r"\d+\.\d+", Number.Float),
            (r"\d+", Number.Integer),
            (r"[A-Z][A-Z0-9_]*", Name.Constant),
            (r"[A-Za-z_][A-Za-z0-9_]*", Name),
        ],
        "function": [
            (r"\s+", Whitespace),
            (r"[A-Za-z_][A-Za-z0-9_]*", Name.Function, "#pop"),
            (r"\(", Punctuation, "parameters"),
        ],
        "parameters": [
            (r"\s+", Whitespace),
            (r"[A-Za-z_][A-Za-z0-9_]*", Name.Variable, "parameters"),
            (r",", Punctuation),
            (r"\)", Punctuation, "#pop"),
        ],
        "import": [
            (r"\s+", Whitespace),
            (r"[A-Za-z_][A-Za-z0-9_, ]*", Name.Namespace, "#pop"),
        ],
    }
