def restore_ip_addresses(s):
    def backtrack(start, path):
        # If we have 4 segments and have used all characters, it's a valid IP
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # Try segments of length 1 to 3
        for length in range(1, 4):
            if start + length > len(s):
                break  # Out of bounds

            segment = s[start:start + length]

            # Check if the segment is valid
            if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                continue

            backtrack(start + length, path + [segment])

    result = []
    backtrack(0, [])
    return result


# Example usage:
s = "25525511135"
print(restore_ip_addresses(s))
