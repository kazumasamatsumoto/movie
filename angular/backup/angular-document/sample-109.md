# #109 「@Output() エイリアス指定」

## 概要


## 学習目標
- @Output()でのエイリアス指定構文を理解する
- 親テンプレートから利用される公開名を管理する
- リファクタリング時にイベント名を段階的に移行する手法を習得する

## 技術ポイント
@Output()イベントの公開名と内部プロパティ名を分離し、APIの互換性を保ちながらイベント名をコントロールする方法を学びます。


- **エイリアス構文**: `@Output('saved') completed = new EventEmitter<void>();`
- **公開API**: 親はエイリアス名のみを知っていればよい
- **移行戦略**: 新旧イベント名を併存させる場合はdocコメントで周知

```typescript
@Output('saved') completed = new EventEmitter<void>();
```

```typescript
this.completed.emit();
```

```html
<app-form (saved)="handleSaved()"></app-form>
```

## 💻 詳細実装例（学習用）
```typescript
// form.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-form',
  standalone: true,
  templateUrl: './form.component.html',
})
export class FormComponent {
  @Output('saved') private readonly savedAlias = new EventEmitter<void>();

  submit(): void {
    this.savedAlias.emit();
  }
}
```

```html
<!-- form.component.html -->
<button type="button" (click)="submit()">保存</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { FormComponent } from './form.component';

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [FormComponent],
  template: `
    <app-form (saved)="handleSaved()"></app-form>
  `,
})
export class ParentComponent {
  handleSaved(): void {
    console.log('保存イベントを受信');
  }
}
```

## ベストプラクティス
- 公開イベント名はドキュメントで共有し、内部プロパティ名はリファクタしやすい命名にする
- エイリアス使用時は`@angular-eslint/no-output-rename`ルールの設定を調整する
- API移行期間は新旧イベント名を併用し、deprecatedコメントで案内する

## 注意点
- エイリアス名が長いとテンプレートで冗長になるので短く分かりやすい名前を心掛ける
- 複数イベントで同じ公開名を付けないようにする
- IDEリファクタリングでプロパティ名だけ変えるとエイリアス文字列を更新し忘れがち

## 関連技術
- `@angular-eslint/no-output-rename`
- APIバージョニング戦略
- SignalOutputのエイリアス（`output({ alias: 'saved' })`）
