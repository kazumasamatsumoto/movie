# #037 「[disabled] 属性バインディング」

## 概要
`[disabled]`プロパティバインディングは、フォーム要素やボタンの有効・無効状態を動的に制御する手法です。boolean値でシンプルに制御でき、フォームバリデーションやユーザー操作の制限に広く使用されます。

## 学習目標
- [disabled]バインディングの基本構文を理解する
- フォームバリデーションとの連携方法を学ぶ
- ユーザー操作の適切な制御方法を習得する

## 技術ポイント
- `[disabled]`プロパティバインディング
- boolean値による状態制御
- フォームバリデーションとの連携
- 条件式による動的制御

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class FormComponent {
  isSubmitting = false;
  isFormValid = false;
}
```

```html
<!-- disabled バインディング -->
<button [disabled]="isSubmitting">送信</button>
<input [disabled]="!isFormValid">
```

```html
<!-- 条件式 -->
<button [disabled]="!name || !email">送信</button>
```

## 💻 詳細実装例（学習用）

```typescript
// disabled-demo.component.ts
import { Component, signal } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-disabled-demo',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <div class="demo">
      <h2>disabled バインディングの例</h2>

      <!-- 基本的な使い方 -->
      <section>
        <h3>基本例</h3>
        <button [disabled]="isDisabled()">
          {{isDisabled() ? '無効' : '有効'}}
        </button>
        <button (click)="toggleDisabled()">切り替え</button>
      </section>

      <!-- フォームバリデーション連携 -->
      <section>
        <h3>フォームバリデーション</h3>
        <form [formGroup]="contactForm">
          <input formControlName="name" placeholder="名前">
          <input formControlName="email" placeholder="メール">

          <!-- フォームが無効な場合はボタンを無効化 -->
          <button [disabled]="contactForm.invalid">送信</button>
        </form>
      </section>

      <!-- 複数条件 -->
      <section>
        <h3>複数条件</h3>
        <input [(ngModel)]="username" placeholder="ユーザー名">
        <input [(ngModel)]="password" type="password" placeholder="パスワード">

        <button [disabled]="!username || !password || password.length < 8">
          ログイン
        </button>
      </section>

      <!-- ローディング状態 -->
      <section>
        <h3>ローディング状態</h3>
        <button [disabled]="isLoading()" (click)="submit()">
          {{isLoading() ? '送信中...' : '送信'}}
        </button>
      </section>

      <!-- 入力フィールドの無効化 -->
      <section>
        <h3>入力フィールド</h3>
        <input [disabled]="isReadOnly()" value="読み取り専用">
        <textarea [disabled]="isReadOnly()">テキストエリア</textarea>
        <select [disabled]="isReadOnly()">
          <option>オプション1</option>
          <option>オプション2</option>
        </select>
        <button (click)="toggleReadOnly()">
          {{isReadOnly() ? '編集可能にする' : '読み取り専用にする'}}
        </button>
      </section>

      <!-- 条件付き無効化 -->
      <section>
        <h3>条件付き無効化</h3>
        <button [disabled]="count() >= maxCount">追加 ({{count()}}/{{maxCount}})</button>
        <button [disabled]="count() <= 0">削除</button>
        <button (click)="increment()">+1</button>
        <button (click)="decrement()">-1</button>
      </section>
    </div>
  `,
  styles: [`
    .demo {
      padding: 20px;
      max-width: 600px;
    }
    section {
      margin: 30px 0;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    h3 {
      margin-top: 0;
      font-size: 18px;
    }
    input, textarea, select, button {
      margin: 5px;
      padding: 8px 12px;
      font-size: 14px;
    }
    button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    input:disabled, textarea:disabled, select:disabled {
      background-color: #f0f0f0;
      cursor: not-allowed;
    }
  `]
})
export class DisabledDemoComponent {
  // Signal による状態管理
  isDisabled = signal(false);
  isLoading = signal(false);
  isReadOnly = signal(false);
  count = signal(5);
  maxCount = 10;

  // フォーム
  contactForm: FormGroup;

  // 双方向バインディング用
  username = '';
  password = '';

  constructor(private fb: FormBuilder) {
    this.contactForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    });
  }

  toggleDisabled() {
    this.isDisabled.update(v => !v);
  }

  toggleReadOnly() {
    this.isReadOnly.update(v => !v);
  }

  async submit() {
    this.isLoading.set(true);
    // 送信処理のシミュレーション
    await new Promise(resolve => setTimeout(resolve, 2000));
    this.isLoading.set(false);
  }

  increment() {
    if (this.count() < this.maxCount) {
      this.count.update(v => v + 1);
    }
  }

  decrement() {
    if (this.count() > 0) {
      this.count.update(v => v - 1);
    }
  }
}
```

### リアクティブフォームでの使用例

```typescript
// reactive-form.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-reactive-form',
  template: `
    <form [formGroup]="registrationForm">
      <input formControlName="username" placeholder="ユーザー名">
      <input formControlName="email" placeholder="メール">
      <input formControlName="password" type="password" placeholder="パスワード">

      <!-- フォーム全体の状態で制御 -->
      <button [disabled]="registrationForm.invalid || isSubmitting">
        {{isSubmitting ? '登録中...' : '登録'}}
      </button>

      <!-- 特定のフィールドの状態で制御 -->
      <button [disabled]="!registrationForm.get('email')?.valid">
        メールを確認
      </button>
    </form>
  `
})
export class ReactiveFormComponent {
  registrationForm: FormGroup;
  isSubmitting = false;

  constructor(private fb: FormBuilder) {
    this.registrationForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }
}
```

## ベストプラクティス
- フォーム送信中はボタンを無効化してダブルクリックを防ぐ
- フォームバリデーションと連携させてUXを向上させる
- 無効化の理由をツールチップやメッセージで明示する
- boolean値で明確に制御する（文字列は避ける）

## 注意点
- `disabled="false"`（文字列）は無効にならない（属性が存在するだけで無効化される）
- `[disabled]="false"`（boolean）で正しく制御する必要がある
- ReactiveFormの`disable()`メソッドとは動作が異なる
- disabled状態の要素はフォーム送信時に値が送信されない

## 関連技術
- [readonly]バインディング
- ReactiveFormsのdisable/enableメソッド
- FormControlのvalidatorステータス
- [class.disabled]によるスタイル制御
