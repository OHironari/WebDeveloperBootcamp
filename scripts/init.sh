#!/bin/zsh

# 仮想環境を有効化
source .venv/bin/activate

# .env ファイルが存在すれば読み込む
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
else
  echo ".env file not found"
fi

