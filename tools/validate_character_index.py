#!/usr/bin/env python3
"""Validate the generated Umamusume character manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from build_character_index import (
    DEFAULT_CHARACTER_DIR,
    DEFAULT_OUTPUT,
    EXCLUDED_FILES,
    iter_entries,
    render,
)


def validate(character_dir: Path, index_path: Path) -> list[str]:
    errors: list[str] = []
    entries = list(iter_entries(character_dir))
    ids: dict[str, str] = {}
    names: dict[str, str] = {}
    aliases: dict[str, str] = {}
    files = {path.name for path in character_dir.glob("*.md")}

    for entry in entries:
        character_id = str(entry["character_id"])
        name = str(entry["canonical_name"])
        markdown = str(entry["markdown"])
        owner = f"{name} ({markdown})"

        if character_id in ids:
            errors.append(f"duplicate character_id {character_id}: {ids[character_id]} and {owner}")
        ids[character_id] = owner

        normalized_name = name.casefold()
        if normalized_name in names:
            errors.append(f"duplicate canonical_name {name}: {names[normalized_name]} and {owner}")
        names[normalized_name] = owner

        if markdown not in files or markdown in EXCLUDED_FILES:
            errors.append(f"invalid Markdown path for {owner}: {markdown}")

        for alias in entry["aliases"]:  # type: ignore[union-attr]
            normalized_alias = str(alias).casefold().strip()
            previous = aliases.get(normalized_alias)
            if previous and previous != owner:
                errors.append(f"duplicate alias {alias!r}: {previous} and {owner}")
            aliases[normalized_alias] = owner

    if not index_path.exists():
        errors.append(f"missing generated manifest: {index_path}")
    elif index_path.read_text(encoding="utf-8") != render(entries):
        errors.append(f"manifest is stale: run python tools/build_character_index.py")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--character-dir", type=Path, default=DEFAULT_CHARACTER_DIR)
    parser.add_argument("--index", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    errors = validate(args.character_dir, args.index)
    if errors:
        print("Character manifest validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Character manifest is valid: {args.index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
