#!/usr/bin/env bash
# Install the Ad Studio skill into Claude Code (~/.claude/skills/ad-video-studio).
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)/skill/ad-video-studio"
DEST="$HOME/.claude/skills/ad-video-studio"

if [ -d "$DEST" ]; then
  BACKUP="$DEST.backup-$(date +%Y%m%d-%H%M%S)"
  echo "Existing install found → backing it up to $BACKUP"
  mv "$DEST" "$BACKUP"
fi
mkdir -p "$HOME/.claude/skills"
cp -R "$SRC" "$DEST"
chmod +x "$DEST"/scripts/*.sh "$DEST"/scripts/*.py "$DEST"/ugc/scripts/*.py 2>/dev/null || true
echo "✓ Installed to $DEST"

missing=()
for tool in ffmpeg ffprobe uv yt-dlp; do command -v "$tool" >/dev/null 2>&1 || missing+=("$tool"); done
if [ ${#missing[@]} -gt 0 ]; then
  echo "Optional tools not found: ${missing[*]}"
  echo "  macOS: brew install ffmpeg uv yt-dlp"
fi
echo "Restart Claude Code, then say: \"make me an ad for <product>\""
