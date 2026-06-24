class Solution(object):
    def compress(self, chars):
        write = 0
        i = 0

        while i < len(chars):
            j = i

            # Find end of current group
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            # Write character
            chars[write] = chars[i]
            write += 1

            # Write count if >1
            count = j - i
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            i = j

        return write