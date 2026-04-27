def ft_filter(function_to_apply, list_of_inputs):
    """Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""  # noqa: E501
    return [x for x in list_of_inputs if function_to_apply(x)]
