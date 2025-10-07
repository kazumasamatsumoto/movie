# #038 「[class] クラスバインディング」

## 概要
クラスバインディングは、要素のCSSクラスを動的に追加・削除する手法です。`[class.className]`構文でboolean値による単一クラス制御、`[class]`でオブジェクトや文字列による複数クラス制御が可能です。

## 学習目標
- クラスバインディングの基本構文を理解する
- 単一クラスと複数クラスの制御方法を学ぶ
- 条件付きスタイリングの実装方法を習得する

## 技術ポイント
- `[class.className]`による単一クラス制御
- `[class]`によるオブジェクト/文字列バインディング
- 動的なUI状態の表現
- 条件式との組み合わせ

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class ButtonComponent {
  isActive = false;
  isPrimary = true;
}
```

```html
<!-- 単一クラス -->
<div [class.active]="isActive">コンテンツ</div>
<button [class.primary]="isPrimary">ボタン</button>
```

```html
<!-- 複数クラス（オブジェクト） -->
<div [class]="{active: isActive, primary: isPrimary}">
```

## 💻 詳細実装例（学習用）

```typescript
// class-binding.component.ts
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-class-binding',
  standalone: true,
  template: `
    <div class="demo">
      <h2>クラスバインディングの例</h2>

      <!-- 単一クラスのバインディング -->
      <section>
        <h3>単一クラス</h3>
        <div [class.active]="isActive()" class="box">
          {{isActive() ? 'アクティブ' : '非アクティブ'}}
        </div>
        <button (click)="toggleActive()">切り替え</button>
      </section>

      <!-- 複数クラス（オブジェクト） -->
      <section>
        <h3>複数クラス（オブジェクト）</h3>
        <div [class]="classObject()" class="card">
          <p>状態: {{status()}}</p>
        </div>
        <button (click)="changeStatus('success')">成功</button>
        <button (click)="changeStatus('error')">エラー</button>
        <button (click)="changeStatus('warning')">警告</button>
      </section>

      <!-- 複数クラス（文字列） -->
      <section>
        <h3>複数クラス（文字列）</h3>
        <div [class]="classString()">
          動的クラス文字列
        </div>
        <button (click)="addClassToString()">クラス追加</button>
      </section>

      <!-- 条件付きクラス -->
      <section>
        <h3>条件付きクラス</h3>
        <div
          [class.highlight]="score() >= 80"
          [class.warning]="score() < 50"
          class="score-card">
          スコア: {{score()}}
        </div>
        <button (click)="changeScore(90)">高スコア</button>
        <button (click)="changeScore(60)">中スコア</button>
        <button (click)="changeScore(30)">低スコア</button>
      </section>

      <!-- ngClass との比較 -->
      <section>
        <h3>ngClass（複雑な条件）</h3>
        <div [ngClass]="{
          'success': status() === 'success',
          'error': status() === 'error',
          'large': size() === 'large',
          'small': size() === 'small'
        }" class="status-box">
          ステータス表示
        </div>
      </section>

      <!-- 組み合わせ -->
      <section>
        <h3>静的クラスと動的クラスの組み合わせ</h3>
        <button
          class="btn"
          [class.btn-primary]="buttonType() === 'primary'"
          [class.btn-secondary]="buttonType() === 'secondary'"
          [class.btn-large]="isLarge()"
          [class.disabled]="isDisabled()">
          ボタン
        </button>
        <button (click)="toggleButtonType()">タイプ変更</button>
        <button (click)="toggleSize()">サイズ変更</button>
      </section>
    </div>
  `,
  styles: [`
    .demo {
      padding: 20px;
    }
    section {
      margin: 30px 0;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    .box {
      padding: 20px;
      border: 2px solid #ccc;
      transition: all 0.3s;
    }
    .box.active {
      border-color: #007bff;
      background-color: #e7f3ff;
    }
    .card {
      padding: 20px;
      border-radius: 8px;
      margin: 10px 0;
    }
    .card.success {
      background-color: #d4edda;
      border: 2px solid #28a745;
    }
    .card.error {
      background-color: #f8d7da;
      border: 2px solid #dc3545;
    }
    .card.warning {
      background-color: #fff3cd;
      border: 2px solid #ffc107;
    }
    .score-card {
      padding: 20px;
      border: 2px solid #ccc;
      border-radius: 4px;
    }
    .score-card.highlight {
      background-color: #d4edda;
      font-weight: bold;
    }
    .score-card.warning {
      background-color: #f8d7da;
      color: #721c24;
    }
    .status-box {
      padding: 20px;
      border-radius: 4px;
    }
    .status-box.success {
      background-color: #28a745;
      color: white;
    }
    .status-box.error {
      background-color: #dc3545;
      color: white;
    }
    .status-box.large {
      font-size: 24px;
    }
    .status-box.small {
      font-size: 12px;
    }
    .btn {
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
    }
    .btn-primary {
      background-color: #007bff;
      color: white;
    }
    .btn-secondary {
      background-color: #6c757d;
      color: white;
    }
    .btn-large {
      font-size: 18px;
      padding: 15px 30px;
    }
    .btn.disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    button {
      margin: 5px;
      padding: 8px 16px;
    }
  `]
})
export class ClassBindingComponent {
  // 単一クラス
  isActive = signal(false);

