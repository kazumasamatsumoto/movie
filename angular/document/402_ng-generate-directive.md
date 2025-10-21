# #402 「ng generate directive コマンド」

## 概要
`ng generate directive`はAngular CLIがディレクティブ雛形を作成するコマンドで、スタンドアロン化やテストファイル生成まで自動化できる。

## 学習目標
- CLIコマンドの構文とオプションを理解する
- 生成されたファイル構成を把握する
- 生成後に調整すべきポイントを知る

## 技術ポイント
- `ng g directive path/name --standalone`
- `--skip-tests`でspec生成を抑制可能
- `--prefix`でselectorプレフィックスを上書き

## 📺 画面表示用コード（動画用）
```bash
ng g directive directives/hover --standalone --prefix=app
```

## 💻 詳細実装例（学習用）
```bash
# ディレクティブ生成
ng g directive shared/focus --standalone

# 生成ファイル
# src/app/shared/focus.directive.ts
# src/app/shared/focus.directive.spec.ts

# focus.directive.ts（雛形）
@Directive({
  selector: '[appFocus]',
  standalone: true
})
export class FocusDirective {
  constructor() {}
}
```

## ベストプラクティス
- 生成直後にselector・プレフィックス・standalone設定を確認
- テストを活用するためspecファイルは基本的に生成する
- コマンドはスクリプト化してチームで共有すると統一性が保たれる

## 注意点
- CLIのプレフィックス設定を変更していないと`app`が自動付与される
- 既存ファイルへの上書きが起きる場合は生成ディレクトリを慎重に選ぶ
- ライブラリプロジェクトでは`ng generate directive --project`オプションが必要

## 関連技術
- Angular CLI Schematics
- Standalone Components
- Workspace設定（angular.json）
