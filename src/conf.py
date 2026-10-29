"""
Sphinx configuration file.

Copyright (C) 2025 George K. Thiruvathukal.
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime
import html
import json
import os
import re
from operator import itemgetter
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx

project = "AI4FM | AI for Formal Methods"
copyright = f"{datetime.datetime.now(datetime.timezone.utc).year}, AI4FM Research Group"  # ruff: ignore[builtin-variable-shadowing]
author = "AI4FM Research Group"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinxcontrib.youtube",
    "sphinxext.opengraph",
    "sphinx_sitemap",
]

templates_path = ["_templates"]
exclude_patterns = ["drafts/**", "archive/**", "_themes/**"]

# Ablog configuration options
blog_authors = {
    "AI4FM": ("AI4FM Research Group", "https://github.com/LoyolaChicagoCS/ai4fm"),
    "GKT": ("George K. Thiruvathukal", "https://gkt.sh/"),
    "KL": ("Konstantin Läufer", "https://laufer.cs.luc.edu/"),
    "MA": ("Mohammed Abuhamad", "https://abuhamad.cs.luc.edu/"),
    "TNW": ("TaiNing Wang", "https://taining.github.io/"),
    "AB": ("Arslan Bisharat", "https://marslan.cs.luc.edu/"),
}
blog_default_author = "AI4FM"
blog_languages = {
    "en": ("English", None),
}
blog_default_language = "en"
post_show_prev_next = False
blog_title = "AI4FM Updates"
blog_feed_fulltext = True

# Sphinx auto section label settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "ai4fm"
html_theme_path = ["_themes"]
html_static_path = ["_static"]
html_extra_path = ["CNAME", "favicon.ico", "robots.txt"]
html_css_files = []
SITE_BASE_URL = os.environ.get("AI4FM_BASE_URL", "https://ai4fm.cs.luc.edu/")
blog_baseurl = SITE_BASE_URL
html_baseurl = SITE_BASE_URL
html_favicon = "_static/images/logo-dark.png"
html_context = {"site_base_url": SITE_BASE_URL}

html_theme_options = {}
html_sidebars = {"**": []}
html_title = project

# Sitemap settings
sitemap_url_scheme = "{link}"
# The blog archive and Sphinx utility pages duplicate or support primary content;
# they are deliberately kept out of search results and the sitemap below.
sitemap_excludes = ["blog/", "blog/**", "genindex/", "search/"]

# OpenGraph / social preview tags
ogp_site_url = SITE_BASE_URL
ogp_image = f"{SITE_BASE_URL}_static/images/logo-light.png"
ogp_description_length = 200
ogp_type = "website"
ogp_custom_meta_tags = [
    (
        '<meta name="keywords" content="formal methods, TLA+, LLMs, model '
        'checking, Loyola University Chicago, AI, verification">'
    ),
    '<meta name="twitter:card" content="summary">',
    (
        '<meta name="google-site-verification" '
        'content="04K9THhTvTqHTgt9pjOMw5pqkSi5_83nQCXMMrDnFsc" />'
    ),
]

DEFAULT_DESCRIPTION = (
    "AI4FM is Loyola University Chicago's AI for Formal Methods research group, "
    "advancing TLA+, formal verification, and rigorous LLM evaluation."
)
# Sphinx already marks its search page noindex. The blog archive and generated
# index are intentionally treated the same way to avoid duplicate search pages.
NOINDEX_PREFIXES = ("blog", "genindex")


def _short_description(text: str, limit: int = 160) -> str:
    """
    Normalize a search snippet without cutting a word when possible.

    Returns:
        A whitespace-normalized description no longer than the given limit.

    """
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    truncated = text[: limit - 3].rsplit(" ", 1)[0]
    return f"{truncated or text[: limit - 3]}..."


def _is_field_metadata(node: nodes.Node) -> bool:
    """
    Return whether a node belongs to a reStructuredText field list.

    Returns:
        Whether the node is nested in a field body.

    """
    ancestor = node.parent
    while ancestor is not None:
        if isinstance(ancestor, nodes.field_body):
            return True
        ancestor = ancestor.parent
    return False


def _description_from_doctree(doctree: nodes.document) -> str:
    """
    Return the first reader-facing paragraph, preferring paper abstracts.

    Returns:
        A concise page description, or an empty string when none is available.

    """
    for section in doctree.findall(nodes.section):
        title = section.next_node(nodes.title)
        if title and title.astext().strip().casefold() == "abstract":
            paragraphs = list(section.findall(nodes.paragraph))
            if paragraphs:
                return _short_description(paragraphs[0].astext())

    for paragraph in doctree.findall(nodes.paragraph):
        if not _is_field_metadata(paragraph):
            return _short_description(paragraph.astext())
    return ""


def seo_context(
    _app: Sphinx,
    pagename: str,
    _templatename: str,
    context: dict[str, object],
    doctree: nodes.document | None,
) -> None:
    """Keep every canonical page's social and search description unique."""
    metatags = str(context.get("metatags", ""))
    if pagename.startswith(NOINDEX_PREFIXES):
        context["metatags"] = (
            metatags + '<meta name="robots" content="noindex, follow" />\n'
        )
        return
    if doctree is None:
        return

    description = (
        DEFAULT_DESCRIPTION
        if pagename == "index"
        else _description_from_doctree(doctree)
    )
    # sphinxext-opengraph adds a description from the whole doctree. Its first
    # field list is bibliographic metadata on paper/post pages, so replace it
    # with a concise reader-facing summary and guarantee a single description.
    metatags = re.sub(
        r'<meta\s+(?:property="og:description"|name="description")\s+'
        r'content="[^"]*"\s*/?>\s*',
        "",
        metatags,
        flags=re.IGNORECASE,
    )
    if description:
        escaped = html.escape(description, quote=True)
        metatags += (
            f'<meta property="og:description" content="{escaped}" />\n'
            f'<meta name="description" content="{escaped}" />\n'
        )
    context["metatags"] = metatags


