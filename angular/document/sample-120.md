# #120 「Input/Output のよくあるエラー」

## 概要
@Input() / @Output()で発生しやすいエラーとその原因、解決方法をまとめます。

## 学習目標
- `NG0303` や `identifier isn’t a known property` など典型的なエラーを理解する
- 意図しないイベント未発火やnull参照の原因を特定する
- エラー対応のチェックリストを整備する

## 技術ポイント
- **NG0303**: 対象ディレクティブをimportsしていない（Standaloneで子コンポーネント未登録）
- **イベント名ミス**: テンプレートのイベント名と@Output名が一致しない
- **Null参照**: 必須Input未設定で`Cannot read properties of undefined`

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<!-- ❌ NG0303: Can't bind to 'value' since it isn't a known property -->
<app-input [value]="name"></app-input>
```

```typescript
@Output() saved = new EventEmitter<void>();
```

```html
<!-- ❌ (save) → 正しいのは (saved) -->
```

## 💻 詳細実装例（学習用）
```typescript
// faulty.component.ts
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-faulty',
  standalone: true,
  templateUrl: './faulty.component.html',
})
export class FaultyComponent {
  @Input({ required: true }) config!: { title: string };
  @Output() saved = new EventEmitter<void>();

  save(): void {
    this.saved.emit();
  }
}
```

```html
<!-- faulty.component.html -->
<button type="button" (click)="save()">保存</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { FaultyComponent } from './faulty.component';

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [FaultyComponent],
  templateUrl: './parent.component.html',
})
export class ParentComponent {
  title = 'エラー例';

  handleSaved(): void {
    console.log('保存完了');
  }
}
```

```html
<!-- parent.component.html -->
<!-- ❌ configを渡し忘れ、savedイベント名を間違えている例 -->
<app-faulty (save)="handleSaved()"></app-faulty>
```

## ベストプラクティス
- Standaloneコンポーネントを使う場合、親のimportsに子を追加し忘れない
- @Output名は過去形にし、テンプレート側で正しいイベント名をバインドする
- 必須Inputには`{ required: true }`を付け、テストで未設定ケースを検知する

## 注意点
- Template type checkingが有効（`strictTemplates`）だとコンパイル時に多くのエラーが検出されるので推奨
- エラーメッセージが英語でも内容を正確に読み取り、該当行やプロパティ名を確認する
- 既存コードをリファクタする際はエイリアスやイベント名を変えた影響がないか確認する

## 関連技術
- Angular Template Type Checking (`strictTemplates`)
- ESLint ルール (`no-input-rename`, `no-output-rename`)
- Angular エラーハンドリング公式ガイド
