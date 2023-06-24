import math

from custom_type import Fun


FUNCTIONS = [
    Fun(description="f(x) = x", f=lambda x: x, short_description="x"),
    Fun(description="f(x) = ln(x)", f=lambda x: math.log(x), short_description="ln(x)"),
    Fun(description="f(x) = exp(x)", f=lambda x: math.e**x, short_description="exp(x)"),
    Fun(description="f(x) = sin(x)", f=lambda x: math.sin(x), short_description="sin(x)"),
    Fun(description="f(x) = tg(x)", f=lambda x: math.tan(x), short_description="tg(x)"),
    Fun(description="f(x) = cos(x)", f=lambda x: math.cos(x), short_description="cos(x)"),
    Fun(description="f(x) = ctg(x)", f=lambda x: math.cos(x) / math.sin(x), short_description="ctg(x)"),
]
