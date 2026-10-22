# GitHub Copilot ハンズオン

本ハンズオンは、実際の開発において想定されるユースケースを疑似体験できる内容としています。開発における GitHub Copilot の便利さを体験してください。

ハンズオンは「プロンプト駆動」で構成していますので、参加者の皆さんは自然言語で GitHub Copilot に指示するだけで進行できます。

Phase 1〜4 の所要時間は約 1 時間です。MCP の体験を行う場合は、追加で Phase 5（約 15 分）を実施してください。

## 目次

- [GitHub Copilot ハンズオン](#github-copilot-ハンズオン)
  - [目次](#目次)
  - [想定するユースケース](#想定するユースケース)
  - [ハンズオンの事前準備](#ハンズオンの事前準備)
    - [a. Codespaces環境で受講する場合](#a-codespaces環境で受講する場合)
    - [b. ローカル環境で受講する場合](#b-ローカル環境で受講する場合)
  - [ハンズオンの進め方](#ハンズオンの進め方)
  - [ハンズオンの後片付け](#ハンズオンの後片付け)
    - [a. Codespaces を利用した場合](#a-codespaces-を利用した場合)
    - [b. ローカル環境を利用した場合](#b-ローカル環境を利用した場合)

## 想定するユースケース

> 1. 既存プロジェクトへの新規参加<br>
>   1-1. プロジェクトの全体像を把握する<br>
>   1-2. 既存のコードを理解する<br>
>   1-3. 機能改修への活用<br>
>   1-4. ドキュメントが整備されていないプロジェクトで、コードから仕様を抽出する<br>
> 2. テストのないプロジェクトに自動テストを導入し、保守性を向上させる
> 3. 特定の技術者に依存したレビュー体制の改善
> 4. より一層の AI 駆動体験(マルチエージェントによる一連の動作)
> 5. Microsoft Learn MCP による公式情報の検索・取得と、MCP 利用時のセキュリティ確認

## ハンズオンの事前準備

ハンズオンを始める前に、受講環境に応じた事前準備を完了してください。

- [Codespaces環境で受講する場合](#a-codespaces環境で受講する場合)
- [ローカル環境で受講する場合](#b-ローカル環境で受講する場合)

### a. Codespaces環境で受講する場合

1. 研修案内で配布されたCodespaces向け事前準備リポジトリを完了してください。
2. 本リポジトリを複製する

   2-1. **「Use this template」** の **「Create a new repository」** を選択してください。

   ![use-template](./assets/use-template.png)

   2-2. Owner をご自身のアカウント、任意のリポジトリ名を入力し、リポジトリの可視性は Private を選択してください。
   2-3. 最後に **「Create repository」** でリポジトリを複製します。

   ![use-template2](./assets/use-template2.png)

3. 複製先で Codespaces を起動

   複製先のリポジトリで **「Code」の「Codespaces」タブ** の **「Create codespace on main」** を選択し、Codespaces を起動します。

   ![start-codespaces](./assets/start-codespaces.png)

4. Codespaces 内の Visual Studio Code で GitHub Copilot にサインインし、ハンズオンを体験

   - Codespaces を起動すると、その環境内で Visual Studio Code が立ち上がります（数分かかる可能性があります）。
   - 右下の Copilot アイコン部分でサインインをした後に、右側のチャットウィンドウを使用してハンズオンを体験してください。

   ![vscode-codespaces](./assets/vscode-codespaces.png)

### b. ローカル環境で受講する場合

1. 研修案内で配布されたローカル環境向け事前準備リポジトリを完了してください。

2. 本リポジトリをローカル環境に用意

   次のいずれかの方法で、本リポジトリをローカル環境に用意してください。

   a. 研修案内で配布された ZIP ファイルを展開し、Visual Studio Code で展開先のフォルダーを開く

   b. 研修案内で指定された本リポジトリをご自身の GitHub アカウントへ複製する

      1. 複製手順は「### a. Codespaces環境で受講する場合の手順2」を参照してください。
      2. その後、複製したリポジトリを clone し、Visual Studio Code でフォルダーを開いてください。

   ```bash
   git clone <複製したリポジトリのURL>
   ```

3. 仮想環境（venv）を作成

   システムのPython環境に影響を与えないよう、リポジトリのルートで仮想環境を作成し、有効化してください。

   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   以降、ハンズオン内で`pip install`などを実行する際は、この仮想環境を有効化した状態で行ってください。

   - Linux（特に Ubuntu / Debian）で `python3 -m venv .venv` の実行時に `venv` モジュールがない旨のエラーが表示された場合は、次のコマンドを実行してください。

   ```bash
   sudo apt install -y python3-venv
   ```

4. ハンズオンを体験

   以上の準備が完了したら、ハンズオンを開始してください。

## ハンズオンの進め方

特に指定がない場合は、Copilot は Agent モードで Model は Auto を使用します(下図：右下のチャットウィンドウ)。

![agent-auto-mode](./assets/agent-auto-mode.png)

AI が新規に作成・編集した内容については、「保持」「keep」が表示されます。必要に応じて、AI の提案を受け入れるか選択してください。

**本ハンズオンでは、「保持」を選択しながら進めてください。**

![ai-suggestion-keep](./assets/ai-suggestion-keep.png)

[phase1.md](phase1.md#phase-1-既存プロジェクトへの新規参加) から始めてください。

| Phase | 内容 | 時間 | 消費 AI Credits 目安(Auto モード利用) |
| --- | --- | --- | --- |
| [Phase 1](phase1.md#phase-1-既存プロジェクトへの新規参加) | 既存プロジェクトへの新規参加 | 15分 | 20 AI Credits(GPT-5.6 Terra) |
| [Phase 2](phase2.md#phase-2-テスト未整備コードへのpytest導入) | テスト未整備コードへの pytest 導入 | 15分 | 15 AI Credits(Claude Sonnet 5) |
| [Phase 3](phase3.md#phase-3-レビュー属人化を減らす運用整備) | レビュー属人化を減らす運用整備 | 20分 | 10 AI Credits(GPT-5.6 Luna) |
| [Phase 4](phase4.md#phase-4-マルチエージェントによる一連の動作体験) | マルチエージェントによる一連の動作体験 | 15分 | 5 AI Credits(GPT-5.6 Luna) |
| [Phase 5](phase5.md#phase-5-microsoft-learn-mcp-を使った公式情報の参照) | Microsoft Learn MCP とセキュリティ | 15分 | MCP 利用状況による |

## ハンズオンの後片付け

### a. Codespaces を利用した場合

Codespacesを利用した場合は、時間単位の従量課金が発生するため、不要になったCodespaceの削除を推奨します。
詳細は[公式ドキュメント](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)をご確認ください。

左上のハンバーガーメニューから、**「Codespaces」** を選択。

![delete-codespaces](./assets/delete-codespaces.png)

削除したい Codespace の「…」から「Delete」で削除します。

![delete-codespaces2](./assets/delete-codespaces2.png)

### b. ローカル環境を利用した場合

1. 仮想環境を無効化

   ハンズオンで作成した仮想環境を無効化するには、次のコマンドを実行してください。

   ```bash
   # Windows (PowerShell)
   deactivate

   # macOS / Linux
   deactivate
   ```

2. このハンズオン用にPythonをインストールし、今後も不要な場合は各OSに応じて以下のコマンドを実行してアンインストールしてください。

   - Linux ( Ubuntu / Debian ) の場合、システム Python 3 自体を削除するとシステムパッケージの依存関係まで削除されるおそれがあるためご注意ください。

| OS | アンインストールコマンド |
| --- | --- |
| Windows (PowerShell) | `winget uninstall -e --id Python.Python.3.14` |
| macOS（Homebrew） | `brew uninstall python` |
| Linux（Ubuntu / Debian） | `sudo apt remove -y python3 python3-venv` |
