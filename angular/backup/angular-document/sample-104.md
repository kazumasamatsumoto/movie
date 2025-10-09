# #104 「@Output() - 子から親へイベント通知」

## 概要
子コンポーネントが@Output()を通じて親へイベントを通知し、親のロジックを呼び出す基本的なパターンを学びます。

## 学習目標
- @Output()とEventEmitterの関係を理解する
- 親テンプレートでイベントを購読する構文を習得する
- イベントデータを$eventで受け取る方法を確認する

## 技術ポイント
- **宣言**: `@Output() saved = new EventEmitter<void>();`
- **発火**: `this.saved.emit();`
- **親での受信**: `<app-child (saved)="handleSave()">`


```typescript
@Output() saved = new EventEmitter<void>();
```

```typescript
submit() { this.saved.emit(); }
```

```html
<app-form (saved)="onSaved()"></app-form>
```

## 💻 詳細実装例（学習用）
```typescript
// child.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-child-form',
  standalone: true,
  templateUrl: './child-form.component.html',
})
export class ChildFormComponent {
  @Output() saved = new EventEmitter<void>();

  submit(): void {
    this.saved.emit();
  }
}
```

```html
<!-- child-form.component.html -->
<button type="button" (click)="submit()">保存</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { ChildFormComponent } from './child-form.component';

@Component({
  selector: 'app-parent-page',
  standalone: true,
  imports: [ChildFormComponent],
  template: `
    <app-child-form (saved)="handleSaved()"></app-child-form>
  `,
})
export class ParentPageComponent {
  handleSaved(): void {
    console.log('親で保存処理を実行');
  }
}
```

## ベストプラクティス
- EventEmitterにはジェネリック型を付け、イベントデータの型を明示する
- イベント名は過去形（saved, closedなど）で命名すると意図が伝わりやすい
- 子コンポーネントはイベント通知に徹し、ビジネスロジックは親に任せる

## 注意点
- EventEmitterはSubjectの代替ではないため、サービス間通信にはRxJS Subjectを使う
- emitを忘れると親にイベントが届かないため、UI操作との紐付けを明確にする
- 親のハンドラが重い処理を持つ場合はThrottleなどで制御する

## 関連技術
- @Output() + $eventデータ
- @Input()との組み合わせ
- SignalOutput（v17+）によるSignalベースのイベント
