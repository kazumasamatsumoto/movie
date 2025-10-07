# #040 「[attr.] 属性バインディング」

## 概要
属性バインディングは、HTML属性を動的に設定する手法です。`[attr.attributeName]`構文を使用し、DOMプロパティが存在しない属性（ARIA属性、data属性、SVG属性など）を制御できます。

## 学習目標
- 属性バインディングとプロパティバインディングの違いを理解する
- ARIA属性やdata属性の動的設定方法を学ぶ
- アクセシビリティ対応の実装方法を習得する

## 技術ポイント
- `[attr.attributeName]`構文
- プロパティバインディングとの使い分け
- ARIA属性によるアクセシビリティ対応
- data属性やカスタム属性の制御

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class AccessibleComponent {
  ariaLabel = 'ユーザー情報を編集';
  dataId = 'user-123';
}
```

```html
<!-- 属性バインディング -->
<button [attr.aria-label]="ariaLabel">編集</button>
<div [attr.data-id]="dataId">ユーザー情報</div>
```

```html
<!-- colspan など -->
<td [attr.colspan]="columnCount">セル</td>
```

## 💻 詳細実装例（学習用）

```typescript
// attribute-binding.component.ts
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-attribute-binding',
  standalone: true,
  template: `
    <div class="demo">
      <h2>属性バインディングの例</h2>

      <!-- ARIA属性（アクセシビリティ） -->
      <section>
        <h3>ARIA属性</h3>
        <button
          [attr.aria-label]="editButtonLabel()"
          [attr.aria-pressed]="isPressed()"
          [attr.aria-expanded]="isExpanded()"
          (click)="toggleExpanded()">
          {{isExpanded() ? '閉じる' : '開く'}}
        </button>

        <div
          [attr.aria-hidden]="!isExpanded()"
          [attr.role]="'region'">
          展開されたコンテンツ
        </div>

        <!-- スクリーンリーダー用 -->
        <input
          type="text"
          [attr.aria-label]="inputLabel()"
          [attr.aria-required]="isRequired()"
          [attr.aria-invalid]="hasError()">
      </section>

      <!-- data属性 -->
      <section>
        <h3>data属性</h3>
        <div
          [attr.data-user-id]="userId()"
          [attr.data-role]="userRole()"
          [attr.data-timestamp]="timestamp()">
          ユーザー情報
        </div>

        <!-- カスタムデータ属性 -->
        <button
          [attr.data-action]="'delete'"
          [attr.data-target]="selectedId()"
          (click)="handleAction($event)">
          削除
        </button>
      </section>

      <!-- テーブル属性 -->
      <section>
        <h3>テーブル属性（colspan/rowspan）</h3>
        <table>
          <tr>
            <td [attr.colspan]="colSpan()">結合セル</td>
          </tr>
          <tr>
            <td>セル1</td>
            <td>セル2</td>
            <td>セル3</td>
          </tr>
        </table>
        <button (click)="changeColspan(1)">1列</button>
        <button (click)="changeColspan(2)">2列</button>
        <button (click)="changeColspan(3)">3列</button>
      </section>

      <!-- SVG属性 -->
      <section>
        <h3>SVG属性</h3>
        <svg width="200" height="200">
          <circle
            [attr.cx]="circleX()"
            [attr.cy]="circleY()"
            [attr.r]="radius()"
            [attr.fill]="circleFill()"
            [attr.stroke]="circleStroke()"
            [attr.stroke-width]="strokeWidth()">
          </circle>
        </svg>
        <button (click)="moveCircle()">移動</button>
        <button (click)="changeRadius()">サイズ変更</button>
      </section>

      <!-- null値の扱い -->
      <section>
        <h3>条件付き属性（null値）</h3>
        <div [attr.title]="showTooltip() ? tooltipText() : null">
          {{showTooltip() ? 'ツールチップあり' : 'ツールチップなし'}}
        </div>
        <button (click)="toggleTooltip()">ツールチップ切替</button>
      </section>

      <!-- プロパティとの違い -->
      <section>
        <h3>プロパティ vs 属性</h3>

        <!-- ❌ DOMプロパティが存在しない場合はエラー -->
        <!-- <div [data-id]="userId()"></div> -->

        <!-- ✅ attr.を使用する -->
        <div [attr.data-id]="userId()">正しい方法</div>

        <!-- ✅ DOMプロパティが存在する場合 -->
        <input [id]="inputId()"> <!-- プロパティバインディング -->
        <input [attr.id]="inputId()"> <!-- 属性バインディング（両方可能） -->
      </section>

      <!-- アクセシビリティの実践例 -->
      <section>
        <h3>アクセシビリティの実践</h3>
        <nav [attr.aria-label]="'メインナビゲーション'">
          <ul [attr.role]="'menubar'">
            @for (item of menuItems; track item.id) {
              <li
                [attr.role]="'menuitem'"
                [attr.aria-current]="currentItem() === item.id ? 'page' : null"
                (click)="selectMenuItem(item.id)">
                {{item.label}}
              </li>
            }
          </ul>
        </nav>
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
    button {
      margin: 5px;
      padding: 8px 16px;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      margin: 10px 0;
    }
    td {
      border: 1px solid #ddd;
      padding: 10px;
      text-align: center;
    }
    svg {
      border: 1px solid #ddd;
      margin: 10px 0;
    }
    nav ul {
      list-style: none;
      padding: 0;
      display: flex;
      gap: 10px;
    }
    nav li {
      padding: 10px 20px;
      background-color: #f0f0f0;
      cursor: pointer;
      border-radius: 4px;
    }
    nav li[aria-current="page"] {
      background-color: #007bff;
      color: white;
      font-weight: bold;
    }
  `]
})
export class AttributeBindingComponent {
  // ARIA属性
  editButtonLabel = signal('ユーザー情報を編集');
  isPressed = signal(false);
  isExpanded = signal(false);
  inputLabel = signal('ユーザー名を入力');
  isRequired = signal(true);
  hasError = signal(false);