  // 複数クラス（オブジェクト）
  status = signal<'success' | 'error' | 'warning'>('success');

  classObject = signal({
    success: true,
    error: false,
    warning: false
  });

  // 複数クラス（文字列）
  classString = signal('box primary');

  // 条件付きクラス
  score = signal(75);

  // ボタンスタイル
  buttonType = signal<'primary' | 'secondary'>('primary');
  size = signal<'normal' | 'large'>('normal');
  isLarge = signal(false);
  isDisabled = signal(false);

  toggleActive() {
    this.isActive.update(v => !v);
  }

  changeStatus(newStatus: 'success' | 'error' | 'warning') {
    this.status.set(newStatus);
    this.classObject.set({
      success: newStatus === 'success',
      error: newStatus === 'error',
      warning: newStatus === 'warning'
    });
  }

  addClassToString() {
    this.classString.update(v => v + ' highlighted');
  }

  changeScore(newScore: number) {
    this.score.set(newScore);
  }

  toggleButtonType() {
    this.buttonType.update(v => v === 'primary' ? 'secondary' : 'primary');
  }

  toggleSize() {
    this.isLarge.update(v => !v);
  }
}
```

### 使い分けの例

```typescript
@Component({
  template: `
    <!-- ✅ 単一クラスの切り替え: [class.className] -->
    <div [class.active]="isActive">シンプル</div>

    <!-- ✅ 複数クラスの切り替え: [class] オブジェクト -->
    <div [class]="{active: isActive, highlight: isHighlighted}">複数</div>

    <!-- ✅ 動的な文字列: [class] 文字列 -->
    <div [class]="'btn btn-' + buttonType">動的文字列</div>

    <!-- ✅ 複雑な条件: ngClass -->
    <div [ngClass]="{
      'text-success': score > 80,
      'text-warning': score >= 50 && score <= 80,
      'text-danger': score < 50
    }">複雑な条件</div>

    <!-- ✅ 静的 + 動的クラスの組み合わせ -->
    <div class="card" [class.card-active]="isActive">組み合わせ</div>
  `
})
export class ClassExamplesComponent {}
```

## ベストプラクティス
- 単一クラスには`[class.className]`を使用（シンプル）
- 複数クラスにはオブジェクト形式を使用
- 静的なクラスは`class`属性に、動的なクラスは`[class]`に分ける
- 複雑な条件式はコンポーネント側でメソッド化する

## 注意点
- 同じクラス名を静的と動的で指定すると動的が優先される
- `[class]`に文字列を渡すと既存のclassが上書きされる可能性がある
- ngClassとの併用は避ける（予期しない動作の原因）
- アニメーションとの併用時はトランジションを考慮する

## 関連技術
- [style]バインディング
- ngClass ディレクティブ
- @HostBinding（コンポーネント自身のクラス制御）
- CSS Modules / Tailwind CSS との統合
