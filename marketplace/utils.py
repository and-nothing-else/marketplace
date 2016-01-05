def int2semantic_ui_class(value):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value
    if not 0 < value <= 16:
        return value
    return (
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen'
            )[value - 1]
