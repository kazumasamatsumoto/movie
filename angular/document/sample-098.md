# #098 「@Input() オブジェクトの受け渡し」

## 概要
オブジェクトを@Input()で受け渡す際の参照共有による副作用や、不変性を保つためのテクニックを解説します。

## 学習目標
- オブジェクトが参照渡しで共有されることを理解する
- 子コンポーネントでの防御的コピー方法を学ぶ
- 推奨される不変データモデルを適用する

## 技術ポイント
- **参照共有**: 親・子で同じオブジェクトを参照する
- **防御的コピー**: `structuredClone`やspread演算子でコピーを作る
- **Readonly化**: TypeScriptで`Readonly<T>`を使いミューテーションを防ぐ

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() user!: Readonly<User>;
```

```typescript
readonly localUser = computed(() => ({ ...this.user }));
```

```html
<p>{{ user.name }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
type User = {
  id: number;
  name: string;
  role: 'admin' | 'user';
};

import { Component, Input, computed, signal } from '@angular/core';

@Component({
  selector: 'app-user-badge',
  standalone: true,
  templateUrl: './user-badge.component.html',
})
export class UserBadgeComponent {
  private readonly _user = signal<User | null>(null);

  @Input({ required: true })
  set user(value: User) {
    this._user.set(structuredClone(value));
  }

  readonly displayUser = computed(() => this._user());
}
```

```html
<!-- user-badge.component.html -->
<ng-container *ngIf="displayUser() as user">
  <div class="user-badge">
    <strong>{{ user.name }}</strong>
    <span>{{ user.role }}</span>
  </div>
</ng-container>
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { UserBadgeComponent } from './user-badge.component';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [UserBadgeComponent],
  templateUrl: './user-list.component.html',
})
export class UserListComponent {
  readonly currentUser = signal<User>({
    id: 1,
    name: '四国めたん',
    role: 'admin',
  });
}
```

```html
<!-- user-list.component.html -->
<app-user-badge [user]="currentUser()"></app-user-badge>
```

## ベストプラクティス
- 子コンポーネントではオブジェクトを直接変更せず、防御的コピーで内部状態を管理する
- `Readonly<T>`やfreezeを使って意図せぬ変更を静的に防ぐ
- 親は新しいオブジェクトを生成してから@Input()に渡し、変更検知を確実に発火させる

## 注意点
- パフォーマンスのために浅いコピーを使う場合でも、ネスト構造が深いときは注意が必要
- structuredCloneはブラウザ対応に留意し、polyfillやライブラリを検討する
- オブジェクトを子でミューテートすると後続のライフサイクルで予測不能な結果になる

## 関連技術
- Immutable.jsやImmer
- Angular Signalsによる状態管理
- RxJS storeパターン
