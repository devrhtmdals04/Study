#!/usr/bin/env sh
# Usage (from project root): source scripts/activate.sh

# Determine project root when sourced from bash/zsh; fallback to current directory.
if [ -n "${BASH_VERSION:-}" ]; then
  _SCRIPT_PATH="${BASH_SOURCE:-}"
elif [ -n "${ZSH_VERSION:-}" ]; then
  _SCRIPT_PATH="${(%):-%N}"
else
  _SCRIPT_PATH=""
fi

if [ -n "$_SCRIPT_PATH" ]; then
  ROOT_DIR="$(cd "$(dirname "$_SCRIPT_PATH")/.." && pwd)"
else
  ROOT_DIR="$(pwd)"
fi

if [ -f "$ROOT_DIR/.venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  . "$ROOT_DIR/.venv/bin/activate"
fi

export MPLCONFIGDIR="$ROOT_DIR/.cache/matplotlib"
export XDG_CACHE_HOME="$ROOT_DIR/.cache"
export IPYTHONDIR="$ROOT_DIR/.cache/ipython"
export JUPYTER_CONFIG_DIR="$ROOT_DIR/.cache/jupyter/config"
export JUPYTER_DATA_DIR="$ROOT_DIR/.cache/jupyter/data"
export JUPYTER_RUNTIME_DIR="$ROOT_DIR/.cache/jupyter/runtime"

mkdir -p \
  "$ROOT_DIR/.cache/fontconfig" \
  "$MPLCONFIGDIR" \
  "$IPYTHONDIR" \
  "$JUPYTER_CONFIG_DIR" \
  "$JUPYTER_DATA_DIR" \
  "$JUPYTER_RUNTIME_DIR" 2>/dev/null || true

echo "Ready: venv=${VIRTUAL_ENV:-none}"
echo "MPLCONFIGDIR=$MPLCONFIGDIR"
echo "JUPYTER_RUNTIME_DIR=$JUPYTER_RUNTIME_DIR"
