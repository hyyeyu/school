"""Smoke tests for the static website artifact."""

from html.parser import HTMLParser
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "dist" / "index.html"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.html_attributes: dict[str, str | None] = {}
        self.meta_viewport = False
        self.title_depth = 0
        self.title_text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.html_attributes = attributes
        elif tag == "meta" and attributes.get("name") == "viewport":
            self.meta_viewport = "width=device-width" in (attributes.get("content") or "")
        elif tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text += data


class StaticSiteTests(unittest.TestCase):
    def test_build_artifact_exists(self) -> None:
        self.assertTrue(SITE.is_file(), "Build artifact dist/index.html must exist")

    def test_document_has_korean_language_and_responsive_viewport(self) -> None:
        parser = SiteParser()
        parser.feed(SITE.read_text(encoding="utf-8"))
        self.assertEqual(parser.html_attributes.get("lang"), "ko")
        self.assertTrue(parser.meta_viewport)

    def test_document_has_a_title(self) -> None:
        parser = SiteParser()
        parser.feed(SITE.read_text(encoding="utf-8"))
        self.assertIn("크리에이터", parser.title_text)


if __name__ == "__main__":
    unittest.main()
