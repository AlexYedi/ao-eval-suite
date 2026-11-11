#!/usr/bin/env bash
# Rebuild the runner's private copy of the pinned Claude Code CLI (e.g. on a new machine).
# Installs the exact version from runner/PIN into PINNED_CLAUDE_BIN and checks its sha256.
# The everyday `claude` on PATH is untouched and keeps auto-updating.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
. "$HERE/PIN"
mkdir -p "$(dirname "$PINNED_CLAUDE_BIN")"
SRC="$HOME/.local/share/claude/versions/$PINNED_CLAUDE_VERSION"
if [ ! -x "$SRC" ]; then
  echo "Installing Claude Code $PINNED_CLAUDE_VERSION alongside the current one..."
  curl -fsSL https://claude.ai/install.sh | bash -s "$PINNED_CLAUDE_VERSION"
fi
cp -p "$SRC" "$PINNED_CLAUDE_BIN"
SHA="$(shasum -a 256 "$PINNED_CLAUDE_BIN" | awk '{print $1}')"
[ "$SHA" = "$PINNED_CLAUDE_SHA256" ] || { echo "sha256 $SHA does not match runner/PIN; not using it." >&2; rm -f "$PINNED_CLAUDE_BIN"; exit 1; }
echo "Pinned CLI ready: $("$PINNED_CLAUDE_BIN" --version) at $PINNED_CLAUDE_BIN"
