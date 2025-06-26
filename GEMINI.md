# GEMINI.md - Gemini CLI向けプロジェクトガイドライン

このファイルは、Gemini CLIがこのプロジェクトを効果的に支援するためのガイドラインとコンテキストを提供します。

## プロジェクト概要

これはシンプルなPython Flask Webアプリケーションです。主な目的は、Gemini CLIを使用して基本的なWebアプリケーション開発、依存関係管理、およびGit統合を実演することです。

## 開発要件

- **言語**: Python 3.x
- **フレームワーク**: Flask
- **依存関係**: `requirements.txt` に記載されています。
- **エントリポイント**: `app.py` (メインのFlaskアプリケーションファイル)

## プロジェクト構造 (想定)

```
./
├── app.py
├── requirements.txt
├── README.md
├── GEMINI.md
└── .gitignore
```

## Gemini CLIの主要タスク

- **コード生成**: `app.py` および `requirements.txt` の作成。
- **依存関係管理**: `pip` を使用したPython依存関係のインストール。
- **アプリケーション実行**: Flask開発サーバーの実行。
- **Git操作**: 変更のステージング、コミット、GitHubへのプッシュ。
- **トラブルシューティング**: 一般的なPython/Flaskの問題のデバッグ。

## アプリケーションの実行方法 (Gemini CLI向け)

1.  依存関係のインストール: `pip install -r requirements.txt`
2.  アプリケーションの実行: `python app.py` (または設定されている場合は `flask run`)

## 重要な注意事項

- プロジェクトの依存関係については、常に `requirements.txt` を参照してください。
- 依存関係管理には仮想環境を使用するようにしてください。
- 標準的なPythonのベストプラクティス (例: PEP 8) に従ってください。