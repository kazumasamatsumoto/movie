# #060 「テンプレートのよくあるエラー」

## 概要
Angularテンプレートで頻出するエラーメッセージとその原因・対処法を整理し、問題発生時に迅速に切り分けるための知識を身につけます。

## 学習目標
- 代表的なテンプレートエラーの意味と発生条件を理解する
- モジュール未登録やライフサイクルの問題を素早く修正できる
- エラーメッセージをヒントに再現手順と解決策をまとめる

## 技術ポイント
- **NG0303**: 必要なディレクティブやモジュールが未登録でバインディングできない
- **NG0100**: 変更検知後に値が変わり整合性が崩れた際に発生
- **テンプレートシンタックスエラー**: 構文ミスや未閉括弧をAOTが検出

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<!-- ❌ NG0303: Can't bind to 'ngModel' without FormsModule -->
```

```html
<!-- ❌ NG0100: ExpressionChangedAfterItHasBeenChecked -->
```

```html
@if (error.code === 'NG0303') {
  <p>FormsModuleをimportsに追加してください</p>
}
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

type TemplateError = {
  code: string;
  message: string;
  cause: string;
  fix: string;
};

@Component({
  selector: 'app-template-errors',
  standalone: true,
  templateUrl: './template-errors.component.html',
})
export class TemplateErrorsComponent {
  errors = signal<TemplateError[]>([
    {
      code: 'NG0303',
      message: `Can't bind to 'ngModel' since it isn't a known property`,
      cause: 'FormsModuleや対象ディレクティブをimportsしていない',
      fix: 'Standaloneコンポーネントならimports: [FormsModule]を追加する',
    },
    {
      code: 'NG0100',
      message: 'ExpressionChangedAfterItHasBeenChecked',
      cause: 'ライフサイクル後に同期的に値を変更している',
      fix: 'AfterViewInitでの値変更をsetTimeout/Signalsに移す、またはロジックを再構成',
    },
    {
      code: 'NG5002',
      message: 'Parser Error: Unexpected token',
      cause: 'テンプレート式の構文ミスや括弧の閉じ忘れ',
      fix: '式をシンプルにし、AOTエラーメッセージの該当行を確認する',
    },
  ]);
}
```

```html
<table>
  <thead>
    <tr>
      <th>コード</th>
      <th>メッセージ</th>
      <th>原因</th>
      <th>対処</th>
    </tr>
  </thead>
  <tbody>
    <tr @for (err of errors(); track err.code)">
      <td>{{ err.code }}</td>
      <td>{{ err.message }}</td>
      <td>{{ err.cause }}</td>
      <td>{{ err.fix }}</td>
    </tr>
  </tbody>
</table>
```

## ベストプラクティス
- エラーが出たら必ず全文を読み、コードとメッセージを検索して公式ドキュメントを確認する
- モジュール未登録が原因の場合は、Standalone importsとprovideの設定を見直す
- ExpressionChanged系エラーはSignalやEffectで副作用を隔離し、ライフサイクル順序を整える

## 注意点
- ビルド時と実行時でエラー内容が異なることがあるため、AOTビルドでも再現させる
- またぎの変更検知を意識して、コンストラクタやngOnInit内でDOM操作を行わない
- ライブラリが自動インポートされない場合は、`schematics`設定や`standalone: true`対応状況をチェックする

## 関連技術
- Angular公式エラーリファレンス
- strictTemplates と ESLintルール
- ChangeDetectionとライフサイクルフック
