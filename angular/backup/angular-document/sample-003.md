# #003 「Component デコレータ - @Component の役割」

## 概要
@ComponentデコレータはクラスをAngular Componentとして機能させる重要な要素です。メタデータを通じてComponentの動作を定義します。

## 学習目標
- @Componentデコレータの役割を理解する
- 主要なメタデータプロパティを習得する
- デコレータの仕組みを理解する

## 技術ポイント
- **デコレータ**: クラスにメタデータを追加するTypeScript機能
- **メタデータ**: Componentの設定情報
- **必須プロパティ**: selector、template/templateUrl

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// @Componentデコレータの基本
@Component({
  selector: 'app-user',
  template: '<p>User Component</p>'
})
export class UserComponent {}
```

```typescript
// 主要なメタデータプロパティ
@Component({
  selector: 'app-card',           // セレクタ
  templateUrl: './card.component.html',  // テンプレート
  styleUrls: ['./card.component.css'],   // スタイル
  standalone: true                // Standalone設定
})
export class CardComponent {}
```

```typescript
// v20のStandalone Component
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule],  // 依存関係
  template: '<header>{{title}}</header>'
})
export class HeaderComponent {
  title = 'My App';
}
```

## 💻 詳細実装例（学習用）

### すべてのメタデータプロパティ
```typescript
import { Component, ChangeDetectionStrategy, ViewEncapsulation } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  // 必須プロパティ
  selector: 'app-advanced',

  // テンプレート設定（どちらか必須）
  template: `<div>Inline Template</div>`,
  // または
  templateUrl: './advanced.component.html',

  // スタイル設定（オプション）
  styles: [`div { color: blue; }`],
  // または
  styleUrls: ['./advanced.component.css'],

  // Standalone設定（v20推奨）
  standalone: true,
  imports: [CommonModule],

  // 変更検知戦略
  changeDetection: ChangeDetectionStrategy.OnPush,

  // ビューカプセル化
  encapsulation: ViewEncapsulation.Emulated,

  // プロバイダー
  providers: [],

  // アニメーション
  animations: [],

  // ホストバインディング
  host: {
    'class': 'app-advanced',
    '[attr.role]': '"region"'
  }
})
export class AdvancedComponent {}
```

### インラインとファイル参照の比較
```typescript
// インラインテンプレート・スタイル（小規模Component向け）
@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="variant">
      {{label}}
    </button>
  `,
  styles: [`
    button {
      padding: 8px 16px;
      border-radius: 4px;
    }
    .primary { background: blue; color: white; }
    .secondary { background: gray; color: white; }
  `]
})
export class ButtonComponent {
  label = 'Click';
  variant = 'primary';
}

// ファイル参照（大規模Component向け）
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {}
```

### 変更検知戦略の設定
```typescript
import { Component, ChangeDetectionStrategy, Input } from '@angular/core';

// Default戦略（デフォルト）
@Component({
  selector: 'app-normal',
  template: `<div>{{data}}</div>`,
  changeDetection: ChangeDetectionStrategy.Default
})
export class NormalComponent {
  @Input() data: string = '';
}

// OnPush戦略（パフォーマンス最適化）
@Component({
  selector: 'app-optimized',
  standalone: true,
  template: `<div>{{data}}</div>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OptimizedComponent {
  @Input() data: string = '';
  // Inputが変更されたときのみ再レンダリング
}
```

### ビューカプセル化の設定
```typescript
import { Component, ViewEncapsulation } from '@angular/core';

// Emulated（デフォルト）: スコープ付きスタイル
@Component({
  selector: 'app-emulated',
  template: `<p>Emulated</p>`,
  styles: [`p { color: blue; }`],
  encapsulation: ViewEncapsulation.Emulated
})
export class EmulatedComponent {}

// None: グローバルスタイル
@Component({
  selector: 'app-none',
  template: `<p>None</p>`,
  styles: [`p { color: red; }`],
  encapsulation: ViewEncapsulation.None
})
export class NoneComponent {}

// ShadowDom: Shadow DOMを使用
@Component({
  selector: 'app-shadow',
  template: `<p>Shadow DOM</p>`,
  styles: [`p { color: green; }`],
  encapsulation: ViewEncapsulation.ShadowDom
})
export class ShadowComponent {}
```

### プロバイダーの設定
```typescript
import { Component } from '@angular/core';
import { DataService } from './services/data.service';

@Component({
  selector: 'app-service-user',
  standalone: true,
  template: `<div>{{data}}</div>`,
  providers: [DataService]  // Component専用のサービスインスタンス
})
export class ServiceUserComponent {
  data: string;

  constructor(private dataService: DataService) {
    this.data = this.dataService.getData();
  }
}
```

### ホストバインディング
```typescript
@Component({
  selector: 'app-host-binding',
  standalone: true,
  template: `<p>Host Binding Example</p>`,
  host: {
    // 静的なクラス
    'class': 'host-component',

    // 動的な属性バインディング
    '[attr.role]': '"region"',
    '[attr.aria-label]': 'ariaLabel',

    // イベントリスナー
    '(click)': 'onClick()',
    '(mouseenter)': 'onMouseEnter()',

    // プロパティバインディング
    '[class.active]': 'isActive',
    '[style.background-color]': 'backgroundColor'
  }
})
export class HostBindingComponent {
  ariaLabel = 'Example component';
  isActive = false;
  backgroundColor = '#f0f0f0';

  onClick() {
    this.isActive = !this.isActive;
  }

  onMouseEnter() {
    this.backgroundColor = '#e0e0e0';
  }
}
```

## ベストプラクティス

1. **Standaloneを使用**: v20ではstandalone: trueを推奨
2. **OnPush戦略の活用**: パフォーマンス向上のため積極的に使用
3. **適切なカプセル化**: 通常はEmulated、必要に応じてNoneを使用
4. **インラインは小規模のみ**: 大きなテンプレートは別ファイルに

## 注意点

- @Componentデコレータは必須
- templateとtemplateUrlは同時に使用不可
- stylesとstyleUrlsは併用可能
- selectorは一意の名前を使用

## 関連技術
- TypeScript Decorators
- Metadata
- Change Detection
- View Encapsulation
- Dependency Injection
