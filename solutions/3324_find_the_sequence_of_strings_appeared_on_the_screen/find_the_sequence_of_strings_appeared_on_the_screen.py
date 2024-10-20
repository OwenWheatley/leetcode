class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        current_string = ""

        next_letter = {chr(i): chr((i - ord('a') + 1) % 26 + ord('a')) for i in range(ord('a'), ord('z') + 1)}

        for c in target:
            current_string += 'a'
            ans.append(current_string)

            while current_string[-1] != c:
                current_string = current_string[:-1] + next_letter[current_string[-1]]
                ans.append(current_string)

        return ans