  // data属性
  userId = signal('user-123');
  userRole = signal('admin');
  timestamp = signal(Date.now());
  selectedId = signal('item-1');

  // テーブル
  colSpan = signal(2);

  // SVG
  circleX = signal(100);
  circleY = signal(100);
  radius = signal(50);
  circleFill = signal('blue');
  circleStroke = signal('black');
  strokeWidth = signal(2);

  // ツールチップ
  showTooltip = signal(true);
  tooltipText = signal('これはツールチップです');

  // ID
  inputId = signal('user-input');

  // メニュー
  menuItems = [
    { id: 'home', label: 'ホーム' },
    { id: 'about', label: '概要' },
    { id: 'contact', label: 'お問い合わせ' }
  ];
  currentItem = signal('home');

  toggleExpanded() {
    this.isExpanded.update(v => !v);
  }

  handleAction(event: Event) {
    const button = event.target as HTMLElement;
    const action = button.getAttribute('data-action');
    const target = button.getAttribute('data-target');
    console.log(`Action: ${action}, Target: ${target}`);
  }

  changeColspan(cols: number) {
    this.colSpan.set(cols);
  }

  moveCircle() {
    this.circleX.update(v => v === 100 ? 150 : 100);
    this.circleY.update(v => v === 100 ? 150 : 100);
  }

  changeRadius() {
    this.radius.update(v => v === 50 ? 70 : 50);
  }

  toggleTooltip() {
    this.showTooltip.update(v => !v);
  }

  selectMenuItem(id: string) {
    this.currentItem.set(id);
  }
}
```

### プロパティ vs 属性の比較

```typescript
@Component({
  template: `
    <!-- プロパティバインディング（DOMプロパティ） -->
    <input [value]="inputValue">        <!-- ✅ プロパティが存在 -->
    <button [disabled]="isDisabled">    <!-- ✅ プロパティが存在 -->

    <!-- 属性バインディング（HTML属性） -->
    <div [attr.data-id]="dataId">       <!-- ✅ DOMプロパティがない -->
    <button [attr.aria-label]="label">  <!-- ✅ ARIA属性 -->
    <td [attr.colspan]="span">          <!-- ✅ テーブル属性 -->
    <svg [attr.viewBox]="viewBox">      <!-- ✅ SVG属性 -->

    <!-- 両方が存在する場合（どちらでも可） -->
    <input [id]="inputId">              <!-- プロパティ -->
    <input [attr.id]="inputId">         <!-- 属性 -->

    <!-- null値で属性を削除 -->
    <div [attr.title]="condition ? text : null">
  `
})
export class ComparisonComponent {}
```

## ベストプラクティス
- DOMプロパティが存在しない属性には必ず`[attr.]`を使用する
- ARIA属性を活用してアクセシビリティを向上させる
- data属性はカスタムデータの保存に使用する
- null値を使って条件付きで属性を削除する
- SVG要素には`[attr.]`を使用する

## 注意点
- プロパティバインディングと属性バインディングは異なる
- 属性は常に文字列値を持つ（boolean値は"true"/"false"文字列になる）
- DOMプロパティが存在する場合は通常プロパティバインディングを優先する
- 属性値にnullを設定すると属性自体が削除される

## 関連技術
- プロパティバインディング `[property]`
- ARIA（Accessible Rich Internet Applications）
- data-* カスタムデータ属性
- SVG（Scalable Vector Graphics）
- HTMLElement.setAttribute()
