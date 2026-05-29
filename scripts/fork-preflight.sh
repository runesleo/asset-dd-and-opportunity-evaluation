#!/usr/bin/env bash
# Fork preflight — run after deleting leo-extensions.md
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0
fail() { echo "🔴 $*"; FAIL=1; }
ok() { echo "✅ $*"; }

echo "=== asset-dd fork-preflight ==="

[[ -f SKILL.md ]] && ok "SKILL.md present" || fail "Missing SKILL.md"
[[ -f references/report-template.md ]] && ok "report-template present" || fail "Missing template"

if [[ -f references/leo-extensions.md ]]; then
  echo "ℹ️  leo-extensions.md still present (optional for author; delete for clean fork)"
else
  ok "leo-extensions removed (clean fork)"
fi

HITS=$(rg -n 'leo-vault|/Users/[a-zA-Z0-9_]+|active-tasks/T[0-9]{3}' . \
  --glob '!scripts/fork-preflight.sh' 2>/dev/null || true)
if [[ -n "$HITS" ]]; then
  fail "Private path leaks:"
  echo "$HITS" | head -15
else
  ok "No private path patterns"
fi

echo "=== exit $FAIL ==="
exit "$FAIL"
