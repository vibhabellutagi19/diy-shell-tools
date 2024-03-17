import re


class GrepSearch:
    def search_text(self, expression: str, input_text: list) -> list:
        results = []
        if expression == "":
            return input_text

        for line in input_text:
            line = line.strip()
            if re.search(expression, line):
                results.append(line)
        return results