# Index the existing CMS documents at build time so new papers and posts appear
# on the homepage automatically, without duplicating titles or page content.
def homepage_context(
    app: Sphinx,
    pagename: str,
    _templatename: str,
    context: dict[str, object],
    _doctree: nodes.document | None,
) -> None:
    """Populate the homepage from existing paper and post source documents."""
    if pagename != "index":
        return
    research, news = [], []
    for docname in sorted(app.env.found_docs):
        if not docname.startswith(("papers/", "posts/")) or docname.endswith("/index"):
            continue
        source = Path(app.env.doc2path(docname)).read_text(encoding="utf-8")
        fields = dict(re.findall(r"^:([^:]+):\s*(.*)$", source, re.MULTILINE))
        item = {"docname": docname, "title": app.env.titles[docname].astext()}
        if docname.startswith("papers/"):
            item.update(
                status=fields.get("Status", ""),
                venue=fields.get("Venue", ""),
                authors=fields.get("Authors", ""),
            )
            research.append(item)
        elif fields.get("blogpost", "").lower() == "true":
            date = datetime.datetime.strptime(fields["date"], "%B %d, %Y").replace(
                tzinfo=datetime.timezone.utc
            )
            item.update(
                date=date.strftime("%B %d, %Y"), iso_date=date.date().isoformat()
            )
            news.append(item)
    # Preserve the research index's editorial order; newly added pages follow it.
    paper_index = Path(app.srcdir, "papers/index.rst").read_text(encoding="utf-8")
    ordered = re.findall(r"\.\. button-link:: ([\w-]+)/", paper_index)
    positions = {"papers/" + slug: index for index, slug in enumerate(ordered)}
    context["research_pages"] = sorted(
        research,
        key=lambda paper: (
            positions.get(paper["docname"], len(positions)),
            paper["title"],
        ),
    )
    context["news_pages"] = sorted(news, key=itemgetter("iso_date"), reverse=True)


LEADERBOARD_DATA = "data/leaderboard.json"
LEADERBOARD_MODES = (("default", "Default"), ("cfgaware", "Configuration-aware"))
LEADERBOARD_DESCRIPTIONS = (
    ("gpt", "Declarative, GPT"),
    ("claude", "Declarative, Claude"),
    ("intent_gpt", "Intent, GPT"),
    ("intent_claude", "Intent, Claude"),
)


def _count(value: int, total: int) -> str:
    return f"{value} ({100 * value / total:.1f}%)" if total else str(value)


