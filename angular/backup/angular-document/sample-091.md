# #091 「@Input() - 親から子へデータを渡す」

## 概要
Angularで親コンポーネントから子コンポーネントへデータを受け渡す基本の仕組みを学びます。@Input()デコレータにより、テンプレートのプロパティバインディングを通じて値を渡せます。

## 学習目標
- 親→子のデータフローを理解する
- 親テンプレートでのバインディング構文を確認する
- 子コンポーネント側でプロパティを定義する方法を習得する

## 技術ポイント
- **@Input()デコレータ**: 親から渡される値を受け取るフィールドを宣言
- **プロパティバインディング**: `[childProp]="parentValue"` の構文
- **単方向データフロー**: 親が値を管理し、子は参照だけ行う


```html
<!-- parent.component.html -->
<app-profile-card [title]="pageTitle"></app-profile-card>
```

```typescript
// profile-card.component.ts
@Input() title = '';
```

```html
<!-- profile-card.component.html -->
<h2>{{ title }}</h2>
```

## 💻 詳細実装例（学習用）
```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { ProfileCardComponent } from './profile-card.component';

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ProfileCardComponent],
  templateUrl: './parent.component.html',
})
export class ParentComponent {
  readonly pageTitle = signal('Angular Input Basics');
  readonly description = signal('親から子へデータを渡す方法を紹介します。');
}
```

```html
<!-- parent.component.html -->
<section>
  <h1>{{ pageTitle() }}</h1>
  <p>{{ description() }}</p>
  <app-profile-card
    [title]="pageTitle()"
    [description]="description()"
  ></app-profile-card>
</section>
```

```typescript
// profile-card.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-profile-card',
  standalone: true,
  templateUrl: './profile-card.component.html',
})
export class ProfileCardComponent {
  @Input() title = '';
  @Input() description = '';
}
```

```html
<!-- profile-card.component.html -->
<article class="card">
  <h2>{{ title }}</h2>
  <p>{{ description }}</p>
</article>
```

## ベストプラクティス
- 親がデータの真実を保持し、子は表示責務に絞る
- @Input()プロパティには型注釈と初期値を設定し、予期しないundefinedを防ぐ
- テンプレートでは小文字のプロパティ名でバインディングし、キャメルケースとの対応を整理する

## 注意点
- 親でプロパティを定義していないと`NG0303`エラーになる
- 親がプロパティを更新しても、子が参照をミューテートすると状態の不整合が起きる
- @Input()は受け取るだけなので、変更結果を親へ戻すには@Output()が必要

## 関連技術
- @Output()でのイベント通知
- Standalone Componentのimports指定
- Signalsとプロパティバインディングの組み合わせ
