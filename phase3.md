# Phase 3: レビュー属人化を減らす運用整備

所要時間: 約 20 分

このハンズオンでは、レビュー観点を個人依存からチーム共有資産へ変換し、
属人的なレビュー体制から脱却し、共通のレビュー観点でのセルフレビュー環境を整備します。

```text
チェックリストの作成  ->  セルフレビュー実施  ->  判定曖昧項目の改善
```

---

## 開発チームで起こるレビューの属人化とその問題点

開発チームにおいて、コードレビューが「特定のベテランエンジニアしかできない」状態に陥ることはよくありますが、その原因とそれによって生じる問題は以下の通りです。

### 1. 属人化する主な原因

- **ドメイン知識・技術スキルの偏り**
特定の機能や高度な技術スタックについて、一部のメンバーしか仕様やコードの背景を理解していないため、他の人がレビューできない。
- **レビュー基準の未明文化（暗黙知化）**
「何を基準にOKとするか」が明文化されておらず、ベテランの「感覚」や「経験」に頼っている。

### 2. 属人化によって起こる問題

- 開発のボトルネック化（速度低下）
- レビュー品質のバラつき
- チーム全体の成長機会の損失
- 特定メンバーへの負荷集中とリスク

---

## 03-1. レビューチェックリストを作成する

> **プロンプト**

```text
レビューの属人化を解消するために、workshop-python/docs/review-checklist-template.md を作成してください。
一般的なレビュー観点をカテゴリ別に整理し、Yes/No 判定可能なチェックリスト形式で出力してください。
```

**Copilot の動き**

- レビューチェックリストのテンプレートを作成します。

✅ **期待する結果**

```text
review-checklist-template.md が作成され、レビュー観点がカテゴリ別に整理される。
```

---

## 03-2. 作成したチェックリストでセルフレビューする

> **プロンプト**

```text
workshop-python/app/task_service.py を対象に、
作成したチェックリストでセルフレビューしてください。
```

**Copilot の動き**

- `task_service.py` を読み取り、チェックリスト項目ごとに該当箇所を照合します。
- 各カテゴリで Yes/No を判定し、根拠を簡潔に出力します。

✅ **期待する結果**

```text
カテゴリ別の Yes/No 判定と、
各判定に対応する1行根拠が出力される。
```

---

## 03-3. レビュー用 skill を作成する

繰り返し使うレビュー手順は、skill に切り出しておくと毎回同じ説明を書かずに再利用できます。ここでは、先ほど作成したチェックリストを使う review 用 skill を作成します。

> **プロンプト**

```text
workshop-python/docs/review-checklist-template.md を参照して、レビュー時に使う review-checklist skill を .github/skills/review-checklist/SKILL.md に作成してください。
description には「どのようなレビュー依頼のときに使う skill か」が分かる説明を入れてください。
skill はレビューのみを行い、コード修正はしないようにしてください。
```

**Copilot の動き**

- `.github/skills/review-checklist/SKILL.md` を作成します。
- frontmatter に `name` と `description` を設定し、本文にレビュー手順を記述します。

✅ **期待する結果**

```text
.github/skills/review-checklist/SKILL.md が作成される。
```

---

## 03-4. 作成した skill を使ってセルフレビューする

まず skill が認識されていることを確認します（VS Code の GitHub Copilot Chat を想定）。
Copilot CLIの場合は、`/skills list` コマンドで skill を確認できます。

```bash
/skills
```

skill を確認できたら、下記のプロンプトを送信します。

> **プロンプト**

```text
workshop-python/app/task_service.py をレビューしてください。
```

**Copilot の動き**

- `review-checklist` skill の `description` を手がかりに、レビュータスクで skill を利用します。
- `task_service.py` と review-checklist の内容を照合し、Yes/No 判定と根拠を出力します。

✅ **期待する結果**

```text
review-checklist skill が使われ、
チェックリストに沿った Yes/No 判定と1行根拠が出力される。
```

---

## ✅ チェックポイント

- [ ] `review-checklist-template.md` が作成されている
- [ ] `task_service.py` のセルフレビュー結果が出力されている
- [ ] `task_service.py` の自己レビュー結果に根拠が1行ずつ付与されている
- [ ] `.github/skills/review-checklist/SKILL.md` が作成されている
- [ ] `review-checklist` skill を使ったセルフレビューを実施できている

---

## 💡 +アクション：繰り返し利用可能なレビューエージェントを作成する

> GitHub Copilot には特定のタスクに特化したカスタムエージェントを作成できる機能(`/create-agent`)があります。<br>
> カスタムエージェントにすることで、特定タスクを依頼するプロンプトを毎回入力する必要がなくなります。<br>
> ここでは、レビューエージェントを作成して利用してみましょう。

### レビューエージェントを作成

> **プロンプト**

```text
/create-agent workshop-python/docs/review-checklist-template.md に基づいてレビューを実施するreview-checklistエージェントを新規作成する。レビューのみを実行し、修正は実行しない。
```

カスタムエージェント作成に当たり、Copilot からいくつかの質問をされます。

### (要手動操作)レビューエージェントを利用してセルフレビュー

chatウィンドウの「Agent」から作成したレビューエージェントを選択し、`task_service.py` を対象にセルフレビューを実施してみましょう。

---

次は [phase4.md](phase4.md#phase-4-マルチエージェントによる一連の動作体験) に進みます。
