
def canconstruct(remaining, strs):
    """
    Determines if the `remaining` string can be constructed using elements from `strs`.

    :param remaining: The target string to construct.
    :param strs: List of strings that can be used to construct the target.
    :return: True if the target can be constructed, False otherwise.
    """
    # Base case: if the remaining string is empty, return True
    if len(remaining) == 0:
        return True

    # Try each string in `strs` to see if it can be a prefix of `remaining`
    for ele in strs:
        # Check if `ele` matches the beginning of `remaining`
        if remaining.startswith(ele):
            # If yes, recursively check with the rest of the string
            if canconstruct(remaining[len(ele):], strs):
                return True

    # If no prefix works, return False
    return False

def canconstruct_memo(remaining, strs,memo={}):
    """
    Determines if the `remaining` string can be constructed using elements from `strs`.

    :param remaining: The target string to construct.
    :param strs: List of strings that can be used to construct the target.
    :return: True if the target can be constructed, False otherwise.
    """
    # Base case: if the remaining string is empty, return True
    if len(remaining) == 0:
        return True

    # Try each string in `strs` to see if it can be a prefix of `remaining`
    for ele in strs:
        # Check if `ele` matches the beginning of `remaining`
        if remaining.startswith(ele):
            suffix=remaining[len(ele):]
            # If yes, recursively check with the rest of the string
            if canconstruct_memo(suffix, strs,memo):
                memo[remaining]=True
                return True
    memo[remaining]=False
    # If no prefix works, return False
    return False





