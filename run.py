import json
from pathlib import Path
from app.crawler.xml_parser import XMLParser

from settings import settings

logger = settings.LOGGER


def main():
    data_dir = Path("data")
    input_file = Path(data_dir, "data.xml")
    output_file = Path(data_dir, "data.json")

    logger.info("Starting the XML parsing process.")

    if not input_file.exists():
        logger.error(f"Input file not found: {input_file}")
        raise FileNotFoundError(f"Input file not found: {input_file}")

    logger.info(f"Reading data from {input_file}")
    with input_file.open("r", encoding="utf-8") as xml_file:
        xml_data = xml_file.read()

    logger.info("Parsing XML data.")
    parser = XMLParser(xml_data)
    parsed_data = parser.parse()

    logger.info("Writing parsed data to JSON file.")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as json_file:
        json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

    logger.info(f"Data successfully written to {output_file}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
