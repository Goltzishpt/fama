class XMLParser:
    def __init__(self, xml):
        self.xml = xml.strip()

    def parse(self, xml=None):
        if xml is None:
            xml = self.xml

        result = {}
        while xml:
            xml = xml.strip()
            if not xml.startswith("<"):
                break

            tag_start = xml.find("<") + 1
            tag_end = xml.find(">", tag_start)
            tag = xml[tag_start:tag_end]

            content, xml = self.parse_tag(tag, xml)
            if "<" in content:
                parsed_content = self.parse(content)
            else:
                parsed_content = int(content) if content.isdigit() else content

            if tag in result:
                if not isinstance(result[tag], list):
                    result[tag] = [result[tag]]
                result[tag].append(parsed_content)
            else:
                result[tag] = parsed_content

        return result

    @staticmethod
    def parse_tag(tag, xml):
        start_tag = f"<{tag}>"
        end_tag = f"</{tag}>"
        start_idx = xml.find(start_tag)
        end_idx = xml.find(end_tag)

        if start_idx == -1 or end_idx == -1:
            return None, xml

        content = xml[start_idx + len(start_tag):end_idx].strip()
        rest = xml[end_idx + len(end_tag):]
        return content, rest
