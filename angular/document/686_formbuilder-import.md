# #686 「FormBuilder のインポート」

## 概要
FormBuilderを利用するには@angular/formsからインポートし、ReactiveFormsModuleを読み込んだ上で依存注入で取得する。

## 学習目標
- FormBuilderのインポート場所を理解する
- モジュール設定との関係を把握する
- 依存注入での取得手順を学ぶ

## 技術ポイント
- import { FormBuilder } from "@angular/forms"
- ReactiveFormsModuleの読み込みが前提
- inject(FormBuilder)でスタンドアロン対応

## 📺 画面表示用コード（動画用）
```typescript
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './example.component.html'
})
export class ExampleComponent {
  protected readonly fb = inject(FormBuilder);
}
```

## ベストプラクティス
- FormBuilderはreadonlyフィールドに格納する
- 共有モジュールにReactiveFormsModuleをまとめておく
- 単体テストではTestBed.inject(FormBuilder)で取得する

## 注意点
- テンプレート駆動フォームだけではFormBuilderは使えない
- インポートを忘れるとDI例外が発生する
- 複数モジュールで使用する場合は提供範囲を確認する

## 関連技術
- FormBuilder
- ReactiveFormsModule
- 依存注入
