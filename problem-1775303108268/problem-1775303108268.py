# Last updated: 04/04/2026, 17:15:08

class Solution:
    def decodeCiphertext(self, encoded_text: str, rows: int) -> str:
        if rows == 1:
            return encoded_text

        N = len(encoded_text)
        cols = N // rows
        i, j, k = 0, 0, 0
        original_text = []

        while k < N:
            original_text.append(encoded_text[k])
            i += 1
            if i == rows:
                i = 0
                j += 1
            k = i*(cols + 1) + j

        return ''.join(original_text).rstrip()
