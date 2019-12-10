from dataclasses import dataclass, asdict, make_dataclass, field, fields
from typing import Literal, TypedDict, Callable, NewType, Generic
from enum import IntEnum

frozendc = dataclass(init=False, frozen=True)
reset = make_dataclass('MyReset', [('normal', Literal[0], field(default=0)),
                                   ('italic', Literal[23], field(default=23)),
                                   ('ul', Literal[24], field(default=24)),
                                   ('inverse', Literal[27], field(default=27)),
                                   ('strike', Literal[29], field(default=29)), ]
                       )()


@dataclass
class Indexable:
    def __getitem__(self, item):
        t = asdict(self)
        return t[item]


@dataclass
class Reset:
    normal: Literal[0] = 0
    italic: Literal[23] = 23
    underline: Literal[24] = 24
    inverse: Literal[27] = 27
    strike: Literal[29] = 29

    def __getitem__(self, item):
        t = asdict(self)
        return t[item]

Reset.lol = 'hi'
ResetKey = NewType('ResetKey', int)
# foo: ResetKey = ResetKey(fields(Reset))


class ResetEnum(IntEnum):
    normal: Literal[0] = 0
    italic: Literal[23] = 23
    underline: Literal[24] = 24
    inverse: Literal[27] = 27
    strike: Literal[29] = 29


@frozendc
class SatBG(Indexable):
    grey: Literal[100] = 100
    red: Literal[101] = 101
    green: Literal[102] = 102
    yellow: Literal[103] = 103
    blue: Literal[104] = 104
    purple: Literal[105] = 105
    turquoise: Literal[106] = 106
    white: Literal[107] = 107


@frozendc
class Sat(Indexable):
    bg: SatBG = SatBG()
    red: Literal[91] = 91
    green: Literal[92] = 92
    yellow: Literal[93] = 93
    blue: Literal[94] = 94
    purple: Literal[95] = 95
    turquoise: Literal[96] = 96
    white: Literal[97] = 97


@frozendc
class BG(Indexable):
    grey: Literal[40] = 40
    red: Literal[41] = 41
    green: Literal[42] = 42
    yellow: Literal[43] = 43
    blue: Literal[44] = 44
    purple: Literal[45] = 45
    turquoise: Literal[46] = 46
    white: Literal[47] = 47


@frozendc
class ColorCodes(Indexable):
    bg: BG = BG()
    sat: Sat = Sat()
    reset: Reset = Reset()
    bold: Literal[1] = 1
    grey: Literal[2] = 2
    italic: Literal[3] = 3
    ul: Literal[4] = 4
    inverse: Literal[7] = 7
    strike: Literal[9] = 9
    doubleul: Literal[21] = 21
    red: Literal[31] = 31
    green: Literal[32] = 32
    yellow: Literal[33] = 33
    blue: Literal[34] = 34
    purple: Literal[35] = 35
    turquoise: Literal[36] = 36
    white: Literal[37] = 37
    darkgrey: Literal[90] = 90


COLOR_CODES = ColorCodes()
reset2 = Reset()

# print(COLOR_CODES.reset['normal'])
# print(ResetEnum['italc'])
# print(reset2.__getitem__('italc'))
# print(foo)
