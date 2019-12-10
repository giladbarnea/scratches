def safe(fn, *dec_args):
    def _shelter(*fn_args, **fn_kwargs):
        try:
            return fn(*fn_args, **fn_kwargs)
        except:
            return False

    return _shelter


@safe
def raises():
    return 1 / 0


@safe
def doesnt_raise():
    return 1 / 1


@safe
def maybe_raises(denom):
    return 2 / denom


@safe
def div(num, denom):
    return num / denom


@safe
def loud_div(num, denom, *, msg):
    print(msg)
    return num / denom


print(raises())  # False
print(doesnt_raise())  # 1.0
print(maybe_raises(0))  # False
print(maybe_raises(1))  # 2.0
print(div(3, 0))  # False
print(div(3, 1))  # 3.0
print(loud_div(4, 0, msg="Dodging a ZeroDivisionError:"))  # False
print(loud_div(4, 1, msg="This went fine:"))  # 4.0