class LeaderboardDirective(Directive):
    """
    Render the TLA+-Bench leaderboard from src/data/leaderboard.json.

    Each model entry holds ``name``, ``model_id``, ``weights`` (open or closed), ``served``,
    ``date`` and ``results``: one object per setting key ``<mode>/<description>`` with
    counts ``gold_a``, ``gold_b`` (specifications passing TLC) and ``sany`` (specifications
    that parse, out of all gold). An optional ``variation`` list holds Gold A pass counts
    for the repeated samples of the main setting. Invalid data stops the build.
    """

    has_content = False

    def run(self) -> list[nodes.Node]:
        env = self.state.document.settings.env
        path = Path(env.srcdir, LEADERBOARD_DATA)
        env.note_dependency(str(path))
        data = json.loads(path.read_text(encoding="utf-8"))
        bench = data["benchmark"]
        a_total, b_total = bench["gold_a"], bench["gold_b"]
        settings = [f"{m}/{d}" for m, _ in LEADERBOARD_MODES for d, _ in LEADERBOARD_DESCRIPTIONS]
        main = data["main_setting"]
        models = data["models"]
        for model in models:
            for key, counts in model["results"].items():
                if key not in settings:
                    raise self.error(f"{model['name']}: unknown setting {key}")
                limits = {"gold_a": a_total, "gold_b": b_total, "sany": a_total + b_total}
                for field, limit in limits.items():
                    if not 0 <= counts[field] <= limit:
                        raise self.error(f"{model['name']} {key}: {field} must be 0..{limit}")
        if not models:
            note = html.escape(data.get("pending_note", "No results are published yet."))
            return [nodes.raw("", f'<p class="leaderboard-empty">{note}</p>', format="html")]

        ranked = sorted(
            (m for m in models if main in m["results"]),
            key=lambda m: m["results"][main]["gold_a"],
            reverse=True,
        )
        def name_cell(model: dict, details: bool) -> str:
            cell = f'<span class="lb-model">{html.escape(model["name"])}</span>'
            if details:
                meta = html.escape(f'{model["weights"]} weights, {model["served"]}, run ')
                date = f'<span class="lb-date">{html.escape(model["date"])}</span>'
                cell += f'<span class="lb-id">{html.escape(model["model_id"])}</span>'
                cell += f'<span class="lb-id">{meta}{date}</span>'
            return f"<td>{cell}</td>"

        rows = []
        for rank, model in enumerate(ranked, 1):
            r = model["results"][main]
            spread = model.get("variation") or []
            variation = f"{min(spread)} to {max(spread)}" if spread else "Not run"
            rows.append(
                f'<tr><td class="num">{rank}</td>{name_cell(model, True)}'
                f'<td class="num">{_count(r["gold_a"], a_total)}</td>'
                f'<td class="num">{_count(r["gold_b"], b_total)}</td>'
                f'<td class="num">{_count(r["gold_a"] + r["gold_b"], a_total + b_total)}</td>'
                f'<td class="num">{_count(r["sany"], a_total + b_total)}</td>'
                f'<td class="num">{html.escape(variation)}</td></tr>'
            )
        main_table = (
            '<table class="leaderboard"><thead><tr><th class="num">Rank</th><th>Model</th>'
            f'<th class="num">Gold A<br>of {a_total}</th><th class="num">Gold B<br>of {b_total}</th>'
            f'<th class="num">All gold<br>of {a_total + b_total}</th>'
            f'<th class="num">Parses<br>of {a_total + b_total}</th>'
            '<th class="num">Gold A range,<br>5 runs at 0.8</th>'
            "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>"
        )
        tables = []
        for mode, mode_label in LEADERBOARD_MODES:
            head = "".join(f'<th class="num">{html.escape(dl)}</th>' for _, dl in LEADERBOARD_DESCRIPTIONS)
            body = []
            for model in ranked:
                cells = []
                for desc, _ in LEADERBOARD_DESCRIPTIONS:
                    r = model["results"].get(f"{mode}/{desc}")
                    cells.append(f'<td class="num">{_count(r["gold_a"], a_total) if r else "Not run"}</td>')
                body.append(f"<tr>{name_cell(model, False)}{''.join(cells)}</tr>")
            tables.append(
                f'<p class="leaderboard-caption">{mode_label} prompt: Gold A specifications '
                f"passing TLC, of {a_total}, for each description.</p>"
                f'<table class="leaderboard"><thead><tr><th>Model</th>{head}</tr></thead>'
                f'<tbody>{"".join(body)}</tbody></table>'
            )
        updated = html.escape(data.get("updated") or "")
        stamp = f'<p class="leaderboard-caption">Last updated {updated}.</p>' if updated else ""
        return [nodes.raw("", stamp + main_table + "".join(tables), format="html")]


def setup(app: Sphinx) -> None:
    """Register homepage data preparation and the leaderboard directive with Sphinx."""
    app.add_directive("leaderboard", LeaderboardDirective)
    app.connect("html-page-context", homepage_context)
    # Run after sphinxext-opengraph has populated the head metadata.
    app.connect("html-page-context", seo_context, priority=1000)
